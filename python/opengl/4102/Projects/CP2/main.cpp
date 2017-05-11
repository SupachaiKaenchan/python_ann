#include <cstdlib>
#include <iostream>

using namespace std;

class Student {
public:
      
    Student(char *n,int a, float w, float h, char s, float g);       
    Student();
    void ShowData();     
private:   
   char name[30];
   int age;
   float weight;
   float height;
   char sex;
   float gpa;
};  

Student::Student(char *n,int a, float w, float h, char s, float g) 
{
         strcpy(name,n);
         age = a;
         weight = w;
         height = h;
         sex = s;  
         gpa = g; 
}
Student::Student() 
{
}
void Student::ShowData() 
{
    cout << "Name: " << name << " age: " << age << " weight: " << weight << "\n";
}


int main(int argc, char *argv[])
{
    Student Not("Tanadech TongBai",25,(float)66,(float)175,'M',(float)3.21);
    Student x;
    Not.ShowData();
    system("PAUSE");
    return EXIT_SUCCESS;
}




