from flask import Flask #Importación de Flask
from flask_bcrypt import Bcrypt

app = Flask(__name__) #Crea instancia de Flask
bcrypt = Bcrypt(app)

#Esta clave es para poder usar la sesión


app.secret_key = "clave_secreta"