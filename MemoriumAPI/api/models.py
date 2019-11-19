from django.db import models

# Create your models here.

class user(models.Model):
    email = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=50)
    contra = models.CharField(max_length=50)
def __str__(self):
	return '%s < %s >' % (self.nombre, self.email)

class atencion(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    puntuacion = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)
def __str__(self):
	return '%s %s %s' % (self.user, self.puntuacion, self.fecha)

class funciones(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    puntuacion = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)
def __str__(self):
	return '%s %s %s' % (self.user, self.puntuacion, self.fecha)

class lenguaje(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    puntuacion = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)
def __str__(self):
	return '%s %s %s' % (self.user, self.puntuacion, self.fecha)

class memoria(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    puntuacion = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)
def __str__(self):
	return '%s %s %s' % (self.user, self.puntuacion, self.fecha)

class percepcion(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    puntuacion = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)
def __str__(self):
	return '%s %s %s' % (self.user, self.puntuacion, self.fecha)

class lectoescritura(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    puntuacion = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)
def __str__(self):
	return '%s %s %s' % (self.user, self.puntuacion, self.fecha)


