#include <cstdlib>
#include <iostream>

using namespace std;

class Human {
private:      
   int id;
   void Showdata();
public:   
   void SetValue(int);
};  

void Human::SetValue(int a)
{
     id = a;
     Showdata();

}
void Human::Showdata()
{
     cout << "Id equals to " << id << "\n";

}


int main(int argc, char *argv[])
{
    Human x;
    x.SetValue(5);
    system("PAUSE");
    return EXIT_SUCCESS;
}
