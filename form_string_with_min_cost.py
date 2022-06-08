def combocheck(words, s, outstr="", outsum=0):
    if s == outstr:
        main_list.append(outsum)
    if len(outstr) > len(s) or outstr not in s:
        return
    for word in words:
        combocheck(words,s,outstr+word,outsum+w_pMap[word])


string = "lockdown"
words = ["lock", "down", "lo", "ck"]
prices = [50, 50, 5, 5]
main_list = []
w_pMap = {words[i]:prices[i] for i in range(len(words))}
combocheck(words, string)
print(min(main_list))


'''
Problem Statement:
Given a string and a list of sub strings and corresponding prices list. Have to find the minimum cost to form the desired string using all available sub-strings.

TestCase:
Input : "lockdown"
        lock down lo ck
        50 50 5 5
Output : 60

TestCase:
Input : "hello"
        hell he l lo o
        50 20 15 25 15
Output : 60

Explanation : 
  desired_string : "hello"
  ways : 1) "hell" + "o" but costs 50 + 15 = 65
         2) "he" + "l" + "lo" costs 20 + 15 + 25 = 60     
  So, the minimum cost to form the string is 60.
         
'''
