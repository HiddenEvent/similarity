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

