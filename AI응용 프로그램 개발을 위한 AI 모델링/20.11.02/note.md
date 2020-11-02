

### __Neural Network__  

- epoch : 전체 훈련 데이터의 학습 횟수
- early stop : cv 데이터에서 보통 조기종료 시점을 판단





### __Regrssion__ 

- 가설함수 (hypothesis func)
- 비용 (cost func) : 대표적으로 MSE
- 경사하강법 (Grdient Descent method) : learning rate + deriv.





### __Modeling  using Keras__ 

- fit (xtrain , ylabel , batch_size , ..) : 모델 학습 메소드 , 배치 사이즈는 몇개의 샘플로 가중치를 갱신하고자 하는지를 의미.
- 