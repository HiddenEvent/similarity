import pandas as pd
import numpy as np
from difflib import SequenceMatcher


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


RowNum = '번호'
sido = '시도'
sgg = '시군구'
emd = '읍명동'
li = '리'
change_yn = '변환여부'
re_sido = '시도_오타'
re_sgg = '시군구_오타'
re_emd = '읍명동_오타'

change_addr = {
    RowNum: [],
    sido: [],
    sgg: [],
    emd: [],
    li: [],
    change_yn: [],
    re_sido: [],
    re_sgg: [],
    re_emd: [],
}

########## 시스템DB 주소
gijun_df = pd.read_csv("./sim_gijun.CSV", error_bad_lines=False, index_col=False)
gijun_list = gijun_df.fillna("").values
gijun_join_list = [''.join(row) for row in gijun_list]
gijun_replace = ['_'.join(row) for row in gijun_list]
# print(len(gijun_join_list))

######### 비교할 주소
se_df = pd.read_csv("./sim_se.CSV", error_bad_lines=False, index_col = False)
# se_df = pd.read_csv("./nosearchAddr.CSV", error_bad_lines=False, index_col=False)
se_list = se_df.fillna("").values
se_join_list = [''.join(row) for row in se_list]
se_replace = ['_'.join(row) for row in se_list]

def searchAddr(se_index, gijun_index):
    se_sido, se_sgg, se_emd = se_replace[se_index].split('_')
    changeTitle = "○"
    sim_sido, sim_sgg, sim_emd, sim_li = gijun_replace[gijun_index].split('_')
    add_addr(se_index, sim_sido, sim_sgg, sim_emd, sim_li, changeTitle, np.nan, np.nan, np.nan)


def nosearch_decipher(se_index, similarList):
    similer_index = max(similarList, key=similarList.get)
    se_sido, se_sgg, se_emd = se_replace[se_index].split('_')
    changeTitle = " <= DB 데이터 변경"
    sim_sido, sim_sgg, sim_emd, sim_li = gijun_replace[similer_index].split('_')
    add_addr(se_index, sim_sido, sim_sgg, sim_emd, sim_li, changeTitle, se_sido, se_sgg, se_emd)


def add_addr(se_index, sim_sido, sim_sgg, sim_emd, sim_li, changeTitle, se_sido, se_sgg, se_emd):
    change_addr[RowNum].append(se_index)
    change_addr[sido].append(sim_sido)
    change_addr[sgg].append(sim_sgg)
    change_addr[emd].append(sim_emd)
    change_addr[li].append(sim_li)
    change_addr[change_yn].append(changeTitle)
    change_addr[re_sido].append(se_sido)
    change_addr[re_sgg].append(se_sgg)
    change_addr[re_emd].append(se_emd)


########################
gijun_len = len(gijun_join_list) - 1
similarList = {}
for se_index, se_val in enumerate(se_join_list):
    similarList.clear()
    for gijun_index, gijun_val in enumerate(gijun_join_list):
        percentage = similar(gijun_val, se_val)
        if percentage == 1.0:
            searchAddr(se_index, gijun_index)
            break
        similarList[gijun_index] = percentage
        if gijun_index == gijun_len:
            nosearch_decipher(se_index, similarList)


def export_date_excel(addr):
    dataF = pd.DataFrame(addr, columns=['번호',
                                        '시도',
                                        '시군구',
                                        '읍명동',
                                        '리',
                                        '변환여부',
                                        '시도_오타',
                                        '시군구_오타',
                                        '읍명동_오타'])
    print(dataF.fillna(""))
    filename = './excel_test.xlsx'
    dataF.to_excel(filename, 'Sheet1', index=False, engine='xlsxwriter')


export_date_excel(change_addr)
