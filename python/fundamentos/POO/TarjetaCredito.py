class TarjetaCredito:

   #Declaramos un atributo de clase que se comparte entre todas las instancias de la clase

   banco = "Banco Internacional de Programadores"
   todas_las_tarjetas = []

   def __init__(self, limite_credito, saldo_pagar):
       self.limite_credito=limite_credito
       self.saldo_pagar=saldo_pagar

       TarjetaCredito.todas_las_tarjetas.append(self)

   def hacer_compra(self, monto):  #recibe como argumento el monto de la compra

       #Evaluamos si puede realizar la compra con un método estático

       if TarjetaCredito.puede_comprar(self.limite_credito, self.saldo_pagar, monto):

           self.saldo_pagar += monto 
           self.limite_credito-=monto  #el saldo a pagar del usuario aumenta en la cantidad del valor recibido
           print(f'Se ha hecho una compra por: {monto}, el nuevo saldo a pagar es{self.saldo_pagar}')
           return self
       else:

           print("Tarjeta Rechazada, has alcanzado tu límite de crédito")
           return self

       
   
   @staticmethod
   def puede_comprar(limite, saldo_utilizado, monto):
       #Revisamos si con la compra, el saldo sobrepasa el límite de crédito

       if (saldo_utilizado + monto) > limite:

           return False

       else:

           return True
   
   @classmethod
   def cambiar_banco(cls, nombreBanco):
       cls.banco=nombreBanco
   
   @classmethod
   def todos_los_saldos(cls):
       total_saldos=0
       for tarjeta in cls.todas_las_tarjetas:
           total_saldos+=tarjeta.saldo_pagar
       return total_saldos

tarjeta_carolina= TarjetaCredito(3000,16)
tarjeta_bruno= TarjetaCredito(3000,5)
tarjeta2= TarjetaCredito(3000,45)
tarjeta3= TarjetaCredito(3000,150)
print(tarjeta_carolina.banco)
tarjeta_bruno.banco="Banco de Chile"
print(tarjeta_bruno.banco)

TarjetaCredito.banco="Banco Comercial"
print(tarjeta_carolina.banco)

print(TarjetaCredito.todos_los_saldos())
print(TarjetaCredito.todas_las_tarjetas[1].saldo_pagar)
TarjetaCredito.cambiar_banco("Super Banco Mundial")
print(TarjetaCredito.banco)

tarjeta_carolina.hacer_compra(150)


