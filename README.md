# stock-py

## 접속

```shell
http://127.0.0.1:8099/stock/
```

![](https://goo.gl/VSsp3f)

데이터가 없는 경우, 위와 같이 콤보박스에 내용이 안나옵니다.

## 관리자 계정 생성

```python
python manage.py createsuperuser
```

관리자 아이디를 생성합니다. 

## 사이트 관리

![](https://goo.gl/ZRa4Zb)

관리자 페이지로 접속한 후, 생성한 관리자 아이디로 로그인 합니다.

## 데이터 입력

![](https://goo.gl/t3Y1nW)

이중에서, Strategy buys, Strategy sells 에 데이터를 입력합니다.

## Strategy buys 에 데이터 입력

`Strategy buys` 선택 후 

![](https://goo.gl/2FUKuq)

오른쪽 상단의 `STRATEGY BUY 추가 +` 버튼을 클릭합니다.

![](https://goo.gl/4fSGNN)

필드에 `RA_5` 를 입력하고 `저장` 합니다.

## Strategy sells 에 데이터 입력

마찬가지로, Strategy sells 에서 추가 버튼을 누르고

![](https://goo.gl/4b3GXa)

필드에 `MAX_10` 를 입력하고 `저장` 합니다.


## Stock codes 에 데이터 입력

![](https://goo.gl/zm8Wio)

Django 사이트 관리에서, `Stock codes` 를 선택하고 데이터를 추가합니다. 

![](https://goo.gl/euvpaU)

yahoo 코드 값과 이름을 입력합니다.

코드 데이터는 /stock/data/kospi_yahoo.csv 파일에 있습니다.

## 웹 접속

이후 `http://127.0.0.1:8099/stock/` 접속 후 `시작` 버튼을 클릭하면 됩니다.


## 추가 수정이 필요합니다. 

Yahoo에서 데이터를 가져오는 부분에서 정상 작동하지 않는 듯 합니다.
 
이 부분 확인이 더 필요한 상황입니다.





---
---
---




구조화는 진행중이여서, 많은 수정이 필요합니다.

**예고 없이 변경이 일어날 수 있습니다.**


## Database 생성

> python3 manage.py makemigrations stock

> python3 manage.py migrate


## 라이브러리 설치

> pip3 install -r requirements.txt


## 설명

sqlite DB를 사용하였습니다.


## 관리자 생성

> python3 manage.py createsuperuser