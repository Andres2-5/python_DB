from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class NewProductForm(FlaskForm):
    nombre = StringField('Ingrese el producto :')
    precio = StringField('Ingrese el precio :')
    submit = SubmitField("Registrar")
    