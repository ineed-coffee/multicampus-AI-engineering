library(readxl)

groceries <- read.csv('C:/임시/RData/groceries.csv')

str(groceries)

install.packages('arules')
library(arules)
groceries <- read.transactions('C:/임시/RData/groceries.csv',sep=",")
summary(groceries)

itemFrequency(groceries[,1:10])
# itemFrequency 함수로 거래 비율을 확인 : Suppory(지지도)

itemFrequencyPlot(groceries,support=0.08)
itemFrequencyPlot(groceries,topN=20)

image(groceries[1:5])

groceryRules <- apriori(groceries,
                        parameter=list(support=0.005,
                                       confidence=0.25,
                                       minlen=2))
# minlen : x->y 의 연관규칙에서 아이템이 minlen 미만인 것들은
# 고려하지 않음음
summary(groceryRules)

inspect(groceryRules[1:5])

inspect(sort(groceryRules, by='lift',decreasing=FALSE)[1:5])


# 전략적으로 berries 상품과 함께 향상도가 높은 상품들을 추출하고자한다.
berryRules <- subset(groceryRules,items %in% 'berries')

write(berryRules,file='berryRules.csv',sep=',',row.names=F)

install.packages('arules')
install.packages('C50')
install.packages('tm')
install.packages('SnoballC')
install.packages('wordcloud')
install.packages('RColorBrewer')
install.packages('e1071')
