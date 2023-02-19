#include<iostream>
using namespace std;

int elementint(int arr[], int n, int ele){
    arr[n] = ele;
    for (int i = 0; i < n+1; i++){
        cout << arr[i] << endl;
    }
    return 0;
}

int main(){
    int arr[] = {1, 2, 3, 4};
    int ele = 10;
    int n = sizeof(arr) / sizeof(arr[0]);
    elementint(arr, n, ele);
    return 0;
}
