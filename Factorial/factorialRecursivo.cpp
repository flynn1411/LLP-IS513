#include<iostream>

using namespace std;

int factorialRecursivo(int n);

int main()
{
    
    int n;
    cout<<"Ingrese el numero para obtener factorial:\t";
    cin>>n;

    cout<<"\n\nEl factorial de "<<n<<" es "<<factorialRecursivo(n)<<".\n";

    return 0;
}

int factorialRecursivo(int n){
    if(n <= 1){
        return 1;
    }else{
        return n*factorialRecursivo(n-1);
    }
}
