from flask import Flask, request
flrom flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
db = SQLAlchemy(app)
#ruta de paginas
@app.route('/')
def get_home():
    return 'Este es el home'


@app.route('/signup')
def sign_up():
    return 'Este es el registro'    

@app.route('/room')
def sign_room():
    return 'Esta es la pagina de una sala'    
# ruta de     otras acciones
@app.route('/song', methods=['GET', 'POST'])
def crud_song():
    if request.method == 'GET':
        #hago algo
        print("Llego un get")
        return'esto fue un get'
    elif request.method == 'POST':
    #hago algo con el post
    #registrar una cancion
        request_data = request.form
        name = request_data['name']
        artist = request_data['artist']
        genre = request_data['genre']
        print('Nombre: '+name)
        print('Artista: '+artist)
        print('Genero: '+genre)
    #Insertar datos en BD
        return'Se genero la canción exitosamente'
    




