from __future__ import unicode_literals
from django.db import models
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
    uno_aux = models.CharField(max_length=45, blank=True, null=True)
    dos_aux = models.CharField(max_length=45, blank=True, null=True)
    tres_aux = models.CharField(max_length=45, blank=True, null=True)
    cuatro_aux = models.CharField(max_length=45, blank=True, null=True)
    cinco_aux = models.CharField(max_length=45, blank=True, null=True)
    def __unicode__(self):
        return self.uno_aux

    """
    class Meta:
        managed = False
        db_table = 'Auxiliar'
    """

#INVENTARIO---------------------------------

class Inventario(models.Model):
    id_inv = models.AutoField(primary_key=True)
    code_admin_inv = models.IntegerField(unique=True)
    contract_subtype_inv = models.CharField(max_length=100, blank=True, null=True)
    province_inv = models.CharField(max_length=45, blank=True, null=True)
    zone_inv = models.IntegerField(blank=True, null=True)
    id_type_inv = models.CharField(max_length=45, blank=True, null=True)
    operator_inv = models.CharField(max_length=45, blank=True, null=True)
    speed_inv = models.CharField(max_length=45, blank=True, null=True)
    id_user_inv = models.ForeignKey('Usuario', db_column='id_user_inv')
    def __unicode__(self):
        return self.code_admin_inv

    """
    class Meta:
        managed = False
        db_table = 'Inventario'
    """

#MENSAJES-----------------------------------

class Mensajes(models.Model):
    id_men = models.AutoField(primary_key=True)
    date_men = models.DateField()
    description_men = models.CharField(max_length=255)
    id_send_men = models.ForeignKey('Usuario', related_name='id_send_men')
    id_receive_men = models.ForeignKey('Usuario', related_name='id_receive_men')
    def __unicode__(self):
        return self.uno_aux

    """
    class Meta:
        managed = False
        db_table = 'Mensajes'
    """

#SUSTRATO-----------------------------------

class Substrata(models.Model):
    id_sub_sub = models.AutoField(primary_key=True)
    province_sub = models.CharField(max_length=45)
    territory_sub = models.CharField(max_length=45)
    series_sub = models.IntegerField()
    id_admin_sub = models.ForeignKey('Inventario', db_column='id_admin_sub')
    service_type_sub = models.CharField(max_length=100)
    zac_zone_sub = models.CharField(max_length=45, blank=True, null=True)
    opening_remarks_sub = models.CharField(max_length=255, blank=True, null=True)
    opening_date_sub = models.CharField(max_length=45, blank=True, null=True)
    postage_date_sub = models.CharField(max_length=45, blank=True, null=True)
    closing_date_sub = models.CharField(max_length=45, blank=True, null=True)
    effective_time_sub = models.FloatField(blank=True, null=True)
    total_time_sub = models.FloatField(blank=True, null=True)
    stops_sub = models.CharField(max_length=45, blank=True, null=True)
    causes_problems_sub = models.CharField(max_length=255, blank=True, null=True)
    cause_types_sub = models.CharField(max_length=45, blank=True, null=True)
    imputed_sub = models.CharField(max_length=45, blank=True, null=True)
    speed_sub = models.CharField(max_length=45, blank=True, null=True)
    fk_sub_gen = models.ForeignKey('SubstrataGeneral', db_column='fk_sub_gen')
    fk_sub_cat = models.ForeignKey('SubstrataCataloged', db_column='fk_sub_cat')
    def __unicode__(self):
        return self.series_sub

    """
    class Meta:
        managed = False
        db_table = 'Substrata'
    """

#SUSTRATO CATALOGADO------------------------

class SubstrataCataloged(models.Model):
    id_sub_cat = models.AutoField(primary_key=True)
    substrata_red_cat = models.CharField(max_length=45)
    substrata_operator_cat = models.CharField(max_length=45)
    year_cat = models.IntegerField()
    month_cat = models.CharField(max_length=45)
    week_cat = models.IntegerField()
    study_week_cat = models.IntegerField()
    impute_cat = models.CharField(max_length=45)
    rpb_cat = models.CharField(max_length=45)
    contract_cat = models.CharField(max_length=45, blank=True, null=True)
    contract_subtype_cat = models.CharField(max_length=45, blank=True, null=True)
    contract_type_cat = models.CharField(max_length=45, blank=True, null=True)
    sla_cat = models.IntegerField(blank=True, null=True)
    slaout_cat = models.IntegerField(blank=True, null=True)
    timeout_vs_sla_repair_cat = models.FloatField(blank=True, null=True)
    slaout_repair_cat = models.IntegerField(blank=True, null=True)
    zone_cat = models.IntegerField(blank=True, null=True)
    fail_type_cat = models.CharField(max_length=45, blank=True, null=True)
    substrata_cat = models.CharField(max_length=45)
    owner_cat = models.CharField(max_length=45)
    imputed_cat = models.CharField(max_length=45)
    timereview_cat = models.IntegerField()
    impute_review_cat = models.CharField(max_length=45, blank=True, null=True)
    postage_date_review_cat = models.CharField(max_length=45, blank=True, null=True)
    time_review_cat = models.CharField(max_length=45, blank=True, null=True)
    description_review_cat = models.CharField(max_length=255, blank=True, null=True)
    comments_review_cat = models.CharField(max_length=255, blank=True, null=True)
    firstweek_review_cat = models.IntegerField()
    id_user_cat = models.ForeignKey('Usuario', db_column='id_user_cat')
    def __unicode__(self):
        return self.substrata_operator_cat

    """
    class Meta:
        managed = False
        db_table = 'Substrata_Cataloged'
    """

#SUSTRATO GENERAL---------------------------

class SubstrataGeneral(models.Model):
    id_sub_gen = models.AutoField(primary_key=True)
    secuence_gen = models.CharField(unique=True, max_length=45)
    cause_type_gen = models.CharField(max_length=45)
    reiterated_gen = models.IntegerField()
    nif_gen = models.CharField(max_length=45)
    operator_gen = models.CharField(max_length=45)
    reopen_gen = models.IntegerField()
    root_gen = models.CharField(max_length=45, blank=True, null=True)
    root_max_gen = models.CharField(max_length=45, blank=True, null=True)
    origin_adress_gen = models.CharField(max_length=45)
    final_adress_gen = models.CharField(max_length=45, blank=True, null=True)
    id_user_gen = models.ForeignKey('Usuario', db_column='id_user_gen')
    def __unicode__(self):
        return self.secuence_gen

    """
    class Meta:
        managed = False
        db_table = 'Substrata_General'
    """