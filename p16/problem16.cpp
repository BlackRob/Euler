#include<iostream>
#include<iomanip>
#include<string>
#include<sstream>
#include<cmath>

using namespace std;

int main()
{
	int power = 0;
	cin >> power;

	double sum = 0;
	double result = pow(2,power);
	cout << "2 to the " << power << " is " << result << '\n';
	for (int i = 0; i <= power; i++){
		sum = sum + fmod(result,10);
		cout << power << ' ' << sum << '\n';
		result = result/10;
		cout << result << '\n';
	} 
	//ostringstream strs;
	//strs << result;
	//string str = strs.str();	
	//cout << str << '\n';
	cout << sum << '\n';
	
	return 0;
}
