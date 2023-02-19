//{ Driver Code Starts
//Initial template for C++

#include <bits/stdc++.h>
using namespace std;

class Solution{
public:
    void reverseInGroups(vector<long long>& arr, int n, int k){
        // code here
        int i = 0;
        while (i<n){
            
            int left = i;
            int right = min(i + k - 1, n - 1);
            while (left < right){
                swap(arr[right], arr[left]);
                left++;
                right--;

            }
            i+= k;
        }
    }
};

//{ Driver Code Starts.
int main() {
    int n;
    cin >> n; 
    vector<long long> arr; 
    int k;
    cin >> k; 

    for(long long i = 0; i<n; i++)
    {
        long long x;
        cin >> x; 
        arr.push_back(x); 
    }
    Solution ob;
    ob.reverseInGroups(arr, n, k);
    
    for(long long i = 0; i<n; i++){
        cout << arr[i] << " "; 
    }
    cout << endl;
  
    return 0;
}


// } Driver Code Ends