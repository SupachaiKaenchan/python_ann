#include <iostream>

using namespace std;

class CPolygon
{
protected:
    int width, height;
public:
    void Set(int w, int h) {width = w; height = h;}
    int area() {return 0;}
};

class CRectangle: public CPolygon
{
public:
    int area() {return width*height;}
};

class CTriangle: public CPolygon
{
public:
    int area() {return (width*height)/2;}
};

int main()
{
    CRectangle R;
    CTriangle Tri;
    R.Set(4,5);
    Tri.Set(4,5);
    cout << "The Area of Rectangle is :" << R.area() << endl ;
    cout << "The Area of Triangle  is :" << Tri.area() << endl ;

    cout << "Press enter to continue ...";
    cin.get();
    return 0;
}
