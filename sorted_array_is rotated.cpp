#include<bits/stdc++.h>
using namespace std;

bool checkRotatedAndSorted(int arr[], int n){
    int x = 0, y = 0;
    for(int i = 0; i < n-1; i++){
        if(arr[i] < arr[i+1]){
            x++;
        }else{
            y++;
        }
    }

    if(y == 1){
        if(arr[n-1] < arr[0]){
            x++;
        }else{
            y++;
        }

        if(y == 1){
            return true;
        }
    }

    return false;
}


int main()
 {
	// int T;
	// //testcases
	// cin>> T;
	
	// while (T--){
    int num;
    //size of array
    cin>>num;
    int arr[num];
    
    //inserting elements
    for(int i = 0; i<num; ++i)
        cin>>arr[i];
    
    bool flag = false;
    // Solution ob;
    
    //function call
    flag = checkRotatedAndSorted(arr, num);
    
    //printing "No" if not sorted and
    //rotated else "Yes"
    if(!flag){
        cout << "No"<<endl;
    }
    else
    cout << "Yes"<<endl;
// 
	// }
	
	return 0;
}

// {1, 3, 4, 2, 6, 5, 8, 7}