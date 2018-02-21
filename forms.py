from wtforms import Form
from wtforms import IntegerField, validators, SubmitField

class BuscaminasForm(Form):
    celdas = IntegerField('Celdas', 
        [
            validators.required(
                'La cantidad de celdas por fila son obligatorias')
        ])
    filas = IntegerField('Filas', 
        [
            validators.required(
                'La cantidad de fila es obligatoria')
        ])

    minas = IntegerField('Minas', 
        [
            validators.required(
                'La cantidad de minas es obligatoria')
        ])

    submit = SubmitField('Jugar')

