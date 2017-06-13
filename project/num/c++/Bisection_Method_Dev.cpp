#include <iostream>
#include <cmath>

#define f(x) (pow(x,5)+pow(x,3)+pow(x,2)-1) 

using namespace std;

int main(int argc, char const *argv[])
{
	

	double a = 0; 
	double b = 1; 
	double m = 0.0;

	double delta = 0.1; 

	bool flag = true; 

	int n = 0; 

	if ( ( f(a)*f(b) ) < 0 ) 
	{
		while(flag) 
		{
			n++; 

			m = (a+b)/2; 

			cout<< "Round. :: "<<n<<endl; 
			cout<< " (f(a)*f(m)) = "<<f(a)*f(m)<<endl;

			if ( (f(a)*f(m)) == 0 || abs(f(m)) < delta) 
			{
				flag = false;

				cout<<endl<<endl;
				cout<< "Found the Root at, Value M is. => "<<m<<endl;
				cout<< "Round. :: "<<n<<endl; 
				cout<< " (f(a)*f(m)) = "<<f(a)*f(m)<<endl;
				
			}else if ( (f(a)*f(m)) < 0 ){ 

						b = m; 
					}else{
						a = m; 
					}
			}

			}else if ( ( f(a)*f(b) ) == 0){

				cout<< "Found the Root at, Value A&B is. => "<<a<<endl; 
				cout<< "Round. :: "<<n++<<endl;
			}else{
				cout<< "Don't Found the Root. !!!"<<endl; 
			}

			return 0;
		}
