# ***********따릉이!!  TMI정보 알려주기************


```python
import pandas as pd
import os 
import numpy as np

```


```python
path = '/home/ubuntu/datascience/data/Seoul_bike.csv'
path2 = '/home/ubuntu/datascience/data/Seoul_bike2.csv'
if os.path.isfile(path):
    pass
else:
    print("Not found '{}'".format(path))
if os.path.isfile(path2):
    pass
else:
    print("Not found '{}'".format(path2))
```


```python
df = pd.read_csv(path)
df2 = pd.read_csv(path2)
df = df.drop('성별', axis=1)
```


```python
df
```


```python
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 6894866 entries, 0 to 6894865
    Data columns (total 11 columns):
     #   Column  Dtype  
    ---  ------  -----  
     0   대여일자    object 
     1   대여시간    int64  
     2   대여소번호   int64  
     3   대여소명    object 
     4   대여구분코드  object 
     5   연령대코드   object 
     6   이용건수    int64  
     7   운동량     object 
     8   탄소량     object 
     9   이동거리    float64
     10  사용시간    int64  
    dtypes: float64(1), int64(4), object(6)
    memory usage: 578.6+ MB


## 19.12.01~ 20.05.31일까지의 평균 사용시간


```python
howmanylike = df['사용시간'].mean()
print("사람들의 평균 이용시간 : {}".format(howmanylike))
```

    사람들의 평균 이용시간 : 36.91760898616449


## 어느 대여소의 이용량이 가장 많을까?


```python
# 가장 많이 이용한 대여소부터 내림차순
popularBi = df['대여소명'].value_counts(ascending=False).reset_index()
popularBi.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>index</th>
      <th>대여소명</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>502. 뚝섬유원지역 1번출구 앞</td>
      <td>21605</td>
    </tr>
    <tr>
      <th>1</th>
      <td>207. 여의나루역 1번출구 앞</td>
      <td>20195</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2102. 봉림교 교통섬</td>
      <td>18163</td>
    </tr>
    <tr>
      <th>3</th>
      <td>113. 홍대입구역 2번출구 앞</td>
      <td>17347</td>
    </tr>
    <tr>
      <th>4</th>
      <td>152. 마포구민체육센터 앞</td>
      <td>16847</td>
    </tr>
  </tbody>
</table>
</div>



## 어느 대여소의 이용량이 가장 적을까?


```python
popularBi.tail().reset_index
```




    <bound method DataFrame.reset_index of                           index  대여소명
    1830                 2812.항동프라자     1
    1831  3110.홍은 현대아이파크 아파트 202동 앞     1
    1832              1775.신원리베르텔 앞     1
    1833           1476.중목초등학교 앞 육교     1
    1834               1391.성북청소년센터     1>



## 코로나 이전과 코로나 직후의 이용량은 변화가 있었을까?


```python
#2019-12-01~2019-12-31
dec = df.copy()
dec = df.loc[df['대여일자'] < '2020-01-01']
dec_mean = df['사용시간'].mean()
```


```python
#2020-01-01 ~ 2020-01-31
jan = df.copy()
jan = jan.loc[jan['대여일자'] < '2020-02-01']
```


```python
jan = jan.loc[jan['대여일자'] > '2019-12-31']
jan_mean = jan['사용시간'].mean()
```


```python
#2020-02-01 ~ 2020-02-31
feb = df.copy()
feb = feb.loc[feb['대여일자'] < '2020-03-01']
```


```python
feb = feb.loc[feb['대여일자'] > '2019-01-31']
feb_mean = feb['사용시간'].mean()
```

작년 자료 비교


```python
print("12월 사용시간 평균 : {}".format(dec_mean))
print("1월 사용시간 평균 : {}".format(jan_mean))
print("2월 사용시간 평균 : {}".format(feb_mean))
print("\n코로나로 인해 바깥활동이 뜸해진 것으로 보인다")
```

    12월 사용시간 평균 : 36.91760898616449
    1월 사용시간 평균 : 22.18185254609704
    2월 사용시간 평균 : 22.744006852092777
    
    코로나로 인해 바깥활동이 뜸해진 것으로 보인다


 

 

 

 

작년자료 비교(2월은 춥기 때문에 코로나와 상관없이 이용건수가 줄어든것 일수도 있기에)


```python
#2018-12-01 ~ 2018-12-31
dec2 = df2.copy()
dec2 = dec2.loc[dec2['대여일자'] < '2019-01-01']
```


```python
dec2 = dec2.loc[dec2['대여일자'] > '2018-11-31']
dec2_sum = dec2['대여건수'].sum()
```


```python
df2
```


```python
#2019-01-01 ~ 2019-01-31
jan2 = df2.copy()
jan2 = jan2.loc[jan2['대여일자'] < '2019-02-01']
```


```python
jan2
```


```python
jan2 = jan2.loc[jan2['대여일자'] > '2018-12-31']
jan2_sum = jan2['대여건수'].sum()
```


```python
#2019-02-01 ~ 2019-02-31
feb2 = df2.copy()
feb2 = feb2.loc[feb2['대여일자'] < '2019-03-01']
```


```python
feb2 = feb2.loc[feb2['대여일자'] > '2019-01-31']
feb2_sum = feb2['대여건수'].sum()
```

 

 


```python
#2018-12-01 ~ 2019-02-31
dec2018 = dec2_sum
jan2019 = jan2_sum
feb2019 = feb2_sum

#2019-12-01 ~ 2020-02-31
dec2019 = dec['이용건수'].count()
jan2020 = jan['이용건수'].count()
feb2020 = feb['이용건수'].count()


print('2018dec : {} / 2019jan : {} / 2019feb : {}'.format(dec2018,jan2019,feb2019))
print('2019dec : {} / 2020jan : {} / 2020feb : {}'.format(dec2019,jan2020,feb2020))
```

 

 

 

따릉이가 활성화 되면서 이용하는 사람들도 매년마다 늘어났을 것이라 추측함으로 
평균편차를 구해 그 갭으로 확인하겠음

 

2019년 평균


```python
#2018-12-01 ~ 2019-02-31
var2019 = df2.copy()
var2019 = var2019.loc[var2019['대여일자'] < '2019-03-01']
```


```python
var2019 = var2019.loc[var2019['대여일자'] > '2018-11-31']
var2019_sum = var2019['대여건수'].sum()
```


```python
var2019_sum
```

2020년 평균


```python
#2019-12-01~2020-02-31
var2020= df2.copy()
var2020 = var2020.loc[var2020['대여일자'] < '2020-03-01']
var2020_mean = var2020['사용시간'].mean()
```


```python
dec_mean
```

 

 


```python
list2019 = np.array[dec2018,jan2019,feb2019]
```


```python
list2019.var()
```


```python
corona_before = np.array[dec2_sum, jan2_sum, feb2_sum]
corona_after = np.array[dec['이용건수'].count(), jan['이용건수'].count(), feb['이용건수'].count()]
```

 

 

## 누가 따릉이를 가장 멀리 갔을까 정기권 / 일일권
올해의 따릉이상


```python
#일일권
long1 = df.copy()
longBi_D = long1.loc[long1['대여구분코드'] == '일일권']
longBi_D = longBi_D.loc[longBi_D['이용건수'] == 1]
longBi_D = longBi_D.sort_values(by=['이동거리'], ascending = False)
longBi_D.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>대여일자</th>
      <th>대여시간</th>
      <th>대여소번호</th>
      <th>대여소명</th>
      <th>대여구분코드</th>
      <th>연령대코드</th>
      <th>이용건수</th>
      <th>운동량</th>
      <th>탄소량</th>
      <th>이동거리</th>
      <th>사용시간</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>6766863</th>
      <td>2020-05-30</td>
      <td>9</td>
      <td>1735</td>
      <td>1735. 도봉역 1,2번 출구사이 건너편</td>
      <td>일일권</td>
      <td>30대</td>
      <td>1</td>
      <td>339599.05</td>
      <td>3060.88</td>
      <td>13193436.13</td>
      <td>181</td>
    </tr>
    <tr>
      <th>6845833</th>
      <td>2020-05-31</td>
      <td>11</td>
      <td>1325</td>
      <td>1325. 상월곡역 4번출구</td>
      <td>일일권</td>
      <td>20대</td>
      <td>1</td>
      <td>496269.26</td>
      <td>3060.46</td>
      <td>13191633.60</td>
      <td>119</td>
    </tr>
    <tr>
      <th>6799712</th>
      <td>2020-05-30</td>
      <td>17</td>
      <td>1006</td>
      <td>1006. 롯데캐슬 115동앞</td>
      <td>일일권</td>
      <td>40대</td>
      <td>1</td>
      <td>376017.68</td>
      <td>3059.63</td>
      <td>13188049.78</td>
      <td>54</td>
    </tr>
    <tr>
      <th>6831334</th>
      <td>2020-05-31</td>
      <td>1</td>
      <td>551</td>
      <td>551. 구의삼성쉐르빌 앞</td>
      <td>일일권</td>
      <td>30대</td>
      <td>1</td>
      <td>292434.55</td>
      <td>3059.38</td>
      <td>13186983.85</td>
      <td>89</td>
    </tr>
    <tr>
      <th>6893756</th>
      <td>2020-05-31</td>
      <td>22</td>
      <td>1297</td>
      <td>1297. 석촌호수교차로(동호 팔각정 앞)</td>
      <td>일일권</td>
      <td>~10대</td>
      <td>1</td>
      <td>349867.99</td>
      <td>3059.30</td>
      <td>13186642.20</td>
      <td>18</td>
    </tr>
  </tbody>
</table>
</div>




```python
#정기권
long2 = df.copy()
longBi_j = long2.loc[long2['대여구분코드'] == '정기권']
longBi_j = longBi_j.loc[longBi_j['이용건수'] == 1]
longBi_j = longBi_j.sort_values(by=['이동거리'], ascending = False)
longBi_j.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>대여일자</th>
      <th>대여시간</th>
      <th>대여소번호</th>
      <th>대여소명</th>
      <th>대여구분코드</th>
      <th>연령대코드</th>
      <th>이용건수</th>
      <th>운동량</th>
      <th>탄소량</th>
      <th>이동거리</th>
      <th>사용시간</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>6562724</th>
      <td>2020-05-27</td>
      <td>16</td>
      <td>1048</td>
      <td>1048. 동부기업(둔촌동)</td>
      <td>정기권</td>
      <td>50대</td>
      <td>1</td>
      <td>255954.03</td>
      <td>3060.26</td>
      <td>13190786.83</td>
      <td>115</td>
    </tr>
    <tr>
      <th>6771618</th>
      <td>2020-05-30</td>
      <td>11</td>
      <td>1243</td>
      <td>1243. 문정 법조단지7</td>
      <td>정기권</td>
      <td>30대</td>
      <td>1</td>
      <td>292480.17</td>
      <td>3059.86</td>
      <td>13189040.67</td>
      <td>179</td>
    </tr>
    <tr>
      <th>6692285</th>
      <td>2020-05-29</td>
      <td>9</td>
      <td>1049</td>
      <td>1049. 강일리버파크 10단지</td>
      <td>정기권</td>
      <td>50대</td>
      <td>1</td>
      <td>255915.03</td>
      <td>3059.80</td>
      <td>13188777.04</td>
      <td>77</td>
    </tr>
    <tr>
      <th>6742144</th>
      <td>2020-05-29</td>
      <td>21</td>
      <td>1010</td>
      <td>1010. 강동세무서</td>
      <td>정기권</td>
      <td>30대</td>
      <td>1</td>
      <td>355132.30</td>
      <td>3059.67</td>
      <td>13188216.80</td>
      <td>122</td>
    </tr>
    <tr>
      <th>6634776</th>
      <td>2020-05-28</td>
      <td>15</td>
      <td>1222</td>
      <td>1222. 잠실새내역 5번 출구 뒤</td>
      <td>정기권</td>
      <td>50대</td>
      <td>1</td>
      <td>355124.59</td>
      <td>3059.60</td>
      <td>13187930.41</td>
      <td>83</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
