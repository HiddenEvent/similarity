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

######### 비교할 주소
se_df = pd.read_csv("./sim_se.CSV", error_bad_lines=False, index_col = False)
# se_df = pd.read_csv("./nosearchAddr.CSV", error_bad_lines=False, index_col=False)
se_list = se_df.fillna("").values
se_list = [''.join(row) for row in se_list]

def searchAddr(se_index, gijun_index):
    juso = se_list[se_index]
    changeTitle = "○"
    add_addr(se_index, juso, changeTitle, np.nan)


def nosearch_decipher(se_index, similarList):
    similer_index = max(similarList, key=similarList.get)
    juso = se_list[se_index]
    changeTitle = "X"
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
for se_index, se_val in enumerate(se_list):
    similarList.clear()
    print('처리중 데이터 = '+str(se_index))
    for gijun_index, gijun_val in enumerate(gijun_list):
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


export_date_excel(change_addr)
