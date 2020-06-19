#!/usr/bin/env python
from models.contacto import Contacto


def agenda_run():
    run = True
    menu = """
        Agenda
        1) Crea tabla contactos
        2) Ingresa 1 contacto
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
            print("Proximamente ...")
        if opt == 3:
            print("Proximamente ...")


if __name__ == "__main__":
    agenda_run()
