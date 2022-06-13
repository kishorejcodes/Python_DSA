def find_the_tic_tac_toe_winner(list_x):
    zero_count = 0
    cross_count = 0
    #row wise check
    for row in list_x:
        zero_count = max(row.count("O"),row.count("o"))
        cross_count = max(row.count("X"),row.count("x"))
        if zero_count == 3 or cross_count == 3:
            return zero_count,cross_count
    #column wise check
    zero_count = 0
    cross_count = 0
    for j in range(len(list_x[0])):
        zero_count = 0
        cross_count = 0
        for i in range(len(list_x)):
            if list_x[i][j] in "oO" :
                zero_count += 1
            elif list_x[i][j] in "xX":
                cross_count += 1
        if zero_count == 3 or cross_count == 3:
            return zero_count,cross_count
    #diagonal wise check
    zero_count = 0
    cross_count = 0
    for i in range(len(list_x)):
        if list_x[i][i] in "oO" :
                zero_count += 1
        elif list_x[i][i] in "xX":
                cross_count += 1
    if zero_count == 3 or cross_count == 3:
            return zero_count,cross_count
    zero_count = 0
    cross_count = 0
    for i in range(len(list_x)):
        len_x = len(list_x) - 1
        if list_x[i][len_x - i] in "oO" :
                zero_count += 1
        elif list_x[i][len_x-i] in "xX":
                cross_count += 1
        if zero_count == 3 or cross_count == 3:
            return zero_count,cross_count
    return zero_count,cross_count


grid_matrix = [["*"]*3 for i in range(3)]
print("GAME START:\nEnter row, column, symbol(X/O)\nex- 2 1 X :")
already = []
i = 0
prev = None
while True:
    try:
        m,n, sym = input().split()
        if sym not in "oOxX" or sym == prev:
            raise ValueError
        if (m,n) in already:
            print("Enter valid co-ordinates:")
            continue
        already.append((m,n))
    except:
        print("Enter valid inputs")
        continue
    m, n = int(m), int(n)
    prev = sym
    grid_matrix[m][n] = sym
    print("-"*10)
    for row in grid_matrix:
        print(" ".join(row))
    print("")
    print("-"*10)
    result = find_the_tic_tac_toe_winner(grid_matrix)
    zero_count, cross_count = result
    if zero_count == 3:
        msg = "##   O_Symbol Won   ##"
        print("#"*len(msg))
        print("##" + " "*(len(msg)-4) + "##")
        print(msg)
        print("##" + " "*(len(msg)-4) + "##")
        print("#"*len(msg))
        break
    elif cross_count == 3:
        #print("X_symbol Won")
        msg = "##   X_Symbol Won   ##"
        print("#"*len(msg))
        print("##" + " "*(len(msg)-4) + "##")
        print(msg)
        print("##" + " "*(len(msg)-4) + "##")
        print("#"*len(msg))
        break
    elif i==8:
        print("Tie")
        msg = "##      Tie      ##"
        print("#"*len(msg))
        print("##" + " "*(len(msg)-4) + "##")
        print(msg)
        print("##" + " "*(len(msg)-4) + "##")
        print("#"*len(msg))
        break
    i += 1
