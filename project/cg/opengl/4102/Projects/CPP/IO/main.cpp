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
      bool operator<(const Distance&);
      friend ostream& operator<<(ostream&,const Distance&);
      friend istream& operator>>(istream&,Distance&);
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
ostream& operator<<(ostream& output,const Distance& param)
{
  output << "Feet Distance : " << param.feet << "  Inches Distance : " << param.inches << endl;
  return output;         
}       
istream& operator>>(istream& input,Distance& param)
{
  input >> param.feet >> param.inches ;
  return input;         
}       



int main(int argc, char *argv[])
{

    Distance D1(11,-4);      
    cout << "The distance is as " << D1 << endl;
    
    Distance D2;
    cout << "Enter the object values: " << endl;
    cin >> D2;
    cout << "The distance is as " << D2 << endl;
    
    if (D1 < D2)
        cout << "D1 is less than D2" << endl;
    else
        cout << "D1 is not less than D2" << endl;
    
    
    system("PAUSE");
    return EXIT_SUCCESS;
}
