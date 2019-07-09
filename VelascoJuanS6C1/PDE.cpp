#include <iostream>
using namespace std;

int main()
{
    double v=1.0;
    double deltax=80.0;
    double dx=2/(deltax-1.0);
    double dt=(deltax*0.25)/v;    //Estabilidad
    
    double t1=0.75;
    double t2=1.25;
    double ti=0.0;
    double tf=2.0;
    
    double U[80];
    double Ufuturo[80];
    double Upasado[80];
    
    for (int i=0;i<80;i++)   //Condiciones iniciales
    {
        if(tf/80<0.75 && tf/80>1.25)
        {
            U[i]=1.0;
            Upasado[i]=1.0;
        }
        else
        {
            U[i]=2.0;
            Upasado[i]=2.0;
        }
    }
    for (int i=1;i<30;i++)    //Tiempo
    {
        for (int e=0;e<=deltax;;e++)    //Espacio
        {
            Ufuturo[e]=(v*dt)/(dx)*(U[e]-Upasado[e-1])+U[e];
            
            Upasado[e]=U[e];
            U[e]=Ufuturo[e];
        }
       
    }
    
    return 0;
}