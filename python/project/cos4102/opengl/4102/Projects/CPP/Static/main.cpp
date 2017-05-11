#include <cstdlib>
#include <iostream>
using namespace std;

class CDummy{
public:
       static int n;
       CDummy() {n++;}      
       ~CDummy() {n--;}            
};      
int CDummy::n = 0;
int main(int argc, char *argv[])
{
    CDummy a;
    CDummy b[5];
    CDummy* c = new CDummy;
    cout << a.n << endl;
    cout << b[1].n << endl;
    cout << c->n << endl;
    cout << CDummy::n << endl;
    delete c;
    cout << a.n << endl;
    cout << CDummy::n << endl;
    
    system("PAUSE");
    return EXIT_SUCCESS;
}
