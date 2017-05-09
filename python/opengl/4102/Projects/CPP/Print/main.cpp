#include <cstdlib>
#include <iostream>
using namespace std;

class PrintData {
public:
    void print(int i) 
    { cout << "Printing Integer:     " << i << endl; }
    void print(double f) 
    { cout << "Printing Float:       " << f << endl; }
    void print(char* c) 
    { cout << "Printing Character:   " << c << endl; }      
};      
int main(int argc, char *argv[])
{
    PrintData pd;
    pd.print(5);
    pd.print(50.26);
    pd.print("Hello C++");
    
    system("PAUSE");
    return EXIT_SUCCESS;
}
