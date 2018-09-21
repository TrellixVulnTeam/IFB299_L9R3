# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Cars(models.Model):
    car_id = models.AutoField(db_column='Car_ID', primary_key=True)  # Field name made lowercase.
    car_makename = models.CharField(db_column='Car_MakeName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    car_model = models.CharField(db_column='Car_Model', max_length=30, blank=True, null=True)  # Field name made lowercase.
    car_series = models.CharField(db_column='Car_Series', max_length=40, blank=True, null=True)  # Field name made lowercase.
    car_seriesyear = models.IntegerField(db_column='Car_SeriesYear', blank=True, null=True)  # Field name made lowercase.
    car_pricenew = models.IntegerField(db_column='Car_PriceNew', blank=True, null=True)  # Field name made lowercase.
    car_enginesize = models.DecimalField(db_column='Car_EngineSize', max_digits=2, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    car_fuelsystem = models.CharField(db_column='Car_FuelSystem', max_length=20, blank=True, null=True)  # Field name made lowercase.
    car_tankcapacity = models.DecimalField(db_column='Car_TankCapacity', max_digits=4, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    car_power = models.IntegerField(db_column='Car_Power', blank=True, null=True)  # Field name made lowercase.
    car_seatingcapacity = models.IntegerField(db_column='Car_SeatingCapacity', blank=True, null=True)  # Field name made lowercase.
    car_standardtransmission = models.CharField(db_column='Car_StandardTransmission', max_length=6, blank=True, null=True)  # Field name made lowercase.
    car_bodytype = models.CharField(db_column='Car_BodyType', max_length=14, blank=True, null=True)  # Field name made lowercase.
    car_drive = models.CharField(db_column='Car_Drive', max_length=5, blank=True, null=True)  # Field name made lowercase.
    car_wheelbase = models.IntegerField(db_column='Car_Wheelbase', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cars'


class Customers(models.Model):
    customer_id = models.IntegerField(db_column='Customer_ID')  # Field name made lowercase.
    customer_name = models.CharField(db_column='Customer_Name', max_length=16)  # Field name made lowercase.
    customer_phone = models.CharField(db_column='Customer_Phone', max_length=14)  # Field name made lowercase.
    customer_address = models.CharField(db_column='Customer_Address', max_length=35)  # Field name made lowercase.
    customer_birthday = models.DateField(db_column='Customer_Birthday', blank=True, null=True)  # Field name made lowercase.
    customer_occupation = models.CharField(db_column='Customer_Occupation', max_length=12)  # Field name made lowercase.
    customer_gender = models.CharField(db_column='Customer_Gender', max_length=1)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'customers'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Orders(models.Model):
    orderid = models.IntegerField(db_column='OrderID')  # Field name made lowercase.
    order_createdate = models.DateField(db_column='Order_CreateDate')  # Field name made lowercase.
    customer_id = models.IntegerField(db_column='Customer_ID')  # Field name made lowercase.
    car_id = models.IntegerField(db_column='Car_ID')  # Field name made lowercase.
    order_pickupdate = models.DateField(db_column='Order_PickupDate')  # Field name made lowercase.
    order_pickupstoreid = models.IntegerField(db_column='Order_PickupStoreID')  # Field name made lowercase.
    order_returndate = models.DateField(db_column='Order_ReturnDate')  # Field name made lowercase.
    order_returnstoreid = models.IntegerField(db_column='Order_ReturnStoreID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'orders'


class Stores(models.Model):
    store_id = models.IntegerField(db_column='Store_ID')  # Field name made lowercase.
    store_name = models.CharField(db_column='Store_Name', max_length=50)  # Field name made lowercase.
    store_address = models.CharField(db_column='Store_Address', max_length=255)  # Field name made lowercase.
    store_phone = models.CharField(db_column='Store_Phone', max_length=18)  # Field name made lowercase.
    store_city = models.CharField(db_column='Store_City', max_length=50)  # Field name made lowercase.
    store_state_name = models.CharField(db_column='Store_State_Name', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'stores'
