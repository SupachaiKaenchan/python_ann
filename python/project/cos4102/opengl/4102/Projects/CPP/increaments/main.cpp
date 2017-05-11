#include <cstdlib>
#include <iostream>
using namespace std;
class MyClass
{
public:
    int m_nCounter;
 
public:
    MyClass() { m_nCounter = 0;}
 
    MyClass& operator++()
    {
        ++this->m_nCounter;
        //this->m_nCounter = this->m_nCounter+1; 
        return *this;
    }
 
    MyClass& operator++(int)
    {
        this->m_nCounter++;
        return *this;
    }
 
    MyClass& operator--()
    {
        --this->m_nCounter;
        return *this;
    }
 
    MyClass& operator--(int)
    {
        this->m_nCounter--;
        return *this;
    }
};
 
int main(int argc, char *argv[])
{
    MyClass counter;
    cout << counter.m_nCounter << endl;
    counter++;
    cout << counter.m_nCounter << endl;
    ++counter; 
    cout << counter.m_nCounter << endl;
    counter--; 
    cout << counter.m_nCounter << endl;
    --counter; 
    cout << counter.m_nCounter << endl;

    
    system("PAUSE");
    return EXIT_SUCCESS;
}
