// Given an array arr[] of size N of positive integers which may have duplicates. The task is to find the maximum and second maximum from the array,
//  and both of them should be different from each other, so If no second max exists, then the second max will be -1.


#include <iostream>
#include <vector>
#include <climits>
#include <algorithm>

using namespace std;

class Solution{
public:
    vector<int> largestAndSecondLargest(int sizeOfArray, int arr[]){
        int max = INT_MIN, max2= INT_MIN;

        
        cout<<"max"<<max<<endl;
        cout<<"max2"<<max2<<endl;
        for(int i = 0; i < sizeOfArray; i++) {
            if(arr[i] > max) {
                max2 = max;
                cout<<max<<endl;
                max = arr[i];
            } else if (arr[i] > max2 && arr[i] != max) {
                max2 = arr[i];
            }
        }

        if(max2 == INT_MIN) {
            max2 = -1;
        }

        return {max, max2};
    }
};

int main() {
    int sizeOfArray;
    cin >> sizeOfArray;
    
    int arr[sizeOfArray];
    
    for(int index = 0; index < sizeOfArray; index++)
        cin >> arr[index];
    
    Solution obj;
    vector<int> ans = obj.largestAndSecondLargest(sizeOfArray, arr);
    cout<<ans[0]<<' '<<ans[1]<<endl;
	
	return 0;
}
