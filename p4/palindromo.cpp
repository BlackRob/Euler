#include<cstdlib>
#include<iostream>
#include<cmath>

using namespace std;

bool isPalindrome(int);

int main() {
	int product=0;
	
	bool palindrome=0;
	for (int i=900; i < 1000; i++) {
		for (int j=i; j < 1000; j++ ) {
			product = i*j;
			if ( isPalindrome(product) ){
				cout << i << " * " << j << " = "
				<< product << endl;
			}
		}
	}
	
	return 0;
}

bool isPalindrome(int testee){
	int digitsInTestee= 0;
	double base=10;
	while ((testee / int(pow(base,digitsInTestee))) > 0){
		digitsInTestee++;
	}
	
	int lsd, msd;
	int i = 0;
	int j = digitsInTestee - 1;
	while (i<j) {
		lsd = (testee / int(pow(base,i))) % 10;
		i++;
		msd = (testee / int(pow(base,j))) % 10;
		j--;
		if (lsd != msd) return 0;
	}
	return 1;
}

