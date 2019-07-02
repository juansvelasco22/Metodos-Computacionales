#include <iostream>
using namespace std;

int multi(int x[], int y[]);
int punto(int x[], int y[]);
    
int main()
{
    //Declara pointer
   // int px*;
   // int py*;
    
    //Declara arreglos
    int x[]={1,2,3,4,5};
    int y[]={10,20,30,40,50};
    
    //Asignar pointer
    //px=x;
   // py=y;
    
    
    cout<<"Multiplicacion es: ";
    cout<<multi(x,y)<<endl;
     
    cout<<"Producto punto es: ";
    cout<<punto(x,y)<<endl;
    
    return 0;
}

int multi(int x[], int y[])
{
    int rtamulti[4];
    for (int i=0;i<=5;i++)
    {
        rtamulti=x[i]*y[i];
    }
   
    return rtamulti;
}

int punto(int x[], int y[])
{
    int rtapunto=0;
    for (int i=0;i<5;i++)
    {
        rtapunto=rtapunto +(x[i]*y[i]);
    }
    return rtapunto;
}

