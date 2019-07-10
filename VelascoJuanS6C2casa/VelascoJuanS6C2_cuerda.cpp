#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    double L=1.0;
    dx=0.005;
    double deltax=L/(dx+1);
    double c=300.0;
    double dt=(0.25*dx)/(c**2);
    double A0=0.01;
    
    double pas[deltax];
    double pres[deltax];
    double fut[deltax];
    
    ofstream outfile;
    
    for (double i=0.0;i<L;i++)
    {
        if(i==(L/2))
        {
            pas[i]=0.01;
        }
        if(i<(L/2))
        {
            pas[i]=(A0/(L/2)*i);

        }
        if(i>(L/2))
        {
            pas[i]=((-A0)/(L/2)*i);
        }       
    }
    
    otfile.open("cuerda.dat");
    
    for (int i=0;i<deltax;i++)
    {
        pres[i]=((c**2*dx**2)/(dt**2))*(pas[e+1]+pas[e-1]-2*pas[e])-pas[e]+2*pas[e];
    }
    
    
    for (int i=0;i<=30;i++)
    {
        for(int d=0;d<deltax;d++)
        {
            outfile << pres[i] << " "; 
        }
        outfile<<"\n";
        
        for (int e=0;e<=deltax;e++)
        {
            fut[e]=((c**2*dx**2)/(dt**2))*(pres[e+1]+pres[e-1]-2*pres[e])-pas[e]+2*pres[e];
        }
        
        for(int e=0;e<=deltax;e++)
        {
            
            pas[e]=pres[e];
            pres[e]=fut[e];
                        
        }
    }
    outfile.close();
    
    return 0;
    
    
}