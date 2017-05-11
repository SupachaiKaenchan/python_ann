#include <cstdlib>
#include <iostream>

using namespace std;
class CRectangle{
private:
    float weight,height;
    float area;
public:
    CRectangle();   
    CRectangle(float, float);
    ~CRectangle();
    void set();
    void Show();
    void SetArea();
};      
CRectangle::CRectangle()
{                        
}
CRectangle::CRectangle(float w, float h)
{
     this->weight = w; this->height = h; this->area = 0;                        
}

void CRectangle::set()
{ 
     cout << " Width  of Rectangle is ";    cin >> this->weight; 
     cout << "\n Height of Rectangle is ";  cin >> this->height; 
}


void CRectangle::SetArea()
{ 
     area = this->weight*this->height; 
}

void CRectangle::Show()
{
     cout << "Area of Rectangle are " << this->area << "\n";                        
}

CRectangle::~CRectangle()
{
   cout << "Good bye from destructor function \n";                      
}

int main(int argc, char *argv[])
{
float k;    
    CRectangle *a;
    CRectangle b;
    b.set();
    b.SetArea();
    b.Show();     
    
    //a = new CRectangle(5.0,6.0);
    //a->SetArea();
    //a->Show();     
    //delete a;
    system("PAUSE");
    return EXIT_SUCCESS;
}




