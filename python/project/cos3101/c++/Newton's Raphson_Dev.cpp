#include <iostream>
#include <cmath>

#define  f(x) (pow(x,2)-9)
#define f1(x) (2*x)

using namespace std;

int main(){
	
	double P0   = 1.0;
	double Pnew = 0.0;

	double delta = 0.001;

	bool flag = true;

	int n = 0;

	while(flag)
	{	
		n++;
		Pnew = P0-( f(P0) / f1(P0) );

		if ( abs(f(Pnew)) == 0 || abs(f(Pnew)) < delta )
		{
			flag = false;
			cout<< "Found the Root at, Value Pnew is. => "<<Pnew<<endl;
			cout<< "Round. :: "<<n<<endl;
			
		}else{
			P0 = Pnew;
		}

	}
	
	return 0;
}
