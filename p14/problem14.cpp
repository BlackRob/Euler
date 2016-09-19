#include<iostream>

using namespace std;

int genSequence(int,int,int,int);

int main()
{
	int sequence = 0;
	int longestSequence = 0;
	int secondLongest = 0;
	int longSeqNumber = 1;

	for(int i=2; i<=999999; i++){
		sequence = genSequence(i,longestSequence,longSeqNumber,secondLongest);
		if (sequence >= longestSequence){
			secondLongest = longestSequence;
			longestSequence = sequence;
			longSeqNumber = i;
			cout << i << ' ' << sequence << endl;
		}
	}
	
	cout << longSeqNumber << '\n';
	
	return 0;
}

int genSequence(int candidate,int longestSequence, int longSeqNumber, 
				int secondLongest){
	int chainLength = 1;
	int originalCandidate = candidate;
	do{
//		cout << candidate << '_';
		if ((candidate % 2) == 0){
			candidate = candidate / 2;
		} 
		else {
			candidate = 3*candidate + 1;
		}
		chainLength++;
		if (candidate == longSeqNumber){
			chainLength = longestSequence + chainLength;
			break;
		}
		if ((candidate < longSeqNumber) && 
				(chainLength + secondLongest < longestSequence)){
			break;
		}
	} while (candidate > 1);
//	cout << "1     " << chainLength << endl;
	return chainLength;
}
