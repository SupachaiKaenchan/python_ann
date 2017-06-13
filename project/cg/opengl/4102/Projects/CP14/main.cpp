#include <cstdlib>
#include <iostream>

using namespace std;
class CObj
{
public:
   int IsMe(CObj& o);                
};      
int CObj::IsMe(CObj& o)
{
   if(this == &o) 
      return 1;
   else return 0;        
   
}
int main(int argc, char *argv[])
{
CObj a;
CObj c;
//CObj *b;
//b = new CObj; 
CObj *b = &a;  
if (b->IsMe(a))

   cout << " b is a" << endl;
else
   cout << " b is not a" << endl; 
    
    system("PAUSE");
    return EXIT_SUCCESS;
}
