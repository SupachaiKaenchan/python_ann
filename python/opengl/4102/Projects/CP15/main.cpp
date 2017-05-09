#include <cstdlib>
#include <iostream>
using namespace std;

class Distance
{
private:
    int feet;
    int inches;
public:
    Distance() {feet = 0; inches = 0;}
    Distance(int f, int i) {feet = f; inches = i;} 
    void operator-();                        
    void DisplayDist();
};
void Distance::DisplayDist()
{ 
     cout << "feet = " << feet << ",  inches = " << inches << endl; 
}
void Distance::operator-(){
         this->feet = feet*-1;
         this->inches = inches*-1;
         //return *this; //Distance(feet,inches);
         
}            
/*Distance Distance::operator-(){
Distance D;
         D.feet = feet*-1;
         D.inches = inches*-1;
         return D;
         
}*/                


int main(int argc, char *argv[])
{
Distance D1(10,11);
Distance D2(-5,-8);
    //D1 = -D1;
    -D1;
    D1.DisplayDist();
              
    system("PAUSE");
    return EXIT_SUCCESS;
}
