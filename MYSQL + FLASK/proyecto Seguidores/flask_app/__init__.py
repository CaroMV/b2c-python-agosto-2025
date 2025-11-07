from flask import Flask #Importación de Flask

app = Flask(__name__) #Crea instancia de Flask

#Esta clave es para poder usar la sesión
app.secret_key = "clave_secreta"