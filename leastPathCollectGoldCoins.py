def findPathGold(matrix, current, dest, temp = []):
    A= [1,2]
    row, col = current[0],current[1]
    if(row<0 or col<0 or row>=len(matrix) or col>=len(matrix[0]) or (row,col) in temp or matrix[row][col]== 1):
        return
    if ((current[0],current[1]) in dest):
        '''if not set(temp+[(row,col)]).issuperset(set(gold_coins)):
            return'''
        if main_list == []:
            main_list.append(temp+[(row,col)])   
        elif len(temp+[(row,col)]) < len(main_list[0]):
                main_list[0] = temp+[(row,col)]
        return 
    findPathGold(matrix,[row+1,col],dest ,temp + [(row,col)] )
    
    findPathGold(matrix,[row,col+1],dest ,temp + [(row,col)] )
    
    findPathGold(matrix,[row-1,col],dest ,temp + [(row,col)] )
    
    findPathGold(matrix,[row,col-1],dest ,temp + [(row,col)] )
    

matrix=[[0,0,0],
        [2,1,0],
        [2,1,0]]
main_list = []
gold_coins = []
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == 2:
            gold_coins.append((i,j))
findPathGold(matrix, [0,0], [(2,2)])
path = main_list[0] if main_list!=[] else -1
if path != -1:
    for coin in gold_coins:
        if coin not in path:
            findPathGold(matrix, list(coin), path)
            new_path = main_list[0] #path of remained gold coin with reference to existing path
            start = new_path[-1]
            index = path.index(start)
            path = path[:index+1] + new_path[:-1][::-1] + new_path[1:] + path[index+1:]         #combining the new path in path
            main_list = []
print(path)


'''
Problem Statement:
Given a matrix. find the path from source being given as position of integer 2 towards the destination by collecting all the gold coins in the middle with least possible travel path.

TestCase:
Input : [[0,0,0],
        [2,1,0],
        [2,1,0]]
Output : [(0, 0), (1, 0), (2, 0), (1, 0), (0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]

TestCase:
Input : [[0,0,0],
        [2,1,0],
        [2,0,0]]
Output : [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]

TestCase:
Input : [[0,0,0],
        [2,1,2],
        [2,0,0]]
Output : [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (1, 2), (2, 2)]

TestCase:
Input : [[0,0,2],
        [2,1,2],
        [2,0,0]]
Output : [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (1, 2), (0, 2), (1, 2), (2, 2)]


Or the quest is to find whether there is a way of collecting all gold at a time in forwardonly path then the code part which is commented in defined function
will take care of the case.

'''
