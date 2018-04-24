##### Fast Campus Data Science School 7th Team Project 2 Classification
# [Walmart Recruiting: Trip Type Classification](https://www.kaggle.com/c/walmart-recruiting-trip-type-classification#description)

![](https://github.com/yunah0515/dss7_SWYA_walmart/blob/master/image/walmart_triptypes640.png?raw=true)

# [ Overview ]

### (1) Team : SWYA 
> - 김선웅 
> - 서원영 
> - 백윤아 

### (2) Dataset : 
> #### Walmart Shopping Records

### (3) Objective : 
> #### 각 고객의 구매정보에 따른 구매 건의 Type을 분류

# [Data Description]

> #### train : 647054 rows, 7 columns
> #### test : 653646 rows, 6 columns
> - 타겟값 TripType을 제외한 동일한 특성의 컬럼

| Index | Feature               | Description                                  | Unique |
|-------|-----------------------|----------------------------------------------|--------|
| 1     | TripType              | Target                                       | 38     |
| 2     | VisitNumber           | 각 손님의 Index                              | 95674  |
| 3     | Weekday               | VisitNumber가 발생한 요일                    | 7      |
| 4     | Upc                   | 구매한 제품의 고유한 바코드                  | 97715  |
| 5     | ScanCount             | 구매 수량 ( 반품 시 - 값으로 표기 )          | 39     |
| 6     | DepartmentDescription | 제품의 대분류                                | 69     |
| 7     | FinelineNumber        | 월마트 자체적으로 정의 한 제품의 소분류 코드 | 5196   |


<br>

# [Evaluation]
> ![](https://github.com/yunah0515/dss7_SWYA_walmart/blob/master/image/evaluation.png?raw=true)

# [Contents]

### (1) EDA & Preprocessing
> - Missing Values
> - Encoding Weekday 
> - Uneven Distribution of TripType
> - Most Frequent & Least Frequent TripType

### (2) Feature Engineering
> - UPC decoding
> - ScanCount seperation
> - Feature encoding
> - Dummy variables
> - Identifing the most frequently purchased items per VisitNumber

### (3) Modeling
> - RandomForest
> - XGBoost

### (4) Results
> - Logarithmic loss : 0.78259
> - Accuracy score : 73.68%
> - Feature Importance Top 20

### (5) Kaggle Submission
> - Total Teams : 1,047 teams 
> - Final Score : 0.79154
> - Leaderboard : 294 / 1,047 (Top 30%)
