from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuración de la base de datos SQLite (cambia 'sqlite:///test.db' al URI de tu base de datos)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Definición del modelo de Usuario para la base de datos
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    contraseña = db.Column(db.String(100), nullable=False)

@app.route('/sign_up', methods=['POST'])
def registro():
    datos_registro = request.json
    nuevo_usuario = Usuario(nombre=datos_registro['nombre'], email=datos_registro['email'], contraseña=datos_registro['contraseña'])
    db.session.add(nuevo_usuario)
    db.session.commit()
    return jsonify({'mensaje': 'Usuario registrado exitosamente'})

@app.route('/login', methods=['POST'])
def inicio_sesion():
    datos_inicio_sesion = request.json
    email = datos_inicio_sesion['email']
    contraseña = datos_inicio_sesion['contraseña']
    
    usuario = Usuario.query.filter_by(email=email, contraseña=contraseña).first()
    if usuario:
        return jsonify({'mensaje': 'Inicio de sesión exitoso', 'usuario': {'nombre': usuario.nombre, 'email': usuario.email}})
    else:
        return jsonify({'mensaje': 'Credenciales incorrectas'})

if __name__ == '__main__':
    # Crear la base de datos si no existe
    db.create_all()
    app.run(debug=True)
