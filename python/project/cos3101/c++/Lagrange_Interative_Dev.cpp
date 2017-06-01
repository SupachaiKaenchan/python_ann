#include <iostream>
#include <cmath>

using namespace std;

int main(){
	
	int x[3] = {0,15,18};
	int f[3] = {22,24,37};
	
	int   n = 3;
	
	float t = 14.9;
	
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

	cout<<"Pn(14.9) = "<<Psum<<endl;
	
	return 0;
}
