#include <cstdlib>
#include <iostream>

using namespace std;
class CMyClass {
    int num;
public:
      CMyClass(int x = 2){
       num = x;
    }                   
    friend int IsNeg(CMyClass a);
         
};
int IsNeg(CMyClass a)
{
       return (a.num < 0) ? 1:0;
}    
int main(int argc, char *argv[])
{
    CMyClass a(-1);
    if (IsNeg(a))
       cout << "negative value" << endl;
    else
       cout << "positive value" << endl;
       
    system("PAUSE");
    return EXIT_SUCCESS;
}
