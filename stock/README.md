
# 설계

## 스케쥴

- 매일 8시 데이터 수집 및 분석 (일별 데이터)
- 매일 9시 실시간 데이터 수집 및 분석 (분별 데이터)

## URLs

- 수집 : /stock/collect/{code}/{type}/
- 분석 : /stock/analyze/{code}/{type}/
- 매수 : /stock/buy/
- 매도 : /stock/sell/
- 시뮬레이터 : /stock/simulate/{code}/

## 소스 구조

- collect
  - yahoo
  - balance_sheet
- manager
  - AccountManager
  - SimulateManager
- strategy
  - buy
  - sell


## 수집대상

- 야후 금융
- 대차대조표
- 주식 달력(http://stockschedule.com)

## 분석

- Tensorflow 를 활용한 예측

### 입력 파라미터

### 예측값

- Open, High, Low, Close

## 매수

## 매도

# 참고

- http://stockschedule.com
