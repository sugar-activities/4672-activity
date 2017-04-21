#!/usr/bin/python
# -*- coding: latin-1 -*-

"""
Rigoberto Sáenz Imbacuán
Desarrollador para Dispositivos Móviles - Colombia Games
Ingeniero de Sistemas y Computación - Universidad Nacional de Colombia
http://www.rigobertosaenz.com/
"""

from gettext import gettext as _
from olpcgames import activity
from sugar.activity.activity import ActivityToolbox, ActivityToolbar


# Clase que permite que Sugar pueda ejecutar el juego, haciendo que el Wrapper de pygame funcione.Esta actividad esta basada en olpcgames.PyGameActivity
class Launcher(activity.PyGameActivity):
    
    # Datos obligatorios para generar una actividad que se pueda importar desde Sugar
    game_name = 'Game'  # Nombre del modulo que tiene la funcion main()
    game_title = _('Colombia Games / OLPC Colombia / ANSPE')  # Actua como subtitulo en ciertas partes
    game_size = None
    
    # Se sobreescribe para remover algunos botones
    def build_toolbar(self):
        
        toolbar = ActivityToolbar(self)
        
        toolbar.keep.hide()
        toolbar.stop.hide()
        # toolbar.share.hide()
        # toolbar.title.hide()
        
        toolbar.show()
        self.set_toolbox(toolbar)
        
        return toolbar