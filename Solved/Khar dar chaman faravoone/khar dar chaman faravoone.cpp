// خر در چمن فراوونه
// ID : 9774

#include <iostream>
using namespace std;
int main()
{
    int a , b , l;
	cin >> a >> b >> l ;
	int sums = 0;
	int count = 1;

    while (count <=l) {
    
    	if (count%2 != 0){
    
    		sums += a;
    	}
    	else
    	{
    
    		sums += b;
    	}
    	
    	count += 1;
    
    }
	cout << sums;
	return 0;
}