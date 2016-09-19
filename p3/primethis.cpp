#include<cstdlib>
#include<iostream>
#include<vector>

using namespace std;

void factorize( unsigned long long, *vector<int> );
int genAPrime( *vector<int> );

int main(){
	unsigned long long number;
	vector<int> primes;
	primes.push_back(3);
	cout << "Enter a number, and I will factor it into primes " ;
	cin >> number;
	cout << number << " is the product ";
	while ( (number % 2) == 0){
                cout << 2 << "*";
                number = number / 2;
        }
	factorize(number, &primes);
	return 0;
}

void factorize(int number, *vector<int> primes){
	if (number == 1 ) {
		cout << endl;
		return;
	}
	int next_prime = *primes.back() );
	while ( (number % next_prime) == 0){
		cout << next_prime << "*";
		number = number / next_prime;
	}
	genAPrime( &primes );
	factorize (number, &primes);
	return;
}

int genAPrime( *vector<int> primes) {
	int vectorlength = int (primes.size());
	int candidate = *primes.back() + 2;
	bool candiIsPrime=0;
	do {	
		for (int i=0; ; i++) {
			if (( candidate % primes.at(i) ) == 0 ) break;
		
		}
		
	} while ( !candiIsPrime);
	
	return candidate;
}
	
