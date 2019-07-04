# include <iostream>
using namespace std;

float derivada();

int main()
{
    float li;
    float ls;
    float h;
    
    cout<<"Ingresar limite inferior";
    cin>> li;
    cout<<"Ingrear limite superior";
    cin>> ls;
    
    int N=1000;
    h=(ls-li)/(N-1);
    
    float x=[1000];
    float x[0]=li;
    float x[999]=ls;
    
    
    for (int i=li;i<ls;i++)
    {
        
    }
    
    float cosx;
    for (int i=0;i<1000;i++)
    {
        cosx[i]=cos(x[i]);
    }
    float cosxh;
    for (int i=0;i<1000;i++)
    {
        cosxh[i]=cos(x[i]-h);
    }
    
    return 0;
}

float derivada()
{
    float derivada=0.0;
    for (int i=0;i<1000;i++)
    {
        derivada=derivada+((cosxh[i]-cosx[i])/h);
    }
    
    
}