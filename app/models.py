from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

#CATEGORIA----------------------------------

class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre_categoria = models.CharField(max_length = 128, unique=True)
    image_categoria = models.ImageField(upload_to='img_categorias', blank=True)
    def __unicode__(self):
        return self.nombre_categoria

#USUARIO------------------------------------

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    user = models.OneToOneField(User)
    activado = models.BooleanField(default=False)
    categoria = models.ManyToManyField(Categoria, blank=True )
    catSugerida = models.ManyToManyField(Categoria, blank=True, related_name="cat_sugerida")
    def __unicode__(self):
        return self.user.username

#LINK---------------------------------------

class Link(models.Model):
    id_link = models.AutoField(primary_key=True)
    nombre_link=models.CharField(max_length = 128, unique=True, default=0)
    link = models.CharField(max_length = 255, unique=True)
    id_categoria = models.ForeignKey(Categoria)
    image_link = models.ImageField(upload_to='img_categorias', blank=True)
    def __unicode__(self):
        return self.link

#AUXILIAR-----------------------------------

class Auxiliar(models.Model):
    id_aux = models.AutoField(primary_key=True)
    uno_aux = models.CharField(max_length=128, blank=True)
    dos_aux = models.CharField(max_length=128, blank=True)
    tres_aux = models.CharField(max_length=128, blank=True)
    cuatro_aux = models.CharField(max_length=128, blank=True)
    cinco_aux = models.CharField(max_length=128, blank=True)
    def __unicode__(self):
        return self.uno_aux

#ARCHIVO------------------------------------

class Archivo(models.Model):
    id_archivo = models.AutoField(primary_key=True)
    name_archivo = models.CharField(max_length=128, unique=True)
    def __unicode__(self):
        return self.name_archivo

#INVENTARIO---------------------------------

class Inventario(models.Model):
    id_inv = models.AutoField(primary_key=True)
    code_admin_inv = models.CharField(max_length=128, blank=True)
    contract_subtype_inv = models.CharField(max_length=100, blank=True)
    province_inv = models.CharField(max_length=128, blank=True)
    zone_inv = models.CharField(max_length=128, blank=True)
    id_type_inv = models.CharField(max_length=128, blank=True)
    operator_inv = models.CharField(max_length=128, blank=True)
    speed_inv = models.CharField(max_length=128, blank=True)
    #id_user_inv = models.ForeignKey('Usuario', db_column='id_user_inv')
    def __unicode__(self):
        return self.code_admin_inv

#MENSAJES-----------------------------------

class Mensajes(models.Model):
    id_men = models.AutoField(primary_key=True)
    date_men = models.DateField(default=timezone.now)
    description_men = models.CharField(max_length=255)
    #id_send_men = models.ForeignKey('Usuario', related_name='id_send_men')
    #id_receive_men = models.ForeignKey('Usuario', related_name='id_receive_men')
    def __unicode__(self):
        return self.date_men

#SUSTRATO CATALOGADO------------------------

class SustratosCatalogados(models.Model):
    id_sus_cat = models.AutoField(primary_key=True)
    #administrativo = models.ForeignKey('Inventario', db_column='administrativo')
    administrativo = models.CharField(max_length=128, blank=True)
    sustrato_red = models.CharField(max_length=128, blank=True)
    sustrato_operadora = models.CharField(max_length=128, blank=True)
    año = models.CharField(max_length=128, blank=True)
    mes = models.CharField(max_length=128, blank=True)
    semana = models.CharField(max_length=128, blank=True)
    semana_estudio = models.CharField(max_length=128, blank=True)
    imputable = models.CharField(max_length=128, blank=True)
    kpi11b = models.CharField(max_length=128, blank=True)
    contrato = models.CharField(max_length=128, blank=True)
    subtipo_contrato = models.CharField(max_length=128, blank=True)
    velocidad = models.CharField(max_length=128, blank=True)
    id_tipo_contrato = models.CharField(max_length=128, blank=True)
    sla = models.CharField(max_length=128, blank=True)
    fuera_de_sla = models.CharField(max_length=128, blank=True)
    tiempo_fuera_vs_sla_tiempo_reparacion = models.CharField(max_length=128, blank=True)
    fuera_sla_tiempo_reparacion = models.CharField(max_length=128, blank=True)
    zona = models.CharField(max_length=128, blank=True)
    provincia = models.CharField(max_length=128, blank=True)
    ########################################################################
    #provincia = models.CharField(max_length=128, blank=True)
    territorio = models.CharField(max_length=128, blank=True)
    serie = models.CharField(max_length=128, blank=True)
    #administrativo = models.ForeignKey('Inventario', db_column='administrativo')
    tipo_de_servicio = models.CharField(max_length=100, blank=True)
    zona_zac = models.CharField(max_length=128, blank=True)
    comentarios_de_apertura = models.CharField(max_length=255, blank=True)
    fecha_de_apertura = models.CharField(max_length=128, blank=True)
    fecha_de_franqueo = models.CharField(max_length=128, blank=True)
    fecha_de_cierre = models.CharField(max_length=128, blank=True)
    tiempo_efectivo = models.CharField(max_length=128, blank=True)
    tiempo_total = models.CharField(max_length=128, blank=True)
    paradas = models.CharField(max_length=128, blank=True)
    causa_del_problema = models.CharField(max_length=255, blank=True)
    imputado_a = models.CharField(max_length=128, blank=True)
    velocidad = models.CharField(max_length=128, blank=True)
    ########################################################################
    causa = models.CharField(max_length=128, blank=True)
    sustrato = models.CharField(max_length=128, blank=True)
    owner = models.CharField(max_length=128, blank=True)
    final_imputado_a = models.CharField(max_length=128, blank=True)
    tiempo = models.CharField(max_length=128, blank=True)
    revisar_tiempos = models.CharField(max_length=128, blank=True)
    imputacion_revisada = models.CharField(max_length=128, blank=True)
    fecha_franqueo_revisada = models.CharField(max_length=128, blank=True)
    tiempo_revisado = models.CharField(max_length=128, blank=True)
    descripcion = models.CharField(max_length=255, blank=True)
    comentarios = models.CharField(max_length=255, blank=True)
    primera_semana = models.CharField(max_length=128, blank=True)
    #id_user_sus_cat = models.ForeignKey('Usuario', db_column='id_user_sus_cat')
    #id_archivo_sus_cat = models.ForeignKey('Archivo', db_column='id_archivo_sus_cat')
    def __unicode__(self):
        return self.administrativo

#SUSTRATO ORIGINAL--------------------------

class SustratosOriginales(models.Model):
    id_sus_gen = models.AutoField(primary_key=True)
    provincia = models.CharField(max_length=128, blank=True)
    territorio = models.CharField(max_length=128, blank=True)
    serie = models.CharField(max_length=128, blank=True)
    secuencia = models.CharField(unique=True, max_length=128, blank=True)
    #administrativo = models.ForeignKey('Inventario', db_column='administrativo')
    administrativo = models.CharField(max_length=128, blank=True)
    tipo_de_servicio = models.CharField(max_length=100, blank=True)
    zona_zac = models.CharField(max_length=128, blank=True)
    comentarios_de_apertura = models.CharField(max_length=255, blank=True)
    fecha_de_apertura = models.CharField(max_length=128, blank=True)
    fecha_de_franqueo = models.CharField(max_length=128, blank=True)
    fecha_de_cierre = models.CharField(max_length=128, blank=True)
    tiempo_efectivo = models.CharField(max_length=128, blank=True)
    tiempo_total = models.CharField(max_length=128, blank=True)
    paradas = models.CharField(max_length=128, blank=True)
    causa_del_problema = models.CharField(max_length=255, blank=True)
    tipo_de_causa = models.CharField(max_length=128, blank=True)
    reiterada = models.CharField(max_length=128, blank=True)
    imputado_a = models.CharField(max_length=128, blank=True)
    nif = models.CharField(max_length=128, blank=True)
    operadora = models.CharField(max_length=128, blank=True)
    velocidad = models.CharField(max_length=128, blank=True)
    reabierta = models.CharField(max_length=128, blank=True)
    raiz = models.CharField(max_length=128, blank=True)
    raiz_maxima = models.CharField(max_length=128, blank=True)
    domicilio_cliente_origen = models.CharField(max_length=128, blank=True)
    domicilio_cliente_destino = models.CharField(max_length=128, blank=True)
    #id_user_sus_gen = models.ForeignKey('Usuario', db_column='id_user_sus_gen')
    #id_archivo_sus_gen = models.ForeignKey('Archivo', db_column='id_archivo_sus_gen')
    def __unicode__(self):
        return self.administrativo






