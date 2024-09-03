#include <iostream>
using namespace std;

int main() {

    int y,x,sum,r;
    cin >> y;
    sum=0;
    x = y;
    while (x>0)
    {
        r = x%10;
        x = x /10;
        sum = sum *10 + r;
    }
    if(sum == y)
    {
        cout << "YES";
    }
    else
    {
        cout << "NO";
    }

    return 0;
}
