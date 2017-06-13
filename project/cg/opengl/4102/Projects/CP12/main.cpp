#include <cstdlib>
#include <iostream>

using namespace std;

class A {
protected:
     int i;
public:
      A(){
       i = 3;
       cout << "Test";
       } 
      A(int k) { i = k;}
};

class B : public A{
protected:      
     int j;
public:
      B(int k, int m):A(k) { j = m;}
      int show() 
      { cout << i << " " << j << endl; }
};

               
int main(int argc, char *argv[])
{
   B b(4,6);
   b.show();
     system("PAUSE");
    return EXIT_SUCCESS;
}
