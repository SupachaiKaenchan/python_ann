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
      Distance operator-() {
         Distance tmp;     
         tmp.feet = -feet;
         tmp.inches = -inches;
         return tmp;         
      }                         
      
};      
int main(int argc, char *argv[])
{
    Distance D(11,-10);
    D = -D;
    D.Display();
    system("PAUSE");
    return EXIT_SUCCESS;
}
