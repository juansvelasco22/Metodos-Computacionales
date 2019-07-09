#include <iostream>
using namespace std;

int main()
{
    double L=1.0;
    dx=0.005;
    double deltax=L/dx;
    double c=300.0;
    double dt=(0.25*dx)/(c**2);
    double A0=0.01;
    
    double pas[deltax];
    double pres[deltax];
    double fut[deltax];
    
    for (double i=0.0;i<L;i++)
    {
        if(i==(L/2))
        {
            pres[i]=0.01;
        }
        else if(i<(L/2))
        {
            pres[i]=(A0/(L/2)*i);

        }
        else if(i>(L/2))
        {
            pres[i]=((-A0)/(L/2)*i);
        }                 
                         
    }
    
    for (int i=0;i<deltax;i++)
    {
        pas[i]=pres[i];
        pas[0]=
    }
    
    
    for (int i=0;i<=30;i++)
    {
        for (int e=0;e<=deltax;e++)
        {
            fut[e]=((c**2*dx**2)/(dt**2))*(pres[e+1]+pres[e-1]-2*pres[e])-pas[e]+2*pres[e];
            
            pas[e]=pres[e];
            pres[e]=fut[e];
                        
        }
    }