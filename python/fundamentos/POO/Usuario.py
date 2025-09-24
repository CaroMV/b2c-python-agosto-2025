class Usuario:

   def __init__(self, nombre, apellido, email):

       self.nombre = nombre

       self.apellido = apellido

       self.email = email

       self.limite_credito = 30000

       self.saldo_pagar = 0

  
   def hacer_compra(self, monto): 

         if monto > self.limite_credito:
             print("Compra no autorizada, excede el límite de crédito")
             return self
         else:
            self.saldo_pagar += monto
            self.limite_credito -= monto
            print(f"Compra autorizada por {monto}. Nuevo saldo a pagar: {self.saldo_pagar}")
            return self
    #     pagar_tarjeta(self, monto): crea un método que pague un monto de la tarjeta de crédito, haciendo que se reduzca el saldo_pagar.
   def pagar_tarjeta(self,monto):
        if monto > self.saldo_pagar:
            print("El monto a pagar excede el saldo a pagar")
            return self
        else:
            self.saldo_pagar -= monto
            self.limite_credito += monto
            print(f"Pago realizado por {monto}. Nuevo saldo a pagar: {self.saldo_pagar}")
            return self
 # mostrar_saldo_usuario(self): crea un método que imprima el nombre completo del usuario y el saldo a pagar de su tarjeta.Ejemplo: “Usuario: Nariyoshi Miyagi, Saldo a Pagar: $50”
   def mostrar_saldo_usuario(self):
       print(f'Usuario: {self.nombre} , saldo a pagar: {self.saldo_pagar}')
       return self
   def transferir_deuda(self, otro_usuario, monto):
        #El saldo del usuario que usa el método, disminuye
        self.saldo_pagar-=monto
        self.limite_credito+=monto
        #otro_usuario representa un objeto creado con la clase usuario
        otro_usuario.saldo_pagar+=monto
        otro_usuario.limite_credito-=monto
        print(f'Se ha transferido la deuda por el monto de {monto}')
        print(f'{self.nombre} tiene un saldo a pagar de : {self.saldo_pagar}')
        print(f'{otro_usuario.nombre} tiene un saldo a pagar de : {otro_usuario.saldo_pagar}')
        return self


carolina = Usuario("Carolina", "Moreno", "cmoreno@skillnest.com")
jesus=Usuario("Jesus", "De leon", "jesus@gmail.com")
carolina.hacer_compra(5000)
carolina.pagar_tarjeta(2000)
carolina.mostrar_saldo_usuario()

carolina.transferir_deuda(jesus,3000)


carolina.hacer_compra(100).hacer_compra(500).pagar_tarjeta(500).mostrar_saldo_usuario()
