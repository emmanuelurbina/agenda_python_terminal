#!/usr/bin/env python
from models.contacto import Contacto


def agenda_run():
    run = True
    menu = """
        Agenda
        1) Crea tabla contactos
        2) Registra contacto
        3) Muestra todos los contactos
        Escribe 0 para terminar
    """
    while run:
        opt = int(input(menu))
        if opt == 0:
            run = False
        if opt == 1:
            Contacto.create_contact_table()
        if opt == 2:
            name = input("Ingresa nombre \n > ")
            email = input("Ingresa email \n > ")
            Contacto.new(name=name, email=email)
        if opt == 3:
            Contacto.all()


if __name__ == "__main__":
    agenda_run()
