#include<iostream>

using namespace std;

long checkPaths(int,int);

const int rightLimit = 20;
const int downLimit = 20;
long temp = 0;

int main()
{
	long paths = 0;

	paths = checkPaths(0,0);
	
	cout << paths << '\n';
	
	return 0;
}

long checkPaths(int startX, int startY){
	int X = startX;
	int Y = startY;
	//cout << startX << ' ' << startY << '\n';
	if (X < rightLimit){
		checkPaths((startX + 1), startY);
	}
	if (Y < downLimit){
		checkPaths(startX, (startY + 1));
	}
	if (X==rightLimit && Y==downLimit) temp++;	

	return temp;
}
