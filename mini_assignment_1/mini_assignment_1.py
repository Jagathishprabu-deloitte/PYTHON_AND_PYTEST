from collections import Counter
from itertools import combinations


class StringClass:
    def __init__(self, value):
        self.str = value

    def length(self):
        return len(self.str)

    def arraylist(self):
        return list(self.str)


class PairsPossible(StringClass):
    def pairs(self):
        pair_possible = list(combinations(self.str, 2))
        return pair_possible


class SearchCommonElements:
    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2

    def common_elements(self):
        dict1 = Counter(set(self.str1))
        dict2 = Counter(set(self.str2))
        final_dict = dict(dict1.items() & dict2.items())
        common_list = []
        for(key, val) in final_dict.items():
            for i in range(0, val):
                common_list.append(key)
        return common_list


class EqualSumPairs(PairsPossible):
    def count(self):
        pair_obj = PairsPossible(self.str)
        pair_list = pair_obj.pairs()
        equal_sum_list = []
        for i in pair_list:
            sum_value = 0
            for j in i:
                sum_value += int(j)
            equal_sum_list.append(sum_value)
        return len(set(equal_sum_list))


stringValue1 = input("Enter String: ")
stringListObject = StringClass(stringValue1)
print("Length of the String: ")
print(stringListObject.length())
print("List of String: ")
print(stringListObject.arraylist())

stringValue2 = input("Enter String: ")
pairsPossibleObject = PairsPossible(stringValue2)
print("Pairs Possible are: ")
print(pairsPossibleObject.pairs())

commonElementsObject = SearchCommonElements(stringValue1, stringValue2)
print("Common Elements are: ")
print(commonElementsObject.common_elements())

equalSumObject = EqualSumPairs(stringValue2)
print("Count of unique sums: ")
print(equalSumObject.count())
