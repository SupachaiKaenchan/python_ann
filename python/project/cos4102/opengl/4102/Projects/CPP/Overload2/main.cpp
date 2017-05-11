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
        tmp.x = this->x + p.x;
        tmp.y = this->y + p.y;
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
    CVector c;
    c = a+b;

    c.ShowVector();
    system("PAUSE");
    return EXIT_SUCCESS;
}
