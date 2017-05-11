#include <cstdlib>
#include <iostream>

using namespace std;
struct stack {
private: 
    int top;
public:          
 	int data[100];
 	stack(){ top = 0;}
 	stack(int k){ top = 0; k++; }
 	void set(void){ top = 0;} 
//	void push(int a);	  // implement outside
    void push(int a) {    assert(top<100); data[top]=a;  top++;  } 
	int pop(void); 	  // implement outside
	bool isEmpty(void); // implement outside
} ;
/*void stack::push(int a){
    assert(top<100);
    data[top]=a;  
    top++;   
}*/
int stack:: pop( ){
   assert(top>0);
   int x=data[--top];     
   return x;
}
bool stack::isEmpty( ){
   return top==0?true:false;
}
int main(int argc, char *argv[])
{
    stack S;
  //  S.set();    
  //  S.top=0;
    S.push(12); 
    S.push(20);
    S.push(30);
    int x=S.pop();
    cout<<x<<endl;
    cout<<S.pop()<<endl;
    cout<<S.isEmpty()<<endl;
    cout<<S.pop()<<endl;
    cout<<S. isEmpty()<<endl;

    system("PAUSE");
    return EXIT_SUCCESS;
}
