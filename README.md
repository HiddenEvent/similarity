# similarity
주소유사도 검사
## 만든이유...
상급기관에서 주기적으로 지역별 통계를 요청하는데 
잘못된 시도, 시군구, 읍면동, 리 정보를 오타나, 표기법 오류
(ex 서울특별시 => 서울시,  / 서초구 => 초서구 등) 
로 인해 디비에서 조회시 데이터를 가져올수 있는 상황이 생기고 이로인해
일일히 수작업으로 데이터가 맞는지 직접 비교를 하는데 꾀 많은 시간이 걸렸다..
이를 자동화 시키기 위해 이 프로젝트로 생각해 진행하게 되었다...

## 흐름
먼저 우리 디비에 있는  시도, 시군구, 읍면동, 리 데이터를 csv로 넣어 둔다음
비교할 데이터 csv를 difflib(SequenceMatcher), pandas를 사용하여 하나씩 비교하여 수치화 시킨다음
가장 큰 값을 뽑아내는 방법으로 만들었다.


## 순서
### 1. 통계 요청 받은 엑셀 자료 
- 시도, 시군구, 읍면동, 리 기준 바꿔준다.
- 시도, 시군구, 읍면동, 리 기준 중복데이터 삭제
- 시도, 시군구, 읍면동, 리 순서로 데이터 정렬

### 2. csv 파일 변환 등 pycharm에 프로젝트안에 upload
- 시도, 시군구, 읍면동, 리 기준 데이터만 따로 CSV파일로 내보내기를 한다.
- 기준이되는 csv파일명은 gijun.CSV로 비교할 csv파일명은 sim_se.CSV로 만들어준다.
- utf-8 인코딩을 한다.
- pycharm에 프로젝트안에 폴더안에 sim_se.CSV파일명으로 upload 한다.

### 3.similer RUN
- xlsx 파일이 하나 떨어진다! 거기안에 데이터를 사용하면 된다 끝!!

## 단점
1. 무조건 유사한 데이터 1개는 무조건 가져오기 때문에 실제 데이터가 DB안에 없어도 가져온다는 것.. 이건 직접 눈으로 확인해야된다..
2. 데이터 전처리 과정은 엑셀로 처리 할 수 밖에 없다는 것...(상급 기관에서 주니까 이건 어쩔수 없는것 같음)

## 만들면서 느낀점..
이걸 만들고나서 단순 노가다 업무를 안할 수 있어 정말 많은 시간을 절약했다...
그럼에도 불구하고 엑셀 작업은 해야된다는 것... 이것까지 추후에는 방법을 고안해 봐야겠다...
추가로...내 컴퓨터에서만 가능 하다는 것... 
나중에는 꼭 배포까지 할 수 있는 수준으로 능력을 올려서 내가 안할 수 있는 경지가 될수 있도록 더욱 노력하자!!