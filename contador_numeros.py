def longitud():
    numero=input("Dime un número: ")
    n_cifras=0
    while numero>0:
        numero=numero/10
        n_cifras=n_cifras+1
longitud()
