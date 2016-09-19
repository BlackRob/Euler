#include<iostream>
#include<fstream>
#include<iomanip>
#include<vector>
#include<math.h>
#include<inttypes.h>

using namespace std;

int testPrime(int x, vector<int> * );  // returns x if x is prime, 0 if not

int main()
{
	ofstream fout;
//	fout.open("generated_primes",fstream::out);
	
	vector<int> primes;
	uint64_t sum = 0;
	// 2,3 and 5 are not placed in vector, but 7 will be
	primes.push_back(7);
//	fout <<  setw(7) << '2' <<  setw(7) << '3' <<  setw(7) << '5' << setw(7) << '7';
	// sum so far
	sum = 2 + 3 + 5 + 7;
	int primecount = 4;
	// How this works:
	// in order to make our search for primes more efficient,
	// we will examine four candidates each time through a loop
	// each loop will cover ten integers; we will not test even
	// numbers or numbers ending in 5, as besides 2 and 5, these
	// numbers will not be prime;
	// we will then check these four candidates against a simple test 
	// (is it a multiple of 3?), then if they pass check them against
	// the primes we already found and placed in our vector, 
	// starting with 7 
	int candi[4] = {11,13,17,19};
	int maxPrime =  2000000;
	int working_decade = 10;
	int temp;
//	fout << '\n' << "primes.at(0) = " << primes.at(0) << '\n' ;
	
	while (working_decade < maxPrime){
		if (!(candi[0] % 3 == 0)){
			temp = testPrime(candi[0],&primes);
			sum = sum + temp;
			if (temp != 0) {
//				fout <<  setw(7) << temp ;
				primecount ++;
				if (primecount % 10 == 0) fout << endl;
			}
		}
		candi[0] = candi[0] + 10;
		
		if (!(candi[1] % 3 == 0)){
			temp = testPrime(candi[1],&primes);
			sum = sum + temp;
			if (temp != 0) {
//				fout <<  setw(7) << temp ;
				primecount ++;
				if (primecount % 10 == 0) fout << endl;
			}
		}
		candi[1] = candi[1] + 10;
		
		if (!(candi[2] % 3 == 0)){
			temp = testPrime(candi[2],&primes);
			sum = sum + temp;
			if (temp != 0) {
//				fout <<  setw(7) << temp ;
				primecount ++;
				if (primecount % 10 == 0) fout << endl;
			}
		}
		candi[2] = candi[2] + 10;
		
		if (!(candi[3] % 3 == 0)){
			temp = testPrime(candi[3],&primes);
			sum = sum + temp;
			if (temp != 0) {
//				fout <<  setw(7) << temp ;
				primecount ++;
				if (primecount % 10 == 0) fout << endl;
			}
		}
		candi[3] = candi[3] + 10;
		
		working_decade = working_decade + 10;
	}
	
	cout << "Sum = " << sum <<  endl;
	// fout.close();
	return 0;
}

int testPrime(int candidate, vector<int> *primes) {
        //cout << candidate << ' ';
        int psize = primes->size();
        //cout << "psize = " << psize;
        int temp = 0;
       	for(int i=0; i < psize; i++){
		temp = candidate % primes->at(i);
//		cout << primes->at(i) << ' ';
		if (temp == 0 ){
			return 0;
		}
	}
	primes->push_back(candidate);
	//cout << '\n';
        return candidate;
}

