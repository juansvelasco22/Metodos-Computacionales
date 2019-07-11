#include <iostream>
#include <fstream>

using namespace std;

double caso1();
double caso2();
double caso3();

int main()
{
    double L=1.0;
    double dx=0.005;
    double deltax=L/(dx);
    double c=300.0;
    double dt=(0.25*dx)/(c*c);
    double A0=0.01;
    double condicion=((c*c*dx*dx)/(dt*dt));
    
    double pas[200];
    double pres[200];
    double fut[200];
    
    cout<<caso1(deltax, pas[], pres[], fut[], condicion, A0,L)<<endl;
    cout<<caso2(deltax, pas[], pres[], fut[], condicion, A0,L)<<endl;
    cout<<caso3(deltax, pas[], pres[], fut[], condicion, A0,L)<<endl;
    
   
    
    return 0;   
}


double caso1(double deltax, double pas[], double pres[], double fut[], double condicion, double A0, double L)
{
    ofstream outfile;
    for (int i=0;i<deltax;i++)  ///Condiciones iniciales caso 1
    {
        if(i==(deltax/2.0))
        {
            pas[i]=A0;
        }
        if(i==0)
        {
            pas[i]=0.0;
        }
        if(i==deltax)
        {
            pas[i]=0.0;
        }
        if(i<(deltax/2.0))
        {
            pas[i]=i*deltax*(A0/(L/2));
        }
        if(i>(deltax/2.0))
        {
            pas[i]=(i*deltax*(A0/(L/2)))+2*A0;
        }       
    }
    
    
     outfile.open("caso1.dat");
    
    for (int i=0;i<deltax;i++) //Condicion inicial
    {
        pres[i]=(1/2)*((condicion)*(pas[i+1]+pas[i-1]-(2.0*pas[i]))-pas[i]+2.0*pas[i]);
    }
    
    
    for (int i=2;i<=30;i++)    //For del tiempo
    {
        
        for(int d=0;d<deltax;d++)
        {
            outfile << pres[i] << " "; 
        }
        outfile <<"\n";
        
        for (int e=1;e<=deltax;e++)   //For del espacio
        {
            fut[e]=(condicion)*(pres[e+1]+pres[e-1]-2*pres[e])-pas[e]+2*pres[e];
        }
        
        for(int h=0;h<=deltax;h++)   //Cambiar datos
        {
            
            pas[h]=pres[h];
            pres[h]=fut[h];

        }
        //outfile<<pas[i]<<endl;
        //cout<<pas[i]<<endl;
        
        
    }
    
    outfile.close();
}

double caso2(double deltax, double pas[], double pres[], double fut[], double condicion, double A0, double L)
{
    
    for (int i=0;i<deltax;i++)  ///Condiciones iniciales caso 2
    {
        if(i==(deltax/2.0))
        {
            pas[i]=A0;
        }
        if(i==0)
        {
            pas[i]=0.0;
        }
        if(i==deltax)
        {
            pas[i]=pas[i-1];
        }
        if(i<(deltax/2.0))
        {
            pas[i]=i*deltax*(A0/(L/2));
        }
        if(i>(deltax/2.0))
        {
            pas[i]=(i*deltax*(A0/(L/2)))+2*A0;
        }       
    }
     outfile.open("caso2.dat");
    
    for (int i=0;i<deltax;i++) //Condicion inicial
    {
        pres[i]=(1/2)*((condicion)*(pas[i+1]+pas[i-1]-(2.0*pas[i]))-pas[i]+2.0*pas[i]);
    }
    
    
    for (int i=2;i<=30;i++)    //For del tiempo
    {
        
        for(int d=0;d<deltax;d++)
        {
            outfile << pres[i] << " "; 
        }
        outfile <<"\n";
        
        for (int e=1;e<=deltax;e++)   //For del espacio
        {
            fut[e]=(condicion)*(pres[e+1]+pres[e-1]-2*pres[e])-pas[e]+2*pres[e];
        }
        
        for(int h=0;h<=deltax;h++)   //Cambiar datos
        {
            
            pas[h]=pres[h];
            pres[h]=fut[h];

        }
        //outfile<<pas[i]<<endl;
        //cout<<pas[i]<<endl;
        
        
    }
    
    outfile.close();
}


double caso3(double deltax, double pas[], double pres[], double fut[], double condicion, double A0, double L)
{
    
     for (int i=0;i<deltax;i++)  ///Condiciones iniciales caso 1
    {
        if(i==(deltax/2.0))
        {
            pas[i]=A0;
        }
        if(i==0)
        {
            pas[i]=0.0;
        }
        if(i==deltax)
        {
            pas[i]=pas[i-1];
        }
        if(i<(deltax/2.0))
        {
            pas[i]=i*deltax*(A0/(L/2));
        }
        if(i>(deltax/2.0))
        {
            pas[i]=(i*deltax*(A0/(L/2)))+2*A0;
        }  
     outfile.open("caso3.dat");
    
    for (int i=0;i<deltax;i++) //Condicion inicial
    {
        pres[i]=(1/2)*((condicion)*(pas[i+1]+pas[i-1]-(2.0*pas[i]))-pas[i]+2.0*pas[i]);
    }
    
    
    for (int i=2;i<=30;i++)    //For del tiempo
    {
        
        for(int d=0;d<deltax;d++)
        {
            outfile << pres[i] << " "; 
        }
        outfile <<"\n";
        
        for (int e=1;e<=deltax;e++)   //For del espacio
        {
            fut[e]=(condicion)*(pres[e+1]+pres[e-1]-2*pres[e])-pas[e]+2*pres[e];
        }
        
        for(int h=0;h<=deltax;h++)   //Cambiar datos
        {
            
            pas[h]=pres[h];
            pres[h]=fut[h];

        }
        //outfile<<pas[i]<<endl;
        //cout<<pas[i]<<endl;
        
        
    }
    
    outfile.close();
}


