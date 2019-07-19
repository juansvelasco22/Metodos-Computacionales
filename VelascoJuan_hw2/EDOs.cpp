#include <iostream>
#include <fstream>
#include <math.h>
using namespace std;

void euler(double dt,string datos);
void LP(double dt, string datos);
void RK4(double dt, string datos);

int main()
{
    euler(0.0001, "e_0.0001.dat");
    euler(0.00001, "e_0.00001.dat");
    euler(0.000001,"e_0.000001.dat");
    LP(0.0001, "LP_0.0001.dat");
    LP(0.00001, "LP_0.00001.dat");
    LP(0.000001,"LP_0.000001.dat");
    return 0;
}

void RK4(double dt, string datos)
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
    double k1;
    double k2;
    double k3;
    double k4;
    
    double k1x;
    double k2x;
    double k3x;
    double k4x;
    
    double k1y;
    double k2y;
    double k3y;
    double k4y;
    
    double k1vx;
    double k2vx;
    double k3vx;
    double k4vx;
    
    double k1vy;
    double k2vy;
    double k3vy;
    double k4vy;
   
    
    
    
    ofstream outfile;
    outfile.open(datos);
    xpas=0.1163;
    ypas=0.9772;
    vxpas=-6.36;
    vypas=0.606;
    
    double t=0.0;
    
    outfile.close();
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
    double r;
    
    ofstream outfile;
    outfile.open(datos);
    
    xpas=0.1163;
    ypas=0.9772;
    vxpas=-6.36;
    vypas=0.606;
    r=sqrt(xpas*xpas+ypas*ypas);
    
    double t=0.0;
    outfile<<xpas<<" "<<ypas<<" "<<vxpas<<" "<<vypas<<" "<<r<<" "<<t<<endl;
    
    //Primer paso se hace con Euler
    
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
    
    //Empieza LeapFrog
    
    for(int i=1;i<=200000;i++)
    {
        r=sqrt(xpas*xpas+ypas*ypas);
        xpres=vxpas*2*dt +xpas;
        ypres=vypas*dt +ypas;
        
        vxpres=(-((G*Msol)/(r*r*r))*xpas)*2*dt+vxpas;
        vypres=(-((G*Msol)/(r*r*r))*ypas)*2*dt+vypas;
        
        outfile<<xpres<<" "<<ypres<<" "<<vxpres<<" "<<vypres<<" "<<r<<" "<<t<<endl;
        
        xpas=xpres;
        ypas=ypres;
        vxpas=vxpres;
        vypas=vypres;
        t=t+dt;
    }
    
    outfile.close();
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