#include <iostream>

using namespace std;

class CPolygon
{
protected:
    int width, height;
public:
    CPolygon() {width = 0; height = 0; }   
    CPolygon(int w,int h) {width = w; height = h;}
};

class CRectangle: public CPolygon
{
    int depth;  
public:
    CRectangle(int w, int h) : CPolygon(w,h) {depth = d;}
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
    cout << "The Area of Rectangle is :" << R.area() << endl ;
    cout << "The Area of Triangle  is :" << Tri.area() << endl ;

    system("PAUSE");
    return EXIT_SUCCESS;
}
