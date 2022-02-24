#include <iostream>
using namespace std;
int main(){
    int n,fact;
    fact=1;
    cin >> n;

    while (n>0)
    {
        fact = fact*n;
        n=n-1;
    }
    cout<<fact<<endl;
    return 0;
}
