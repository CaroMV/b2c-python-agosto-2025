from flask_app import app
from flask_app.controllers import mascotas  # Importamos el controlador

from flask_app.controllers import usuarios

if __name__ == "__main__":
    app.run(debug=True)