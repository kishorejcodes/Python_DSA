def solution(R):
    # write your code in Python 3.6
    rev_R = R[::-1]
    timeDict = {"S":[30,40], "A":[20,5]}
    on_foot = 0
    on_scoo = 0
    temp1, temp2, temp3 = 0, 0, 0
    state = False
    result, result2 = 0, 0
    total = 0
    for seg in rev_R:
        #print(seg)
        f, s = timeDict[seg]
        on_foot += f
        on_scoo += s
        total += s
        if on_foot < total:
            result2 = on_foot
            temp3 = total
        if on_foot <= on_scoo  and f < s:
            #print("If")
            temp1 += f
            temp2 += s
            state = True
        else:
            #print("Else")
            result += temp1
            on_scoo = on_scoo - temp2
            temp1, temp2 = 0, 0
            state = False
        #print(on_foot, on_scoo)
    output1 = on_scoo + result
    output2 = total - temp3 + result2
    if state:
        output1 = output2
    #output1 = on_scoo + result
    #print(result)    
    return (min(output1, output2))
    

string = input()
solution(string)    #function to find the shortest time

'''
Problem Statement:
You have to be at your work as soon as possible. The road on your route to work may consist of two types of surface: asphalt or sand. To simplify the description, it will be denoted by a string R consisting only of the letters: "A" for an asphalt segment and "S" for a sand segment. All segments represent the same distance. For example, R = "SAAS" describes a road comprising of sand, asphalt, asphalt and sand segments.

When you go on foot, you need 20 minutes to pass through an asphalt segment and 30 minutes through a sand segment. You also have an electric scooter, which needs 5 minutes to pass through an asphalt segment and 40 minutes through a sand segment.

You start your journey on the scooter, but at any point you can get off the scooter and go on foot for the rest of the journey. What is the shortest time in which you can get to work?


TestCase:
Input : "SSA"
Output: 80

TestCase:
Input : "ASAASS"
Output: 115

TestCase:
Input : "SSSSAAA"
Output: 175




'''


