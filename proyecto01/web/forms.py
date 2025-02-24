from django import forms
from .models import *

# Formulario de Login
class formularioLogin(forms.Form):
    nombre_usuario = forms.CharField(
        label="Nombre",
        required=True,
        widget=forms.TextInput(
            attrs={'placeholder': 'Nombre de usuario'}
        )
    )
    clave_usuario = forms.CharField(
        label="Clave Usuario",
        required=True,
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Ingresá tu clave'}
        )
    )
#
# Formulario de Contacto basado en Modelo
class formularioContacto(forms.ModelForm):
    class Meta:
        model = MensajeContacto
        fields = ['nombre', 'dni', 'telefono', 'email', 'mensaje']
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre'}),
            'dni': forms.TextInput(attrs={'placeholder': 'DNI'}),
            'telefono': forms.TextInput(attrs={'placeholder': 'Teléfono'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email'}),
            'mensaje': forms.Textarea(attrs={'placeholder': 'Dejanos tu mensaje...'}),
        }

    def clean_nombre(self):
        nombre = self.cleaned_data.get("nombre")
        if not nombre.isalpha():
            raise forms.ValidationError('El campo "nombre" solo puede contener letras')
        return nombre

    def clean_dni(self):
        dni = str(self.cleaned_data.get("dni"))
        if not dni.isdigit():
            raise forms.ValidationError('El campo "DNI" solo puede contener números')
        if len(dni) != 8:
            raise forms.ValidationError('El campo "DNI" debe contener 8 dígitos')
        return dni
    
    def clean_telefono(self):
        telefono = str(self.cleaned_data.get("telefono"))
        if not telefono.isdigit():
            raise forms.ValidationError('El campo "Teléfono" solo puede contener números')
        return telefono

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if "@" not in email:
            raise forms.ValidationError('Ingresá una dirección de email válida. Ejemplo nombre@email.com')
        return email

    def clean_mensaje(self):
        mensaje = self.cleaned_data.get("mensaje")
        if len(mensaje) < 10:    
            raise forms.ValidationError('El campo "Mensaje" debe contener al menos 10 caracteres')
        return mensaje    
# 
# Form avanzado hecho con GPT
class formularioAvanzado(forms.Form):
    longitud = forms.DecimalField(
        label='Largo (m)',
        widget=forms.NumberInput(attrs={'placeholder': 'Largo (m)'}),
        min_value=10,
        max_value=120,
        required=False
    )
    ancho = forms.DecimalField(
        label='Ancho (m)',
        widget=forms.NumberInput(attrs={'placeholder': 'Ancho (m)'}),
        min_value=10,
        max_value=90,
        required=False
    )
    opciones_suelo = [
        ('', 'Seleccione el tipo de suelo'),
        ('cesped_natural', 'Césped Natural'),
        ('cesped_artificial', 'Césped Artificial'),
        ('arcilla', 'Arcilla'),
        ('cemento', 'Cemento'),
        ('parquet', 'Parquet'),
    ]
    tipo_suelo = forms.ChoiceField(
        label='Tipo de Suelo',
        widget=forms.Select(attrs={'placeholder': 'Tipo de Suelo'}),
        choices=opciones_suelo,
        required=False
    )
    opciones_red = [
        ('', 'Seleccione el tipo de red'),
        ('standard', 'Estándar'),
        ('reinforced', 'Reforzada'),
    ]
    tipo_red = forms.ChoiceField(
        label='Tipo de Red',
        widget=forms.Select(attrs={'placeholder': 'Tipo de Red'}),
        choices=opciones_red,
        required=False
    )
    iluminacion = forms.BooleanField(
        label='Iluminación',
        widget=forms.CheckboxInput(
            attrs={
                'class': 'placeholderCustom',
                'placeholder': 'Iluminación'
            }),
        required=False
    )
    marcador = forms.BooleanField(
        label='Marcador Electrónico',
        widget=forms.CheckboxInput(
            attrs={
                'class': 'placeholderCustom',
                'placeholder': 'Marcador Electrónico'
            }),
        required=False
    )
    gradas = forms.BooleanField(
        label='Graderías',
        widget=forms.CheckboxInput(
            attrs={
                'class': 'placeholderCustom',
                'placeholder': 'Graderías'
            }),
        required=False
    )
    campo_texto = forms.CharField(
        label='Comentarios Adicionales',
        widget=forms.Textarea(attrs={'placeholder': 'Comentarios Adicionales'}),
        max_length=255,
        required=False
    )
#
#formulario para vista parametrizada
class CanchaFilterForm(forms.Form):
    tipo_suelo = forms.ChoiceField(
        label='Tipo de Suelo',
        choices=Cancha.TIPOS_SUELO,
        required=False,
        widget=forms.Select(attrs={'placeholder': 'Seleccione el tipo de suelo'})
    )
    tipo_red = forms.ChoiceField(
        label='Tipo de Red',
        choices=Cancha.TIPOS_RED,
        required=False,
        widget=forms.Select(attrs={'placeholder': 'Seleccione el tipo de red'})
    )
    iluminacion = forms.BooleanField(
        label='Iluminación',
        required=False,
        widget=forms.CheckboxInput()
    )
    marcador = forms.BooleanField(
        label='Marcador Electrónico',
        required=False,
        widget=forms.CheckboxInput()
    )
    gradas = forms.BooleanField(
        label='Graderías',
        required=False,
        widget=forms.CheckboxInput()
    )
# Forms basados en los modelos cancha, cliente y venta
class CanchaForm(forms.ModelForm):
    class Meta:
        model = Cancha
        fields = ['longitud', 'ancho', 'tipo_suelo', 'tipo_red', 'iluminacion', 'marcador', 'gradas']
        widgets = {
            'longitud': forms.NumberInput(attrs={'placeholder': 'Largo (m)'}),
            'ancho': forms.NumberInput(attrs={'placeholder': 'Ancho (m)'}),
            'tipo_suelo': forms.Select(attrs={'placeholder': 'Seleccione el tipo de suelo'}),
            'tipo_red': forms.Select(attrs={'placeholder': 'Seleccione el tipo de red'}),
            'iluminacion': forms.CheckboxInput(attrs={'class': 'placeholderCustom', 'placeholder': 'Iluminación'}),
            'marcador': forms.CheckboxInput(attrs={'class': 'placeholderCustom', 'placeholder': 'Marcador Electrónico'}),
            'gradas': forms.CheckboxInput(attrs={'class': 'placeholderCustom', 'placeholder': 'Graderías'}),
        }

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['comentarios']
        widgets = {
            'comentarios': forms.Textarea(attrs={'placeholder': 'Comentarios Adicionales'}),
        }

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['dni', 'apellido', 'nombre', 'email']
        widgets = {
            'dni': forms.TextInput(attrs={'placeholder': 'DNI'}),
            'apellido': forms.TextInput(attrs={'placeholder': 'Apellido'}),
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
        }
        