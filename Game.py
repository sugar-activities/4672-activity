#!/usr/bin/python
# -*- coding: latin-1 -*-

"""
Rigoberto Sáenz Imbacuán
Desarrollador para Dispositivos Móviles - Colombia Games
Ingeniero de Sistemas y Computación - Universidad Nacional de Colombia
http://www.rigobertosaenz.com/
"""
from src.Controller import GlobalsController, FontController, ResourceController, \
    AudioController, eMusic, eScreen
from src.View import View
import pygame
import sys


class App:

    @staticmethod
    def doInit():
        
        # Inicializamos PyGame
        pygame.init()
        pygame.font.init()
        pygame.mixer.init(GlobalsController.AUDIO_FREQ, GlobalsController.AUDIO_BITSIZE, GlobalsController.AUDIO_CHANNELS, GlobalsController.AUDIO_BUFFER)
        pygame.mixer.set_num_channels(23)
        
        # Inicializamos la View
        View().doInit()
        
        # Inicializamos los modulos del Controller que lo requieran
        FontController.doInit()
        ResourceController.doInit()
        
    @staticmethod    
    def launchGame():
        
        # Reproducimos la musica de fondo
        AudioController.playMusic(eMusic.PICKING)
        
        # Mostramos el Splash de inicio
        View.showScreen(eScreen.SPLASH_START)
        
    @staticmethod
    def closeGame():
        
        # Detenemos el motor de Pygame
        pygame.mixer.quit()
        pygame.quit() 
        
        # Terminamos la ejecucion del ejecutable
        sys.exit() 

    @staticmethod
    def handleException(exception):
        pass

# Funcion Main del juego, que puede ser ejecutada como un juego Standalone o importada como una actividad Sugar
def main():
    App.doInit()
    App.launchGame()


# Para el caso en el que el juego sea ejecutado de modo Standalone, por CLI u otro metodo diferente a la plataforma Sugar
if __name__ == "__main__":
    main()
