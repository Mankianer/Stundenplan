import mankianerplan
from mergedeep import merge

print("Hallo")

if __name__ == '__main__':
    dict1 = {"test": {"test2": "test2"}, "test3": "test3"}
    dict2 = {"test": {"test": "test"}}

    dict3 = merge(dict1, dict2)
    print(dict3)