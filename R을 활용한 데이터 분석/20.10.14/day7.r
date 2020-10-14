library(readxl)

sms_raw <- read.csv('C:/임시/RData/sms_spam_ansi.txt')
str(sms_raw)

sms_raw$type <- factor(sms_raw$type)
str(sms_raw)

table(sms_raw$type) # 4812 hams 747 spams

# 우도표를 만드려면 -> 단어부터 모두 추출해야함 
#  -> tm패키지 -> Corpus 구축

install.packages('tm')

library(tm)

tm::stopwords('en')

tm::removeWords('of so many people',stopwords('en'))

IMDB <- read.csv('C:/임시/RData/IMDB-Movie-Data.csv')

str(IMDB)

summary(IMDB)

sum(is.na(IMDB$Metascore))

colSums(is.na(IMDB))

IMDB2 <- na.omit(IMDB) # 모든 변수에 대해 결측값 하나라도 있으면 버림
colSums(is.na(IMDB2))

# 특정 변수에 결측값이 있는 경우만 행을 삭제하고자 한다면
IMDB3 <- IMDB[complete.cases(IMDB[,12]),]
colSums(is.na(IMDB3))

IMDB$Metascore[is.na(IMDB$Metascore)] <- 50

# 극단치 제거 : IQR RUle

# 1분위 수 
Q1 <- quantile(IMDB$Revenue..Millions.,probs=c(0.25),na.rm = T)
Q3 <- quantile(IMDB$Revenue..Millions.,probs=c(0.75),na.rm = T)
IQR <- Q3-Q1
LC <- Q1-(1.5*IQR)
UC <- Q3+(1.5*IQR)

# 정상범위 추출 : subset
IMDB2 <-subset(IMDB, IMDB$Revenue..Millions.>LC&IMDB$Revenue..Millions.<UC)

# 부분 문자열 추출 : substr
IMDB$Actors[1] # "Chris Pratt, Vin Diesel, Bradley Cooper, Zoe Saldana"
substr(IMDB$Actors[1],1,5) # 인덱스 ? 

# 문자열 붙이기
paste(IMDB$Actors[1],'_',"A")

# 문자열 분할
strsplit(IMDB$Actors[1],split=',')

# 문자열 대체
gsub(","," ",IMDB$Genre)
IMDB$Genre2 <-gsub(","," ",IMDB$Genre)


# ----------------------------
# 텓스트 마이닝 

CORPUS <- Corpus(VectorSource(IMDB$Genre2))

# 특수문자 제거 , 숫자 , 소문자 통일
CORPUS_tm <- tm_map(CORPUS,removePunctuation) # 특수문자 제거
tm_map(CORPUS_tm,removeNumbers) # 숫자 제거
tm_map(CORPUS_tm,tolower) # 소문자 통일

# DTM 생성
DTM <- DocumentTermMatrix(CORPUS_tm)
DTM

inspect(DTM)

DTM <- as.data.frame(as.matrix(DTM))

IMDB_Genre <-cbind(IMDB,DTM)

IMDB$Description # 단어도 중복이 많고 조사, 동사, 명사 등 복잡

CORPUS <- Corpus(VectorSource(IMDB$Description))
CORPUS_tm <- tm_map(CORPUS,stripWhitespace) # 공백문자 제거
CORPUS_tm <- tm_map(CORPUS_tm,removeNumbers) # 숫자자문자 제거
CORPUS_tm <- tm_map(CORPUS_tm,tolower) # 소문자 통일
CORPUS_tm <- tm_map(CORPUS_tm,removePunctuation) # 구두점 제거

DTM <- DocumentTermMatrix(CORPUS_tm)
inspect(DTM)

IMDB$Description[155]

CORPUS_tm <- tm_map(CORPUS_tm,removeWords,c(stopwords('en'),'my','custom','words'))

TDM <- TermDocumentMatrix(CORPUS_tm)
m <- as.matrix(TDM)

rowSums(m)

sort(rowSums(m),decreasing = T)
v <- sort(rowSums(m),decreasing = T)

names(v)
d <- data.frame(word=names(v),freq=v)

install.packages('SnowballC') # 어근 추출 패키지
library(SnowballC)

install.packages('wordcloud')
library(wordcloud)

install.packages('RColorBrewer')
library(RColorBrewer)

wordcloud(words=d$word, freq=d$freq , min.freq=5,
          max.words=200,random.order=F,
          colors=brewer.pal(8,'Dark2'))

library(tm)
sms_corpus <- VCorpus(VectorSource(sms_raw$text))
sms_corpus
inspect(sms_corpus)

as.character(sms_corpus[[1]])
lapply(sms_corpus[1:3],as.character)

sms_corpus_clean <- tm_map(sms_corpus,removeNumbers)
sms_corpus_clean <- tm_map(sms_corpus_clean,content_transformer(tolower))
sms_corpus_clean <- tm_map(sms_corpus_clean,removePunctuation)
sms_corpus_clean <- tm_map(sms_corpus_clean,removeWords,stopwords())

removePunctuation('hello..., ; : hihihi')


myreplace <- function(x){
  gsub("[[:punct:]]+"," ",x)
}
myreplace('hello...,..world')

library(SnowballC)
wordStem(c('learned','learn','learning','learns')) #1

tm_map(c('learned','learn','learning','learns'),stemDocument)

sms_corpus_clean <- tm_map(sms_corpus_clean,stemDocument)
sms_corpus_clean <- tm_map(sms_corpus_clean,stripWhitespace)

lapply(sms_corpus_clean[1:3],as.character)
lapply(sms_corpus[1:3],as.character)

sms_dtm <- DocumentTermMatrix(sms_corpus_clean)
inspect(sms_dtm)

#-----------여기까지 전처리----------------------------------

# 1. train/test split
# 2. wordcloud 시각화 (optional)

sms_train_labels <- sms_raw[1:4169,]$type # 학습 정답
sms_test_labels <- sms_raw[4170:5559,]$type # 예측 정답

sms_dtm_train <- sms_dtm[1:4169,]
sms_dtm_test <- sms_dtm[4170:5559,]

table(sms_train_labels)
prop.table(table(sms_test_labels))

#--트레이닝 데이터->베이지안 필터기-> 테스트 데이터->
# 분류 예측 비교

wordcloud(sms_corpus_clean,min.freq = 50,random.order = F)

spam <- subset(sms_raw,type=='spam')
ham <- subset(sms_raw,type=='ham')

wordcloud(spam$text , max.words = 40)
wordcloud(ham$text, max.words = 50)

install.packages('e1071')
library(e1071)

sms_dtm_freq_train <- removeSparseTerms(sms_dtm_train,0.999)
sms_dtm_freq_train
sms_dtm_train

sms_freq_words <- findFreqTerms(sms_dtm_train,5)
str(sms_freq_words) # 문자 벡터 , 1151개 단어 벡터 

sms_dtm_freq_train<- sms_dtm_train[,sms_freq_words]
sms_dtm_freq_test<- sms_dtm_test[,sms_freq_words]

# 나이브베이즈 분류기는 범주형 데이터에 대하 훈련하도록 되어있음
# 현재 희소행렬(단어횟수,숫자)-> 범주형 변환
# 셀의 값이 1 이상 -> YES , 아니면 -> NO

inspect(sms_dtm_freq_train)

convertCounts <- function(x){
  x<-ifelse(x>0,'YES','NO')
}

sms_train <- apply(sms_dtm_freq_train, MARGIN = 2, convertCounts)
sms_train

sms_test <- apply(sms_dtm_freq_test, MARGIN = 2, convertCounts)

sms_train[,1]
str(sms_train)

sms_Classifier <- naiveBayes(sms_train,sms_train_labels,laplace = 1)

sms_test_pred <- predict(sms_Classifier,sms_test)

library(gmodels)

CrossTable(sms_test_pred,sms_test_labels,
           dnn=c('predicted','actual'))
print((1189+166)/1390)

#내일 연습문제
#새로운 이메일 제목 -> 'free cash..club' -> 햄/스팸 ? (smsClassifier)
#sms_Classifier <- naiveBayes(sms_train,sms_train_labels,laplace = 1)