#include <cstdlib>
#include <iostream>
using namespace std;
class CVector{
private:
      int x,y;  
public:
      CVector() { x = 0; y = 0;}
      CVector(int,int);
      CVector operator+(const CVector&); 
      void ShowVector();
};      
CVector::CVector(int a, int b)
{
 x = a;
 y = b;                    
}
CVector CVector::operator+(const CVector& p)
{
CVector tmp;
        tmp.x = x + p.x;
        tmp.y = y + p.y;
        return tmp;
}
void CVector::ShowVector()
{
     cout << "x is " << x << " and y is " << y << endl;
}

int main(int argc, char *argv[])
{
    CVector a(3,1);
    CVector b(1,2);
    CVector c(1,1);
    CVector d;
    
//    d = (a+b)+c;
    d = a.operator+(b);
    d = d.operator+(c);
    d.ShowVector();
    system("PAUSE");
    return EXIT_SUCCESS;
}
