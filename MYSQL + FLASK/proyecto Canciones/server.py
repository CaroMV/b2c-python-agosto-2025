#debemos importar los controladores
from flask_app.controllers import usuarios
from flask_app.controllers import canciones

from flask_app import app




if __name__=="__main__":
    app.run(debug=True)