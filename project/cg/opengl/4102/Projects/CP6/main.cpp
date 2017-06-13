#include <cstdlib>
#include <iostream>

using namespace std;
class MyTest{
  // static int count;
   int total;
   int count;
public:
    MyTest(){
      total = 0;
      count = 0;
   }         
   void AddData(){
      total += 115;
      count = count+1;        
   }                     
   void Show(){
   cout << "total is " << total << "  Count is " << count << "\n";               
   }
   static int getCount() {
      return count;       
   }                    
};      int MyTest::count = 0;
int main(int argc, char *argv[])
{
    MyTest  a,b; 
    cout << MyTest::getCount() << "\n"; 
    a.AddData();  
    a.AddData();  
    a.Show();
    b.Show();  
    system("PAUSE");
    return EXIT_SUCCESS;
}
