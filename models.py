from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/buscaminas_client.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

class Buscaminas(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    cantidad_fila = db.Column(db.Integer)
    cantidad_celda = db.Column(db.Integer)
    cantidad_minas = db.Column(db.Integer)


if __name__ == '__main__':
    manager.run()