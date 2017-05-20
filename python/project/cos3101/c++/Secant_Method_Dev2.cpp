#include <iostream>
#include <cmath>

#define f(x) (pow(x,3)+(3*pow(x,2))-(9*x)-11) 

using namespace std;

int main(int argc, char const *argv[])
{
	double P0   = -3.0;
	double P1   = 1.0;
	double Pnew = 0.0;

	double delta = 0.000001;

	bool flag = true;

	int n = 0;

	while(flag)
	{	
		n++;
		Pnew = P1-(  (f(P1)*(P1-P0)) / (f(P1)-f(P0))  );

		if ( abs(f(Pnew)) == 0 || abs(f(Pnew)-P1) < delta )
		{
			flag = false;
			cout<< "Found the Root at, Value Pnew is. => "<<Pnew<<endl;
			cout<< "Round. :: "<<n<<endl;
			cout<< "f(Pnew). :: "<<f(Pnew)<<endl;			
		}else{
			P0 = P1;
			P1 = Pnew;
		}

	}
	

	return 0;
}
