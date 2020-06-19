import peewee as pw
from conection import db


class Contacto(pw.Model):
    name = pw.CharField(unique=True, max_length=50, index=True)
    email = pw.CharField(max_length=50)

    class Meta:
        database = db
        db_table = 'contactos'

    @classmethod
    def create_contact_table(cls):
        if not Contacto.table_exists():
            Contacto.create_table()
            print("Se creo la tabla -contactos- exitosamente")
        else:
            print("La tabla -contactos- ya existe")
