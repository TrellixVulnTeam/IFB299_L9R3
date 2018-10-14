import django_tables2 as tables
class customerTable (tables.Table):
    class meta:
        model=Customers

class vehicleTable(tables.Table):
    class meta:
        model=Cars


#we may need this page.... not sure yet.....