#include <iostream>
using namespace std;
int main()
{
    int a,b,c,d,e;
    cin>>a>>b;
    d=a;
    e=b;
    while(b>0){
        c=a%b;
        a=b;
        b=c;
    }
    cout<<a<<" "<<(d*e)/a<<endl;
}
