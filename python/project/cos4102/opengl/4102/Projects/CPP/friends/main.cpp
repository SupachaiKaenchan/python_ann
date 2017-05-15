#include <iostream>

using namespace std;

class CSquare;

class CRectangle
{
private:
    int width, height;
public:
     CRectangle(){width = 0; height = 0;}
     int Area(){return width*height;}
     void Convert(CSquare);

};

class CSquare
{
    int side;
public:
    CSquare(int s){side = s;}
    friend class CRectangle;
};

void CRectangle::Convert(CSquare param)
{
    width = param.side;
    height = param.side;
}

int main()
{
    CSquare S(5);
    CRectangle R;
    R.Convert(S);
    std::cout << "The area of this rectangle is :" << R.Area() << endl;
    std::cout << "Press enter to continue ...";
    std::cin.get();
    return 0;
}
