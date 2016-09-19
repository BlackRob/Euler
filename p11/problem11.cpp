/* Problem 11 from project euler;
* given a 20x20 grid of 2 digit numbers, find the greatest product of 
* any four adjacent numbers (horizontal, vertical or diagonal)
*/

#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;

int main()
{
	int gp=0;	// greatest product
	int cp=0;	// current product
	/* we need to create and fill our array;
	the numbers will be read from an external file
	*/
	int g[20][20];
	ifstream gridfile;
	gridfile.open("grid");
	
	for (int i =0; i<20; i++){
		for (int j=0; j<20; j++){
			if (!gridfile) return 1;
			gridfile >> g[i][j];
		}
	}
	gridfile.close();
	
	// test horizontal possibilities
	for (int i=0; i<20; i++){
		for (int j=0; j<16; j++){
			cp = g[i][j] * g[i][j+1] * g[i][j+2] * g[i][j+3];
			if (cp > gp) gp  = cp;
		}
	}

	// test vertical possibilites
	for (int i=0; i<16; i++){
		for (int j=0; j<20; j++){
			cp = g[i][j] * g[i+1][j] * g[i+2][j] * g[i+3][j];
			if (cp > gp) gp = cp;
		} 
	}

	// test for forward diagonal
	for (int i=0; i<16; i++){
		for (int j=0; j<16; j++){
			cp = g[i][j] * g[i+1][j+1] * g[i+2][j+2] * g[i+3][j+3];
			if (cp > gp) gp = cp;
		}
	}

	// test for backward diagonal
	for (int i=0; i<16; i++){
		for (int j=3; j<20; j++){
			cp = g[i][j] * g[i+1][j-1] * g[i+2][j-2] * g[i+3][j-3];
			if (cp > gp) gp = cp;
		}
	}
	
	cout << gp << '\n';

	return 0;
}
