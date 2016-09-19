#include<cstdlib>
#include<iostream>
#include<limits>

using namespace std;

int main(){
	int a = 1, b = 2;
	int i = 0, sum = 2;
	for (; i < 4000000; ){
		i = a + b;
		if ( i % 2 == 0) sum = sum + i;
		a = b;
		b = i;
	}
	cout << sum << endl; 
	return 0 ;
}
