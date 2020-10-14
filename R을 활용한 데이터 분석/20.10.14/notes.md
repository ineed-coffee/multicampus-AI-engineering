- Corpus : 특정 도메인에서 통용되는 단어의 전체 집합
  - ex) 법령코퍼스 , 
  - 텍스트 마이닝의 첫 단계 - 코퍼스 생성



- __Text  mining__ 
  1. Corpus 생성
  2. 단어 문서 행렬(Text Document Matrix) 생성 (혹은 전치된 DTM)
  3. 문자 전처리 (불용어 , 조사, 숫자 제거 등)
  4. 분석 모델링 내일 연습문제

ex)

|       | 문서1 | 문서2 | ...  | 문서N |
| ----- | ----- | ----- | ---- | ----- |
| hello | 0     | 0     | ...  | 1     |
| sky   | 2     | 0     | ...  | 0     |
| hi    | 0     | 1     | ...  | 1     |
| ...   | 1     | 3     | ...  | 0     |



__new installed package__ 

- tm : for text mining
- SnowballC : extracting word roots (run , running, ran ,runs, ...etc)
- wordcloud
- RColorBrewer
- e1071 : bayesian filter package