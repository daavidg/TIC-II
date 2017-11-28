def suma(num1,num2):
    resp=num1+num2
    return resp
def resta(num1,num2):
    resp=num1-num2
    return resp
def mult(num1,num2):
    resp=num1*num2
    return resp
def div(num1,num2):
    resp=num1/num2
    return resp

def menu_principal():
    seguir="Si"
    num1=input("Dime un número: ")
    num2=input("Dime otro número: ")
    while (seguir=="Si"):
        print "Qué deseas hacer con los números: "
        print "1. Sumarlos"
        print "2. Restarlos"
        print "3. Multiplicarlos"
        print "4. Dividirlos"
        respuesta=input()
        if (respuesta==1):
            print num1, "+", num2, "=", suma(num1,num2)
        if (respuesta==2):
            print num1, "-", num2, "=", resta(num1,num2)
        if (respuesta==3):
            print num1, "*", num2, "=", mult(num1,num2)
        if (respuesta==4):
            print num1, "/", num2, "=", div(num1,num2)
        seguir=raw_input("¿Quieres seguir usando este programa? Si o no: ")
            
menu_principal()
