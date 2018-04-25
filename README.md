##### Fast Campus Data Science School 7th Team Project 2 Classification
# [Walmart Recruiting: Trip Type Classification](https://www.kaggle.com/c/walmart-recruiting-trip-type-classification#description)


![](https://github.com/yunah0515/dss7_SWYA_walmart/blob/master/image/walmart_triptypes640.png?raw=true)


# [ Overview ]

### (1) Team : SWYA 
> - SunWoong Kim (novdov) 
> - WonYoung Seo (lucaseo)
> - YunAh Baek (yunah0515)

### (2) Dataset : 
> #### Walmart Shopping Records

### (3) Objective : 
> #### Classification of each customers' TripType

<br>

# [Data Description]

> #### train : 647054 rows, 7 columns
> #### test : 653646 rows, 6 columns

| Index | Feature               | Description                                  | Unique |
|-------:|:-----------------------:|:----------------------------------------------:|--------:|
| 1     | TripType              | a categorical id representing the type of shopping trip the customer made                                       | 38     |
| 2     | VisitNumber           | an id corresponding to a single trip by a single customer                              | 95674  |
| 3     | Weekday               | the weekday of the trip                    | 7      |
| 4     | Upc                   | the UPC number of the product purchased                  | 97715  |
| 5     | ScanCount             | the number of the given item that was purchased. A negative value indicates a product return          | 39     |
| 6     | DepartmentDescription | a high-level description of the item's department                                | 69     |
| 7     | FinelineNumber        | a more refined category for each of the products, created by Walmart | 5196   |


<br>

# [Evaluation]
> ![](https://github.com/yunah0515/dss7_SWYA_walmart/blob/master/image/evaluation.png?raw=true)

<br>

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
