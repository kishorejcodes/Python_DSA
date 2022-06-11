# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import time
class Test:
    def removeReverse(self,S): 
        #code here
        for char in S:
            if S.count(char) > 1:
                S = S.replace(char, "", 1)
                S = self.removeReverse(S[::-1])
                break
        return S

t0 = time.time()        
obj = Test()
print(obj.removeReverse("dcdbeadadcdbeadadcdbeadadcdbeadadcdbeadadcdbeadadcdbeadadcdbeadadcdbeadadcdbeadadcdbeadadcdbeadadcdbeadadcdbeadadcdbeadadcdbeadadcdbeadadcdbeadadcdbeadadcdbeadadcdbeadadcdbeadadcdbeadadcdbeadadcdbeadadcdbeadadcdbeadadcdbeadadcdbeadadcdbeadadcdbeadadcdbeadadcdbeadadcdbeadadcdbeadadcdbeadadcdbeadadcdbeadadcdbeadadcdbeadadcdbeadadcdbeadadcdbeadadcdbeadadcdbeadadcdbeadadcdbeadadcdbeadadcdbeadadcdbeadadcdbeadadcdbeadadcdbeadadcdbeadadcdbeadadcdbeadadcdbeadadcdbeadadcdbeadadcdbeadadcdbeadadcdbeadadcdbeadadcdbeadadcdbeadadcdbeadadcdbeadadcdbeadadcdbeadadcdbeadadcdbeadadcdbeada"))
t1 = time.time()
print(t1- t0)

'''
Problem Statement:
Given a string S which consists of only lower case English
alphabets. you have to perform the below operations: If the string S
contains any repeating character and reverse the string and again perform 
the above operation on the modified string,
otherwise , you stop.
You have to find the final string.

Testcase:
Input : S = "abab"
Output : ba
Explanation:
The first non repeating character is a. after removing the first
character , S="bab" .After reversing the string S = "bab".
In 2 nd operation: the first non repeating character is b.After removing and reversing S = "ba".
Now the string doesn't contain any repeating character.

'''