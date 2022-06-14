def func_build_graph(S1,S2):      
    hashmap = {}
    for i in range(len(S1)):
        if (S1[i] not in hashmap): hashmap[S1[i]] = [S2[i]]
        else: hashmap[S1[i]] += [S2[i]]
        if (S2[i] not in hashmap): hashmap[S2[i]] =  [S1[i]]
        else: hashmap[S2[i]] += [S1[i]]
    return hashmap

def func_traversal(key, dict_a, visited): # Function to traverse through chars in DFS
    stack = [key]
    while (len(stack) > 0):
        elem = stack.pop()
        visited.add(elem)
        for val in dict_a[elem]:
            if (val not in visited):
                stack.append(val)
    return list(visited)


S1 = input()  # "abc","dcba"
S2 = input()  #"def","edcb"

S3 = input()  #"xyz","decb"

dict_a = func_build_graph(S1, S2)  # Function to build the hashmap
already = []
relations = []
counter = 0
for key in dict_a.keys():
    if (key not in already):
        Visited = func_traversal(key, dict_a, visited = set())# Function to traverse through chars in DFS
        relations.append(Visited)
        already.extend(Visited)
    else: pass
new_S3 = []
for char in S3:
    found = False
    for i in range(len(relations)):
        if (char in relations[i]):
            new_S3.append(min(relations[i]))    # To get small character possible for string3
            found = True
        else: pass
    if not(found):
        new_S3.append(char)
print("".join(new_S3))  # Final Lexicographically Short String result


'''
Problem Statement:
Input to your program are 3 strings S1 S2 and S3 of lower case alphabets and no spaces or special characters. S1 and S2 are the same size. Here are the constraints on S1 and S2:
In string S1 and S2 the alphabets at the same index can be replaced with each other.
If alphabet p can be replaced with q then q can also be replaced with p
If alphabet p can be replaced with alphabet q , and the alphabet q can be replaced with alphabet r then alphabet p can also be replaced with r.
1 <  length of strings  S1,S2,S3 < 999999
length of string S1 = length of string S2
All the strings consist of lowercase English letters.
Ex : You are given two strings:
S1−pqr
S2−zrg
 
Here, the alphabet p can be replaced with alphabet z, alphabet q can be replaced with r, and alphabet r with g. The alphabet q can also be replaced with g according to the 3rd rule above.

Input format
First line: String S1
Second line: String S2
Third line: String S3
Output format
You can replace any alphabet of S3 with any of these alternatives based on the properties learned from S1 and S2. By doing so you can construct many such new strings. Out of all these strings your program should output the smallest string assuming they are sorted lexicographically.



TestCase:
Input : dcba
        edcb
        decb
Output : aaaa

TestCase:
Input : gefdha
        efhagh
        hefagm
Output : aaaaam

TestCase:
Input : pistol    #S1
        poison    #S2
        toilet    #S3
Output : iiilei   #Output
'''
