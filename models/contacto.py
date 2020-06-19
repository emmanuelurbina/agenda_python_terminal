import peewee as pw
from tabulate import tabulate as table
from conection import db


class Contacto(pw.Model):
    name = pw.CharField(unique=True, max_length=50, index=True)
    email = pw.CharField(max_length=50)

    class Meta:
        database = db
        db_table = 'contactos'

    @classmethod
    def new(cls, name, email):
        try:
            contacto = Contacto()
            contacto.name = name
            contacto.email = email
            contacto.save()
            print("Se guardo correctamente, {name}".format(name=name))
        except:
            print("Ocurrio un error interno")

    @classmethod
    def all(cls):
        try:
            contactos = Contacto().select()
            results = []
            for contacto in contactos:

                print(
                    table([[f"{contacto.id}", f"{contacto.name}", f"{contacto.email}"]], headers=["id", "Nombre", "E-mail"], tablefmt="pretty"))

        except:
            print("Ocurrio un error interno")

    @classmethod
    def create_contact_table(cls):
        if not Contacto.table_exists():
            Contacto.create_table()
            print("Se creo la tabla -contactos- exitosamente")
        else:
            print("La tabla -contactos- ya existe")
