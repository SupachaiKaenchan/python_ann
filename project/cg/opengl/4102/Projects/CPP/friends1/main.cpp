#include <iostream>

using namespace std;

class CPolygon
{
protected:
    int width, height;
public:
    CPolygon(int w,int h) {width = w; height = h;}
};

class CRectangle: public CPolygon
{
public:
    CRectangle(int w, int h) : CPolygon(w,h) {}
    int area() {return width*height;}
};

class CTriangle: public CPolygon
{
public:
    int area() {return (width*height)/2;}
};

int main()
{
    CRectangle R(2,2);
    CTriangle Tri;
    cout << "The Area of Rectangle is :" << R.area() << endl ;
    cout << "The Area of Triangle  is :" << Tri.area() << endl ;

    cout << "Press enter to continue ...";
    cin.get();
    return 0;
}
