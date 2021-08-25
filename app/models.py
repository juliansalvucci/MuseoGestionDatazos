from django.db import models
from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL  
from django.utils.translation import ugettext_lazy as _  #conversión de idiomas
from django.contrib.auth.models import User              #trae los usuarios logueados en el sistema.
from django.core.validators import MinValueValidator

class Tecnica(models.Model):
    descripcion = models.TextField(
        _('descripción'),
        help_text=_('Descripción de la obra')
    )
    nombre = models.CharField(    
        _('Nombre de Obra'),              
        help_text=_('Nombre de la obra'), 
        max_length=200,  
    )
    def __str__(self):   
        return '{}'.format(self.nombre)

class Estilo(models.Model):
    descripcion = models.TextField(
        _('descripción'),
        help_text=_('Descripción de la obra')
    )
    nombre = models.CharField(    
        _('Nombre del estilo'),              
        help_text=_('Nombre del estilo aplicado'), 
        max_length=200,  
    )
    def __str__(self):   
        return '{}'.format(self.nombre)

class TipoRestauracion(models.Model):
    descripcion = models.TextField(
       _('Descripción del tipo de restauracion'),
       help_text=_('Descripción'),
    )
    nombre = models.CharField(    
        _('Nombre de tipo de restauración'),              
        help_text=_('nombre tipo'), 
        max_length=200,  
    )
    class Meta:
        verbose_name = 'Tipo de restauración',
        verbose_name_plural = 'Tipo de restauraciones'
    def __str__(self):   
        return '{}'.format(self.nombre)

class Especialidad(models.Model):
    descripcion = models.TextField(
      _('descripción'),
      help_text=_('Descripción de la obra')
    )
    nombre = models.CharField(    
        _('Nombre de Obra'),              
        help_text=_('Nombre de la obra'), 
        max_length=200,  
    )
    estilo = models.ForeignKey(
        Estilo,
        verbose_name=_('Estilo'),
        help_text=_('Estilo'),
        related_name= 'Estilo',
        on_delete=models.SET_NULL,
        blank = False,
        null = True
    )
    tecnica = models.ForeignKey(
        Tecnica,
        verbose_name=_('Tecnica'),
        help_text=_('Técnica'),
        related_name='Tecnica',
        on_delete=models.SET_NULL,
        blank = False,
        null = True
    )
    
    class Meta:
        ordering = ['nombre']
        verbose_name = 'Especialidad',
        verbose_name_plural = 'Especialidades'
    
    def __str__(self):  
        return '{}'.format(self.nombre)
    
class Restaurador(models.Model):
    apellido = models.CharField(    
        _('Apellido'),              
        help_text=_('Apellido restaurador'), 
        max_length=200,  
    )
    nombre = models.CharField(    
        _('Nombre'),              
        help_text=_('Nombre restaurador'), 
        max_length=200
    )
    email = models.EmailField(
        _('E-mail'),
        help_text=_('Nombre restaurador'), 
        max_length=200, 
    )
    calle = models.CharField(
        _('Calle'),
        max_length=200, 
        null = True,
    )
    numero = models.IntegerField(
        _('Numero'),
        null = True,
    )
    telefono = models.PositiveBigIntegerField(
        _('Teléfono'),
        help_text=_('Teléfono de restaurador'), 
    )
    especialidad = models.ForeignKey(
        Especialidad,
        verbose_name=_('Especialidad'),
        help_text=_('Especialidad derestaurador'),
        related_name='%(app_label)s_%(class)s_related',
        on_delete=models.SET_NULL,
        blank = False,
        null = True
    )
    class Meta:
        ordering = ['nombre']
        verbose_name = 'Restaurador'
        verbose_name_plural = 'Restauradores'
    def __str__(self):   
        return '{} {}'.format(self.nombre,self.apellido)

class Restauracion(models.Model):
    descripcion = models.TextField(
        _('descripción'),
        help_text=_('Descripción de la obra')
    )
    fecha_reingreso = models.DateField(
        _('fecha de reingreso ingreso'),
        help_text=_('fecha de primer ingreso de la obra'),
        null=True
    )
    fecha_salida = models.DateField(
        _('fecha de salida'),
        help_text=_('fecha de salida de la obra')
    )
    precio = models.DecimalField(
        _('Precio de la reparación'),
        help_text=_('precio de la reparación'),
        max_digits=15, 
        decimal_places=2,
        default = 0
    )
    restaurador = models.ForeignKey(
        Restaurador,
        verbose_name=_('Restaurador'),
        help_text=_('restaurador que realizó la restauración'),
        related_name='%(app_label)s_%(class)s_related',
        on_delete=models.SET_NULL,
        blank = False,
        null = True
    )
    tipo_restauracion = models.ForeignKey(
        TipoRestauracion,
        verbose_name=_('Tipo de restauración'),
        help_text=_('Tipo de restauración aplicada'),
        related_name='%(app_label)s_%(class)s_related',
        on_delete=models.SET_NULL,
        blank = False,
        null = True
    )
    obra= models.ForeignKey(
        "Obra",
        verbose_name=_('Obra'),
        help_text=_('Obra'),
        related_name='%(app_label)s_%(class)s_related',
        on_delete=models.SET_NULL,
        blank = False,
        null = True
    )
    class Meta:
        ordering = ['fecha_reingreso']
        verbose_name = 'Restauración',
        verbose_name_plural = 'Restauraciones'
    def __str__(self):  
        return '{} {}'.format(self.fecha_reingreso,self.descripcion)
    
class Artista(models.Model):
    apellido = models.CharField(    
        _('Apellido'),              
        help_text=_('Apellido del artista'), 
        max_length=200,  
    )
    nombre = models.CharField(    
        _('Nombre'),              
        help_text=_('Nombre del artista'), 
        max_length=200,  
    )
    class Meta:
        ordering = ['nombre']
    def __str__(self):  
        return '{} {}'.format(self.nombre, self.apellido)

class Obra(models.Model):
    nombre = models.CharField(    
        _('Nombre de Obra'),              
        help_text=_('Nombre de la obra'), 
        max_length=200,  
    )
    peso = models.IntegerField(
        _('peso'),
        help_text=_('peso en kg')
    )
    valuacion = models.DecimalField(
        _('valuación'),
        help_text=_('valuación en pesos'),
        max_digits=10, 
        decimal_places=2,
        default = 0
    )
    alto = models.IntegerField(
        _('alto'),
       help_text=_('alto de la obra')
    )
    ancho = models.IntegerField(
       _('ancho'),
       help_text=_('ancho de la obra')
    )
    descripcion = models.TextField(
       _('descripción'),
       help_text=_('Descripción de la obra')
    )
    fecha_creacion = models.DateField(
       _('fecha de creación'),
       help_text=_('fecha de creación de la obra')
    )
    fecha_primer_ingreso = models.DateField(
       _('fecha de primer ingreso'),
       help_text=_('fecha de primer ingreso de la obra')
    )
    tecnica = models.ForeignKey(
        Tecnica,
        verbose_name=_('Tecnica'),
        help_text=_('Tecnica empleada para la reparación'),
        related_name='%(app_label)s_%(class)s_related',
        on_delete=models.SET_NULL,
        blank = False,
        null = True
    )
    estilo = models.ForeignKey(
        Estilo,
        verbose_name=_('Estilo'),
        help_text=_('Estilo de reparación'),
        related_name='%(app_label)s_%(class)s_related',
        on_delete=models.SET_NULL,
        blank = False,
        null = True
    )
    #restauracion = models.ForeignKey(
        #Restauracion,
        #verbose_name=_('Restauración'),
        #help_text=_('Restauraciones de obra'),
        #related_name='%(app_label)s_%(class)s_related',
        #on_delete=models.SET_NULL,
        #blank = True,
        #null = True
    #)
    artista = models.ForeignKey(
        Artista,
        verbose_name=_('Artista'),
        help_text=_('Artista creador de la'),
        related_name='%(app_label)s_%(class)s_related',
        on_delete=models.SET_NULL,
        blank = True,
        null = True
    )
    class Meta:
        ordering = ['nombre']
    def __str__(self):   
        return '{}'.format(self.nombre)

class RestauradorEspecialidad(models.Model):
    especialidad = models.ForeignKey(
        Especialidad,
        verbose_name=_('Especialidad'),
        related_name='%(app_label)s_%(class)s_related',
        on_delete=models.SET_NULL,
        blank = True,
        null = True
    )
    restaurador = models.ForeignKey(
        Restaurador,
        verbose_name=_('Restaurador'),
        related_name='%(app_label)s_%(class)s_related',
        on_delete=models.SET_NULL,
        blank = True,
        null = True
    )
    class Meta:
        verbose_name = 'Restaurador por especialidad',
        verbose_name_plural = 'Restaurador por especialidades'
    def __str__(self):   
        return '{}'.format(self.restaurador,self.especialidad)



  








