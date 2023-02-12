
#Question1: **Tralling factorials of zero**

formula is= [n/5] + [n/25] + [n/125]..........n
how many zeros are their in number at the end.
#include<iostream>
using namespace std;

int main(){
	int res = 0;
	int n = 10;
	for(int i=5; i<n; i=i*5){
		res = res + (n/i)
	}
	cout<<"result is:"<<res;
	return 0;
}

#**Question2**: **Given an array of N integers. Find the first element that occurs at least K number of times**.

Input :
N = 7, K = 2
A[] = {1, 7, 4, 3, 4, 8, 7}
Output :
4
Explanation:
Both 7 and 4 occur 2 times. 
But 4 is first that occurs 2 times
As at index = 4, 4 has occurred 
atleast 2 times whereas at index = 6,
7 has occurred atleast 2 times.

>>>>>> code write <<<<<<<<<
class Solution:
    def firstElementKTime(self,  a, n, k):
        # code here
        test= {}
        for i in range(0,len(a)):
            if(a[i] in test.keys()):
                test[a[i]]+=1
            else:
                test[a[i]] = 1
            if(test[a[i]] == k):
                return a[i]
                break
        return -1
        
#**Question3**: **how many balloon we can create from given string S**

Input:
S: loonbalxballpoon
Output: 2
Explanation:
Here, the number of occurence of 'b' = 2
of occurence of 'a' = 2
of occurence of 'l' = 4
of occurence of 'o' = 4
of occurence of 'n' = 2
So, we can form 2 "balloon" using the letters.

>>>>>>code<<<<<<<<<
def maxInstance (s : str) -> int:
    t = 'balon'
    count = 0
    test = {}
    result = 0
    co = 0
    for i in range(len(s)):
        if(s[i] in test.keys()):
            test[s[i]] += 1
        else:
            test[S[i]] = 1
    for i in range(len(t)):
        if t[i] in test.keys():
            count += test[t[i]]
    b= test['b']
    a = test['a']
    l = test['l']
    o = test['o']
    n = test['n']
    while count >0 :
        if b >=1 and a >=1 and l >=2 and o >= 2 and n >=1:
            co +=1
            # print("balloon")
            b = b - 1 
            a = a - 1
            l = l - 2
            o = o - 2
            n = n - 1
        count -= 1 
    return co
<!-- # S = 'bnlbllanmbaamnmobbanablboolonlol' -->
<!-- # S= 'loonbalxballpoon' -->
S = 'nlaebolko'
print(maxInstance(S))

