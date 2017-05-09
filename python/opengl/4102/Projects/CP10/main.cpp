#include <cstdlib>
#include <iostream>

using namespace std;
class Point{
protected:
       int x;
       int y;   
public:
       Point()
       {x = 0; y =0;}
       Point(int xv,int yv)
       {SetX(xv); SetY(yv);}
       void SetX(int xv)
       { x = xv;}
       void SetY(int yv)
       { y = yv;}
       void Show()
       { cout << "x is : " << x << " y is : " << y << endl;}   
}; 
class Point3D:public Point {
protected:
       int z;  
public:
      Point3D():Point()
      { z = 0;} 
      Point3D(int xv, int yv, int zv):Point(xv,yv)
      {SetZ(zv);}         
      void SetZ(int zv)
       { z = zv;} 
      void Show()
       {Point::Show();
       cout << "z is : " << z << endl;
       }                                          
};        

    
int main(int argc, char *argv[])
{
    Point3D p(3,5,7);
    p.Show();
    system("PAUSE");
    return EXIT_SUCCESS;
}
