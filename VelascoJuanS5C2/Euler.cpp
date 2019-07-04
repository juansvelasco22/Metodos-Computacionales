#include <iostream>
using namespace std;

float funcion(float x, float y);

int main()
{
    float min=0.0;
    float max=4.0;
    float inicial=1.0;
    float h=0.01;
    const int puntos=(max-min)/h;
    float x[puntos];
    float y[puntos];
    for (int i=0;i<puntos;i++)
    {
        x[i]=0.0;
        y[i]=0.0;
    }
    x[0]=min;
    y[0]=1.0;
    for (int i=1; i<puntos;i++)
    {
        x[i] = x[i-1] + h;
        y[i] = y[i-1] + h * funcion(x[i-1],y[i-1]);
    }
    
    cout<<x<<endl;
    cout<<y<<endl;
    
    
    return 0;
}

float funcion(float x, float y)
{
    return -y;
}
