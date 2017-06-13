#include <cstdlib>
#include <iostream>

using namespace std;

class CVector {
      int x,y;
public:
      CVector() {x = 0; y = 0;}
      CVector(int,int);
      CVector operator+(const CVector&); 
      void Show();
}; 
CVector::CVector(int a, int b)
{
         x = a;
         y = b;            
} 
void CVector::Show()
{
    cout << "x: " << x << endl;
    cout << "y: " << y << endl;         
}

CVector CVector::operator+(const CVector& k)
{
    CVector tmp;
    tmp.x = x + k.x;    
    tmp.y = y + k.y;    
    return tmp;    
        
        
}        
int main(int argc, char *argv[])
{
    CVector o1(3,1);
    CVector o2(2,3);
    CVector o;
    o = o1+o2;
    o.Show();
   // o = o1.operator+(o2);
    system("PAUSE");
    return EXIT_SUCCESS;
}
