#include<iostream>
#include<cstdio>
#include<cmath>

using namespace std;

int main()
{
	int power = 0;
	cin >> power;

	double sum = 0;
	double result = pow(2,power);
	
	char buffer [1000] = {0};
	
	cout << "2 to the power " << power << " is " << '\n';
	printf("%lf\n",result);
	cout << "The sum of it's digits is " << '\n';
	sprintf(buffer,"%lf",result);
	for (int i = 0; i < 1000; i++){
		if (buffer[i] == '.'){ 
			cout << i << '\n';
			break;
		}		
		sum = sum + (buffer[i] - '0');
	}
	cout << sum << '\n';
	
	return 0;
}
