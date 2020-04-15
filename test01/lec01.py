from difflib import SequenceMatcher
import operator
# from scipy import spatial
#
#

dataSetI = ["서울","신도림","대구","대전"]
dataSetII = ["서울","신도림"]
intList = {}
# result = 1 - spatial.distance.cosine(dataSetI, dataSetII)
# print(result)
# for x in range(10):
#     # intList.clear()
#     print(intList)
#     for i, v in enumerate(dataSetI):
#         intList[i] = v
#
# print(intList)

# testdic = {'서울': 0.1, '대전': 0.2, '대구':0.5 , '대전':0.2}
# print(max(testdic.values()))

state = {1:1000, 2:3000, 3: 100, 4:3000}
result = max(state, key=state.get)
print(result)

# def similar(a, b):
#     return SequenceMatcher(None, a, b).ratio()
# result = similar("서울","서울") #would have a high prob.
# if result == 1.0 :
#     print(result)
#
# print()
# index, sim_sido, sim_sgg, sim_emd, sim_li, changeTitle,se_sido, se_sgg, se_emd
search_addr = {
    'RowNum': [],
    '시도': [],
    '시군구': [],
    '읍명동': [],
    '리': [],
    '변환여부': [],
    '시도_오타': [],
    '시군구_오타': [],
    '읍명동_오타': [],
}
nosearch_addr = {}
search_addr['RowNum'].append(1)
search_addr['RowNum'].append(2)
print(search_addr)