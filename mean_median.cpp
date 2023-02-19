#include<bits/stdc++.h>
using namespace std;

class Solution{
    public:
    //Function to find median of the array elements.
    int median(int A[],int N)
    {
        
        sort(A,A+N);
        
        if (N%2 != 0){
            return (double)A[N/2];
        }
        return (double)(A[(N - 1) / 2] + A[N / 2]) / 2.0;
        //your code here
        //If median is in fraction then convert it to integer and return
    }
    //Function to find mean of the array elements.
    int mean(int A[],int N)
    {
        //your code here
        double count = 0;
        for(int i = 0;i<N;i++)
            count += A[i];
        return (double)count/(double)N;
    }
};


//{ Driver Code Starts.

int main()
{
    //testcase
    // int T;
    // cin>>T;
   
    //looping testcase
    // while(T--)
    // {
        //number of elements in array
    int N;
    cin>>N;
    int a[N];
    
    //inseting elements in the array
    for(int i=0;i<N;i++){
        cin>>a[i];
    }
    Solution ob;
    cout<<ob.mean(a,N)<<" "<<ob.median(a,N)<<endl;
    // }
    return 0;
}

// {1, 3, 4, 2, 6, 5, 8, 7}