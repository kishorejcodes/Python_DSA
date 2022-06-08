def func(list_x, SUM=0):
    for item in list_x:
        if type(item)==list:
            SUM = func(item,SUM)
        else:
            SUM += item
    return SUM


liLi = [[1,2,[1,2,[1,4,9]]],1,2,[1,1000]]
print("SUM:",func(liLi))


'''
Problem Statement:
Given the major list that could contain even more lists nested inside. Sum of all the numbers in major list should be found.

TestCase:
Input: [[1,2,[1,2,[1,4,9]]],1,2,[1,1000]]
Output: SUM:1024

TestCase:
Input: [9,4,7,[1,[3,7],10],11]
Output : 52

'''
