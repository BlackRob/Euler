#include<iostream>

using namespace std;

int main()
{
	int letters = 0;

	int ones = 0;
	int tens = 0;
	int huns = 0;

	for (int i=1; i < 1000; i++){
		cout << i << " ";
		
		huns = i / 100;
		tens = (i % 100) / 10;
		ones = i % 10;
		
		// hundreds place
		switch (huns) {
		case 0:
			cout << "";
			letters = letters + 0;
			break;
		case 1:
			cout << "one hundred ";
			letters = letters + 10;
			break;
		case 2:
			cout << "two hundred ";
			letters = letters + 10;
			break;
		case 3:
			cout << "three hundred ";
			letters = letters + 12;
			break;
		case 4:
			cout << "four hundred ";
			letters = letters + 11;
			break;
		case 5:
			cout << "five hundred ";
			letters = letters + 11;
			break;
		case 6:
			cout << "six hundred ";
			letters = letters + 10;
			break;
		case 7:
			cout << "seven hundred ";
			letters = letters + 12;
			break;
		case 8:
			cout << "eight hundred ";
			letters = letters + 12;
			break;
		case 9:
			cout << "nine hundred ";
			letters = letters + 11;
			break;
		}
		
		// add "and" between hundreds and tens if needed	
		if ((huns > 0) && ((tens != 0) || (ones != 0))){
			cout << "and ";
			letters = letters + 3;
		}
		
		// tens place --we handle teens separately
		switch (tens) {
		case 0:
			cout << "";
			letters = letters + 0;
			break;
		case 1:
			cout << "";	// handle teens separately
			letters = letters + 0;
			break;
		case 2:
			cout << "twenty ";
			letters = letters + 6;
			break;
		case 3:
			cout << "thirty ";
			letters = letters + 6;
			break;
		case 4:
			cout << "forty ";
			letters = letters + 5;
			break;
		case 5:
			cout << "fifty ";
			letters = letters + 5;
			break;
		case 6:
			cout << "sixty ";
			letters = letters + 5;
			break;
		case 7:
			cout << "seventy ";
			letters = letters + 7;
			break;
		case 8:
			cout << "eighty ";
			letters = letters + 6;
			break;
		case 9:
			cout << "ninety ";
			letters = letters + 6;
			break;
		}
		
		// teens	
		if (tens == 1){
			switch (ones){
			case 0:
				cout << "ten ";
				letters = letters + 3;
				break;
			case 1:
				cout << "eleven ";
				letters = letters + 6;
				break;
			case 2:
				cout << "twelve ";
				letters = letters + 6;
				break;
			case 3:
				cout << "thirteen ";
				letters = letters + 8;
				break;
			case 4:
				cout << "fourteen ";
				letters = letters + 8;
				break;
			case 5:
				cout << "fifteen ";
				letters = letters + 7;
				break;
			case 6:
				cout << "sixteen ";
				letters = letters + 7;
				break;
			case 7:
				cout << "seventeen ";
				letters = letters + 9;
				break;
			case 8:
				cout << "eighteen ";
				letters = letters + 8;
				break;
			case 9:
				cout << "nineteen ";
				letters = letters + 8;
				break;
			}
		}
		
		// ones	
		if (tens != 1){
			switch (ones){
			case 0:
				cout << "";
				letters = letters + 0;
				break;
			case 1:
				cout << "one ";
				letters = letters + 3;
				break;
			case 2:
				cout << "two ";
				letters = letters + 3;
				break;
			case 3:
				cout << "three ";
				letters = letters + 5;
				break;
			case 4:
				cout << "four ";
				letters = letters + 4;
				break;
			case 5:
				cout << "five ";
				letters = letters + 4;
				break;
			case 6:
				cout << "six ";
				letters = letters + 3;
				break;
			case 7:
				cout << "seven ";
				letters = letters + 5;
				break;
			case 8:
				cout << "eight ";
				letters = letters + 5;
				break;
			case 9:
				cout << "nine ";
				letters = letters + 4;
				break;
			}
		}
			
		cout << "\n";	
			 
	}
		
	letters = letters + 11;
	
	
	cout << letters << '\n';
	
	return 0;
}

