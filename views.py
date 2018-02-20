from flask import Flask, render_template, request, redirect, url_for
from forms import BuscaminasForm
import requests
from models import Buscaminas, db


app = Flask(__name__)
app.secret_key = 'kjhKJHJKhjkHJKhjkhKJhkjHJKhkjHKJhkJHkj89798h87H98kLoH6820D0s9s'


@app.route('/', methods=['GET', 'POST'])
def home():
    form = BuscaminasForm(request.form)

    if request.method == 'POST':
        
        buscaminas = Buscaminas(
                cantidad_fila = form.filas.data,
                cantidad_celda = form.celdas.data,
                cantidad_minas = form.minas.data
        )

        db.session.add(buscaminas)
        db.session.commit()

        tablero = requests.put('http://127.0.0.1:5555/partida/{}/generar_tablero'.format(
            buscaminas.id), data = {
            'cantidad_minas': buscaminas.cantidad_minas,
            'celdas_x': buscaminas.cantidad_celda,
            'celdas_y': buscaminas.cantidad_fila
            })

        return redirect(url_for('juego', id_buscaminas=buscaminas.id))
    else:
        return render_template('configuracion_buscaminas.html', form=form)


@app.route('/juego/<int:id_buscaminas>', methods=['GET', 'POST'])
def juego(id_buscaminas):

    req = requests.get('http://127.0.0.1:5555/partida/{}'.format(id_buscaminas))
    if req.ok:
        filas = req.json()

    return render_template('juego.html', filas=filas['Filas'], id_partida=filas['Partida'], id_buscaminas=id_buscaminas)

@app.route('/juego/buscamina/<int:id_buscaminas>/partida/<int:id_partida>/<int:x>/<int:y>')
def chequear(id_buscaminas, id_partida, x, y):

    req = requests.post('http://127.0.0.1:5555/partida/{}/chequear_casillero/x/{}/y/{}'.format(id_partida, x, y))
    if req.ok:
        return redirect(url_for('juego', id_buscaminas=id_buscaminas))

    else:
        return 'Error'


if __name__ == '__main__':
    app.run(debug=False, port=5000)