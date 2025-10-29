// هم نهشتی اعداد
// ID : 592
// https://quera.org/problemset/592/
// https://b2n.ir/295907


#include <iostream>
using namespace std;
void poo(int);
int main() {
	long long x,n,o;
	cin>>x>>n;
	o=n-x;
	if(o<0){
		o*= -1;
	}
	for(int i=2; i<=o; i++) {
		if(o%i == 0) {
			cout<<i<<" ";
		}
	}


}
