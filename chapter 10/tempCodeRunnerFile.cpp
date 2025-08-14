#include<iostream>
using namespace std;

int main(){
    int n;
    cin>>n;

    for(int i=1;; i<=n; i++){
        int ans = ans+ i;
        cout<<ans<<" ";
    }
    return 0;
}