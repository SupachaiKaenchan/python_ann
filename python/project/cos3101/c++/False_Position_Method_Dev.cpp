#include <iostream>
#include <cmath>

#define f(x) ( 6+(2*x)-pow(x,3) ) 

using namespace std;

int main(int argc, char const *argv[])
{
	double a   = -2.0;
	double b   =  3.0;
	double c   =  0.0;

	double delta = 0.00000001;

	bool flag = true;

	int n = 0;
	
	if( (f(a)*f(b)) < 0 ){

		while(flag)
		{	
			n++;
			c = b-(  (f(b)*(b-a)) / (f(b)-f(a))  );
			
			if(n == 3){
				cout<< "Round 3 => Found the Root at, Value Pnew is. => "<<c<<endl;
				cout<< "Round. :: "<<n<<endl;
				cout<< "C. :: "<<f(c)<<endl;
			}
			
			if ( f(c) == 0 || abs(f(c)) < delta )
			{
				flag = false;
				cout<< "Found the Root at, Value Pnew is. => "<<c<<endl;
				cout<< "Round. :: "<<n<<endl;
				cout<< "C. :: "<<f(c)<<endl;			
			}else if(f(a)*f(c) < 0){
					b = c;
			}else{
					a = c;
			}
		}
	}else if( f(a)*f(b) == 0 ){
				cout<< "Found the Root at, Value Pnew is. => "<<a<<endl;
				cout<< "Round. :: "<<n<<endl;
	}else{
		cout<< "Don't Found the Root. "<<endl;
	}
		

	return 0;
}
