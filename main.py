from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# 'postgresql://<usuario>:<contraseña>@<direccion de la db>:<puerto>/<nombre de la db>
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/rockoladb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'some-secret-key'

db = SQLAlchemy(app)

# Importar los modelos
from models import Song, User, Room

# Crear el esquema de la DB
db.create_all()
db.session.commit()

# Rutas de paginas
@app.route('/register')
def register():
    return render_template("register.html")


@app.route('/create-user', methods=['POST'])
def create_user():
    email = request.form["email"]
    password = request.form["password"]

    user = User(email, password)
    db.session.add(user)
    db.session.commit()
    return "ok"


@app.route('/room')
def enter_room():
    return render_template("room.html")

@app.route('/create-room', methods=['POST'])
def create_room():
    room_code = request.form["room_code"]
    print("El codigo de sala es")
    print(room_code)

    return "ok"















# Rutas de otras acciones
@app.route('/song', methods=['GET','POST'])
def crud_song():
    if request.method == 'GET':
        # Hago algo
        print("Llegó un GET")

        # insertar canción
        name = "Perfect"
        artist = "Ed Sheeran"
        genre = "Rock"
        album = "Romanticonas de Viviana"
        year = 2017
        link = "https://youtu.be/2Vv-BfVoq4g"

        entry = Song(name,artist,genre,album,year,link)
        db.session.add(entry)
        db.session.commit()

        return 'Esto fue un GET'

    elif request.method == 'POST':
        # Registrar una cancion
        request_data = request.form
        name = request_data['name']
        artist = request_data['artist']
        genre = request_data['genre']

        print("Nombre:" + name)
        print("Artista:" + artist)
        print("Genero:" + genre)

        # Insertar en la base de datos la canción

        return 'Se registro la canción exitosamente'


@app.route('/updatesong')
def update_song():
    old_name = "Imagine"
    new_name = "Despacito"
    old_song = Song.query.filter_by(name=old_name).first()
    old_song.name = new_name
    db.session.commit()
    return "Actualización exitosa"


@app.route('/getsongs')
def get_songs():
    songs = Song.query.all()
    print(songs[0].artist)
    return "Se trajo la lista de canciones"


@app.route('/deletesong')
def delete_song():
    song_name = "Despacito"
    song = Song.query.filter_by(name=song_name).first()
    db.session.delete(song)
    db.session.commit()
    return "Se borro la canción"






    





























@app.route('/post-request', methods=['POST'])
def post_req():
    request_data = request.form
    print(request_data)
    print(request_data['name'])
    return "Post success"
