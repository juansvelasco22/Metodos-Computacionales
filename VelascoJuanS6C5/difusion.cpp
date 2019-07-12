#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    double L=100.0;
    double coef=0.01; //cambiar unidades
    double dx=1.0;
    double tf=2500.0;
    double Tempini=50.0;
    double delta=100.0;
    double dt=(0.25*dx)/coef;
    double cond=(coef*dt)/(dx*dx);
    int contador=0;
    
    
    double pres[100][100];
    double fut[100][100];
    
    ofstream outfile;
    outfile.open("placat0.dat");
    
    for (int x=0;x<100;x++)
    {
        for (int y=0;y<100;y++)
        {
            pres[x][y]=50.0;
            
            if(x<=40 && x>=20 && y<=60 && y>=40) //Revisar limites (invertidos)
            {
                pres[x][y]=100.0;
                fut[x][y]=pres[x][y];
            }  
        } 
    }
    for(int i=0;i<=100;i++)
    {
        for (int j=0;j<=100;j++)
        {
            outfile<<pres[i][j]<<" ";
        }
        outfile<<"\n";
    }
    outfile.close();
    
    
    
    outfile.open("placat100.dat");
    
    
    for(int t=1;t<=2500;t++)
    {
        contador=contador+1;
        for(int x=1;x<100;x++)
        {
            for(int y=1;y<100;y++)
            {
                fut[x][y]=((cond*(pres[x+1][y]+pres[x-1][y]-2*pres[x][y]))+(cond*(pres[x][y+1]+pres[x][y-1]-2*pres[x][y])))+pres[x][y];
            }
        }
        
        for(int x=1;x<100;x++)
        {
            for(int y=1;y<100;y++)
            {
                pres[x][y]=fut[x][y];
            }
        }
        
        if(contador==100)
        {
            for(int i=0;i<=100;i++)
            {
                for(int j=0;j<=100;j++)
                {
                    outfile<<pres[i][j]<<" ";
                }
                outfile<<"\n";
            }
        }
    }
    
        
        
    outfile.close();
    
    
    return 0;
}