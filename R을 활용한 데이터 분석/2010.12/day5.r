install.packages('ggplot2')
installed.packages('proxy')
install.packages('dplyr')
install.packages('readxl')

member <- data.frame(spent=c(10,1,1,17,4,6,1,15,22,3,0,3,7,0,2),
           time=c(15,2,10,7,5,7,1,10,18,3,1,3,7,10,2))

res <- kmeans(member,3)
res

# 클러스터링 시각화 및 속성 

install.packages('fpc')
library(fpc)
library(dplyr)
library(ggplot2)
library(readxl)

fpc::plotcluster(member, res$cluster)

res$centers

res$totss # 1028.667
# total sum of square : 각 (클러스터와 데이터간 거리 제곱의 합) 의 전체 합

res$withinss # 88.22222   0.50000 147.00000
# withinss : 데이터 응집력

res$tot.withinss # 235.7222
# 응집력의 총합 : 작을수록 좋은 수치

res$betweenss # 792.9444
# 클러스터간 떨어져 있는 거리 : 클수록 좋은 수치치

res$size # 9 2 4
# 각 클러스터에 소속된 데이터의 수

res$iter # 2
# 클러스터링에 있어서 몇번 반복되었나

#--------------------------------------------------------------

# 인사이트 도출을 위해서는 클러스터 별 연산 필요

member$cluster <- res$cluster
member

aggregate(data=member,spent~cluster,max)

#---------------------------------------------------------------

install.packages('NbClust')
library(NbClust)

# 4차원 이상의 데이터에 대해서는 일반적인 시각화가 불가능하기 때문에 
# NbClust 패키지 활용

nb <- NbClust(iris[,1:4],min.nc = 2,max.nc = 5,method = 'kmeans')

# 출력 그림은 각 응집도

nb$Best.partition

iris_scale <- scale(iris[,-5])
k.max=10
wss <- rep(NA,k.max)
nClust <- list()

for(i in 1:k.max){
  iris_res <- kmeans(iris_scale,centers=i)
  wss[i] <- iris_res$tot.withinss
  nClust[[i]] <- iris_res$size
}

wss
nClust

# elbow - point 확인을 위한 plot

plot(1:k.max,wss,type='b')

fitk <- kmeans(iris_scale,3)
str(fitk)

plot(iris,col=fitk$cluster)

table(predicted=fitk$cluster,Actual=iris$Species)

#------------------------------------------------------------------

# h-clustering

a <- matrix(rnorm(100),nrow=5) # 5행 2열 표준정규분포 데이터

# 5개의 데이터를 h-clustering을 활용하여 군집화

#hclust(거리행렬,method=거리 구하는 방법,members=)

dist(a)

h <-hclust(dist(a),method = 'single')
# single : 클러스터간 가장 가까운 데이터 사이의 거리
plot(h)


#------------------------------------------------------------------

# knn - 가장 가까운 거리에 있는 k개의 데이터를 추출하여 레이블링 

wbcd <- read.csv("C:/임시/RData/wisc_bc_data.csv",stringsAsFactors = F)

# 범주형에 대해서는 chr 보다는 카테고리형(R에서는 factor) 로 불러오는것이 옳다.
# stringsAsFactors는 모든 문자컬럼에 대해 적용하므로 섞여있을 때는 as.Type() 으로 개별처리 해줘야한다.

wbcd$diagnosis <- factor(wbcd$diagnosis,levels=c('B','M'),
       labels = c('Benign', 'Malignant'))

str(wbcd)

round(proportions(table(wbcd$diagnosis))*100,1)

wbcd[c('radius_mean','area_mean','smoothness_mean')]

wbcd <- wbcd[-1]

# 정규화

normalize <- function(x){
  return ((x-min(x))/(max(x)-min(x)))
}

normalize(c(1,2,3,4,5))

wbcd_n <- as.data.frame(lapply(wbcd[2:31],normalize))

wbcd_train <- wbcd_n[1:469,]
wbcd_test <- wbcd_n[470:569,]

wbcd_train_labels <- wbcd[1:469,1]
wbcd_test_labels <- wbcd[470:569,1]

library(class)

wbcd_test_pred <- knn(train=wbcd_train ,
                      test=wbcd_test ,
                      cl=wbcd_train_labels , k=21)

wbcd_test_pred

install.packages('gmodels')
library(gmodels)

CrossTable(x=wbcd_test_labels,y=wbcd_test_pred)


# 표준화

wbcd_z <- as.data.frame(scale(wbcd[-1]))
wbcd_train <- wbcd_z[1:469,]
wbcd_test <- wbcd_z[470:569,]
wbcd_test_pred <- knn(train=wbcd_train ,
                      test=wbcd_test ,
                      cl=wbcd_train_labels , k=21)
CrossTable(x=wbcd_test_labels,y=wbcd_test_pred)

for(i in c(5,11,15,27)){
  cur_pred <- knn(train=wbcd_train ,
                        test=wbcd_test ,
                        cl=wbcd_train_labels , k=i)
  CrossTable(x=wbcd_test_labels,y=cur_pred)
}



predict.kmeans <- function(x, newdata){
  
}
data(iris)
mydata <- iris
m <- mydata[1:4]
train <- head(m,100)
xNew<- head(m,10)
xNew

norm_eucl <- function(train){
  print(train/apply(train,1,function(x)sum(x^2)^.5))

}

m_norm <- norm_eucl(train)













