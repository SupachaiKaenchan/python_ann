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
      void Display() { cout << "Feet Distance : " << feet << "  Inches Distance : " << inches << endl;}
      bool operator<(const Distance&);

};
bool Distance::operator<(const Distance& param){
     if (feet < param.feet)
         return true;
     else if (feet == param.feet){
          if (inches < param.inches)
             return true;
          else
             return false;             
     } else return false;              
}      
int main(int argc, char *argv[])
{
    Distance D1(11,-4), D2(11,-5);
    if (D1 < D2)
        cout << "D1 is less than D2" << endl;
    else
        cout << "D1 is not less than D2" << endl;
        
    system("PAUSE");
    return EXIT_SUCCESS;
}
