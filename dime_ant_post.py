def dime_ant_post():
    numero=input("Dime un n�mero: ")
    for cont in range(numero-15, numero, 1):
        print cont
    for cont in range(numero+1, numero+16, 1):
        print cont
dime_ant_post()
