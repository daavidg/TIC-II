#include<iostream>

int main(){
    /*Esto es un comentario que ocupa
    m�s de una l�nea del p*/
    //Esto es un comentario en una l�nea
    /*Definici�n de variables*/
    int a;
    int b;
    int c;
    int solucion,salir;
    /*Inicializaci�n de variables*/
    a=2;
    b=4;
    c=-1;
    solucion=a+b+c;
    std::cout<< "La solucion es: " << solucion << std::endl;
    std::cout<<"Para seguir, toca cualquier tecla"
    std::cin>>salir;
    return 0;
}
