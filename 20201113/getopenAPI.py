
import urllib.request
import json
import pandas as pd
from pandas.io.json import json_normalize

import os

# API 인증키 값 : 000000000000000000000000
#
# [ 입력 명세 ]
# Key : STRING : 인증키 : OPENAPI에서 발급된 인증키
# type : STRING : 요청파일 타입 : "xml: xml", "xml파일: xmlf", "엑셀파일: xls", "json파일 : json"
# service : STRING : 서비스명 : realtimeStationArrival
# start_index : INTEGER : 요청시작위치 : 정수 입력
# end_index : INTEGER : 요청종료위치 : 정수 입력
# statnNm : STRING : 지하철역명 : 지하철역명
#다
# [ 예시 ]
#                                          <key>                          <type><service>            <s><e><statnNm>
# "http://swopenAPI.seoul.go.kr/api/subway/43446575696c637734334d537a5353/json/realtimeStationArrival/0/5/서울"
#


def makeAPIURL( strKey, strType, strService, strSIndex, strEIndex, strStationName ):

    strURL = __BASIC_URL# basic_url
    strURL = os.path.join( strURL, strKey )#basic_url/strKey
    strURL = os.path.join( strURL, strType )#basic_url/strKey/strType
    strURL = os.path.join( strURL, strService )#basic_url/strKey/strType/strService
    strURL = os.path.join( strURL, strSIndex )#basic_url/strKey/strType/strService/strSindex
    strURL = os.path.join( strURL, strEIndex )#basic_url/strKey/strType/strService/strSindex/strEIndex
    strURL = os.path.join( strURL, strStationName )#basic_url/strKey/strType/strService/strSindex/strEIndex/strStationName

    return strURL # 이런식으로 path.join해가면서 얻어와야하는 정보를 알려준


# url = __BASIC_URL
# url = os.path.join( url, __API_KEY )
# url = os.path.join( url, __RETURN_TYPE )
# url = os.path.join( url, __SERVICE_NAME )
# url = os.path.join( url, start_index )
# url = os.path.join( url, end_index )
# url = os.path.join( url, stationName )

if __name__ == "__main__":
    __API_KEY = "43446575696c637734334d537a5353"
    __RETURN_TYPE = "json"
    __SERVICE_NAME = "realtimeStationArrival"
    __BASIC_URL = "http://swopenAPI.seoul.go.kr/api/subway"

    start_index = "0"
    end_index = "1"
    stationName = "강남"
    strName = urllib.request.quote( stationName )

    strAPIURL = makeAPIURL( __API_KEY, __RETURN_TYPE, __SERVICE_NAME, start_index, end_index, strName)
    # print( strAPIURL )

    # url을 불러오고 이것을 인코딩을 utf-8로 전환하여 결과를 받는다.
    req = urllib.request.Request( strAPIURL )
    data = urllib.request.urlopen( req ).read()
    json_str = data.decode("utf-8")
    # print( json_str )

    # 받은 데이터가 문자열이라서 이를 json으로 변환한다.
    json_object = json.loads( json_str )
    print( json_object )

    # json 파일로 API로 넘어온 json 파일 저장하기
    jsonFile = open("liveStation.json", "w" , encoding="utf-8")
    print( type( json_object ) )
    jsonFile.write( json.dumps( json_object, ensure_ascii=False , indent = 4))
    jsonFile.close()
    

    
    
    
    #43446575696c637734334d537a5353
