#include <iostream>

using namespace std;

class Shape
{
protected:
       int width;
       int height;
public:
       void setWidth(int w){ width = w;}
       void setHeight(int h){ height = h;}
};
class PaintCost
{
public:
        int getCost(int area){return area*70;}
};
class Rectangle: public Shape, public PaintCost
{
public:
        int getArea(){return width*height;}
};

int main()
{
Rectangle Rect;
int area;

        Rect.setWidth(5);
        Rect.setHeight(7);
        area = Rect.getArea();

        cout << "The total area is :" << area << endl;
        cout << "The paint costs for this area are :" << Rect.getCost(area) << endl;


    std::cout << "Press enter to continue ...";
    std::cin.get();
    return 0;
}
