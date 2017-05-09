#include <iostream>

using namespace std;

class CRectangle
{
        int width, height;
public:
        CRectangle(){width = 0; height =0;}
        CRectangle(int w,int h){width = w; height =h;}
        int Area(){return width*height;}
        friend CRectangle duplicate(CRectangle);
};
CRectangle duplicate(CRectangle param)
{
    CRectangle tmp;
    tmp.width = param.width*2;
    tmp.height = param.height*2;
    return tmp;
}


int main(int argc, char *argv[])
{
    CRectangle Rect1(4,5),Rect2;
    Rect2 = duplicate(Rect1);
    cout << "The area of this rectangle is : " << Rect2.Area() << endl;

    system("PAUSE");
    return EXIT_SUCCESS;
}
