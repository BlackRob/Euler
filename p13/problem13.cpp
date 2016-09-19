#include<iostream>
#include<fstream>

using namespace std;

int main()
{
	int sum=0;
	int carry=0;
	short numbers[101][55];

	ifstream numberfile;
	numberfile.open("numbers.txt");
	for(int i=0; i<=99; i++){
		for(int j=0; j<=49; j++){
			numbers[i][j] = short(numberfile.get() - 48);
		}
		numbers[i][50] = short(numberfile.get() - 10);
		numbers[i][51] = 0;
		numbers[i][52] = 0;
		numbers[i][53] = 0;
		numbers[i][54] = 0;
	}
        numberfile.close();

	for(int i=49; i>=0; i--){
		for(int j=0; j<=99; j++){
			sum = numbers[j][i] + sum;
		}
		sum = sum + carry;
		numbers[100][i+5] = sum % 10;
		carry = (sum - numbers[100][i+5])/ 10;
		sum = 0;
	}
	cout << carry << '\n';

	for(int i=4; i>=0; i--){
		numbers[100][i] = short(carry % 10);
		carry = (carry - numbers[100][i])/ 10;
	}

	for(int i=0; i<=54; i++){
		cout << numbers[100][i];
	}
	cout << '\n';	

	return 0;
}
	
