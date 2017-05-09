#include <cstdlib>
#include <iostream>

using namespace std;

class CPolygon
{
protected:
    int width, height;
public:
    virtual void Set(int, int) = 0;
    virtual int area()  = 0;
};


class CRectangle: public CPolygon
{
public:
    void Set(int w, int h) {width = w; height = h;}
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
    system("PAUSE");
    return EXIT_SUCCESS;
}







