#include <cstdlib>
#include <iostream>
#include <cmath>

using namespace std;

class CPoint {
private:
   float x,y;
   float dist;
   char name[20];
public:
   CPoint(float x,float y, char *n){
      this->x = x;
      this->y = y;
   }                 
   float getX() {
      return x;
   }                        
   float getY() {
      return y;
   }                        
   void distance() {
      dist = sqrt(pow(x,2) + pow(y,2));
   }                        
   void Show() {
     cout << "x value is " << x << "\n";
     cout << "y value is " << y << "\n";
     cout << "The name point is " << name << "\n";
     cout << "distance is " << dist << "\n";              
   }      
};      
int main(int argc, char *argv[])
{
    CPoint c(2.5,5.0,"vertex");
    c.distance();
    c.Show();
    system("PAUSE");
    return EXIT_SUCCESS;
}
