library(ggplot2)
library(dplyr)
mpg = as.data.frame(ggplot2::mpg)

# Q1 자동차 배기량에 따른 고속도록 연비
# displ 4이하 차량과 5이상 차량의 hwy 평균 비교
print('mean hwy of displ <=4')
mpg %>% 
  filter(displ<=4) %>% 
  summarise(mean_under_4 = mean(hwy))
print('mean hwy of displ >=5')
mpg %>% filter(displ>=5) %>% 
  summarise(mean_over_5 = mean(hwy))
#------------배기량 4 이하 차량이 고속도로 연비가 더 좋음-----------------------

# Q2 자동차 제조 회사별 도시 연비
# 'audi' , 'toyota' 그룹의 cty 평균 비교
mpg %>% filter(manufacturer %in% c('audi','toyota')) %>% 
  group_by(manufacturer) %>%
  summarise(cty_mean=mean(cty))
#--------- toyoya 제조사의 도시 연비가 더 높음----------------------------------

# Q3 'chevrolet','ford','honda' 제조사들의 hwy 평균 조사
mpg %>% filter(manufacturer %in% c('chevrolet','ford','honda')) %>% 
  group_by(manufacturer) %>%
  summarise(hwy_mean=mean(hwy))
#------c:21.9------f:19.4------h:32.6-------------------------------------------

# Q4 mpg 객체의 'class' , 'cty' 컬럼만 추출하여 새 데이터 생성
mpg_part <- mpg %>% select('class','cty')
head(mpg_part)
#--------------------잘 나옴----------------------------------------------------

# Q5 새로 생성한 데이터에서 class 분류(suv , compact)에 따른 cty 평균 조사
mpg_part %>% filter(class %in% c('compact','suv')) %>% 
  group_by(class) %>% summarise(cty_mean = mean(cty))
#--------c:20.1--------------s:13.5---------------------------------------------

# Q6 'audi' 에서 생산한 자동차 중 hwy가 높은 1~5위의 자동차 정보 출력
mpg %>% filter(manufacturer=='audi') %>% 
  arrange(desc(hwy)) %>% head(5)
#-------------------------------------------------------------------------------

# Q7 mpg 의 복사본을 만들고, cty + hwy 한 '합산 연비 변수' 추가
mpg_new <- mpg
mpg_new <- mpg_new %>% mutate(cty_hwy = cty+hwy)
#-------------------------------------------------------------------------------

# Q8 합산 연비 변수를 반으로 나눈 평균 연비 변수 추가
mpg_new <- mpg_new %>% mutate(mean_cty_hwy = cty_hwy/2)
#-------------------------------------------------------------------------------

# Q9-1 평균 연비 변수가 가장 높은 자동차 3종의 데이터 출력
mpg_new %>% arrange(desc(mean_cty_hwy)) %>% head(3)
# Q9-2 ????

#-------------------------------------------------------------------------------

# Q10 회사별로 "suv" 자동차의 통합 연비 평균을 구해 내림차순으로 정렬, 1~5위까지 출력
mpg %>% filter(class=='suv') %>%
  group_by(manufacturer) %>%
  summarise(mean_cty_hwy=mean(cty+hwy)) %>% 
  arrange(desc(mean_cty_hwy)) %>% 
  head(5)
#-------------------------------------------------------------------------------

# Q11 class 분류에 따른 cty 평균
mpg %>% group_by(class) %>% 
  summarise(cty_mean=mean(cty))
#-------------------------------------------------------------------------------

# Q12 11번 문제의 데이터를 cty 평균 기준으로 정렬하여 출력
mpg %>% group_by(class) %>% 
  summarise(cty_mean=mean(cty)) %>% 
  arrange(desc(cty_mean))
#-------------------------------------------------------------------------------

# Q13 제조사별 hwy 평균을 구하고 가장 높은 3위 출력
mpg %>% group_by(manufacturer) %>% 
  summarise(hwy_mean=mean(hwy)) %>% 
  arrange(desc(hwy_mean)) %>% 
  head(3)
#-------------------------------------------------------------------------------

# Q14 각 회사별 compact 차종 수 내림차순 출력
mpg %>% group_by(manufacturer) %>% 
  filter(class=='compact') %>% 
  summarise(compact_n = n()) %>% 
  arrange(desc(compact_n))
#-------------------------------------------------------------------------------