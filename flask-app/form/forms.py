from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import SelectField, SubmitField
from wtforms.validators import DataRequired

class selectionForm(FlaskForm):
    report = SelectField(label='Seleccione una reporte',
                         validators=[DataRequired()],
                         choices=[
                             (1, 'Todos los Productos presentes en orden Alfabético'),
                             (2, 'Todos los Proveedores con Dirección perteneciente a Alajuela'),
                             (3, 'Todos los Proveedores con Dirección perteneciente a Cartago y Guanacaste'),
                             (4, 'Todos los Cantones de Heredia y Puntarenas juntos'),
                             (5, 'Todas las Ordenes de Compra de los Proveedores de Limón'),
                             (6, 'Todos los Productos de la Línea de Comida perteneciente a Carnes')
                        ])
    option = SelectField(label='Seleccione un formato',
                         validators=[DataRequired()],
                         choices=[
                             (1, 'XML'),
                             (2, 'JSON')
                           ])
    download = SubmitField('Descargar')


class deserializationForm(FlaskForm):
    file = FileField(label='Elija un archivo XML',
                     validators=[FileRequired(),
                                  FileAllowed(['xml', 'XML'], 'Solo se permiten archivos XML')
                                ])
    upload = SubmitField('Deserializar archivo')