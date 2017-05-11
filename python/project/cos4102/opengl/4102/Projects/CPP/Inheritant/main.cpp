#include <iostream>

using namespace std;

class CPolygon
{
protected:
    int width, height;
public:
    CPolygon() {width = 0; height = 0;}
    CPolygon(int w, int h) {width = w; height = h;}
    void Set(int w, int h) {width = w; height = h;}
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
    CTriangle(int w, int h) : CPolygon(w,h) {}

    int area() {return (width*height)/2;}
};

int main()
{
    CRectangle R(4,5);
    CTriangle Tri(4,5);
    //R.Set(4,5);
    //Tri.Set(4,5);
    cout << "The Area of Rectangle is :" << R.area() << endl ;
    cout << "The Area of Triangle  is :" << Tri.area() << endl ;

    cout << "Press enter to continue ...";
    cin.get();
    return 0;
}
