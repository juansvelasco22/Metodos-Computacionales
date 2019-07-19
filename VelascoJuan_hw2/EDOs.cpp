#include <iostream>
#include <fstream>
#include <math.h>
using namespace std;

void euler(double dt,string datos);
void LF(double dt, string datos);

int main()
{
    euler(0.0001, "e_0.005.dat");
    euler(0.00001, "e_0.001.dat");
    euler(0.000001,"e_0.0001.dat");
    return 0;
}

void LP(double dt, string datos)
{
    double G=6.674*pow(10,-29);
    double  Msol=1.989*pow(10,30);
    
    double xpres;
    double xpas;
    double ypres;
    double ypas;
    double vxpres;
    double vxpas;
    double vypres;
    double vypas;
    
    ofstream outfile;
    outfile.open(datos);
    
    xpas=0.1163;
    ypas=0.9772;
    vxpas=-6.36;
    vypas=0.606;
}

void euler(double dt, string datos)
{
    double G=6.674*pow(10,-29);
    double  Msol=1.989*pow(10,30);
    
    double xpres;
    double xpas;
    double ypres;
    double ypas;
    double vxpres;
    double vxpas;
    double vypres;
    double vypas;
    
    
    
    ofstream outfile;
    outfile.open(datos);
    xpas=0.1163;
    ypas=0.9772;
    vxpas=-6.36;
    vypas=0.606;
    
    double t=0.0;
    
    for(int i=1;i<=200000;i++)
    {
        double r=sqrt(xpas*xpas+ypas*ypas);
        xpres=vxpas*dt +xpas;
        ypres=vypas*dt +ypas;
        
        vxpres=(-((G*Msol)/(r*r*r))*xpas)*dt+vxpas;
        vypres=(-((G*Msol)/(r*r*r))*ypas)*dt+vypas;
        
        outfile<<xpres<<" "<<ypres<<" "<<vxpres<<" "<<vypres<<" "<<r<<" "<<t<<endl;
        
        xpas=xpres;
        ypas=ypres;
        vxpas=vxpres;
        vypas=vypres;
        t=t+dt;
        
    }
    
    outfile.close();
    
}