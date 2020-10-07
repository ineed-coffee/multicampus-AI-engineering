library(ggplot2)
library(dplyr)

df <- data.frame(gender=c('m','f',NA,'m','f'),
                 score=c(5,4,3,4,NA))
df
is.na(df)
table(is.na(df))
mean(df$score) # R에서는 결측값이 있으면 계산이 안됨됨

# R에서 결측값 처리
df_new <-df %>% 
  filter(!is.na(score))
mean(df_new$score)

# R에서 drop (행단위)
na.omit(df)
mean(df$score,na.rm=T)


# R에서 indexing : 판다스와 다르게 행-열 순으로 참조
exam = read.csv('./R연습데이터셋/csv_exam.csv')
exam[c(3,8,15),'math'] <- NA # 다중 참조는 배열로 전달

exam %>% 
  summarise(meanm=mean(math,na.rm=T))

exam$math
#퀴즈1 : math 결측값을 평균값으로 대체

exam$math[is.na(exam$math)] <- mean(exam$math,na.rm=T)

# R에서 outlier 제거
ol<-data.frame(gen=c(1,2,1,2,3),
           score=c(5,4,1,3,4))
ol
table(ol)

# 범주형 이상치 - 결측값 간주 - 제외
ol$gen <- ifelse(ol$gen==3,NA,ol$gen)

# 연속형 이상치 - 정상범위 설정 후 결측 간주 - 제외
ol$score <- ifelse(ol$score>4,NA,ol$score)

ol

# R 분석
ol %>% 
  filter(!is.na(gen) & !is.na(score)) %>% 
  group_by(gen) %>% 
  summarise(ms=mean(score))

# 데이터전처리 -> 머신러닝/딥러닝

# 정상범위 : 논리적(통계적) 판단 근거
# 논리적? : 성인 몸무게는 40~150kg
# 통계적? : 데이터 상하위 0.3% 극단치 (IQR*1.5)
mpg = ggplot2::mpg
boxplot(mpg$hwy)
boxplot(mpg$hwy)$stats

# 한국인 삶의 질 분석 : koweps 데이터
install.packages('foreign')
library(foreign)
library(readxl)

raw_welfare <- read.spss(file='./R연습데이터셋/Koweps_hpc10_2015_beta1.sav',to.data.frame=TRUE)
welfare <- raw_welfare # 복사본
head(welfare,1)
View(welfare)
dim(welfare)

# 데이터 분석에 필요한 컬럼만 
welfare<-rename(welfare, 
                sex=h10_g3,
                birth=h10_g4,
                marriage=h10_g10,
                religion=h10_g11,
                income=p1002_8aq1,
                code_job=h10_eco9,
                code_region=h10_reg7
)
welfare

table(welfare$sex)
welfare$sex <- ifelse(welfare$sex==1,'male','female')
qplot(welfare$income)

# 범위지정
qplot(welfare$income)+xlim(0,1000)

welfare$income <- ifelse(welfare$income %in% c(0,5000),NA,welfare$income)
table(is.na(welfare$income))

# na 가 아닌 데이터에 대해 성별에 따른 급여 평균 조사

sex_income <- welfare %>% filter(!is.na(income)) %>% 
  group_by(sex) %>% 
  summarise(mean_income = mean(income))

sex_income

ggplot(data=sex_income , aes(x=sex,y=mean_income))+geom_col()

summary(welfare$birth)

table(is.na(welfare$birth))

welfare <- welfare %>% mutate(age=2015-birth+1)
summary(welfare$age)
qplot(welfare$age)

# 나이에 따른 급여 평균
age_income <- welfare %>% filter(!is.na(income)) %>% 
  group_by(age) %>% 
  summarise(meanincome = mean(income))

ggplot(data=age_income , aes(x=age,y=meanincome))+geom_col()
ggplot(data=age_income , aes(x=age,y=meanincome))+geom_line()

# 연령대로 나누어서 young(<30) , middle(<60) , old(>=60)

welfare <- welfare %>% mutate(ageg=ifelse(age<30,'young',ifelse(age<60,'middle','old')))

# 연령 구분별 월급 평균 
ageg_income <- welfare %>% group_by(ageg) %>% 
  summarise(mean_ageg_income = mean(income,na.rm=T))

# plot + 정렬
ggplot(data=ageg_income , aes(x=ageg,y=mean_ageg_income))+geom_col()+
  scale_x_discrete(limits=c('young','middle','old'))

sex_income_ageg = welfare %>% group_by(ageg,sex) %>% 
  summarise(mean=mean(income,na.rm = T))

sex_income_age = welfare %>% group_by(age,sex) %>% 
  summarise(mean=mean(income,na.rm = T))

ggplot(data=sex_income_ageg , aes(x=ageg,y=mean,fill=sex))+geom_col(position = 'dodge')+
  scale_x_discrete(limits=c('young','middle','old'))

# 직업군에 따른 급여 비교

list_job <- read_excel('./R연습데이터셋/Koweps_Codebook.xlsx',col_names=T,sheet=2)
welfare <- left_join(welfare,list_job,id="code_job")

welfare %>% 
  filter(!is.na(code_job)) %>% 
  select(code_job,job)

# 퀴즈 4 : 직업별 월급 평균 출력

job_income <- welfare %>% filter(!is.na(job)) %>% 
  group_by(job) %>% 
  summarise(mean=mean(income,na.rm = T))

top20 <- job_income %>% 
  arrange(desc(mean)) %>% 
  head(20)

ggplot(data=top20,aes(x=job,y=mean))+geom_col()+coord_flip()

bottom10 <- job_income %>% 
  arrange(mean) %>% 
  head(10)

ggplot(data=bottom10,aes(x=job,y=mean))+geom_col()+coord_flip()


# 퀴즈 5 남성 직업 빈도 상위 10개 출력

job_male <- welfare %>% filter(sex=='male' & !is.na(job)) %>% 
  group_by(job) %>% 
  summarise(cnt=n()) %>% 
  arrange(desc(cnt)) %>% 
  head(10)

job_female <- welfare %>% filter(sex=='female' & !is.na(job)) %>% 
  group_by(job) %>% 
  summarise(cnt=n()) %>% 
  arrange(desc(cnt)) %>% 
  head(10)

# 종교가 있는 사림이 이혼을 더/덜할까

table(welfare$religion)
welfare$religion <- ifelse(welfare$religion==1,'Yes','No')
qplot(welfare$religion)

# 이혼 여부 변수 생성

welfare$group_marriage <- ifelse(welfare$marriage==1,'marriage',
                                 ifelse(welfare$marriage==3,'divorce',NA))
table(welfare$group_marriage)
qplot(welfare$group_marriage)

religion_marriage <- welfare %>% 
  filter(!is.na(group_marriage)) %>% 
  group_by(religion,group_marriage) %>% 
  summarise(cnt=n()) %>% 
  mutate(tot_group=sum(cnt)) %>%
  mutate(pct = round(cnt/tot_group*100,1))

divorce <- religion_marriage %>% 
  filter(group_marriage=='divorce') %>% 
  select(religion,pct)

divorce
