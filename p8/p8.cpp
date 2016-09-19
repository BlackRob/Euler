#include(iostream)
#include(fstream)
#include(cstdlib)

using namespace std;

void processArray(int[]);

int main()
{
	int anarray[1000];
	char ch;
	int i=0;
	ifstream numberlist;
	numberlist.open("thousanddigit.txt");
	while(!numberlist.eof()){
		numberlist.get(ch);
		anarray[i] = ch - 48;
		i++;
	}

	void processArray{anarray);

	return 0;
}

void processArray(int[] tharray){
	int a,b,c,d,e;
	for (int i=0;
