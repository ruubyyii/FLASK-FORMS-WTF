from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired,Email, Length, EqualTo, ValidationError

#VALIDACIONES PERSONALIZADAS

def no_palabra(form, field):
    if field.data == 'admin':
        raise ValidationError('El campo username no puede ser admin')
    
    if not field.data[0].isalpha():
        raise ValidationError('No puede empezar por algo que no sea una letra.')

class Persona(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired(),
        Length(min=3, max=10)     
        ])
    email = StringField('Email', validators=[
        DataRequired(),
        Length(min=5, max=12),
        Email()
    ])
    telefono = StringField('Telefono', validators=[
        DataRequired(),
        Length(min=9, max=14)
    ])
    password = PasswordField('Password', validators=[
        DataRequired(),
        Length(min=4, max=8),
        EqualTo('confirm', message='Passwords must match inutil!')
    ])
    confirm = PasswordField('Repeat password',
    validators = [
        DataRequired(),
        Length(min=6, max=14)
    ])

    submit = SubmitField('Enviar')

class PersonaMacro(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired(),
        Length(min=3, max=10),  
        no_palabra
        ])
    email = StringField('Email', validators=[
        DataRequired(),
        Length(min=5, max=12),
        Email()
    ])
    telefono = StringField('Telefono', validators=[
        DataRequired(),
        Length(min=9, max=14)
    ])
    password = PasswordField('Password', validators=[
        DataRequired(),
        Length(min=4, max=8),
        EqualTo('confirm', message='Passwords must match inutil!')
    ])
    confirm = PasswordField('Repeat password',
    validators = [
        DataRequired(),
        Length(min=6, max=14)
    ])

    submit = SubmitField('Enviar')

