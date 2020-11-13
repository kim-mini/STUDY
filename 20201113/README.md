## datasience

```
use to pandas / numpy
```
---

[datasience](https://github.com/kim-mini/STUDY/blob/main/20201113/data%20science.md)

ex)

<img src="https://postfiles.pstatic.net/MjAyMDExMTNfMjYg/MDAxNjA1MjM1NzA2Nzgx.m9r8J9FoO_IjPNhYO8YfgJIOs8Efj32ETKUO5z50pvAg.BQFfUdde7u-gRcvQ5XP_4HAy5dlJnxSPUDdou7neBmIg.PNG.kimmin2_/image.png?type=w966" width="50%">


---

## get openAPI

[get openAPI code](https://github.com/kim-mini/STUDY/blob/main/20201113/getopenAPI.py)

```python

def makeAPIURL( strKey, strType, strService, strSIndex, strEIndex, strStationName ):

    strURL = __BASIC_URL# basic_url
    strURL = os.path.join( strURL, strKey )#basic_url/strKey
    strURL = os.path.join( strURL, strType )#basic_url/strKey/strType
    strURL = os.path.join( strURL, strService )#basic_url/strKey/strType/strService
    strURL = os.path.join( strURL, strSIndex )#basic_url/strKey/strType/strService/strSindex
    strURL = os.path.join( strURL, strEIndex )#basic_url/strKey/strType/strService/strSindex/strEIndex
    strURL = os.path.join( strURL, strStationName )#basic_url/strKey/strType/strService/strSindex/strEIndex/strStationName

    return strURL # 이런식으로 path.join해가면서 얻어와야하는 정보를 알려준다

```



```python

 __API_KEY = "인증키번호"
    __RETURN_TYPE = "json"
    __SERVICE_NAME = "realtimeStationArrival"
    __BASIC_URL = "http://swopenAPI.seoul.go.kr/api/subway"

    start_index = "0"
    end_index = "1"
    stationName = "강남"
    strName = urllib.request.quote( stationName )

    strAPIURL = makeAPIURL( __API_KEY, __RETURN_TYPE, __SERVICE_NAME, start_index, end_index, strName)# 위의 정보들을 다 적어준다
   
   
```


```python

# url을 불러오고 이것을 인코딩을 utf-8로 전환하여 결과를 받는다.
    req = urllib.request.Request( strAPIURL ) #http에게 요청을 함
    data = urllib.request.urlopen( req ).read() # http에서 읽어온 값을 data에 저장
    json_str = data.decode("utf-8") # 읽어온 파일을 utf-8로 읽겠다

```

```python

    json_object = json.loads( json_str ) #데이터를 json으로 받기로 했으니까 json에 넣어준다
    print( json_object ) # 그리고 출력해봄

```

```python

 jsonFile = open("liveStation.json", "w" , encoding="utf-8") #jsonfile 수정 가능하도록 오픈
    print( type( json_object ) )
    jsonFile.write( json.dumps( json_object, ensure_ascii=False , indent = 4)) #파이썬에서 key와 value 형태의 자료구조인 Dictionary 객체를 JSON 문자열로 만들시 json.dumps() 를 사용
    jsonFile.close()

```

이런식으로 json에 저장이 된다


![](https://github.com/kim-mini/STUDY/blob/main/20201113/%EC%BA%A1%EC%B2%98.PNG)
