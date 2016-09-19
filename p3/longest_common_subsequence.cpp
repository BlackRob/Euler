/*	Rob Austin's solution to problem 5, Homework 8, CSE 331
*	Program implements the dynamic programming algorithm as described
*	in the class notes.  This program assumes that the input will be in the
*	form of a readable ascii text file; it searches for the longest common 
*	subsequence of capital letters, and will ignore lowercase letters, numbers,
*	punctuation marks or non-printing characters.
*	
*******************************************************************************/

#include<iostream>
#include<string>
#include<cstdlib>
#include<fstream>
#include<vector>

using namespace std;

void getData( vector<char>* );

int main(){
	// tell user what's going on
	cout << " This program accepts two files and compares them to find the " 
		<< "longest subsequence they have in common.  The user should know: " 
		<< endl << "   - the subsequence will only consist of uppercase, "
		<< "printable ascii characters " << endl << "   - the files must exist, "
		<< "be in the present working directory, and be readable " << endl
		<< endl;
	// read in data:
	vector<char> v1;
	vector<char> v2;
	getData(&v1);
	getData(&v2);
	int size1 = v1.size();
	int size2 = v2.size();
	
	// a little test for my getData function
	cout << "This is what I have for v1" << endl;
	for (int i=0; i < size1; i++){
		cout << v1.at(i); }
	cout << endl << "Size of v1: " << size1;
	cout << endl << "This is what I have for v2" << endl;
	for (int j=0; j < size2; j++){
		cout << v2.at(j); }
	cout << endl << "Size of v2: " << size2;
  
	// find longest common substring of v1 and v2
	// first, create and fill in table
	
	int table[size1+1][size2+1];
	for (int i=0; i <= size1; i++) {
		for (int j=0; j <= size2; j++) {
			table[i][j]=0; }
		}	

	for (int i=1; i <= size1; i++){
		for (int j=1; j <= size2; j++) {
			if ( v1.at(i-1) == v2.at(j-1) ) 
				table [i][j] = table[i-1][j-1] + 1;
			else { 
				table[i][j] = table[i-1][j];
				if (table[i][j-1] > table[i][j])
					table[i][j] = table[i][j-1];
				}
			}
		}

	// second, examine the table to find and print a longest common subsequence
	// to do this, we must first create a data structure to hold the LCS 
	// temporarily, because it will be traced out of the table in reverse order;
	// we then we read it out of the DS backwards, and we're done
	vector<char> scl;
	
	for ( int j = size2; j > 1;) {
		for ( int i = size1; i > 1;) {
			if ( table[i][j] == table[i][j-1] ) j--;
				else if ( table[i][j] == table[i-1][j] ) i--;
					else { i--; j--; scl.push_back( v1.at(i));}
			}
		}
	
	cout << endl << "Length of longest common subsequence : "; 
	cout << table[size1][size2] << endl;
	cout << "A longest common subsequence : ";
	while (!scl.empty()){
		cout << scl.back();
		scl.pop_back();
		}
	cout << endl;
	return 0;
	}

void getData( vector<char>* vctr ){
	string flname;
	char tmp;
	ifstream streamy;
	// do all this until we get a valid file name
	while ( vctr->empty() ) {
		// ask for file
		cout << "Please enter the name of a file " ; 
		// read in name of file
		getline(cin,flname);
		// try to open file
		streamy.open(flname.c_str());
		if (!streamy) {
			cout << "I either cannot find or cannot read that file.  Try again\n";
			}
		// if file opened, read all the uppercase characters into the vector
		else {
			while (!streamy.eof()) {
				streamy.get(tmp);
				if ((tmp >= 65) && (tmp <= 90)){
					vctr->push_back(tmp);
					}
				}
			} 	
		}
	// if all went well, close file
	streamy.close();
  }
	
