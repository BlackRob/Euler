#include<cstdlib>
#include<iostream>

using namespace std;

int main()
{
	int sum = 0;
	for (int i=3; i<1000; i=i+3){
		sum = sum + i;
	}
	for (int i=5; i<1000; ){
		sum = sum + i ;
		i=i+5;
		if (i%15 == 0) i=i+5;
	}
	cout << sum << endl;
	return 0;

}
