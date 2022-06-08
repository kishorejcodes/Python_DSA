def func(s):
    i = len(s)
    while i>=0:
        if (s[:i] == s[:i][::-1]):
            return s[i:][::-1] + s
        i -= 1


string = "kissiking"
result = func(string)
print(result)
print(len(result)-len(string))

'''
Problem Statement:
Given a string. You have make it a palindrome by adding any characters at the leftside of string and find the minimum operations needed to make.

TestCase:
Input : "kissiking"
Output : "gnikissiking"
         3
         
TestCase:
Input : "fghijihgfedcba"
Output : "abcdefghijihgfedcba"
         5
         
TestCase:
Input : "ksolais"
Output : "sialosksolais"
         6
'''
