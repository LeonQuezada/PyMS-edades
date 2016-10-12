# -*- coding: utf-8 -*-
from lettuce import step, world
from edades import Edades

#@step(u'dado que ingreso la edad 0')
#def dado_que_ingreso_la_edad_0(step):
#    world.edad = Edades()

@step(u'cuando consulto mi mensaje')
def cuando_consulto_mi_mensaje(step):
    pass

@step(u'dado que ingreso la edad "([^"]*)"')
def dado_que_ingreso_la_edad_group1(step, edad1):
    edad = Edades()
    world.mensaje = edad.mensaje(int(edad1))

@step(u'entoces ve que "([^"]*)"')
def entoces_ve_que_group1(step, mensaje_esperado):
    assert world.mensaje == mensaje_esperado,'mensaje esperado '+mensaje_esperado+'y se obtubo '+world.mensaje
