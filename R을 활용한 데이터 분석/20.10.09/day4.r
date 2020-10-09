library(ggplot2)
library(dplyr)
library(readxl)

# kmeans 를 이용한 클러스터링(sns data)

sns_data <- read.csv('./R연습데이터셋/snsdata.csv')

str(sns_data)

table(sns_data$gender) # F:22054 , M:5222
table(!is.na(sns_data$gender)) # NA : 2724

# table 함수에서 NA 포함 옵션
table(sns_data$gender,useNA = 'ifany')

table(sns_data$gradyear , useNA = 'ifany') # 2006~2009 각각 7500 씩씩

# 오후실습1. gender 값 대체 : na 값을 갖는 학생과 가장 유사한 학생 10명 -> 성별 판단 -> 클러스터링

table(!is.na(sns_data$age))

summary(sns_data$age)

sns_data$age <- ifelse(sns_data$age>=13 &sns_data$age<20,sns_data$age,NA)
# 정상범위 밖은 결측값 처리

sns_data$female = ifelse(sns_data$gender=="F",1,0) # ifelse 처리는 NA가 포함 X
table(sns_data$female)

sns_data$no_gender = ifelse(is.na(sns_data$gender),1,0)
table(sns_data$no_gender)

sns_data$female = ifelse(sns_data$gender=="F"&!is.na(sns_data$gender),1,0) 
# ifelse 조건에서NA 검사를 포함하면 처리 가능
table(sns_data$female)

# 결측을 제외한 나이 평균 : 대체값으로 활용은 어렵
mean(sns_data$age , na.rm=T)

# Q1. 졸업연도에 따른 나이의 평균
sns_data %>% group_by(gradyear) %>% 
  summarise(mean_age = mean(age,na.rm=T)) 

aggregate(data=sns_data,age~gradyear,mean,na.rm=T)
# 집계함수 전달로 수행하는 aggregate func

# R 함수 몇개
x <- 1:10
mean(x)
ave(x) # 입력백터와 동일한 길이의 벡터를 출력

mygroup <- rep(1:2,c(3,7))
mygroup
ave(x,mygroup,FUN=mean)
ave(x,mygroup,FUN=sum)
ave(x,mygroup,FUN=function(a)sum(a^2))

kd

x       # 1  2  3  4  5  6  7  8  9 10
mygroup # 1  1  1  2  2  2  2  2  2  2 # 그룹 번호
# ave (데이터 , 그룹정보 , 적용함수) 
# -> 데이터를 각 그룹별로 적용함수를 적용해 반환받은 값으로 동일하게 채움


#------------------------------------------------------------------------

ave_age <- ave(sns_data$age,sns_data$gradyear , FUN= function(x) mean(x,na.rm=T))
# 졸업년도 별로 모두 평균값으로 바꿔버린 ave_age


sns_data$age <- ifelse(is.na(sns_data$age),ave_age,sns_data$age)
# 결측값이면 ave_age 에서 , 아니면 원본값
summary(sns_data$age)

class(sns_data[5:40])

interests <- sns_data[5:40]
lapply(interests,scale) # 리스트 형식으로 반환

interests_z <- as.data.frame(lapply(interests,scale))

set.seed(12345)

teen_clusters <- kmeans(interests_z,5)

teen_clusters
# 각 클러스터에 대한 해석은 분석작의 몫

summary(teen_clusters$centers[1,]) # shopping , 

teen_clusters$centers[1,][order(teen_clusters$centers[1,])]
# 그룹1 : 운동 싫어함, 쇼핑 좋아함

teen_clusters$centers[2,][order(teen_clusters$centers[2,])]
# 그룹2 : 별 특생이 없음. 내성적??

teen_clusters$centers[3,][order(teen_clusters$centers[3,])]
# 그룹3 : 이성에 대한 관심이 많음

teen_clusters$centers[4,][order(teen_clusters$centers[4,])]
# 그룹4 : 운동에 미친 사람들

teen_clusters$centers[5,][order(teen_clusters$centers[5,])]
# 그룹5 : 문제아 집단 , 그루밍족 

sns_data$cluster <- teen_clusters$cluster

sns_data[1:10,c('cluster','gender','age','friends')]

aggregate(data=sns_data,age~cluster,mean)

aggregate(data=sns_data,female~cluster,mean)

aggregate(data=sns_data,friends~cluster,mean)


# 여기까지는 분석이고 , 새로운 데이터가 들어왔을때 예측은 어떻게할까?

str(interests_z)


# 코사인 유사도 메소드를 위한 proxy 패키지
install.packages('proxy')
library(proxy)
# d1,d2,d3 : 문서번호 , C : 단어 등장 횟수 벡터
d1 <- c(1,0,5)
d2 <- c(4,7,3)
d3 <- c(40,70,30)

#벡터연결 -> rbind (row-bind) : matrix 반환
doc <- rbind(d1,d2,d3)
colnames(doc)<-c('sky','cloud','rain')

# 거리벡터
dist(doc,method = 'cosine')

dist(doc,method = 'euclidean')


# 1차 데이터 분석 프로젝트 진행 (4명정도 조 , 발표)
# 추천시스템 , 시각화(분석) , 사회 이슈 , 판매(번들 상품), 고객 분류 등
# data.go.kr , uci.edu , 데이콘 , 크롤링

# 2차 텍스트 분류 프로젝트 진행 예정(10월 말 ~ 11월 초)