#include <iostream>
#include <cmath>

#define f(x) (x+(2/x))

using namespace std;

int main(){
	
	int x[3] = {1,2,3};
	int f[3] = {f(x[0]),f(x[1]),f(x[2])};
	
	int   n = 2;
	
	float t = 1.5;
	
	double Psum = 0.0;
	
	for(int i = 0; i < n; i++){
		
		double mult=1.0;
		
		for(int j = 0; j < n; j++){
			
			if( i != j){
				
				mult =  mult*( (t-x[j]) / (x[i]-x[j]) ) ;
			}
		}
		
		Psum = Psum+f[i]*mult;
		
	}

	cout<<"Pn(1.5) = "<<Psum<<endl;
	
	return 0;
}
