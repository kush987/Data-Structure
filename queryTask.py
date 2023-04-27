''' Given a string s whose length is n and array queries of length q where each elements of queries is either of type 1 query or type 2 query which is explained ahead.

There are two types of query.

Query type 1 : ["1",ind,char]  "1" denotes this is type 1 query. In this query you have to change the character at index ind in s to character char.(Data type of ind,char is string in input)

Query Type 2: ["2",left,right,k]  "2" denotes this is type 2 query. In this query you have to return kth lexographically largest character  in the subtring of s (it is the kth largest character in sorted order , not the kth distinct character) starting from index left and ending at index right both left and right are inclusive. (Data type of left,right,k is string in input)

You have to perform each query in the same order as given in  queries and return an array res such that res array contains the answer for each type2 query in same order as it appeared in queries.

Note : 0 based indexing is used. '''

''' EXAMPLE 1:
Input:
n=4
s="abab"
q=2
queries={{"1","2","d"},{"2","1","3","1"}}
Output: 
{"d"}
Explanation:
First query is of type 1 so after changing character at index 2 
to d  s becomes abdb . Now Second query is of type 2 in which 
the 1st(k=1) lexographically largest character is "d" in substring "bdb"(s[1:3]). So we 
returned a array with result of type 2 query {"d"}. '''

''' EXAMPLE 2:
Input:
n=3
s="aaa"
q=3
queries={{"1","1","e"},{"1","2","c"},{"2","1","2","2"}}
Output:
{"c"}
Explanation:
After applying first two queries s becomes aec. Now for 
the last query which is a type 2 second largest character 
in subtring s starting from index 1 to ending at index 2 is "c". '''




from typing import List


class Solution:
    def easyTask(self, n, s, q, queries) -> List[int]:
        # code here
        res = []
        for i in queries:
            if i[0] == "1":
                b_s = list(s)
                b_s[int(i[1])] = i[2]
                s = "".join(b_s)
            elif i[0] == "2":
                b_s = list(s)
                res.append(sorted(b_s[int(i[1]):int(i[2])+1],reverse=True)[int(int(i[3])-1)])
        return res
    
        # res = []
        # for i in queries:
        #     if i[0] == "1":
        #         ind, char = int(i[1]), i[2]
        #         s = s[:ind] + char + s[ind+1:]
        #     else:
        #         left, right, k = int(i[1]), int(i[2]), int(i[3])
        #         substr = s[left:right+1]
        #         res.append(sorted(substr, reverse=True)[k-1])
        # return res

n = int(input("size of string>>: " ))
s = input("please enter the string of n size: ").strip()
q = int(input("please choose the number of queries: "))
que = []
for i in range(q):
    qe = input().split()
    if qe[0] == "1":
        que.append([qe[0],qe[1],qe[2]])
    else:
        que.append([qe[0],qe[1],qe[2],qe[3]])

# print(n,s,q, que)
obj = Solution()
res = obj.easyTask(n,s, q, que)
print(res)
# 4
# abab
# 2
# 1 2 d
# 2 1 3 1

# 3
# aaa
# 3
# 1 1 e
# 1 2 c
# 2 1 2 2

# 10
# bjryukrooy
# 3
# 2 2 6 1
# 1 2 x
# 2 7 8 2
