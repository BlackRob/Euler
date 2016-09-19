#include<iostream>

using namespace std;

int main()
{
	int count = 3;
	int divisors = 0;
	int triangleNumber = 3;
	cout << "1: 1\n";
	int dividend = 0;
	for(; divisors <= 500; count++){
		divisors=0;
		cout << triangleNumber << ": ";
		for (int i = 1;; i++){
			dividend = triangleNumber / i;
			if (triangleNumber % i == 0){
				if (dividend <= i){
					cout << "\nDivisors = " << divisors << '\n';
					break;
				}
				cout << i << ", " << dividend << ' ';
				divisors = divisors + 2;
			}
		}
		triangleNumber = triangleNumber + count;
		cout << '\n';
	}
	return 0;	
}
