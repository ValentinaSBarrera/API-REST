# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Categorias(models.Model):
    nombre = models.CharField(max_length=50)
    icono = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'categorias'

class ListasDeLaCompra(models.Model):
    id_usuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='id_usuario', blank=True, null=False)
    id_producto = models.ForeignKey('Productos', models.DO_NOTHING, db_column='id_producto', blank=True, null=False)

    class Meta:
        managed = False
        db_table = 'listas_de_la_compra'


class Marcas(models.Model):
    nombre = models.CharField(max_length=255, blank=True, null=True)
    id_supermercado = models.ForeignKey('Supermercados', models.DO_NOTHING, db_column='id_supermercado', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'marcas'


class Productos(models.Model):
    nombre = models.CharField(max_length=255, blank=True, null=True)
    marca = models.ForeignKey(Marcas, models.DO_NOTHING, db_column='marca', blank=True, null=True)
    precio = models.FloatField(blank=True, null=True)
    tamano = models.CharField(max_length=150, blank=True, null=True)
    imagen = models.CharField(max_length=255, blank=True, null=True)
    tipo = models.ForeignKey('Tipos', models.DO_NOTHING, db_column='tipo', blank=True, null=True)
    favorito = models.IntegerField(blank=True, null=True)

    class Meta: 
        managed = False
        db_table = 'productos'


class Subcategorias(models.Model):
    nombre = models.CharField(max_length=255, blank=True, null=True)
    icono = models.CharField(max_length=255, blank=True, null=True)
    id_categoria = models.ForeignKey(Categorias, models.DO_NOTHING, db_column='id_categoria', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subcategorias'


class Supermercados(models.Model):
    nombre_super = models.CharField(max_length=255, blank=True, null=True)
    logo_super = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supermercados'


class Tipos(models.Model):
    nombre = models.CharField(max_length=255, blank=True, null=True)
    id_subcategoria = models.ForeignKey(Subcategorias, models.DO_NOTHING, db_column='id_subcategoria', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipos'


class Usuarios(models.Model):
    nombre_usuario = models.CharField(max_length=255, blank=True, null=False)
    email = models.CharField(max_length=255, blank=True, null=False)
    contrasena = models.CharField(max_length=255, blank=True, null=False)

    class Meta:
        managed = False
        db_table = 'usuarios'
        
