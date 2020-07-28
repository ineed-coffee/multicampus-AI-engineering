# n = int(input('n 값을 입력 : '))

# i=0
# s=0
# while i<=n:
#     s+=i
#     i+=1
# print(s)

# from array import *

# arr1 = array('i',[10,20,30,40])
# print(arr1)

# arr1.insert(1,100)
# print(arr1)

# arr1.remove(30)
# print(arr1)

# arr3 = [None]*3

# arr3[0]=int(input())
# arr3[1]=int(input())
# arr3[2]=int(input())

# Max_val = arr3[0]
# if arr3[1]>Max_val: Max_val=arr3[1]
# if arr3[2]>Max_val: Max_val=arr3[2]
# print(Max_val)

# def maxvalue(in_list):
#     if not in_list:
#         return None

#     return_val = in_list[0]
#     for i in in_list:
#         if i> return_val: return_val=i
#     return return_val


# def reversearr(arr_in):
#     L=len(arr_in)
#     for i in range(L//2):
#         arr_in[i],arr_in[L-1-i]=arr_in[L-1-i],arr_in[i]

# import numpy as np

# d = np.array([[1,2,3,4],[2,3,4,5],[3,4,5,6]])
# print(d)

class LinearSearch:

    def __init__(self,data,key):
        self.__data = data
        self.__key = key

    def getSearchExist(self):
        for i in self.__data:
            if i == self.__key:
                return True
        return False

    def getSearchCount(self):
        return_value=0
        for i in self.__data:
            if i == self.__key:
                return_value+=1
        return return_value

    def getSearchElements(self):
        return_list =[]
        for i in range(len(self.__data)):
            if self.__data[i]==self.__key:
                return_list.append(self.__data[i])
        return return_list

    def getSearchIndexes(self):
        return_list =[]
        for i in range(len(self.__data)):
            if self.__data[i]==self.__key:
                return_list.append(i)
        return return_list

L = LinearSearch(list(range(100)),5)