//problem3.cpp
#include<iostream>
#include<cstdlib>
#include<vector>
#include<inttypes.h>

using namespace std;

uint64_t genPrime( vector< uint64_t > * );

int main(){
	// a vector to hold the primes we must generate
	// this vector will only hold odd primes, meaning 2 will be treated separately
	vector< uint64_t > primeV;
	// insert an initial prime
	primeV.push_back(3);
	//	cout << "2\n";
	// basically just loop through and generate 10001 primes:
	// but, 2 is prime 1, 3 is prime 2, and when we enter the loop 
	// the size of the vector is 1, and it has the second prime in it, so 
	// we want to go to 10000
	for ( int i=1; i<=10000; i++){
		primeV.push_back(genPrime(&primeV));
	}

	cout << primeV.back() << endl;
	
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

