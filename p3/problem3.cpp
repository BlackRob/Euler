//problem3.cpp
#include<iostream>
#include<cstdlib>
#include<vector>
#include<inttypes.h>

using namespace std;

uint64_t genPrime( vector< uint64_t > * );

int main(){
	// declare our number
	uint64_t elNumero = 600851475143;
	cout << elNumero << " = ";
	// a vector to hold the primes we must generate
	// this vector will only hold odd primes, meaning 2 will be treated separately
	vector< uint64_t > primeV;
	// insert an initial prime
	primeV.push_back(3);
	// divide out all "2" factors
	while (elNumero % 2 == 0){
		cout << "2 x ";
		elNumero = elNumero / 2;
	}
	// check if the largest prime in the vector is a factor of elNumero,
	// if not generate the next rpime to test
	while ( primeV.back() != elNumero ){
		// check if our number is evenly divisible by the largest prime
		if ( elNumero % primeV.back()== 0 ){
			// if so, print out prime, 
			cout << primeV.back() << " x ";
			elNumero = elNumero / primeV.back();
			// then repeat with same prime
			// (since it may be divisible multiple times)	
		}
		// if not, generate a new prime
		else {primeV.push_back(genPrime(&primeV));}
	}
	cout <<  elNumero << ".\n";
	return 0;
}

uint64_t genPrime( vector< uint64_t > *primes) {
        uint64_t  candidate = primes->back() + 2;
        int primesSize = primes->size();
       	for(int i=0; i<primesSize; i++){
		if (( candidate % primes->at(i)) == 0 ){
			i=0;
			candidate = candidate + 2;
		}
	}
        return candidate;
}

