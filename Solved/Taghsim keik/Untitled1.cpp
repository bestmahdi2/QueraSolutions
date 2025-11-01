#include <iostream>
#include<math.h>
#include <bits/stdc++.h>
using namespace std;
int poop(int m)
{
    int t=log2(m);
    if(log2(m) == t)
    {
        return t;
    }
    else return -1;

}
int gcd(int x, int y)
{
	if (x < y)
	{
		int temp = x;
		x = y;
		y = temp;
	}

	while (y != 0)
	{
		int remainder = x % y;
		x = y;
		y = remainder;
	}

	int r = x;
	return r;
}
int main()
{
    int a,n,b;
    cin>>n;
    int s[n];
    for(int i=0; i<n; i++)
    {
        cin>>a>>b;
        int t=gcd(a,b);
        a/=t;
        b/=t;
        s[i]=poop(b);
    }
    for(int i=0; i<n; i++)
    {
        cout<<s[i]<<endl;
    }
}
