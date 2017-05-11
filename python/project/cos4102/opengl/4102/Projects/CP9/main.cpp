#include <cstdlib>
#include <iostream>

using namespace std;
class CMajor {
      int a, b;
public:
      CMajor(int x = 1.0, int y = 2.0){
          a = x; b = y;
      } 
      friend class CMinor;          
};

class CMinor {
public:
      int findMin(CMajor k);
      int findMax(CMajor k);
};
int CMinor::findMin(CMajor k)
{
    return (k.a < k.b) ? k.a:k.b;       
}    

int CMinor::findMax(CMajor k)
{
    return (k.a > k.b) ? k.a:k.b;       
}    

             
int main(int argc, char *argv[])
{   CMajor m(3,4);
    CMinor n;
    cout << "min value is " << n.findMin(m) << endl;
    cout << "max value is " << n.findMax(m) << endl;
    system("PAUSE");
    return EXIT_SUCCESS;
}
