import pandas as pd
import numpy as np
from difflib import SequenceMatcher
import xlsxwriter
import time

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

RowNum = '번호'
juso = '주소'
change_yn = '변환여부'
re_juso = '주소_오타'

change_addr = {
    RowNum: [],
    juso: [],
    change_yn: [],
    re_juso: [],
}

########## 시스템DB 주소
gijun_df = pd.read_csv("./gijun.CSV", error_bad_lines=False, index_col=False)
gijun_list = gijun_df.fillna("").values
gijun_list = [''.join(row) for row in gijun_list]
rm_list = []
gijun_replace = [row.split(' ') for row in gijun_list]
gijun_replace = [''.join(row) for row in gijun_replace]

######### 비교할 주소
se_df = pd.read_csv("./sim_se.CSV", error_bad_lines=False, index_col = False)
# se_df = pd.read_csv("./nosearchAddr.CSV", error_bad_lines=False, index_col=False)
se_list = se_df.fillna("").values
se_list = [''.join(row) for row in se_list]
se_replace = [row.split(' ') for row in se_list]
se_replace = [''.join(row) for row in se_replace]

def searchAddr(se_index, gijun_index):
    juso = se_list[se_index]
    rm_juso = gijun_list[gijun_index]
    rm_list.append(rm_juso)

    changeTitle = "kt 접수주소"
    add_addr(se_index, juso, changeTitle, np.nan)


def nosearch_decipher(se_index, similarList):
    similer_index = max(similarList, key=similarList.get)
    juso = se_list[se_index]
    changeTitle = "kt 접수주소 제외"
    re_juso = gijun_list[similer_index]
    add_addr(se_index, juso, changeTitle, re_juso)


def add_addr(se_index, sim_juso, changeTitle, se_juso):
    change_addr[RowNum].append(se_index)
    change_addr[juso].append(sim_juso)
    change_addr[change_yn].append(changeTitle)
    change_addr[re_juso].append(se_juso)


########################
gijun_len = len(gijun_list) - 1
similarList = {}
for se_index, se_val in enumerate(se_replace):
    similarList.clear()
    print('데이터 처리중  = '+str(se_index))
    for gijun_index, gijun_val in enumerate(gijun_replace):
        percentage = similar(gijun_val, se_val)
        if percentage == 1.0:
            searchAddr(se_index, gijun_index)
            break
        similarList[gijun_index] = percentage
        if gijun_index == gijun_len:
            nosearch_decipher(se_index, similarList)


def export_date_excel(addr):
    dataF = pd.DataFrame(addr, columns=[RowNum,
                                        juso,
                                        change_yn,
                                        re_juso])
    print(dataF.fillna(""))
    filename = './excel_test.xlsx'
    dataF.to_excel(filename, 'Sheet1', index=False, engine='xlsxwriter')

print(len(gijun_list)-len(rm_list))
s = set(rm_list)
temp3 = [x for x in gijun_list if x not in s]
print(len(temp3))
for row in temp3 :
    add_addr(np.nan, row, 'KTOA 보편대상 미포함 주소', np.nan)

export_date_excel(change_addr)
