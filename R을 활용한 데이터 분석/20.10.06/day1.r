# 스크립트 창
# ctrl + L : clear console interface
print('what is R?')


# install.packages("readxl")


library(readxl)
eng <- c(50,60,70) # 벡터
mat <- c(70,80,90)

df <- data.frame(eng,mat)
df

class <- c(1,1,2)
dfm<-data.frame(eng,mat,class)
dfm

mean(dfm$eng)

read_excel("./R연습데이터셋/excel_exam.xlsx")

read_excel("./R연습데이터셋/excel_exam_novar.xlsx",col_names=F)

read_excel("./R연습데이터셋/excel_exam_sheet.xlsx",sheet=3)

data = read.csv("./R연습데이터셋/csv_exam.csv")
str(data) # 파이선 df.info

write.csv(data,file='savefile.csv')

exam = read.csv("savefile.csv")
head(exam)
View(exam)     
dim(exam) # 파이썬 df.shape
summary(exam) # 파이썬 df.describe

install.packages('dplyr')
library(dplyr)

reexam = rename(exam,eng=english)
reexam

reexam$plus_me <- reexam$math+reexam$eng
reexam

reexam$result <-ifelse(reexam$math>=70,'pass','fail') # 파이썬 np.where

install.packages("ggplot2")
library(ggplot2)
gplot(reexam$result)

reexam$hakjum <- ifelse(reexam$math<50,'C',ifelse(reexam$math<80,'B','A'))
reexam

table(reexam$hakjum) # 파이썬 value_counts


exam <- read.csv("./R연습데이터셋/csv_exam.csv")
exam
exam %>% filter(class==1) # 파이프라인??

exam %>% filter(class %in% c(1,3,5)) # in 

exam %>% select(math) # 조건을 거는건 아니고 열 선택만
exam %>% select(-math,-class) # 특정 열 빼고

exam %>% 
  filter(class==1) %>% 
  select(english)     # pipe-line 이 유연한 코딩이 가능한 이유

exam %>% 
  select(id,math) %>% 
  head

exam %>%      # 정렬
  arrange(desc(math))

exam %>%      # 다차 정렬
  arrange(class,math)

# 파생 변수 추가 (특성 공학)
exam %>% 
  mutate(total=math+english+science) %>% 
  head

# groupby 집계
exam %>% 
  summarise(mean_math = mean(math))

exam %>% 
  group_by(class) %>% 
  summarise(mean_math = mean(math),
            sum_math = sum(math),
            median_math = median(math),
            n=n())
ggplot2::mpg
