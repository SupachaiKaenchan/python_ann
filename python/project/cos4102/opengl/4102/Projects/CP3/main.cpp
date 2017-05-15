#include <cstdlib>
#include <iostream>

using namespace std;

class Circle
{
private:
    double radius; 
public:                
    Circle(double r = 0.0) { radius = r;}
    
    void Show(); 
    void Show(Circle); 
          
};      

void Circle::Show()
{
    cout << "Radius of circle is " << radius << "\n";     
}
void Circle::Show(Circle c)
{
    cout << "Radius of circle is " << c.radius << "\n";     
}     

     
int main(int argc, char *argv[])
{   
    Circle* c;
    for (int i = 0; i < 1000000; i++) {
       c = new Circle;
       delete c;
    }    
    cout << "Complete" << endl;  
    
    system("PAUSE");
    return EXIT_SUCCESS;
}






