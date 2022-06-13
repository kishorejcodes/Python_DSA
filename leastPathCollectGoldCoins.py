def findPathGold(matrix, current, temp = []):
    row, col = current[0],current[1]
    if(row<0 or col<0 or row>=len(matrix) or col>=len(matrix[0]) or (row,col) in temp or matrix[row][col]==1):
        return
    if ((current[0],current[1]) == (len(matrix)-1, len(matrix)-1)):
        if main_list == []:
            main_list.append(temp+[(row,col)])
        elif len(temp+[(row,col)]) < len(main_list[0]):
                main_list[0] = temp+[(row,col)]
        return
    findPathGold(matrix,[row+1,col],temp + [(row,col)] )
    findPathGold(matrix,[row,col+1],temp + [(row,col)] )
    findPathGold(matrix,[row-1,col],temp + [(row,col)] )
    findPathGold(matrix,[row,col-1],temp + [(row,col)] )
    

matrix=[[0,2,0],[0,1,1],[0,0,0]]
main_list = []
for i in range(len(matrix[0])):
        if matrix[0][i] == 2:
            start = [0,i]
findPathGold(matrix, start)
print(main_list[0])


'''
Problem Statement:
Given a matrix. find the path from source being given as position of integer 2 towards the destination by collecting all the gold coins in the middle with least possible path.




'''
