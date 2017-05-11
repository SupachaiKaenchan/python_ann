#include <cstdlib>
#include <iostream>
using namespace std;

class Coordinate {
public:
   Coordinate() { cout << "Hello Coordinate" << endl;}                
};      

class Point {
public:
   Point() { cout << "Hello Point" << endl;}                
protected:
   Coordinate x;
   Coordinate y;          
};

class Point3D: public Point {
public:
      Point3D() { cout << "Hello Z" << endl;}                

protected:
   Coordinate z;
};

int main(int argc, char *argv[])
{
    Point3D p;
    system("PAUSE");
    return EXIT_SUCCESS;
}
