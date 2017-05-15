#include <cstdlib>
#include <iostream>

using namespace std;
class CDummy {
public:
     static int n;
     CDummy (){ n++;}
     ~CDummy (){n--;}             
};
int CDummy::n = 0;
      

int main(int argc, char *argv[])
{
    CDummy a;
    CDummy b[5];
    CDummy *c;
    c = new CDummy;
    cout << CDummy::n << endl;
    delete c;
    cout << CDummy::n << endl;
     
    system("PAUSE");
    return EXIT_SUCCESS;
}
