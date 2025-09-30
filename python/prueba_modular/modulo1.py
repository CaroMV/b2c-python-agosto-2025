
print("Ejecutandose el modulo1")
print("El valor del __name__ es:", __name__)

import modulo2
import modulo3

if __name__=="__main__":
    print("el modulo 1 se está ejecutando directamente")
else:
    print("modulo 1 se está importando")