# hi guys in this video we will create bubble sort algorithm in python

def sort(List):
    items = len(List)

    for i in range(items):
        for j in range(items - i - 1):
            if (List[j] > List[j+1]):
                List[j] , List[j+1] = List[j+1] , List[j]

    return List

# input data
Input = [10,2,3,4,489,213,25,123]
# test 
print(sort(Input))
print("worked !!!")