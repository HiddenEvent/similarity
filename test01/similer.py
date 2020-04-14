import pandas as pd
import numpy as np
from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

result_addr = []
nosearch_addr = []
nosearch_data = {0: "없는 데이터 ROW"}



########## 시스템적 주소
gijun_df = pd.read_csv("./sim_gijun.CSV", error_bad_lines=False, index_col = False)

# non 값 0으로 처리 하고 리스트로 변환
gijun_list = gijun_df.fillna("").values

gijun_join_list = [''.join(row) for row in gijun_list]

# print(len(gijun_join_list))

######### 비교할 주소
# se_df = pd.read_csv("./sim_se.CSV", error_bad_lines=False, index_col = False)
se_df = pd.read_csv("./nosearchAddr.CSV", error_bad_lines=False, index_col = False)
se_list = se_df.fillna("").values
se_join_list = [''.join(row) for row in se_list]
# print(len(se_join_list)) # 나와야 될 데이터 692개
#


def realAddr(addr):
    result_addr.append(addr)

def nosearch_decipher(se_index, similarList ) :
    similer_index = max(similarList, key=similarList.get)
    # 조회할 데이터 
    noaddrString = '[ '+str(se_index)+'번 ]'+se_join_list[se_index]+" => "+gijun_join_list[similer_index]+'\n'
    nosearch_addr.append(noaddrString)
    
########################
gijun_len = len(gijun_join_list)-1
similarList = {}
for se_index, se_val in enumerate(se_join_list):
    similarList.clear()
    for gijun_index, gijun_val in enumerate(gijun_join_list):
        percentage = similar(gijun_val, se_val)
        if percentage == 1.0:
            realAddr(gijun_val)
            break

        similarList[gijun_index] = percentage

        if gijun_index == gijun_len:
            nosearch_decipher(se_index, similarList)


print('    ===========real')
print(result_addr)
print('    ===========real_len')
print(len(result_addr))
print('    ===========noserch')
print(nosearch_addr)
print('    ===========noserch_len')
print(len(nosearch_addr))

