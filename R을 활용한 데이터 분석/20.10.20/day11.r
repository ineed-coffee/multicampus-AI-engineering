library(readxl)
insurance <- read.csv('D:/R/rwork/R연습데이터셋/insurance.csv',stringsAsFactors=T)
str(insurance)

# 회귀모델은 생성전에 정규성에 대한 확인부터

# 종속변수 요약통계 확인
summary(insurance$expenses)
hist(insurance$expenses)

# 독립변수와 종속 변수간 상관분석

cor(insurance[c('age','bmi','children','expenses')])

pairs(insurance[c('age','bmi','children','expenses')])

install.packages('psych')
library(psych)
pairs.panels(insurance[c('age','bmi','children','expenses')])

# lm 모델에서 formula 작성 방식 => '종속변수 ~ 독립변수'
# lm(expenses~독립1+독립2+독립3+...,data=insurance)

ins_model <- lm(expenses~age+children+bmi+sex+smoker+region,data=insurance)
ins_model

summary(ins_model)

# Resuduals (잔차 : 예측의 오차에 대한 요약)

# Coefficients
# Pr(>|t|) : 추정된 계수가 실제 0일 확률 추정치.
# p 값이 작은 경우 해당 특징변수가 종속변수와 관계가 없을 가능성이 아주 낮다는 의미.
# 오른쪽에 *** 으로 표시되는 계수값은 유의 수준을 의미

# Multiple R-squared (다중 r 제곱값) : 모델이 종속변수 값을 얼마만큼 잘 설명하는지 (1에 가까울 수록 모델을 잘 설명하고 있음을 나타냄)

str(ins_model)

temp <- data.frame(age=25,children=2,bmi=30,sex='female',smoker='yes',region='northeast')

predict(ins_model,newdata=temp)

insurance[1:10,-7]
write(insurance[1:10,-7],file='insmodeltest.csv',sep=',')
class(insurance[1:10,-7])

predict(ins_model,newdata=insurance[1:10,-7])
insurance[1:10,7]
