#!/usr/bin/python
# -*- coding: latin-1 -*-

"""
Rigoberto Sáenz Imbacuán
Desarrollador para Dispositivos Móviles - Colombia Games
Ingeniero de Sistemas y Computación - Universidad Nacional de Colombia
http://www.rigobertosaenz.com/
"""
from src.Controller import ResourceController, GlobalsController, eScreen, \
    AudioController, FontController, eConnectionState, ConnectionController, \
    eConnectionMethod, eCharacterGender, eMotionColumn, eMotionRow, eClientId, \
    eRestaurantState, eSound, eMusic, eChefLevel, eMotionBlock, eIngredientsTab, \
    eLeafUserId, eQuestionAnswer
from src.Model import Client, Chef, FoodTimeBanner, RecipeMaker, OrderSelector, \
    Label, OrderAssigner, TutorialManager, TriviaManager
import datetime
import olpcgames
import os
import pygame
import random
import urllib


class View:
    
    __clock = None
    __displaySurface = None
    __currentScreen = None
    
    @staticmethod
    def doInit():
        
        # Cargamos el cursor standard de Sugar
        if olpcgames.ACTIVITY:  # Running as Activity
            a, b, c, d = pygame.cursors.load_xbm(ResourceController.cursor_Sugar, ResourceController.cursor_SugarMask)
            pygame.mouse.set_cursor(a, b, c, d)

        # Este reloj se usa para correr el juego a un FPS determinados
        View.__clock = pygame.time.Clock()

        # Determinamos la resolucion de pantalla
        if olpcgames.ACTIVITY:  # Running as Activity
            resolution = (0, 0)
            flags = pygame.FULLSCREEN
            
        else:
            resolution = (GlobalsController.DISPLAY_WIDTH, GlobalsController.DISPLAY_HEIGHT)
            flags = 0
        
        # Creamos la superficie principal
        View.__displaySurface = pygame.display.set_mode(resolution, flags)
            
        # Titulo de la ventana del juego (Solo Standalone)
        pygame.display.set_caption("Super Chef - Colombia Games / OLPC Colombia / ANSPE")
        
        # Color inicial de fondo
        View.__displaySurface.fill((255, 255, 255))
    
    @staticmethod
    def showScreen(screenId):
        
        # Desactivamos la pantalla actual
        if View.__currentScreen is not None:
            View.__currentScreen.deactivate()
        
        # Creamos una nueva pantalla de acuerdo a la solicitud
        if screenId == eScreen.SPLASH_START:
            __currentScreen = ScreenStartSplash(View.__clock, View.__displaySurface)
            __currentScreen.activate()
            
        elif screenId == eScreen.SPLASH_INTER:
            __currentScreen = ScreenInterSplash(View.__clock, View.__displaySurface)
            __currentScreen.activate()            

        elif screenId == eScreen.SPLASH_CLOSE:
            __currentScreen = ScreenCloseSplash(View.__clock, View.__displaySurface)
            __currentScreen.activate()

        elif screenId == eScreen.LOGIN:
            __currentScreen = ScreenLogin(View.__clock, View.__displaySurface)
            __currentScreen.activate()

        elif screenId == eScreen.REGISTRATION:
            __currentScreen = ScreenRegistration(View.__clock, View.__displaySurface)
            __currentScreen.activate()
            
        elif screenId == eScreen.SELECT_GENDER:
            __currentScreen = ScreenSelectGender(View.__clock, View.__displaySurface)
            __currentScreen.activate()
            
        elif screenId == eScreen.SELECT_TUTORIAL:
            __currentScreen = ScreenSelectTutorial(View.__clock, View.__displaySurface)
            __currentScreen.activate()
            
        elif screenId == eScreen.RESTAURANT:
            __currentScreen = ScreenRestaurant(View.__clock, View.__displaySurface)
            __currentScreen.activate()

class ScreenStartSplash:
    
    def __init__(self, clock, displaySurface):
        
        # Screen
        self.__clock = clock
        self.__displaySurface = displaySurface
        self.__isActive = False
        
        # Time
        self.__count = 1
        self.__to2SplashTime = 30
        self.__to3SplashTime = 60
        self.__to4SplashTime = 90
        self.__to5SplashTime = 120
        self.__endTime = 150
        
        # Image
        self.__image = None
        self.__imageId = 1
        self.__doUpdateImage()
        
        # Text
        self.__text = Label("Proyecto de Innovación Social", FontController.font60, (255, 255, 0), (0, 150))
        self.__text.setPosition((600 - (self.__text.getTextRenderLen() / 2), self.__text.getPosition()[1]))
        
        self.__shadow = Label("Proyecto de Innovación Social", FontController.font60, (0, 0, 0), (0, 150 + 4))
        self.__shadow.setPosition((600 + 4 - (self.__shadow.getTextRenderLen() / 2), self.__shadow.getPosition()[1]))

    def __doTask(self):
        
        # Operaciones de la Screen
        self.__count = self.__count + 1
        
        if self.__count == self.__to2SplashTime:
            self.__imageId = self.__imageId + 1
            self.__doUpdateImage()
            
        elif self.__count == self.__to3SplashTime:
            self.__imageId = self.__imageId + 1
            self.__doUpdateImage()
            
        elif self.__count == self.__to4SplashTime:
            self.__imageId = self.__imageId + 1
            self.__doUpdateImage()
            
        elif self.__count == self.__to5SplashTime:
            self.__imageId = self.__imageId + 1
            self.__doUpdateImage()
            
        elif self.__count >= self.__endTime:
            
            # ------------------------------------------------------------------------------------------
            # No persistencia
            # ------------------------------------------------------------------------------------------
            View.showScreen(eScreen.SELECT_TUTORIAL)
            return
            # ------------------------------------------------------------------------------------------
            # Para activar la persistencia del juego solo es necesario remover el codigo anterior (Ver Tambien ScreenCloseSplash)
            # ------------------------------------------------------------------------------------------
            
            
            # Determinamos si el archivo existe y contiene los datos necesarios para el login
            persistedRootUserId = None
            persistedUsername = None
            persistedPassword = None
                
            try:
                openedFile = None
                
                # Abrimos el archivo en modo Solo Lectura
                if olpcgames.ACTIVITY:  # Running as Activity
                    name = os.path.join(olpcgames.util.get_activity_root(), 'data', 'UserInfo.txt')
                    openedFile = open(name, 'r')
                else:
                    openedFile = open('UserInfo.txt', 'r')
                    
                # Recorremos el archivo linea por linea
                for lineIndex in enumerate(openedFile):
                    
                    # Primera linea: Root User Id
                    if lineIndex[0] == 0:
                        
                        # Obtenemos el contenido de la linea correspondiente
                        lineContent = lineIndex[1]
                        
                        # Extraemos el nombre de usuario de la linea leida (removemos tambien el salto de linea al final)
                        persistedRootUserId = lineContent[11:len(lineContent) - 1]
                                            
                    # Segunda linea: Username
                    if lineIndex[0] == 1:
                        
                        # Obtenemos el contenido de la linea correspondiente
                        lineContent = lineIndex[1]
                        
                        # Extraemos el nombre de usuario de la linea leida (removemos tambien el salto de linea al final)
                        persistedUsername = lineContent[9:len(lineContent) - 1]
                        
                    # Tercera linea: Password
                    if lineIndex[0] == 2:
                        
                        # Obtenemos el contenido de la linea correspondiente
                        lineContent = lineIndex[1]
                        
                        # Extraemos el password de la linea leida
                        persistedPassword = lineContent[9:len(lineContent) - 1]
                        
                        # Finalizamos el recorrido del archivo
                        break
                    
            except:
                persistedRootUserId = None
                persistedUsername = None
                persistedPassword = None
                
            finally:
                # Se cierra el archivo, sin importar lo que haya pasado
                try:
                    openedFile.close
                except:
                    pass
                
            # Verificamos que los datos persistidos hayan sido leidos correctamente
            if (persistedRootUserId == None) or (persistedRootUserId == "") or (persistedUsername == None) or (persistedUsername == "") or (persistedPassword == None) or (persistedPassword == ""):
                
                # Pantalla para la creacion del archivo
                View.showScreen(eScreen.REGISTRATION)
                
            else:
                # Guardamos los datos obtenidos del archivo
                GlobalsController.INFO_ROOT_USER_ID = persistedRootUserId
                GlobalsController.INFO_USERNAME = persistedUsername
                GlobalsController.INFO_PASSWORD = persistedPassword
                
                # Mostramos la pantalla de Login
                View.showScreen(eScreen.LOGIN)
            
        # Detectamos todos los eventos y ejecutamos las acciones correspondientes
        if pygame.event:
            for event in pygame.event.get():
                 
                # Evento cerrar el juego
                if event.type == pygame.QUIT:
                    pass
                    
                # Eventos del sistema
                elif event.type == pygame.USEREVENT:
                    pass
                    
                # Deteccion de click de mouse
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pass
                    
                # Deteccion de teclas presionadas
                elif event.type == pygame.KEYDOWN:
                    pass
                    
    def __doPaint(self):
        
        # Screen content
        self.__displaySurface.fill((255, 255, 255))
        self.__displaySurface.blit(self.__image, (0, 0))
        
        # Text
        if self.__imageId == 1:
            self.__shadow.doPaint(self.__displaySurface)
            self.__text.doPaint(self.__displaySurface)
        
        # Actualizamos la pantalla
        pygame.display.flip()
        
    def __doUpdateImage(self):
        if self.__imageId == 1:
            self.__image = ResourceController.background_Splash_1
        elif self.__imageId == 2:
            self.__image = ResourceController.background_Splash_2
        elif self.__imageId == 3:
            self.__image = ResourceController.background_Splash_3
        elif self.__imageId == 4:
            self.__image = ResourceController.background_Splash_4
        elif self.__imageId == 5:
            self.__image = ResourceController.background_Splash_5

    def activate(self):
        
        # Indicamos que esta pantalla pasa a estado Activo
        self.__isActive = True
        
        # Ocultamos el cursor
        pygame.mouse.set_visible(False)        
        
        # Ordanamos que comience el pintado de la pantalla
        self.__run()

    def deactivate(self):
        
        # Indicamos que esta pantalla pasa a estado Inactivo
        self.__isActive = False

    def __run(self):
        
        # Loop principal
        while self.__isActive is True:

            # Realizamos las operaciones propias del model
            self.__doTask()
            
            # Pintamos el resultado en pantalla
            self.__doPaint()
            
            # Running as Activity
            if olpcgames.ACTIVITY:
                pass
            else:
                # Saltamos a la siguiente iteracion
                self.__clock.tick(5)


class ScreenInterSplash:
    
    def __init__(self, clock, displaySurface):
        
        # Screen
        self.__clock = clock
        self.__displaySurface = displaySurface
        self.__isActive = False
        
        # Time
        self.__count = 1
        self.__endTime = 20
        
        # Hover
        self.__hoverCloseGame = False
        
    def __doTask(self):
        
        # Mouse Hover Detection
        (xPos, yPos) = pygame.mouse.get_pos()

        # Outside
        self.__hoverCloseGame = False
        
        # Close Game
        if (xPos >= 1200 - 87) and (xPos <= 1200) and (yPos >= 0) and (yPos <= 0 + 74): 
            self.__hoverCloseGame = True

        # Conteo para el cambio de pantalla
        self.__count = self.__count + 1
            
        if self.__count >= self.__endTime:
            View.showScreen(eScreen.RESTAURANT)
        
        # Detectamos todos los eventos y ejecutamos las acciones correspondientes
        if pygame.event:
            for event in pygame.event.get():
                 
                # Evento cerrar el juego
                if event.type == pygame.QUIT:
                    View.showScreen(eScreen.SPLASH_CLOSE)
                    
                # Eventos del sistema
                elif event.type == pygame.USEREVENT:
                    pass
                    
                # Deteccion de click de mouse
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.__doMouseAction(event)
                    
                # Deteccion de teclas presionadas
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        View.showScreen(eScreen.SPLASH_CLOSE)

    def __doPaint(self):
        
        # Screen content
        self.__displaySurface.blit(ResourceController.background_Splash_5, (0, 0))
        
        # Buttons with Hover
        if self.__hoverCloseGame == True:
            self.__displaySurface.blit(ResourceController.input_CloseGame_On, (1200 - 87, 0))
        else:
            self.__displaySurface.blit(ResourceController.input_CloseGame_Off, (1200 - 87, 0))
        
        # Actualizamos la pantalla
        pygame.display.flip()
        
    def activate(self):
        
        # Indicamos que esta pantalla pasa a estado Activo
        self.__isActive = True
        
        # Ocultamos el cursor
        pygame.mouse.set_visible(True)
        
        # Ordanamos que comience el pintado de la pantalla
        self.__run()

    def deactivate(self):
        
        # Indicamos que esta pantalla pasa a estado Inactivo
        self.__isActive = False

    def __run(self):
        
        # Loop principal
        while self.__isActive is True:

            # Realizamos las operaciones propias del model
            self.__doTask()
            
            # Pintamos el resultado en pantalla
            self.__doPaint()
            
            # Running as Activity
            if olpcgames.ACTIVITY:
                pass
            else:
                # Saltamos a la siguiente iteracion
                self.__clock.tick(5)
            
    def __doMouseAction(self, event):
        
        # Detectamos la posicion en X y Y del click
        xPos, yPos = event.pos

        # Close Game
        if (xPos >= 1200 - 87) and (xPos <= 1200) and (yPos >= 0) and (yPos <= 0 + 74):
            View.showScreen(eScreen.SPLASH_CLOSE)


class ScreenCloseSplash:
    
    def __init__(self, clock, displaySurface):
        
        # Detenemos la reproduccion de cualquier audio activo
        AudioController.stopMusic()
        AudioController.stopSounds()
        
        # Screen
        self.__clock = clock
        self.__displaySurface = displaySurface
        self.__isActive = False
        
        # Time
        self.__count = 1
        self.__endTime = 30
        
        # Control
        self.__dataProcessDefined = False
        self.__dataSentDefined = False
        
        self.__sendBatchThread = None
        self.__sendBatchInProgress = False
        
        # Text
        self.__text = Label("Impulsa el Cambio...", FontController.font60, (255, 255, 0), (0, 150))
        self.__text.setPosition((600 - (self.__text.getTextRenderLen() / 2), self.__text.getPosition()[1]))
        
        self.__shadow = Label("Impulsa el Cambio...", FontController.font60, (0, 0, 0), (0, 150 + 4))
        self.__shadow.setPosition((600 + 4 - (self.__shadow.getTextRenderLen() / 2), self.__shadow.getPosition()[1]))
        
    def __doTask(self):

        # ------------------------------------------------------------------------------------------
        # No persistencia
        # ------------------------------------------------------------------------------------------
        self.__dataSentDefined = True
        self.__dataProcessDefined = True
        # ------------------------------------------------------------------------------------------
        # Para activar la persistencia del juego solo es necesario remover el codigo anterior (Ver Tambien ScreenStartSplash)
        # ------------------------------------------------------------------------------------------
        
        
        if self.__dataProcessDefined == False:

            # Obtenemos la hora de finalizacion de la sesion de juego
            GlobalsController.INFO_FINISH_TIME = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            
            try:
                # Almacenamos la informacion de la sesion de juego recien finalizada
                openedFile = None
                
                # Creamos un archivo
                if olpcgames.ACTIVITY:  # Running as Activity
                    name = os.path.join(olpcgames.util.get_activity_root(), 'data', 'UserInfo.txt')
                    openedFile = open(name, 'a')
                else:
                    openedFile = open('UserInfo.txt', 'a')
                    
                # Escibimos el contenido apropiado
                openedFile.write('''---------------\n''')
                openedFile.write('''leafUserId:''' + str(GlobalsController.INFO_LEAF_USER_ID) + '''\n''')
                openedFile.write('''startDatetime:''' + str(GlobalsController.INFO_START_TIME) + '''\n''')
                openedFile.write('''finishDatetime:''' + str(GlobalsController.INFO_FINISH_TIME) + '''\n''')
                openedFile.write('''stars:''' + str(GlobalsController.INFO_STARS) + '''\n''')
                
            finally:
                # Se cierra el archivo, sin importar lo que haya pasado
                try:
                    openedFile.close
                except:
                    pass
            
            # Y se almaceno la informacion
            self.__dataProcessDefined = True
            
        elif self.__dataSentDefined == False:
            
            # Determinamos si hay un envio de batch en proceso
            if self.__sendBatchInProgress == False:
                
                # Armamos el JSON a enviar con los datos en batch
                fileLinesToProcess = None
                
                try:
                    openedFile = None
                    
                    # Abrimos el archivo en modo lectura
                    if olpcgames.ACTIVITY:  # Running as Activity
                        name = os.path.join(olpcgames.util.get_activity_root(), 'data', 'UserInfo.txt')
                        openedFile = open(name, 'r')
                    else:
                        openedFile = open('UserInfo.txt', 'r')
                        
                    # Escibimos el contenido apropiado
                    fileLinesToProcess = openedFile.readlines()
                    
                finally:
                    # Se cierra el archivo, sin importar lo que haya pasado
                    try:
                        openedFile.close
                    except:
                        pass
                    
                if (fileLinesToProcess == None) or (fileLinesToProcess == ""):
                    
                    # Falla en la creacion o envio del JSON
                    self.__dataSentDefined = True
                    return
                
                # Procesamos las lineas obtenidas:
                
                # Removemos los datos no relevantes en este momento: userId, username y password
                fileLinesToProcess = fileLinesToProcess[3:]
                
                # Variable para controlar la linea leida por bloque de informacion
                index = 0
                
                # Cadena con el batch de informacion a enviar
                batchDataToSend = ""
                
                for currentLine in fileLinesToProcess:
                    
                    if index == 0:  # Separador
                        
                        # La coma separadora solo se coloca despues de colocar el primer bloque
                        if batchDataToSend != "":
                            batchDataToSend = batchDataToSend + ''','''
                        index = index + 1

                    elif index == 1:  # Leaf User Id
                        batchDataToSend = batchDataToSend + '''
                            { "leafUserId": "''' + currentLine[11:len(currentLine) - 1] + '''", '''
                        index = index + 1

                    elif index == 2:  # Start Datetime
                        batchDataToSend = batchDataToSend + '''"startDatetime": "''' + currentLine[14:len(currentLine) - 1] + '''", '''
                        index = index + 1
                    
                    elif index == 3:  # Finish Datetime
                        batchDataToSend = batchDataToSend + '''"finishDatetime": "''' + currentLine[15:len(currentLine) - 1] + '''", '''
                        index = index + 1

                    elif index == 4:  # Stars
                        batchDataToSend = batchDataToSend + '''"stars": "''' + currentLine[6:len(currentLine) - 1] + '''"}'''
                        index = 0
                    
                # Iniciamos el proceso de envio de los datos en batch
                try:
                    # Parametros de conexion
                    url = 'http://www.transformando.gov.co/api/public/index/batch'
                    jsonParameters = '''
                    {
                        "gameId": "''' + str(GlobalsController.GAME_ID) + '''",
                        "rootUserId": "''' + str(GlobalsController.INFO_ROOT_USER_ID) + '''",
                        "data": [''' + batchDataToSend + '''
                        ]
                    }'''
                    
                    jsonParameters = jsonParameters.replace("\n", "")
                    jsonParameters = jsonParameters.replace("  ", "")
                    
                    
                    ''' parameters = urllib.parse.urlencode({'data': jsonParameters}) '''
                    parameters = urllib.urlencode({'data': jsonParameters})
                                        
                    # Hacemos la solicitud por POST
                    self.__sendBatchThread = ConnectionController(eConnectionMethod.POST, url, parameters)
                    self.__sendBatchThread.start()
                    
                    # Levantamos la bandera correspondiente
                    self.__sendBatchInProgress = True
                    
                except:
                    # Falla en la creacion o envio del JSON
                    self.__dataSentDefined = True

            # Envio del batch en progreso            
            elif self.__sendBatchInProgress == True:
                
                # Si hay un hilo tratando de conectarse
                if self.__sendBatchThread != None:
                    
                    if self.__sendBatchThread.getState() == eConnectionState.CONNECTING:
                        # Esperamos hasta que se defina la situacion de la conexion
                        pass
                    
                    elif self.__sendBatchThread.getState() == eConnectionState.SUCCESS:
                        
                        # Datos en Batch enviados correctamente, ahora debemos eliminar del archivo el batch de datos enviados
                        newFile = None
                        
                        # Creamos un archivo
                        if olpcgames.ACTIVITY:  # Running as Activity
                            name = os.path.join(olpcgames.util.get_activity_root(), 'data', 'UserInfo.txt')
                            newFile = open(name, 'w+')
                        else:
                            newFile = open('UserInfo.txt', 'w+')
                            
                        # Escibimos el contenido apropiado
                        newFile.write('''rootUserId:''' + str(GlobalsController.INFO_ROOT_USER_ID) + '''\n''')
                        newFile.write('''username:''' + str(GlobalsController.INFO_USERNAME) + '''\n''')
                        newFile.write('''password:''' + str(GlobalsController.INFO_PASSWORD) + '''\n''')
                        
                        # Se cierra el archivo
                        try:
                            newFile.close
                        except:
                            pass
                        
                        # Levantamos la bandera para que comience el proceso de cerrado del juego                        
                        self.__dataSentDefined = True 
                        
                    elif self.__sendBatchThread.getState() == eConnectionState.FAILURE:
                        
                        # Falla de la conexion
                        self.__dataSentDefined = True

        # Ya se definio la situacion del batch de datos, ya puede comenzar el proceso de cerrado
        else:
            # Conteo para evitar Race Conditions y permitir el almacenamiento persistente
            self.__count = self.__count + 1
                
            if self.__count >= self.__endTime:
                from Game import App
                App.closeGame()
            
        # Detectamos todos los eventos y ejecutamos las acciones correspondientes
        if pygame.event:
            for event in pygame.event.get():
                 
                # Evento cerrar el juego
                if event.type == pygame.QUIT:
                    pass
                    
                # Eventos del sistema
                elif event.type == pygame.USEREVENT:
                    pass
                    
                # Deteccion de click de mouse
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pass
                    
                # Deteccion de teclas presionadas
                elif event.type == pygame.KEYDOWN:
                    pass

    def __doPaint(self):
        
        # Screen content
        self.__displaySurface.blit(ResourceController.background_Splash_1, (0, 0))
        
        # Text
        self.__shadow.doPaint(self.__displaySurface)
        self.__text.doPaint(self.__displaySurface)
        
        # Actualizamos la pantalla
        pygame.display.flip()

    def activate(self):
        
        # Indicamos que esta pantalla pasa a estado Activo
        self.__isActive = True
        
        # Ocultamos el cursor
        pygame.mouse.set_visible(False)        
        
        # Ordanamos que comience el pintado de la pantalla
        self.__run()

    def deactivate(self):
        pass
        
    def __run(self):
        
        # Loop principal
        while self.__isActive is True:

            # Realizamos las operaciones propias del model
            self.__doTask()
            
            # Pintamos el resultado en pantalla
            self.__doPaint()
            
            # Running as Activity
            if olpcgames.ACTIVITY:
                pass
            else:
                # Saltamos a la siguiente iteracion
                self.__clock.tick(GlobalsController.GAME_FPS)
            
            
class ScreenLogin:

    def __init__(self, clock, displaySurface):
        
        # Screen
        self.__clock = clock
        self.__displaySurface = displaySurface
        self.__isActive = False
        
        # Input
        self.__loginInProgress = False
        self.__textboxUser = TextBox(385, 525, 440, 20, FontController.font30, False)
        self.__textboxPass = TextBox(385, 646, 440, 20, FontController.font30, True)
        
        # Login Control
        self.__loginStatus = Label("", FontController.font18, (255, 200, 200), (0, 796))
        self.__showLoginControls = False
        
        # User Checked
        self.__userCheck = False
        self.__userCheckTotalTime = 20
        self.__userCheckCurrentTime = 1
        
        # Hover
        self.__hoverCloseGame = False
        self.__hoverLoginButton = False
        self.__hoverLoginMainUser = False
        self.__hoverLoginParent = False
        self.__hoverLoginUncle = False
        self.__hoverLoginBrother = False
        self.__hoverLoginCousin = False
        self.__hoverLoginFriend = False
        
    def __doTask(self):
        
        # Mouse Hover Detection
        (xPos, yPos) = pygame.mouse.get_pos()
        
        # Outside
        self.__hoverCloseGame = False
        self.__hoverLoginButton = False
        self.__hoverLoginMainUser = False
        self.__hoverLoginParent = False
        self.__hoverLoginUncle = False
        self.__hoverLoginBrother = False
        self.__hoverLoginCousin = False
        self.__hoverLoginFriend = False
        
        # Close Game
        if (xPos >= 1200 - 87) and (xPos <= 1200) and (yPos >= 0) and (yPos <= 0 + 74): 
            self.__hoverCloseGame = True
        # Login Button
        elif (xPos >= 420) and (xPos <= 420 + 330) and (yPos >= 730) and (yPos <= 730 + 65) and (self.__showLoginControls == True):
            self.__hoverLoginButton = True
        # Main User
        elif (xPos >= 325) and (xPos <= 325 + 540) and (yPos >= 450) and (yPos <= 450 + 350) and (self.__showLoginControls == False):
            self.__hoverLoginMainUser = True
        # Parents
        elif (xPos >= 495) and (xPos <= 495 + 248) and (yPos >= 110) and (yPos <= 110 + 158):
            self.__hoverLoginParent = True
        # Uncle
        elif (xPos >= 750) and (xPos <= 750 + 246) and (yPos >= 190) and (yPos <= 190 + 156):
            self.__hoverLoginUncle = True
        # Brother
        elif (xPos >= 245) and (xPos <= 245 + 246) and (yPos >= 190) and (yPos <= 190 + 156):
            self.__hoverLoginBrother = True
        # Cousin
        elif (xPos >= 58) and (xPos <= 58 + 246) and (yPos >= 344) and (yPos <= 344 + 156):
            self.__hoverLoginCousin = True
        # Friend
        elif (xPos >= 922) and (xPos <= 922 + 246) and (yPos >= 345) and (yPos <= 345 + 156):
            self.__hoverLoginFriend = True
            
        # Si el usuario ya ha sido verificado
        if self.__userCheck == True:
            if self.__userCheckCurrentTime < self.__userCheckTotalTime:
                self.__userCheckCurrentTime = self.__userCheckCurrentTime + 1
            else:
                View.showScreen(eScreen.SELECT_TUTORIAL)
        
        # Detectamos todos los eventos y ejecutamos las acciones correspondientes
        if pygame.event:
            for event in pygame.event.get():
                 
                # Evento cerrar el juego
                if event.type == pygame.QUIT:
                    from Game import App
                    App.closeGame()
                    
                # Eventos del sistema
                elif event.type == pygame.USEREVENT:
                    pass
                    
                # Deteccion de click de mouse
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.__doMouseAction(event)
                    
                # Deteccion de teclas presionadas
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        from Game import App
                        App.closeGame()
                    elif event.key == pygame.K_RSHIFT:
                        self.__switchCase()
                    elif event.key == pygame.K_LSHIFT:
                        self.__switchCase()
                    else:
                        self.__doKeyAction(event)
                        
    def __doPaint(self):
        
        # Background
        self.__displaySurface.blit(ResourceController.background_Login, (0, 0))

        if self.__showLoginControls == True:
            
            # Background
            self.__displaySurface.blit(ResourceController.input_LoginInput, (163, 320))
            
            # TextBox
            self.__textboxUser.doPaint(self.__displaySurface)
            self.__textboxPass.doPaint(self.__displaySurface)
        
            # Buttons with Hover
            if self.__loginInProgress == False:
                if self.__hoverLoginButton == True:
                    self.__displaySurface.blit(ResourceController.input_Login_On, (420, 730))
                else:
                    self.__displaySurface.blit(ResourceController.input_Login_Off, (420, 730))
            else:
                self.__displaySurface.blit(ResourceController.input_Connecting, (420, 730))
        else:
            if self.__hoverLoginMainUser == True:
                self.__displaySurface.blit(ResourceController.input_LoginMainUser, (310, 345))
            
        if self.__hoverLoginParent == True:
            self.__displaySurface.blit(ResourceController.input_LoginParent, (485, 74))
            
        if self.__hoverLoginUncle == True:
            self.__displaySurface.blit(ResourceController.input_LoginUncle, (740, 150))
            
        if self.__hoverLoginBrother == True:
            self.__displaySurface.blit(ResourceController.input_LoginBrother, (230, 150))
            
        if self.__hoverLoginCousin == True:
            self.__displaySurface.blit(ResourceController.input_LoginCousin, (45, 305))
            
        if self.__hoverLoginFriend == True:
            self.__displaySurface.blit(ResourceController.input_LoginFriend, (910, 305))
            
        # Login Status
        self.__loginStatus.doPaint(self.__displaySurface)
        
        if self.__hoverCloseGame == True:
            self.__displaySurface.blit(ResourceController.input_CloseGame_On, (1200 - 87, 0))
        else:
            self.__displaySurface.blit(ResourceController.input_CloseGame_Off, (1200 - 87, 0))
        
        # Actualizamos la pantalla
        pygame.display.flip()

    def activate(self):
        
        # Indicamos que esta pantalla pasa a estado Activo
        self.__isActive = True
        
        # Mostramos el cursor
        pygame.mouse.set_visible(True)
        
        # Ordanamos que comience el pintado de la pantalla
        self.__run()

    def deactivate(self):
        
        # Indicamos que esta pantalla pasa a estado Inactivo
        self.__isActive = False

    def __run(self):
        
        # Loop principal
        while self.__isActive is True:

            # Realizamos las operaciones propias del model
            self.__doTask()
            
            # Pintamos el resultado en pantalla
            self.__doPaint()
            
            # Running as Activity
            if olpcgames.ACTIVITY:
                pass
            else:
                # Saltamos a la siguiente iteracion, respetando el FPS establecido
                self.__clock.tick(GlobalsController.GAME_FPS)
                
    def __doKeyAction(self, event):
        
        # Si no hay algun evento en progreso...
        if self.__userCheck == False:
            
            self.__textboxUser.doKeyAction(event)
            self.__textboxPass.doKeyAction(event)
        
    def __doMouseAction(self, event):
        
        if self.__userCheck == False:
        
            # Removemos el foco de todas la cajas de texto
            self.__textboxUser.quitFocus()
            self.__textboxPass.quitFocus()
            
            # Detectamos la posicion en X y Y del click
            xPos, yPos = event.pos
    
            # Close Game
            if (xPos >= 1200 - 87) and (xPos <= 1200) and (yPos >= 0) and (yPos <= 0 + 74):
                from Game import App
                App.closeGame()
            
            # Login Button
            elif (xPos >= 420) and (xPos <= 420 + 330) and (yPos >= 730) and (yPos <= 730 + 65) and (self.__showLoginControls == True):
                
                # Reiniciamos esta bandera dado que un nuevo proceso de verificacion de usuario va a comenzar
                self.__userCheck = False
        
                # Reiniciamos los mensajes de estado
                self.__loginStatus.setText("")
                
                # Obtenemos los datos ingresados
                username = self.__textboxUser.getText()
                password = self.__textboxPass.getText()
                
                # Verificamos si todos los datos fueron ingresados
                if (username == "") or (password == ""):
                    self.__loginStatus.setText("Se deben llenar todos los campos.")
                    self.__loginStatus.setPosition((585 - (self.__loginStatus.getTextRenderLen() / 2), self.__loginStatus.getPosition()[1]))
                    return
                
                # Verificamos que los datos ingresados correspondan con los persistidos
                if (GlobalsController.INFO_USERNAME == username) and (GlobalsController.INFO_PASSWORD == password):
                    self.__loginStatus.setText("Login exitoso. Ingresando al juego...")
                    self.__loginStatus.setPosition((585 - (self.__loginStatus.getTextRenderLen() / 2), self.__loginStatus.getPosition()[1]))
                    
                    # Indicamos el usuario que va a jugar
                    GlobalsController.INFO_LEAF_USER_ID = eLeafUserId.MAIN_USER
                    GlobalsController.INFO_START_TIME = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")  
                    
                    # Levantamos la bandera correspondiente
                    self.__userCheck = True
                    
                else:
                    self.__loginStatus.setText("Datos incorrectos.")
                    self.__loginStatus.setPosition((585 - (self.__loginStatus.getTextRenderLen() / 2), self.__loginStatus.getPosition()[1]))
            
            # Main User
            elif (xPos >= 325) and (xPos <= 325 + 540) and (yPos >= 450) and (yPos <= 450 + 350) and (self.__showLoginControls == False):
                self.__showLoginControls = True
                self.__textboxUser.takeFocus()
                
            # Parents
            elif (xPos >= 495) and (xPos <= 495 + 248) and (yPos >= 110) and (yPos <= 110 + 158):
                # Indicamos el usuario que va a jugar
                GlobalsController.INFO_LEAF_USER_ID = eLeafUserId.PARENTS
                GlobalsController.INFO_START_TIME = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                
                # Cambiamos a la pantalla correspondiente
                View.showScreen(eScreen.SELECT_TUTORIAL)
                
            # Uncle
            elif (xPos >= 750) and (xPos <= 750 + 246) and (yPos >= 190) and (yPos <= 190 + 156):
                # Indicamos el usuario que va a jugar
                GlobalsController.INFO_LEAF_USER_ID = eLeafUserId.UNCLE
                GlobalsController.INFO_START_TIME = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                                
                # Cambiamos a la pantalla correspondiente
                View.showScreen(eScreen.SELECT_TUTORIAL)
                
            # Brother
            elif (xPos >= 245) and (xPos <= 245 + 246) and (yPos >= 190) and (yPos <= 190 + 156):
                # Indicamos el usuario que va a jugar
                GlobalsController.INFO_LEAF_USER_ID = eLeafUserId.BROTHER
                GlobalsController.INFO_START_TIME = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                
                # Cambiamos a la pantalla correspondiente
                View.showScreen(eScreen.SELECT_TUTORIAL)
                
            # Cousin
            elif (xPos >= 58) and (xPos <= 58 + 246) and (yPos >= 344) and (yPos <= 344 + 156):
                # Indicamos el usuario que va a jugar
                GlobalsController.INFO_LEAF_USER_ID = eLeafUserId.COUSIN
                GlobalsController.INFO_START_TIME = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                
                # Cambiamos a la pantalla correspondiente
                View.showScreen(eScreen.SELECT_TUTORIAL)
                
            # Friend
            elif (xPos >= 922) and (xPos <= 922 + 246) and (yPos >= 345) and (yPos <= 345 + 156):
                # Indicamos el usuario que va a jugar
                GlobalsController.INFO_LEAF_USER_ID = eLeafUserId.FRIEND
                GlobalsController.INFO_START_TIME = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                
                # Cambiamos a la pantalla correspondiente
                View.showScreen(eScreen.SELECT_TUTORIAL)
                    
            # Textbox
            else:
                self.__textboxUser.doMouseAction(event)
                self.__textboxPass.doMouseAction(event)
        
    def __switchCase(self):
        if self.__userCheck == False:
            self.__textboxUser.switchCase()
            self.__textboxPass.switchCase()
        

class ScreenRegistration:

    def __init__(self, clock, displaySurface):
        
        # Screen
        self.__clock = clock
        self.__displaySurface = displaySurface
        self.__isActive = False
        
        # Registration Input
        self.__textboxNames = TextBox(110, 148, 440, 20, FontController.font30, False)
        self.__textboxAge = TextBox(110, 263, 150, 2, FontController.font30, False)
        self.__textboxSchool = TextBox(110, 375, 440, 20, FontController.font30, False)
        self.__textboxGrade = TextBox(110, 487, 440, 20, FontController.font30, False)
        
        self.__textboxUsername = TextBox(620, 148, 440, 20, FontController.font30, False)
        self.__textboxPassword1 = TextBox(620, 263, 440, 20, FontController.font30, True)
        self.__textboxPassword2 = TextBox(620, 375, 440, 20, FontController.font30, True)
        self.__textboxNames.takeFocus()
        
        # Registration Control
        self.__registrationThread = None
        self.__registrationInProgress = False
        self.__registrationStatus = Label("", FontController.font18, (255, 200, 200), (0, 445))
        
        # Login Input
        self.__textboxLoginUsername = TextBox(110, 682, 440, 20, FontController.font30, False)
        self.__textboxLoginPassword = TextBox(620, 682, 440, 20, FontController.font30, True)
        
        # Login Control
        self.__loginThread = None
        self.__loginInProgress = False
        self.__loginStatus = Label("", FontController.font18, (255, 200, 200), (770, 770))
        
        # User Checked
        self.__userCheck = False
        self.__userCheckTotalTime = 20
        self.__userCheckCurrentTime = 1
        
        # Hover
        self.__hoverCloseGame = False
        self.__hoverRegistration = False
        self.__hoverLoginButton = False
        
    def __doTask(self):
        
        # Mouse Hover Detection
        (xPos, yPos) = pygame.mouse.get_pos()
        
        # Outside
        self.__hoverCloseGame = False
        self.__hoverRegistration = False
        self.__hoverLoginButton = False
        
        # Close Game
        if (xPos >= 1200 - 87) and (xPos <= 1200) and (yPos >= 0) and (yPos <= 0 + 74): 
            self.__hoverCloseGame = True
        # Registration Button
        elif (xPos >= 670) and (xPos <= 670 + 330) and (yPos >= 475) and (yPos <= 475 + 65):
            self.__hoverRegistration = True
        # Login Button
        elif (xPos >= 435) and (xPos <= 435 + 330) and (yPos >= 750) and (yPos <= 750 + 65):
            self.__hoverLoginButton = True

        # Si el usuario ya ha sido verificado
        if self.__userCheck == True:
            if self.__userCheckCurrentTime < self.__userCheckTotalTime:
                self.__userCheckCurrentTime = self.__userCheckCurrentTime + 1
            else:
                View.showScreen(eScreen.SELECT_TUTORIAL)

        # Determinamos si hay un registro en proceso
        elif self.__registrationInProgress == True:
            
            # Si hay un hilo tratando de conectarse
            if self.__registrationThread != None:
                
                if self.__registrationThread.getState() == eConnectionState.CONNECTING:
                    
                    if self.__registrationStatus.text == "Conectando":
                        self.__registrationStatus.setText("Conectando.")
                    elif self.__registrationStatus.text == "Conectando.":
                        self.__registrationStatus.setText("Conectando..")
                    elif self.__registrationStatus.text == "Conectando..":
                        self.__registrationStatus.setText("Conectando...")
                    elif self.__registrationStatus.text == "Conectando...":
                        self.__registrationStatus.setText("Conectando")
                
                elif self.__registrationThread.getState() == eConnectionState.SUCCESS:
                    
                    # Obtenemos la respuesta dada por el servidor
                    result = self.__registrationThread.getResult()
                    
                    # Si el registro fue exitoso
                    if result[11:15] == 'true':
                        
                        # Leemos el id retornado
                        newUserId = result[23:43]
                        
                        # Si el nombre de usuario elegido ya existe
                        if newUserId == "":
                            self.__registrationStatus.setText("El Nombre de Usuario ya existe.")
                            self.__registrationStatus.setPosition((835 - (self.__registrationStatus.getTextRenderLen() / 2), self.__registrationStatus.getPosition()[1]))
                            
                            # Se alista todo para una nueva conexion
                            self.__registrationInProgress = False
                            self.__registrationThread = None
                            
                        else:
                            try:
                                newFile = None
                                
                                # Creamos un archivo
                                if olpcgames.ACTIVITY:  # Running as Activity
                                    name = os.path.join(olpcgames.util.get_activity_root(), 'data', 'UserInfo.txt')
                                    newFile = open(name, 'w+')
                                else:
                                    newFile = open('UserInfo.txt', 'w+')
                                    
                                # Volvemos a obtener los datos a persistir
                                username = self.__textboxUsername.getText()
                                password = self.__textboxPassword1.getText()
                            
                                # Escibimos el contenido apropiado
                                newFile.write('''rootUserId:''' + newUserId + '''\n''')
                                newFile.write('''username:''' + username + '''\n''')
                                newFile.write('''password:''' + password + '''\n''')
                                
                                # Se cierra el archivo
                                try:
                                    newFile.close
                                except:
                                    pass
                                
                                # El registro fue exitoso, levantamos la bandera correspondiente
                                self.__userCheck = True
                                
                                # Almacenamos la informacion en el juego
                                GlobalsController.INFO_ROOT_USER_ID = newUserId
                                GlobalsController.INFO_LEAF_USER_ID = eLeafUserId.MAIN_USER
                                GlobalsController.INFO_USERNAME = username
                                GlobalsController.INFO_PASSWORD = password
                                GlobalsController.INFO_START_TIME = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                                
                                # Informamos al usuario
                                self.__registrationStatus.setText("Registro exitoso. Ingresando al juego...")
                                self.__registrationStatus.setPosition((835 - (self.__registrationStatus.getTextRenderLen() / 2), self.__registrationStatus.getPosition()[1]))
                                
                                # Ya no se necesita la conexion abierta
                                self.__registrationInProgress = False
                                self.__registrationThread = None
                                
                            except:
                                # Fue lanzada una excepcion relacionada con la apertura del archivo
                                self.__registrationStatus.setText("Error en el Registro.")
                                self.__registrationStatus.setPosition((835 - (self.__registrationStatus.getTextRenderLen() / 2), self.__registrationStatus.getPosition()[1]))
                                
                                # Se alista todo para una nueva conexion
                                self.__registrationInProgress = False
                                self.__registrationThread = None
                                
                                # Se cierra el archivo, sin importar lo que haya pasado
                                try:
                                    newFile.close
                                except:
                                    pass
                                
                    else:
                        # Error en la respuesta del servidor
                        self.__registrationStatus.setText("Error en el Registro.")
                        self.__registrationStatus.setPosition((835 - (self.__registrationStatus.getTextRenderLen() / 2), self.__registrationStatus.getPosition()[1]))
                        
                        # Se alista todo para una nueva conexion
                        self.__registrationInProgress = False
                        self.__registrationThread = None
                        
                elif self.__registrationThread.getState() == eConnectionState.FAILURE:
                    
                    # Falla de la conexion
                    self.__registrationStatus.setText("Error de Conexión.")
                    self.__registrationStatus.setPosition((835 - (self.__registrationStatus.getTextRenderLen() / 2), self.__registrationStatus.getPosition()[1]))
                    
                    # Se alista todo para una nueva conexion
                    self.__registrationInProgress = False
                    self.__registrationThread = None
                    
        # Determinamos si hay un login en proceso
        elif self.__loginInProgress == True:
            
            # Si hay un hilo tratando de conectarse
            if self.__loginThread != None:
                
                if self.__loginThread.getState() == eConnectionState.CONNECTING:
                    
                    if self.__loginStatus.text == "Conectando":
                        self.__loginStatus.setText("Conectando.")
                    elif self.__loginStatus.text == "Conectando.":
                        self.__loginStatus.setText("Conectando..")
                    elif self.__loginStatus.text == "Conectando..":
                        self.__loginStatus.setText("Conectando...")
                    elif self.__loginStatus.text == "Conectando...":
                        self.__loginStatus.setText("Conectando")
                
                elif self.__loginThread.getState() == eConnectionState.SUCCESS:
               
                    # Obtenemos la respuesta dada por el servidor
                    result = self.__loginThread.getResult()
                    
                    # Si el login fue exitoso
                    if result[11:15] == 'true':
                        
                        # Leemos el id retornado
                        newUserId = result[23:len(result) - 2]
                        
                        # Si el nombre de usuario elegido no existe
                        if newUserId == "":
                            self.__loginStatus.setText("El Nombre de Usuario no existe.")
                            
                            # Se alista todo para una nueva conexion
                            self.__loginInProgress = False
                            self.__loginThread = None
                            
                        else:
                            try:
                                newFile = None
                                
                                # Creamos un archivo
                                if olpcgames.ACTIVITY:  # Running as Activity
                                    name = os.path.join(olpcgames.util.get_activity_root(), 'data', 'UserInfo.txt')
                                    newFile = open(name, 'w+')
                                else:
                                    newFile = open('UserInfo.txt', 'w+')
        
                                # Volvemos a obtener los datos a persistir
                                username = self.__textboxLoginUsername.getText()
                                password = self.__textboxLoginPassword.getText()
                            
                                # Escibimos el contenido apropiado
                                newFile.write('''rootUserId:''' + newUserId + '''\n''')
                                newFile.write('''username:''' + username + '''\n''')
                                newFile.write('''password:''' + password + '''\n''')
                                
                                # Se cierra el archivo
                                try:
                                    newFile.close
                                except:
                                    pass
                                
                                # El registro fue exitoso, levantamos la bandera correspondiente
                                self.__userCheck = True
                                
                                # Almacenamos la informacion en el juego
                                GlobalsController.INFO_ROOT_USER_ID = newUserId
                                GlobalsController.INFO_LEAF_USER_ID = eLeafUserId.MAIN_USER
                                GlobalsController.INFO_USERNAME = username
                                GlobalsController.INFO_PASSWORD = password
                                GlobalsController.INFO_START_TIME = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                                
                                # Informamos al usuario
                                self.__loginStatus.setText("Login exitoso. Ingresando al juego...")
                                
                                # Ya no se necesita la conexion abierta
                                self.__loginInProgress = False
                                self.__loginThread = None
                                
                            except:
                                # Fue lanzada una excepcion relacionada con la apertura del archivo
                                self.__loginStatus.setText("Error en el Login.")
                                
                                # Se alista todo para una nueva conexion
                                self.__loginInProgress = False
                                self.__loginThread = None
                                
                                # Se cierra el archivo, sin importar lo que haya pasado
                                try:
                                    newFile.close
                                except:
                                    pass
                                
                    else:
                        # Error en la respuesta del servidor
                        self.__loginStatus.setText("Error en el Login.")
                        
                        # Se alista todo para una nueva conexion
                        self.__loginInProgress = False
                        self.__loginThread = None
                      
                elif self.__loginThread.getState() == eConnectionState.FAILURE:
                    
                    self.__loginStatus.setText("Error de Conexión.")
                    
                    # Se alista todo para una nueva conexion
                    self.__loginInProgress = False
                    self.__loginThread = None
                
        # Detectamos todos los eventos y ejecutamos las acciones correspondientes
        if pygame.event:
            for event in pygame.event.get():
                 
                # Evento cerrar el juego
                if event.type == pygame.QUIT:
                    from Game import App
                    App.closeGame()
                    
                # Eventos del sistema
                elif event.type == pygame.USEREVENT:
                    pass
                    
                # Deteccion de click de mouse
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.__doMouseAction(event)
                    
                # Deteccion de teclas presionadas
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        from Game import App
                        App.closeGame()
                    elif event.key == pygame.K_RSHIFT:
                        self.__switchCase()
                    elif event.key == pygame.K_LSHIFT:
                        self.__switchCase()
                    else:
                        self.__doKeyAction(event)
                        
    def __doPaint(self):
        
        # Background
        self.__displaySurface.blit(ResourceController.background_Registration, (0, 0))

        # TextBox
        self.__textboxNames.doPaint(self.__displaySurface)
        self.__textboxAge.doPaint(self.__displaySurface)
        self.__textboxSchool.doPaint(self.__displaySurface)
        self.__textboxGrade.doPaint(self.__displaySurface)
        self.__textboxUsername.doPaint(self.__displaySurface)
        self.__textboxPassword1.doPaint(self.__displaySurface)
        self.__textboxPassword2.doPaint(self.__displaySurface)
        self.__textboxLoginUsername.doPaint(self.__displaySurface)
        self.__textboxLoginPassword.doPaint(self.__displaySurface)

        # Buttons with Hover
        if self.__registrationInProgress == False:
            if self.__hoverRegistration == True:
                self.__displaySurface.blit(ResourceController.input_Registration_On, (670, 475))
            else:
                self.__displaySurface.blit(ResourceController.input_Registration_Off, (670, 475))
        else:
            self.__displaySurface.blit(ResourceController.input_Connecting, (670, 475))
            
        if self.__loginInProgress == False:
            if self.__hoverLoginButton == True:
                self.__displaySurface.blit(ResourceController.input_Login_On, (435, 750))
            else:
                self.__displaySurface.blit(ResourceController.input_Login_Off, (435, 750))
        else:
            self.__displaySurface.blit(ResourceController.input_Connecting, (435, 750))

        # Connecton Status
        self.__registrationStatus.doPaint(self.__displaySurface)
        self.__loginStatus.doPaint(self.__displaySurface)
        
        if self.__hoverCloseGame == True:
            self.__displaySurface.blit(ResourceController.input_CloseGame_On, (1200 - 87, 0))
        else:
            self.__displaySurface.blit(ResourceController.input_CloseGame_Off, (1200 - 87, 0))
        
        # Actualizamos la pantalla
        pygame.display.flip()

    def activate(self):
        
        # Indicamos que esta pantalla pasa a estado Activo
        self.__isActive = True
        
        # Mostramos el cursor
        pygame.mouse.set_visible(True)
        
        # Ordanamos que comience el pintado de la pantalla
        self.__run()

    def deactivate(self):
        
        # Indicamos que esta pantalla pasa a estado Inactivo
        self.__isActive = False
        
    def __run(self):
        
        # Loop principal
        while self.__isActive is True:

            # Realizamos las operaciones propias del model
            self.__doTask()
            
            # Pintamos el resultado en pantalla
            self.__doPaint()
            
            # Running as Activity
            if olpcgames.ACTIVITY:
                pass
            else:
                # Saltamos a la siguiente iteracion, respetando el FPS establecido
                self.__clock.tick(GlobalsController.GAME_FPS)
                
    def __doKeyAction(self, event):
        
        # Si no hay algun evento en progreso...
        if (self.__registrationInProgress == False) and (self.__loginInProgress == False) and (self.__userCheck == False):
            
            self.__textboxNames.doKeyAction(event)
            self.__textboxAge.doKeyAction(event)
            self.__textboxSchool.doKeyAction(event)
            self.__textboxGrade.doKeyAction(event)
            self.__textboxUsername.doKeyAction(event)
            self.__textboxPassword1.doKeyAction(event)
            self.__textboxPassword2.doKeyAction(event)
            self.__textboxLoginUsername.doKeyAction(event)
            self.__textboxLoginPassword.doKeyAction(event)
        
    def __doMouseAction(self, event):
        
        if self.__userCheck == False:
        
            # Removemos el foco de todas la cajas de texto
            self.__textboxNames.quitFocus()
            self.__textboxAge.quitFocus()
            self.__textboxSchool.quitFocus()
            self.__textboxGrade.quitFocus()
            self.__textboxUsername.quitFocus()
            self.__textboxPassword1.quitFocus()
            self.__textboxPassword2.quitFocus()
            self.__textboxLoginUsername.quitFocus()
            self.__textboxLoginPassword.quitFocus()
            
            # Detectamos la posicion en X y Y del click
            xPos, yPos = event.pos
    
            # Close Game
            if (xPos >= 1200 - 87) and (xPos <= 1200) and (yPos >= 0) and (yPos <= 0 + 74):
                from Game import App
                App.closeGame()
            
            # Registration Button
            elif (xPos >= 670) and (xPos <= 670 + 330) and (yPos >= 475) and (yPos <= 475 + 65):
                
                if self.__registrationInProgress == False:
                
                    # Desabilitamos el registro
                    self.__registrationInProgress = True
                    
                    # Reiniciamos esta bandera dado que un nuevo proceso de verificacion de usuario va a comenzar
                    self.__userCheck = False
                    
                    # Reiniciamos los mensajes e estado
                    self.__loginStatus.setText("")
                    self.__registrationStatus.setText("")
                    
                    # Verificamos los datos a enviar
                    names = self.__textboxNames.getText()
                    age = self.__textboxAge.getText()
                    school = self.__textboxSchool.getText()
                    grade = self.__textboxGrade.getText()
                    username = self.__textboxUsername.getText()
                    password1 = self.__textboxPassword1.getText()
                    password2 = self.__textboxPassword2.getText()
                    
                    # Verificamos si todos los datos fueron ingresados
                    if (names == "") or (age == "") or (school == "") or (grade == "") or (username == "") or (password1 == "") or (password2 == ""):
    
                        self.__registrationStatus.setText("Se deben llenar todos los campos.")
                        self.__registrationStatus.setPosition((835 - (self.__registrationStatus.getTextRenderLen() / 2), self.__registrationStatus.getPosition()[1]))
                        
                        # Se alista todo para una nueva conexion
                        self.__registrationInProgress = False
                        self.__registrationThread = None
                        return
                                    
                    # Verificamos si las contraseñas coinciden
                    if password1 != password2:
                        
                        self.__registrationStatus.setText("Las contraseñas no coinciden.")
                        self.__registrationStatus.setPosition((835 - (self.__registrationStatus.getTextRenderLen() / 2), self.__registrationStatus.getPosition()[1]))
                        
                        # Se alista todo para una nueva conexion
                        self.__registrationInProgress = False
                        self.__registrationThread = None
                        return
                    
                    try:
                        self.__registrationStatus.setText("Conectando...")
                        self.__registrationStatus.setPosition((835 - (self.__registrationStatus.getTextRenderLen() / 2), self.__registrationStatus.getPosition()[1]))
                    
                        # Parametros de conexion
                        url = 'http://www.transformando.gov.co/api/public/index/register'
                        jsonParameters = '''
                        {
                            "gameId": "''' + str(GlobalsController.GAME_ID) + '''",
                            "newUser": {
                                "name": "''' + names + '''",
                                "nickname": "''' + username + '''",
                                "password": "''' + password1 + '''",
                                "age": "''' + age + '''",
                                "school": "''' + school + '''",
                                "degree": "''' + grade + '''"
                            }
                        }'''                      
                          
                        ''' parameters = urllib.parse.urlencode({'data': jsonParameters}) '''
                        parameters = urllib.urlencode({'data': jsonParameters})
                                            
                        # Hacemos la solicitud por POST
                        self.__registrationThread = ConnectionController(eConnectionMethod.POST, url, parameters)
                        self.__registrationThread.start()
                        
                    except:
                        self.__registrationStatus.setText("Error de Conexión.")
                        self.__registrationStatus.setPosition((835 - (self.__registrationStatus.getTextRenderLen() / 2), self.__registrationStatus.getPosition()[1]))
                        
                        # Se alista todo para una nueva conexion
                        self.__registrationInProgress = False
                        self.__registrationThread = None
            
            # Login Button
            elif (xPos >= 435) and (xPos <= 435 + 330) and (yPos >= 750) and (yPos <= 750 + 65):
        
                if self.__loginInProgress == False:
                
                    # Desabilitamos el registro
                    self.__loginInProgress = True
                    
                    # Reiniciamos esta bandera dado que un nuevo proceso de verificacion de usuario va a comenzar
                    self.__userCheck = False
                    
                    # Reiniciamos los mensajes e estado
                    self.__loginStatus.setText("")
                    self.__registrationStatus.setText("")
                    
                    # Verificamos los datos a enviar
                    username = self.__textboxLoginUsername.getText()
                    password = self.__textboxLoginPassword.getText()
                    
                    # Verificamos si todos los datos fueron ingresados
                    if (username == "") or (password == ""):
    
                        self.__loginStatus.setText("Se deben llenar todos los campos.")
                        
                        # Se alista todo para una nueva conexion
                        self.__loginInProgress = False
                        self.__loginThread = None
                        return
                                    
                    try:
                        self.__loginStatus.setText("Conectando...")
                    
                        # Parametros de conexion
                        url = 'http://www.transformando.gov.co/api/public/index/checkuser'
                        
                        ''' parameters = urllib.parse.urlencode({'user': username, 'pass': password}) '''
                        parameters = urllib.urlencode({'user': username, 'pass': password})
                        
                        # Hacemos la solicitud por POST
                        self.__loginThread = ConnectionController(eConnectionMethod.POST, url, parameters)
                        self.__loginThread.start()
                        
                    except:
                        self.__loginStatus.setText("Error de Conexión.")
                        
                        # Se alista todo para una nueva conexion
                        self.__loginInProgress = False
                        self.__loginThread = None
            
            # Textbox
            else:
                self.__textboxNames.doMouseAction(event)
                self.__textboxAge.doMouseAction(event)
                self.__textboxSchool.doMouseAction(event)
                self.__textboxGrade.doMouseAction(event)
                self.__textboxUsername.doMouseAction(event)
                self.__textboxPassword1.doMouseAction(event)
                self.__textboxPassword2.doMouseAction(event)
                self.__textboxLoginUsername.doMouseAction(event)
                self.__textboxLoginPassword.doMouseAction(event)
        
    def __switchCase(self):
        if self.__userCheck == False:
            self.__textboxNames.switchCase()
            self.__textboxAge.switchCase()
            self.__textboxSchool.switchCase()
            self.__textboxGrade.switchCase()
            self.__textboxUsername.switchCase()
            self.__textboxPassword1.switchCase()
            self.__textboxPassword2.switchCase()
            self.__textboxLoginUsername.switchCase()
            self.__textboxLoginPassword.switchCase()
        

class ScreenSelectGender:

    def __init__(self, clock, displaySurface):
        
        # Screen
        self.__clock = clock
        self.__displaySurface = displaySurface
        self.__isActive = False
        
        # Hover
        self.__hoverCloseGame = False
        self.__hoverMale = False
        self.__hoverFemale = False

    def __doTask(self):
        
        # Mouse Hover Detection
        (xPos, yPos) = pygame.mouse.get_pos()
        
        # Outside
        self.__hoverCloseGame = False
        self.__hoverMale = False
        self.__hoverFemale = False
        
        # Close Game
        if (xPos >= 1200 - 87) and (xPos <= 1200) and (yPos >= 0) and (yPos <= 0 + 74): 
            self.__hoverCloseGame = True
        # Gender Male
        elif (xPos >= 150) and (xPos <= 500) and (yPos >= 150) and (yPos <= 900):
            self.__hoverMale = True
        # Gender Female
        elif (xPos >= 700) and (xPos <= 1050) and (yPos >= 150) and (yPos <= 900):
            self.__hoverFemale = True
        
        # Detectamos todos los eventos y ejecutamos las acciones correspondientes
        if pygame.event:
            for event in pygame.event.get():
                 
                # Evento cerrar el juego
                if event.type == pygame.QUIT:
                    View.showScreen(eScreen.SPLASH_CLOSE)
                    
                # Eventos del sistema
                elif event.type == pygame.USEREVENT:
                    pass
                    
                # Deteccion de click de mouse
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.__doMouseAction(event)
                    
                # Deteccion de teclas presionadas
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        View.showScreen(eScreen.SPLASH_CLOSE)

    def __doPaint(self):
        
        # Background
        self.__displaySurface.blit(ResourceController.background_SelectGender, (0, 0))
        
        # Buttons with Hover
        if self.__hoverMale == True:
            self.__displaySurface.blit(ResourceController.input_GenderMale_On, (120, 80))
        else:
            self.__displaySurface.blit(ResourceController.input_GenderMale_Off, (120, 80))
        
        if self.__hoverFemale == True:
            self.__displaySurface.blit(ResourceController.input_GenderFemale_On, (680, 110))
        else:
            self.__displaySurface.blit(ResourceController.input_GenderFemale_Off, (680, 110))
            
        if self.__hoverCloseGame == True:
            self.__displaySurface.blit(ResourceController.input_CloseGame_On, (1200 - 87, 0))
        else:
            self.__displaySurface.blit(ResourceController.input_CloseGame_Off, (1200 - 87, 0))
        
        # Actualizamos la pantalla
        pygame.display.flip()

    def activate(self):
        
        # Indicamos que esta pantalla pasa a estado Activo    
        self.__isActive = True
        
        # Mostramos el cursor
        pygame.mouse.set_visible(True)
        
        # Ordanamos que comience el pintado de la pantalla
        self.__run()

    def deactivate(self):
        
        # Indicamos que esta pantalla pasa a estado Inactivo
        self.__isActive = False

    def __run(self):
        
        # Loop principal
        while self.__isActive is True:

            # Realizamos las operaciones propias del model
            self.__doTask()
            
            # Pintamos el resultado en pantalla
            self.__doPaint()
            
            # Running as Activity
            if olpcgames.ACTIVITY:
                pass
            else:
                # Saltamos a la siguiente iteracion, respetando el FPS establecido
                self.__clock.tick(GlobalsController.GAME_FPS)

    def __doMouseAction(self, event):
        
        # Detectamos la posicion en X y Y del click
        xPos, yPos = event.pos

        # Close Game
        if (xPos >= 1200 - 87) and (xPos <= 1200) and (yPos >= 0) and (yPos <= 0 + 74):
            View.showScreen(eScreen.SPLASH_CLOSE)
        
        # Login Button
        elif (xPos >= 150) and (xPos <= 500) and (yPos >= 150) and (yPos <= 900):
            GlobalsController.CHEF_GENDER = eCharacterGender.MALE
            View.showScreen(eScreen.SPLASH_INTER)
            
        elif (xPos >= 700) and (xPos <= 1050) and (yPos >= 150) and (yPos <= 900):
            GlobalsController.CHEF_GENDER = eCharacterGender.FEMALE
            View.showScreen(eScreen.SPLASH_INTER)        
        

class ScreenSelectTutorial:

    def __init__(self, clock, displaySurface):
        
        # Screen
        self.__clock = clock
        self.__displaySurface = displaySurface
        self.__isActive = False
        
        # Hover
        self.__hoverCloseGame = False
        self.__hoverTutorialYes = False
        self.__hoverTutorialNo = False
        
        
    def __doTask(self):
        
        # Mouse Hover Detection
        (xPos, yPos) = pygame.mouse.get_pos()
        
        # Outside
        self.__hoverCloseGame = False
        self.__hoverTutorialYes = False
        self.__hoverTutorialNo = False
        
        # Close Game
        if (xPos >= 1200 - 87) and (xPos <= 1200) and (yPos >= 0) and (yPos <= 0 + 74): 
            self.__hoverCloseGame = True
        # Tutorial Yes
        elif (xPos >= 600 - 225) and (xPos <= 600 - 225 + 450) and (yPos >= 550) and (yPos <= 550 + 75):
            self.__hoverTutorialYes = True
        # Tutorial No
        elif (xPos >= 600 - 150) and (xPos <= 600 - 150 + 300) and (yPos >= 650) and (yPos <= 650 + 80):
            self.__hoverTutorialNo = True
        
        # Detectamos todos los eventos y ejecutamos las acciones correspondientes
        if pygame.event:
            for event in pygame.event.get():
                 
                # Evento cerrar el juego
                if event.type == pygame.QUIT:
                    View.showScreen(eScreen.SPLASH_CLOSE)
                    
                # Eventos del sistema
                elif event.type == pygame.USEREVENT:
                    pass
                    
                # Deteccion de click de mouse
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.__doMouseAction(event)
                    
                # Deteccion de teclas presionadas
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        View.showScreen(eScreen.SPLASH_CLOSE)

    def __doPaint(self):
        
        # Background
        self.__displaySurface.blit(ResourceController.background_Kitchen, (0, 0))
        self.__displaySurface.blit(ResourceController.background_Transparent, (0, 0))
        self.__displaySurface.blit(ResourceController.game_TutorialWelcome, (600 - 400, 50))
        
        # Buttons with Hover
        if self.__hoverTutorialYes == True:
            self.__displaySurface.blit(ResourceController.input_TutorialYes_On, (600 - 225, 550))
        else:
            self.__displaySurface.blit(ResourceController.input_TutorialYes_Off, (600 - 225, 550))
        
        if self.__hoverTutorialNo == True:
            self.__displaySurface.blit(ResourceController.input_TutorialNo_On, (600 - 150, 650))
        else:
            self.__displaySurface.blit(ResourceController.input_TutorialNo_Off, (600 - 150, 650))
            
        if self.__hoverCloseGame == True:
            self.__displaySurface.blit(ResourceController.input_CloseGame_On, (1200 - 87, 0))
        else:
            self.__displaySurface.blit(ResourceController.input_CloseGame_Off, (1200 - 87, 0))
        
        # Actualizamos la pantalla
        pygame.display.flip()

    def activate(self):
        
        # Indicamos que esta pantalla pasa a estado Activo    
        self.__isActive = True
        
        # Mostramos el cursor
        pygame.mouse.set_visible(True)
        
        # Ordanamos que comience el pintado de la pantalla
        self.__run()

    def deactivate(self):
        
        # Indicamos que esta pantalla pasa a estado Inactivo
        self.__isActive = False
        
    def __run(self):
        
        # Loop principal
        while self.__isActive is True:

            # Realizamos las operaciones propias del model
            self.__doTask()
            
            # Pintamos el resultado en pantalla
            self.__doPaint()
            
            # Running as Activity
            if olpcgames.ACTIVITY:
                pass
            else:
                # Saltamos a la siguiente iteracion, respetando el FPS establecido
                self.__clock.tick(GlobalsController.GAME_FPS)
        
    def __doMouseAction(self, event):
        
        # Detectamos la posicion en X y Y del click
        xPos, yPos = event.pos

        # Close Game
        if (xPos >= 1200 - 87) and (xPos <= 1200) and (yPos >= 0) and (yPos <= 0 + 74):
            View.showScreen(eScreen.SPLASH_CLOSE)

        # Button Tutorial Yes
        elif (xPos >= 600 - 225) and (xPos <= 600 - 225 + 450) and (yPos >= 550) and (yPos <= 550 + 75):
            GlobalsController.SHOW_TUTORIAL = True
            View.showScreen(eScreen.SELECT_GENDER)
            
        # Button Tutorial No
        elif (xPos >= 600 - 150) and (xPos <= 600 - 150 + 300) and (yPos >= 650) and (yPos <= 650 + 80):
            GlobalsController.SHOW_TUTORIAL = False
            View.showScreen(eScreen.SELECT_GENDER)
            

class ScreenRestaurant:

    def __init__(self, clock, displaySurface):
        
        # Clientes
        self.__clients = list()
        self.__clients.append(Client(eClientId.CLIENT_A_ROW2, eMotionColumn.COLUMN_1, eMotionRow.ROW_2))
        self.__clients.append(Client(eClientId.CLIENT_B_ROW2, eMotionColumn.COLUMN_3, eMotionRow.ROW_2))
        self.__clients.append(Client(eClientId.CLIENT_C_ROW2, eMotionColumn.COLUMN_5, eMotionRow.ROW_2))
        self.__clients.append(Client(eClientId.CLIENT_D_ROW2, eMotionColumn.COLUMN_7, eMotionRow.ROW_2))
        self.__clients.append(Client(eClientId.CLIENT_E_ROW3, eMotionColumn.COLUMN_1, eMotionRow.ROW_3))
        self.__clients.append(Client(eClientId.CLIENT_F_ROW3, eMotionColumn.COLUMN_3, eMotionRow.ROW_3))
        self.__clients.append(Client(eClientId.CLIENT_G_ROW3, eMotionColumn.COLUMN_5, eMotionRow.ROW_3))
        self.__clients.append(Client(eClientId.CLIENT_H_ROW3, eMotionColumn.COLUMN_7, eMotionRow.ROW_3))
        
        # General
        self.__chef = Chef()
        self.__foodTimeBanner = FoodTimeBanner()
        
        # State
        self.__state = eRestaurantState.RESTAURANT
        
        # Managers and Selectors
        self.__tutorialManager = TutorialManager()
        self.__triviaManager = TriviaManager()
        self.__orderAssigner = OrderAssigner()
        self.__orderSelector = OrderSelector()
        self.__recipeMaker = RecipeMaker()
        
        # Trivia Control
        self.__showTrivia = False
        self.__triviaNextLimit = 30
        
        # Screen
        self.__clock = clock
        self.__displaySurface = displaySurface
        self.__isActive = False
        
        # Bandera para activar el primer cliente de manera inmediata
        self.__firstClient = True
        
        # Show New Chef Level
        self.__showNewLevel = False
        self.__showNewLevelTotalTime = 25
        self.__showNewLevelCurrentTime = 1
        
        # Labels
        self.__textStars = Label("" , FontController.font22, (255, 255, 255), (106, -3))
        self.__textGotStars1 = Label("Haz conseguido" , FontController.font40, (255, 255, 255), (600 - 165, 220))
        self.__textGotStars2 = Label("" , FontController.font100, (255, 255, 0), (300, 260))
        self.__textGotStars3 = Label("Haz alcanzado el nivel" , FontController.font40, (255, 255, 255), (600 - (475 / 2), 470))
        
        # Hover
        self.__hoverCloseGame = False
        self.__hoverCancel = False
            
        self.__hoverTriviaManager = list()
        index = 0
        while index < 3:
            self.__hoverTriviaManager.append(False)
            index = index + 1
            
        self.__hoverOrderAssignment = list()
        index = 0
        while index < 40:
            self.__hoverOrderAssignment.append(False)
            index = index + 1
        
        self.__hoverOrderSelection = list()
        index = 0
        while index < 8:
            self.__hoverOrderSelection.append(False)
            index = index + 1

        self.__hoverRecipeMaker = list()
        index = 0
        while index < 8:
            self.__hoverRecipeMaker.append(False)
            index = index + 1

    def __doTask(self):
        
        # Mouse Hover Detection
        (xPos, yPos) = pygame.mouse.get_pos()
        
        # Reiniciamos el Hover
        self.__resetHover()
        
        # Close Game
        if (xPos >= 1200 - 87) and (xPos <= 1200) and (yPos >= 0) and (yPos <= 0 + 74): 
            self.__hoverCloseGame = True
        
        if self.__state == eRestaurantState.RESTAURANT:
        
            # Ordenamos la ejecucion correspondiente
            for client in self.__clients:
                client.doTask()

            self.__foodTimeBanner.doTask(True)
            self.__chef.doTask(self.__tutorialManager)
            
            # Determinamos cuantos clientes deberian estar activos, de acuerdo al dia
            noClientsTarget = self.__foodTimeBanner.day + 2
            if noClientsTarget > 8:
                noClientsTarget = 8
                
            # Contamos los clientes que estan activos
            activeClients = list()
            inactiveClients = list()
            for client in self.__clients:
                if client.isActive() == True:
                    activeClients.append(client)
                else:
                    inactiveClients.append(client)
                    
            # Contamos la cantidad de clientes a activar
            noClientsToActivate = noClientsTarget - len(activeClients) 
            
            # Activamos solo un cliente por iteracion...
            if noClientsToActivate > 0:
                
                if GlobalsController.SHOW_TUTORIAL == True:
                    
                    # Lo activamos, le enviamos como parametro los clientes activos para que en la activacion no se seleccionen recetas ya seleccionadas por los clientes activos
                    if self.__firstClient == True:
                        clientToActivate = inactiveClients[6]
                        clientToActivate.activate(activeClients, self.__foodTimeBanner.foodTime, True)
                        self.__firstClient = False
                    else:
                        clientToActivate = random.choice(inactiveClients)
                        clientToActivate.activate(activeClients, self.__foodTimeBanner.foodTime, False)
                
                else:
                    # Determinamos el cliente a activar
                    clientToActivate = random.choice(inactiveClients)
                    
                    # Lo activamos, le enviamos como parametro los clientes activos para que en la activacion no se seleccionen recetas ya seleccionadas por lo clientes activos
                    if self.__firstClient == True:
                        clientToActivate.activate(activeClients, self.__foodTimeBanner.foodTime, True)
                        self.__firstClient = False
                    else:
                        clientToActivate.activate(activeClients, self.__foodTimeBanner.foodTime, False)

            # Si se requiere mostrar la pantalla de asignacion de ordenes
            if self.__chef.isAssigningOrder == True:
                
                # Detememos todos los sonidos
                AudioController.stopSounds()
                
                # Indicamos que ahora se debe visualizar la seleccion de ordenes
                self.__state = eRestaurantState.ORDER_ASSIGNMENT
                AudioController.playSound(eSound.ORDER, 1)
                
                # Reiniciamos el asignador de ordenes
                self.__orderAssigner.doReset()

                # Le avisamos al tutorial que avance al siguiente paso
                self.__tutorialManager.nextStep(2)
                
                # Determinamos cuantos clientes deberian estar activos, de acuerdo al dia
                noClientsTarget = self.__foodTimeBanner.day + 2
                if noClientsTarget > 8:
                    noClientsTarget = 8
                
                # Contamos los clientes que estan activos
                activeClients = list()
                for client in self.__clients:
                    if client.isActive() == True:
                        activeClients.append(client)
                
                # Le indicamos el tiempo de comida actual y la lista de clientes activos
                self.__orderAssigner.setRecipeFoodTime(self.__foodTimeBanner.foodTime, activeClients)
                
                # Reiniciamos el Hover
                self.__resetHover()
                
            # Si se requiere mostrar la pantalla de seleccion de ordenes
            elif self.__chef.isSelectingOrder == True:
                
                # Detememos todos los sonidos
                AudioController.stopSounds()
                
                # Indicamos que ahora se debe visualizar la seleccion de ordenes
                self.__state = eRestaurantState.ORDER_SELECTION
                AudioController.playSound(eSound.FRIDGE, 1)
                
                # Reiniciamos el selector de Ingredientes
                self.__orderSelector.doReset()
                
                # Le indicamos los clientes con ordenes a atender
                self.__orderSelector.setClientsWithActiveOrders(self.__chef.getClientsWithActiveOrders())
                
                # Le avisamos al tutorial que avance al siguiente paso
                self.__tutorialManager.nextStep(5)
                
                # Reiniciamos el Hover
                self.__resetHover()
                
            # Si el chef alcanzo un nuevo nivel
            elif self.__chef.hasReachNewlevel == True:
                
                # Detememos todos los sonidos
                AudioController.stopSounds()
                
                # Preparamos todo para mostrar la pantalla correspondiente
                self.__showNewLevel = True
                self.__showNewLevelCurrentTime = 1
                self.__chef.newLevelAnnounced()
                
                AudioController.playSound(eSound.FOOD_TIME_CHANGE, 1)
                
            # Si ha sobrepasado el limite de 30, 60, 90.. estrellas y aun no se le ha mostrado la trivia
            elif (self.__chef.stars >= self.__triviaNextLimit) and (self.__showTrivia == False):
                
                # Detememos todos los sonidos
                AudioController.stopSounds()
            
                # Levantamos la bandera que evita mostrar la trivia varias veces al alcanzar un limite
                self.__showTrivia = True
                
                # Indicamos que ahora se debe visualizar la seleccion de ordenes
                self.__state = eRestaurantState.TRIVIA
                
                # Reiniciamos el selector de Ingredientes
                self.__triviaManager.doReset(self.__foodTimeBanner.foodTime)
                
                # Reiniciamos el Hover
                self.__resetHover()
                
        
        elif self.__state == eRestaurantState.ORDER_ASSIGNMENT:

            # Order 1
            if (xPos >= 230) and (xPos <= 230 + 95) and (yPos >= 210) and (yPos <= 210 + 95):
                self.__hoverOrderAssignment[0] = True
            # Order 2     
            elif (xPos >= 325) and (xPos <= 325 + 95) and (yPos >= 210) and (yPos <= 210 + 95):
                self.__hoverOrderAssignment[1] = True
            # Order 3     
            elif (xPos >= 420) and (xPos <= 420 + 95) and (yPos >= 210) and (yPos <= 210 + 95):
                self.__hoverOrderAssignment[2] = True
            # Order 4     
            elif (xPos >= 515) and (xPos <= 515 + 95) and (yPos >= 210) and (yPos <= 210 + 95):
                self.__hoverOrderAssignment[3] = True
            # Order 5     
            elif (xPos >= 610) and (xPos <= 610 + 95) and (yPos >= 210) and (yPos <= 210 + 95):
                self.__hoverOrderAssignment[4] = True
            # Order 6     
            elif (xPos >= 705) and (xPos <= 705 + 95) and (yPos >= 210) and (yPos <= 210 + 95):
                self.__hoverOrderAssignment[5] = True
            # Order 7     
            elif (xPos >= 800) and (xPos <= 800 + 95) and (yPos >= 210) and (yPos <= 210 + 95):
                self.__hoverOrderAssignment[6] = True
            # Order 8     
            elif (xPos >= 895) and (xPos <= 895 + 95) and (yPos >= 210) and (yPos <= 210 + 95):
                self.__hoverOrderAssignment[7] = True
                
            # Order 9
            elif (xPos >= 230) and (xPos <= 230 + 95) and (yPos >= 310) and (yPos <= 310 + 95):
                self.__hoverOrderAssignment[8] = True
            # Order 10 
            elif (xPos >= 325) and (xPos <= 325 + 95) and (yPos >= 310) and (yPos <= 310 + 95):
                self.__hoverOrderAssignment[9] = True
            # Order 11 
            elif (xPos >= 420) and (xPos <= 420 + 95) and (yPos >= 310) and (yPos <= 310 + 95):
                self.__hoverOrderAssignment[10] = True
            # Order 12 
            elif (xPos >= 515) and (xPos <= 515 + 95) and (yPos >= 310) and (yPos <= 310 + 95):
                self.__hoverOrderAssignment[11] = True
            # Order 13 
            elif (xPos >= 610) and (xPos <= 610 + 95) and (yPos >= 310) and (yPos <= 310 + 95):
                self.__hoverOrderAssignment[12] = True
            # Order 14 
            elif (xPos >= 705) and (xPos <= 705 + 95) and (yPos >= 310) and (yPos <= 310 + 95):
                self.__hoverOrderAssignment[13] = True
            # Order 15 
            elif (xPos >= 800) and (xPos <= 800 + 95) and (yPos >= 310) and (yPos <= 310 + 95):
                self.__hoverOrderAssignment[14] = True
            # Order 16 
            elif (xPos >= 895) and (xPos <= 895 + 95) and (yPos >= 310) and (yPos <= 310 + 95):
                self.__hoverOrderAssignment[15] = True
                
            # Order 17
            elif (xPos >= 230) and (xPos <= 230 + 95) and (yPos >= 410) and (yPos <= 410 + 95):
                self.__hoverOrderAssignment[16] = True
            # Order 18 
            elif (xPos >= 325) and (xPos <= 325 + 95) and (yPos >= 410) and (yPos <= 410 + 95):
                self.__hoverOrderAssignment[17] = True
            # Order 19 
            elif (xPos >= 420) and (xPos <= 420 + 95) and (yPos >= 410) and (yPos <= 410 + 95):
                self.__hoverOrderAssignment[18] = True
            # Order 20 
            elif (xPos >= 515) and (xPos <= 515 + 95) and (yPos >= 410) and (yPos <= 410 + 95):
                self.__hoverOrderAssignment[19] = True
            # Order 21 
            elif (xPos >= 610) and (xPos <= 610 + 95) and (yPos >= 410) and (yPos <= 410 + 95):
                self.__hoverOrderAssignment[20] = True
            # Order 22 
            elif (xPos >= 705) and (xPos <= 705 + 95) and (yPos >= 410) and (yPos <= 410 + 95):
                self.__hoverOrderAssignment[21] = True
            # Order 23 
            elif (xPos >= 800) and (xPos <= 800 + 95) and (yPos >= 410) and (yPos <= 410 + 95):
                self.__hoverOrderAssignment[22] = True
            # Order 24 
            elif (xPos >= 895) and (xPos <= 895 + 95) and (yPos >= 410) and (yPos <= 410 + 95):
                self.__hoverOrderAssignment[23] = True
                
            # Order 25
            elif (xPos >= 230) and (xPos <= 230 + 95) and (yPos >= 510) and (yPos <= 510 + 95):
                self.__hoverOrderAssignment[24] = True
            # Order 26    
            elif (xPos >= 325) and (xPos <= 325 + 95) and (yPos >= 510) and (yPos <= 510 + 95):
                self.__hoverOrderAssignment[25] = True
            # Order 27    
            elif (xPos >= 420) and (xPos <= 420 + 95) and (yPos >= 510) and (yPos <= 510 + 95):
                self.__hoverOrderAssignment[26] = True
            # Order 28    
            elif (xPos >= 515) and (xPos <= 515 + 95) and (yPos >= 510) and (yPos <= 510 + 95):
                self.__hoverOrderAssignment[27] = True
            # Order 29    
            elif (xPos >= 610) and (xPos <= 610 + 95) and (yPos >= 510) and (yPos <= 510 + 95):
                self.__hoverOrderAssignment[28] = True
            # Order 30    
            elif (xPos >= 705) and (xPos <= 705 + 95) and (yPos >= 510) and (yPos <= 510 + 95):
                self.__hoverOrderAssignment[29] = True
            # Order 31    
            elif (xPos >= 800) and (xPos <= 800 + 95) and (yPos >= 510) and (yPos <= 510 + 95):
                self.__hoverOrderAssignment[30] = True
            # Order 32    
            elif (xPos >= 895) and (xPos <= 895 + 95) and (yPos >= 510) and (yPos <= 510 + 95):
                self.__hoverOrderAssignment[31] = True
                
            # Order 33
            elif (xPos >= 230) and (xPos <= 230 + 95) and (yPos >= 610) and (yPos <= 610 + 95):
                self.__hoverOrderAssignment[32] = True
            # Order 34    
            elif (xPos >= 325) and (xPos <= 325 + 95) and (yPos >= 610) and (yPos <= 610 + 95):
                self.__hoverOrderAssignment[33] = True
            # Order 35    
            elif (xPos >= 420) and (xPos <= 420 + 95) and (yPos >= 610) and (yPos <= 610 + 95):
                self.__hoverOrderAssignment[34] = True
            # Order 36    
            elif (xPos >= 515) and (xPos <= 515 + 95) and (yPos >= 610) and (yPos <= 610 + 95):
                self.__hoverOrderAssignment[35] = True
            # Order 37    
            elif (xPos >= 610) and (xPos <= 610 + 95) and (yPos >= 610) and (yPos <= 610 + 95):
                self.__hoverOrderAssignment[36] = True
            # Order 38    
            elif (xPos >= 705) and (xPos <= 705 + 95) and (yPos >= 610) and (yPos <= 610 + 95):
                self.__hoverOrderAssignment[37] = True
            # Order 39    
            elif (xPos >= 800) and (xPos <= 800 + 95) and (yPos >= 610) and (yPos <= 610 + 95):
                self.__hoverOrderAssignment[38] = True
            # Order 40    
            elif (xPos >= 895) and (xPos <= 895 + 95) and (yPos >= 610) and (yPos <= 610 + 95):
                self.__hoverOrderAssignment[39] = True
        
            # Ordenamos la ejecucion correspondiente
            self.__foodTimeBanner.doTask(True)
            self.__orderAssigner.doTask()
            
            # Si se requiere mostrar el restaurante
            if self.__orderAssigner.wasOrderSelected() == True:
                
                # Indicamos que ahora se debe visualizar el restaurante
                self.__state = eRestaurantState.RESTAURANT
                
                # Le asignamos la orden elegida al cliente seleccionado
                self.__chef.assignOrderToSelectedClient(self.__orderAssigner.getSelectedOrder())                
                
                # Reiniciamos el asignador de ordenes para uso posterior
                self.__orderAssigner.doReset()
                
                # Le avisamos al tutorial que avance al siguiente paso
                self.__tutorialManager.nextStep(3)
                
                # Reiniciamos el Hover
                self.__resetHover()

        elif self.__state == eRestaurantState.ORDER_SELECTION:
            
            # Order 1
            if (xPos >= 160) and (xPos <= 160 + 410) and (yPos >= 100) and (yPos <= 100 + 80):
                self.__hoverOrderSelection[0] = True
            # Order 2
            elif (xPos >= 160) and (xPos <= 160 + 410) and (yPos >= 185) and (yPos <= 185 + 80):
                self.__hoverOrderSelection[1] = True
            # Order 3
            elif (xPos >= 160) and (xPos <= 160 + 410) and (yPos >= 270) and (yPos <= 270 + 80):
                self.__hoverOrderSelection[2] = True
            # Order 4
            elif (xPos >= 160) and (xPos <= 160 + 410) and (yPos >= 355) and (yPos <= 355 + 80):
                self.__hoverOrderSelection[3] = True
            # Order 5
            elif (xPos >= 160) and (xPos <= 160 + 410) and (yPos >= 440) and (yPos <= 440 + 80):
                self.__hoverOrderSelection[4] = True
            # Order 6
            elif (xPos >= 160) and (xPos <= 160 + 410) and (yPos >= 525) and (yPos <= 525 + 80):
                self.__hoverOrderSelection[5] = True
            # Order 7
            elif (xPos >= 160) and (xPos <= 160 + 410) and (yPos >= 610) and (yPos <= 610 + 80):
                self.__hoverOrderSelection[6] = True
            # Order 8
            elif (xPos >= 160) and (xPos <= 160 + 410) and (yPos >= 695) and (yPos <= 695 + 80):
                self.__hoverOrderSelection[7] = True
            
            # Ordenamos la ejecucion correspondiente
            self.__chef.doTask(self.__tutorialManager)            
            self.__orderSelector.doTask()
            
            # Si ya fue seleccionada la orden a atender
            if self.__orderSelector.wasOrderSelected() == True:
                
                # Indicamos que ahora se debe visualizar el selector de ingredientes
                self.__state = eRestaurantState.RECIPE_MAKER
                
                # Le informamos al chef que la order a atender ya fue seleccionada
                self.__chef.orderSelected(self.__orderSelector.getSelectedClient())
                
                # Le informamos al selector de ingredientes cual fue la receta seleccionada
                self.__recipeMaker.orderSelected(self.__orderSelector.getSelectedClient())
                
                # Reiniciamos el selector de ordenes para un uso posterior
                self.__orderSelector.doReset()
                
                # Le avisamos al tutorial que avance al siguiente paso
                self.__tutorialManager.nextStep(6)
                
                # Reiniciamos el Hover
                self.__resetHover()
                
                # Reproducimos la musica de fondo correspondiente
                AudioController.playMusic(eMusic.QUIET)
                
        elif self.__state == eRestaurantState.RECIPE_MAKER:
            
            # Cancel
            if (xPos >= 710) and (xPos <= 710 + 160) and (yPos >= 760) and (yPos <= 760 + 56):
                if(GlobalsController.SHOW_TUTORIAL == False):
                    self.__hoverCancel = True
            # Group 1
            elif (xPos >= 250 + (55 * 0)) and (xPos <= 250 + (55 * 0) + 50) and (yPos >= 90) and (yPos <= 90 + 50):
                self.__hoverRecipeMaker[0] = True
            # Group 2
            elif (xPos >= 250 + (55 * 1)) and (xPos <= 250 + (55 * 1) + 50) and (yPos >= 90) and (yPos <= 90 + 50):
                self.__hoverRecipeMaker[1] = True
            # Group 3
            elif (xPos >= 250 + (55 * 2)) and (xPos <= 250 + (55 * 2) + 50) and (yPos >= 90) and (yPos <= 90 + 50):
                self.__hoverRecipeMaker[2] = True
            # Group 4
            elif (xPos >= 250 + (55 * 3)) and (xPos <= 250 + (55 * 3) + 50) and (yPos >= 90) and (yPos <= 90 + 50):
                self.__hoverRecipeMaker[3] = True
            # Group 5
            elif (xPos >= 250 + (55 * 4)) and (xPos <= 250 + (55 * 4) + 50) and (yPos >= 90) and (yPos <= 90 + 50):
                self.__hoverRecipeMaker[4] = True
            # Group 6
            elif (xPos >= 250 + (55 * 5)) and (xPos <= 250 + (55 * 5) + 50) and (yPos >= 90) and (yPos <= 90 + 50):
                self.__hoverRecipeMaker[5] = True
            # Group 7
            elif (xPos >= 250 + (55 * 6)) and (xPos <= 250 + (55 * 6) + 50) and (yPos >= 90) and (yPos <= 90 + 50):
                self.__hoverRecipeMaker[6] = True
            # Group 8
            elif (xPos >= 250 + (55 * 7)) and (xPos <= 250 + (55 * 7) + 50) and (yPos >= 90) and (yPos <= 90 + 50):
                self.__hoverRecipeMaker[7] = True
            
            # Ordenamos la ejecucion correspondiente
            self.__chef.doTask(self.__tutorialManager)
            self.__recipeMaker.doTask()
            
            # Si ya fueron seleccionados los ingredientes para el plato
            if self.__recipeMaker.ingredientsMarkedAsReady() == True:
                
                # Indicamos que ahora se debe visualizar la cocina
                self.__state = eRestaurantState.RESTAURANT
                AudioController.playSound(eSound.FRIDGE, 1)
                
                # Le informamos al chef que los ingredientes ya fueron seleccionados
                self.__chef.ingredientsPicked()
                
                # Reiniciamos el selector de Ingredientes para un uso posterior
                self.__recipeMaker.doReset()
                
                # Le avisamos al tutorial que avance al siguiente paso
                self.__tutorialManager.nextStep(16)
                
                # Reiniciamos el Hover
                self.__resetHover()
                
                # Reproducimos la musica de fondo correspondiente
                AudioController.playMusic(eMusic.RESTAURANT)
                
        elif self.__state == eRestaurantState.TRIVIA:
            
            # Answer 1
            if (xPos >= 0) and (xPos <= 400) and (yPos >= 150) and (yPos <= 150 + 574):
                self.__hoverTriviaManager[0] = True
            # Answer 2
            elif (xPos >= 400) and (xPos <= 800) and (yPos >= 150) and (yPos <= 150 + 574):
                self.__hoverTriviaManager[1] = True
            # Answer 3
            elif (xPos >= 800) and (xPos <= 1200) and (yPos >= 150) and (yPos <= 150 + 574):
                self.__hoverTriviaManager[2] = True
            
            # Ordenamos la ejecucion correspondiente
            self.__triviaManager.doTask()
            
            # Si ya fue respondida la pregunta de la trivia
            if self.__triviaManager.wasTriviaAnswered() == True:
                
                # Bajamos la bandera para poder mostrar la trivia cuando se alcance el nuevo limite
                self.__showTrivia = False
                
                # Subimos el limite a alcanzar
                self.__triviaNextLimit = self.__triviaNextLimit + 30
                
                # Premiamos al jugador con 5 estrellas
                self.__chef.stars = self.__chef.stars + 5 
                
                # Indicamos que ahora se debe visualizar el restaurante
                self.__state = eRestaurantState.RESTAURANT
                
                # Reiniciamos el Hover
                self.__resetHover()
                
                # Reproducimos la musica de fondo correspondiente
                AudioController.playMusic(eMusic.RESTAURANT)
                
        # Detectamos todos los eventos y ejecutamos las acciones correspondientes
        if pygame.event:
            for event in pygame.event.get():
                
                # Evento cerrar el juego
                if event.type == pygame.QUIT:
                    GlobalsController.INFO_STARS = self.__chef.stars
                    View.showScreen(eScreen.SPLASH_CLOSE)
                    
                # Eventos del sistema
                elif event.type == pygame.USEREVENT:
                    pass
                    
                # Deteccion de click de mouse
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.__doMouseAction(event)
                    
                # Deteccion de teclas presionadas
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        GlobalsController.INFO_STARS = self.__chef.stars
                        View.showScreen(eScreen.SPLASH_CLOSE)
                    else:
                        self.__doKeyAction(event)

    def __doPaint(self):
        
        # El orden de pintado es estricto, de acuerdo a su posicion en el eje Y
        self.__displaySurface.blit(ResourceController.background_Kitchen, (0, 0))
        
        # Si el restaurante esta activado
        if self.__state == eRestaurantState.RESTAURANT:      
                
            # Chef antes de la primera fila
            if self.__chef.getPositionXY()[1] < 200:
                self.__chef.doPaint(self.__displaySurface)
                
            # Tiempos de Comida
            self.__foodTimeBanner.doPaint(self.__displaySurface, True)
            
            # Chef entre la primera y la segunda fila
            if self.__chef.getPositionXY()[1] == 200:
                self.__chef.doPaint(self.__displaySurface)
            
            # Sillas fila 1
            self.__displaySurface.blit(ResourceController.game_Chair, (10, 485))
            self.__displaySurface.blit(ResourceController.game_Chair, (320, 485))
            self.__displaySurface.blit(ResourceController.game_Chair, (630, 485))
            self.__displaySurface.blit(ResourceController.game_Chair, (940, 485))
            
            # Mesas fila 1
            self.__displaySurface.blit(ResourceController.game_Table, (80, 400))
            self.__displaySurface.blit(ResourceController.game_Table, (390, 400))
            self.__displaySurface.blit(ResourceController.game_Table, (700, 400))
            self.__displaySurface.blit(ResourceController.game_Table, (1010, 400))
            
            # Clientes fila 1
            for client in self.__clients:
                if client.getRow() == eMotionRow.ROW_2:
                    client.doPaint(self.__displaySurface)
    
            # Chef entre la segunda y la tercera fila
            if (self.__chef.getPositionXY()[1] > 200) and (self.__chef.getPositionXY()[1] <= 430):
                self.__chef.doPaint(self.__displaySurface)
            
            # Sillas fila 2
            self.__displaySurface.blit(ResourceController.game_Chair, (10, 715))
            self.__displaySurface.blit(ResourceController.game_Chair, (320, 715))
            self.__displaySurface.blit(ResourceController.game_Chair, (630, 715))
            self.__displaySurface.blit(ResourceController.game_Chair, (940, 715))
            
            # Mesas fila 2
            self.__displaySurface.blit(ResourceController.game_Table, (80, 630))
            self.__displaySurface.blit(ResourceController.game_Table, (390, 630))
            self.__displaySurface.blit(ResourceController.game_Table, (700, 630))
            self.__displaySurface.blit(ResourceController.game_Table, (1010, 630))
                
            # Clientes fila 2
            for client in self.__clients:
                if client.getRow() == eMotionRow.ROW_3:
                    client.doPaint(self.__displaySurface)
                    
            # Si se necesita mostrar que el chef avanzo de nivel
            if self.__showNewLevel == True:
                
                # Mostramos el mensaje
                if self.__showNewLevelCurrentTime < self.__showNewLevelTotalTime:
                    self.__showNewLevelCurrentTime = self.__showNewLevelCurrentTime + 1
                    
                    # Background
                    self.__displaySurface.blit(ResourceController.background_Transparent, (0, 0))
                    self.__displaySurface.blit(ResourceController.game_ChefNewLevel, (600 - 310, 50))
                    
                    # Text
                    if self.__chef.level == eChefLevel.LEVEL_1_JUNIOR:
                        self.__textGotStars2.setPosition((300, 260))
                        self.__textGotStars2.setText("25 Estrellas")
                    elif self.__chef.level == eChefLevel.LEVEL_2_SENIOR:
                        self.__textGotStars2.setPosition((300, 260))
                        self.__textGotStars2.setText("50 Estrellas")
                    elif self.__chef.level == eChefLevel.LEVEL_3_SUPER:
                        self.__textGotStars2.setPosition((270, 260))
                        self.__textGotStars2.setText("100 Estrellas")
                    
                    self.__textGotStars1.doPaint(self.__displaySurface)
                    self.__textGotStars2.doPaint(self.__displaySurface)    
                    self.__textGotStars3.doPaint(self.__displaySurface)
                    
                    # New Level
                    if self.__chef.level == eChefLevel.LEVEL_1_JUNIOR:
                        self.__displaySurface.blit(ResourceController.game_ChefLevel1, (510, 580))
                        self.__displaySurface.blit(ResourceController.game_ChefHatBronze, (350, 520))
                    elif self.__chef.level == eChefLevel.LEVEL_2_SENIOR:
                        self.__displaySurface.blit(ResourceController.game_ChefLevel2, (510, 580))
                        self.__displaySurface.blit(ResourceController.game_ChefHatSilver, (350, 520))
                    elif self.__chef.level == eChefLevel.LEVEL_3_SUPER:
                        self.__displaySurface.blit(ResourceController.game_ChefLevel3, (510, 580))
                        self.__displaySurface.blit(ResourceController.game_ChefHatGold, (350, 520))
                    
                else:
                    # El mensaje ya fue mostrado
                    self.__showNewLevelCurrentTime = 1
                    self.__showNewLevel = False
                    
        # Si la asignacion de ordenes esta activada
        elif self.__state == eRestaurantState.ORDER_ASSIGNMENT:
            self.__orderAssigner.doPaint(self.__displaySurface, self.__hoverOrderAssignment)
            
            # Tiempos de Comida
            self.__foodTimeBanner.doPaint(self.__displaySurface, False)
            
        # Si la seleccion de ordenes a atender esta activada
        elif self.__state == eRestaurantState.ORDER_SELECTION:
            self.__orderSelector.doPaint(self.__displaySurface, self.__hoverOrderSelection)
        
        # Si la seleccion de alimentos esta activada 
        elif self.__state == eRestaurantState.RECIPE_MAKER:
            
            hoverRecipeMaker = list()
            
            for currentHover in self.__hoverRecipeMaker:
                hoverRecipeMaker.append(currentHover)
                
            hoverRecipeMaker.append(self.__hoverCancel)
            
            self.__recipeMaker.doPaint(self.__displaySurface, hoverRecipeMaker)
            
        # Si la trivia esta activada 
        elif self.__state == eRestaurantState.TRIVIA:
            self.__triviaManager.doPaint(self.__displaySurface, self.__hoverTriviaManager)
            
        # Fondo de datos generales
        self.__displaySurface.blit(ResourceController.game_StarsBackground, (0, 0))
        
        # Cantidad de estrellas
        self.__displaySurface.blit(ResourceController.game_Star, (80, 4))
        self.__textStars.setText("x " + str(self.__chef.stars))
        self.__textStars.doPaint(self.__displaySurface)
        
        # Nivel del Chef
        if self.__chef.level == eChefLevel.LEVEL_0_NONE:
            self.__displaySurface.blit(ResourceController.game_ChefHatMiniNone, (5, 0))
        elif self.__chef.level == eChefLevel.LEVEL_1_JUNIOR:
            self.__displaySurface.blit(ResourceController.game_ChefHatMiniBronze, (5, 0))
        elif self.__chef.level == eChefLevel.LEVEL_2_SENIOR:
            self.__displaySurface.blit(ResourceController.game_ChefHatMiniSilver, (5, 0))
        elif self.__chef.level == eChefLevel.LEVEL_3_SUPER:
            self.__displaySurface.blit(ResourceController.game_ChefHatMiniGold, (5, 0))
            
        # Tutorial
        self.__tutorialManager.doPaint(self.__displaySurface)
        
        # Buttons with Hover
        if self.__hoverCloseGame == True:
            self.__displaySurface.blit(ResourceController.input_CloseGame_On, (1200 - 87, 0))
        else:
            self.__displaySurface.blit(ResourceController.input_CloseGame_Off, (1200 - 87, 0))

        # Actualizamos la pantalla
        pygame.display.flip()

    def activate(self):
        
        # Indicamos que esta pantalla pasa a estado Activo
        self.__isActive = True
        
        # Mostramos el cursor
        pygame.mouse.set_visible(True)
        
        # Ordanamos que comience el pintado de la pantalla
        self.__run()

    def deactivate(self):
        
        # Indicamos que esta pantalla pasa a estado Inactivo
        self.__isActive = False

    def __run(self):
        
        # Reproducimos la musica de fondo
        AudioController.playMusic(eMusic.RESTAURANT)
        
        # Loop principal
        while self.__isActive is True:

            # Realizamos las operaciones propias del model
            self.__doTask()
            
            # Pintamos el resultado en pantalla
            self.__doPaint()
            
            # Running as Activity
            if olpcgames.ACTIVITY:
                pass
            else:
                # Saltamos a la siguiente iteracion, respetando el FPS establecido
                self.__clock.tick(GlobalsController.GAME_FPS)
        
    def __doMouseAction(self, event):
        
        # Detectamos la posicion en X y Y del click
        xPos, yPos = event.pos

        # Close Game
        if (xPos >= 1200 - 87) and (xPos <= 1200) and (yPos >= 0) and (yPos <= 0 + 74):
            GlobalsController.INFO_STARS = self.__chef.stars
            View.showScreen(eScreen.SPLASH_CLOSE)
        
        elif self.__state == eRestaurantState.RESTAURANT:
        
            # Detectamos en cual mesa o parte de la cocina fue realizado el click
            selectedBlockId = None
            clientId = None
            
            # Fila 1
            # ROW1_STOVE
            if (xPos >= 60) and (xPos <= 300) and (yPos >= 0) and (yPos <= 200):
                selectedBlockId = eMotionBlock.ROW1_STOVE
                clientId = None
            # ROW1_SINK
            elif (xPos >= 365) and (xPos <= 615) and (yPos >= 0) and (yPos <= 200):
                selectedBlockId = eMotionBlock.ROW1_SINK
                clientId = None
            # ROW1_FRIDGE
            elif (xPos >= 705) and (xPos <= 900) and (yPos >= 0) and (yPos <= 200):
                selectedBlockId = eMotionBlock.ROW1_FRIDGE
                clientId = None
            # ROW1_DISHWASHER
            elif (xPos >= 980) and (xPos <= 1200) and (yPos >= 0) and (yPos <= 200):
                selectedBlockId = eMotionBlock.ROW1_DISHWASHER
                clientId = None
    
            # Fila 2
            # ROW2_BLOCK_A
            elif (xPos >= 0) and (xPos <= 270) and (yPos >= 308) and (yPos <= 540):
                selectedBlockId = eMotionBlock.ROW2_BLOCK_A
                clientId = eClientId.CLIENT_A_ROW2
            # ROW2_BLOCK_B
            elif (xPos >= 305) and (xPos <= 580) and (yPos >= 308) and (yPos <= 540):
                selectedBlockId = eMotionBlock.ROW2_BLOCK_B
                clientId = eClientId.CLIENT_B_ROW2
            # ROW2_BLOCK_C
            elif (xPos >= 615) and (xPos <= 890) and (yPos >= 308) and (yPos <= 540):
                selectedBlockId = eMotionBlock.ROW2_BLOCK_C
                clientId = eClientId.CLIENT_C_ROW2
            # ROW2_BLOCK_D
            elif (xPos >= 925) and (xPos <= 1200) and (yPos >= 308) and (yPos <= 540):
                selectedBlockId = eMotionBlock.ROW2_BLOCK_D
                clientId = eClientId.CLIENT_D_ROW2
            
            # Fila 3
            # ROW3_BLOCK_E
            elif (xPos >= 0) and (xPos <= 270) and (yPos >= 540) and (yPos <= 825):
                selectedBlockId = eMotionBlock.ROW3_BLOCK_E
                clientId = eClientId.CLIENT_E_ROW3
            # ROW3_BLOCK_F
            elif (xPos >= 305) and (xPos <= 580) and (yPos >= 540) and (yPos <= 825):
                selectedBlockId = eMotionBlock.ROW3_BLOCK_F
                clientId = eClientId.CLIENT_F_ROW3
            # ROW3_BLOCK_G
            elif (xPos >= 615) and (xPos <= 890) and (yPos >= 540) and (yPos <= 825):
                selectedBlockId = eMotionBlock.ROW3_BLOCK_G
                clientId = eClientId.CLIENT_G_ROW3
            # ROW3_BLOCK_H
            elif (xPos >= 925) and (xPos <= 1200) and (yPos >= 540) and (yPos <= 825):
                selectedBlockId = eMotionBlock.ROW3_BLOCK_H
                clientId = eClientId.CLIENT_H_ROW3
    
            # Si el click fue realizado dentro de alguno de los puntos
            if selectedBlockId != None:
    
                # Determinamos si algun cliente fue seleccionado    
                selectedClient = self.__getClientById(clientId)
    
                # Si algun cliente fue seleccionado...
                if selectedClient != None:
                    
                    # Le ordenamos al chef que calcule la orden a ejecutar
                    self.__chef.calculateCommand(selectedBlockId, selectedClient)
                    
                else:
                    # Le ordenamos al chef que calcule la orden a ejecutar
                    self.__chef.calculateCommand(selectedBlockId, None)
                    
        elif self.__state == eRestaurantState.ORDER_ASSIGNMENT:

            # Order 1
            if (xPos >= 230) and (xPos <= 230 + 95) and (yPos >= 210) and (yPos <= 210 + 95):
                self.__orderAssigner.clickOnOrder(1)
            # Order 2     
            elif (xPos >= 325) and (xPos <= 325 + 95) and (yPos >= 210) and (yPos <= 210 + 95):
                self.__orderAssigner.clickOnOrder(2)
            # Order 3     
            elif (xPos >= 420) and (xPos <= 420 + 95) and (yPos >= 210) and (yPos <= 210 + 95):
                self.__orderAssigner.clickOnOrder(3)
            # Order 4     
            elif (xPos >= 515) and (xPos <= 515 + 95) and (yPos >= 210) and (yPos <= 210 + 95):
                self.__orderAssigner.clickOnOrder(4)
            # Order 5     
            elif (xPos >= 610) and (xPos <= 610 + 95) and (yPos >= 210) and (yPos <= 210 + 95):
                self.__orderAssigner.clickOnOrder(5)
            # Order 6     
            elif (xPos >= 705) and (xPos <= 705 + 95) and (yPos >= 210) and (yPos <= 210 + 95):
                self.__orderAssigner.clickOnOrder(6)
            # Order 7     
            elif (xPos >= 800) and (xPos <= 800 + 95) and (yPos >= 210) and (yPos <= 210 + 95):
                self.__orderAssigner.clickOnOrder(7)
            # Order 8     
            elif (xPos >= 895) and (xPos <= 895 + 95) and (yPos >= 210) and (yPos <= 210 + 95):
                self.__orderAssigner.clickOnOrder(8)
                
            # Order 9
            elif (xPos >= 230) and (xPos <= 230 + 95) and (yPos >= 310) and (yPos <= 310 + 95):
                self.__orderAssigner.clickOnOrder(9)
            # Order 10 
            elif (xPos >= 325) and (xPos <= 325 + 95) and (yPos >= 310) and (yPos <= 310 + 95):
                self.__orderAssigner.clickOnOrder(10)
            # Order 11 
            elif (xPos >= 420) and (xPos <= 420 + 95) and (yPos >= 310) and (yPos <= 310 + 95):
                self.__orderAssigner.clickOnOrder(11)
            # Order 12 
            elif (xPos >= 515) and (xPos <= 515 + 95) and (yPos >= 310) and (yPos <= 310 + 95):
                self.__orderAssigner.clickOnOrder(12)
            # Order 13 
            elif (xPos >= 610) and (xPos <= 610 + 95) and (yPos >= 310) and (yPos <= 310 + 95):
                self.__orderAssigner.clickOnOrder(13)
            # Order 14 
            elif (xPos >= 705) and (xPos <= 705 + 95) and (yPos >= 310) and (yPos <= 310 + 95):
                self.__orderAssigner.clickOnOrder(14)
            # Order 15 
            elif (xPos >= 800) and (xPos <= 800 + 95) and (yPos >= 310) and (yPos <= 310 + 95):
                self.__orderAssigner.clickOnOrder(15)
            # Order 16 
            elif (xPos >= 895) and (xPos <= 895 + 95) and (yPos >= 310) and (yPos <= 310 + 95):
                self.__orderAssigner.clickOnOrder(16)
                
            # Order 17
            elif (xPos >= 230) and (xPos <= 230 + 95) and (yPos >= 410) and (yPos <= 410 + 95):
                self.__orderAssigner.clickOnOrder(17)
            # Order 18 
            elif (xPos >= 325) and (xPos <= 325 + 95) and (yPos >= 410) and (yPos <= 410 + 95):
                self.__orderAssigner.clickOnOrder(18)
            # Order 19 
            elif (xPos >= 420) and (xPos <= 420 + 95) and (yPos >= 410) and (yPos <= 410 + 95):
                self.__orderAssigner.clickOnOrder(19)
            # Order 20 
            elif (xPos >= 515) and (xPos <= 515 + 95) and (yPos >= 410) and (yPos <= 410 + 95):
                self.__orderAssigner.clickOnOrder(20)
            # Order 21 
            elif (xPos >= 610) and (xPos <= 610 + 95) and (yPos >= 410) and (yPos <= 410 + 95):
                self.__orderAssigner.clickOnOrder(21)
            # Order 22 
            elif (xPos >= 705) and (xPos <= 705 + 95) and (yPos >= 410) and (yPos <= 410 + 95):
                self.__orderAssigner.clickOnOrder(22)
            # Order 23 
            elif (xPos >= 800) and (xPos <= 800 + 95) and (yPos >= 410) and (yPos <= 410 + 95):
                self.__orderAssigner.clickOnOrder(23)
            # Order 24 
            elif (xPos >= 895) and (xPos <= 895 + 95) and (yPos >= 410) and (yPos <= 410 + 95):
                self.__orderAssigner.clickOnOrder(24)
                
            # Order 25
            elif (xPos >= 230) and (xPos <= 230 + 95) and (yPos >= 510) and (yPos <= 510 + 95):
                self.__orderAssigner.clickOnOrder(25)
            # Order 26    
            elif (xPos >= 325) and (xPos <= 325 + 95) and (yPos >= 510) and (yPos <= 510 + 95):
                self.__orderAssigner.clickOnOrder(26)
            # Order 27    
            elif (xPos >= 420) and (xPos <= 420 + 95) and (yPos >= 510) and (yPos <= 510 + 95):
                self.__orderAssigner.clickOnOrder(27)
            # Order 28    
            elif (xPos >= 515) and (xPos <= 515 + 95) and (yPos >= 510) and (yPos <= 510 + 95):
                self.__orderAssigner.clickOnOrder(28)
            # Order 29    
            elif (xPos >= 610) and (xPos <= 610 + 95) and (yPos >= 510) and (yPos <= 510 + 95):
                self.__orderAssigner.clickOnOrder(29)
            # Order 30    
            elif (xPos >= 705) and (xPos <= 705 + 95) and (yPos >= 510) and (yPos <= 510 + 95):
                self.__orderAssigner.clickOnOrder(30)
            # Order 31    
            elif (xPos >= 800) and (xPos <= 800 + 95) and (yPos >= 510) and (yPos <= 510 + 95):
                self.__orderAssigner.clickOnOrder(31)
            # Order 32    
            elif (xPos >= 895) and (xPos <= 895 + 95) and (yPos >= 510) and (yPos <= 510 + 95):
                self.__orderAssigner.clickOnOrder(32)
                
            # Order 33
            elif (xPos >= 230) and (xPos <= 230 + 95) and (yPos >= 610) and (yPos <= 610 + 95):
                self.__orderAssigner.clickOnOrder(33)
            # Order 34    
            elif (xPos >= 325) and (xPos <= 325 + 95) and (yPos >= 610) and (yPos <= 610 + 95):
                self.__orderAssigner.clickOnOrder(34)
            # Order 35    
            elif (xPos >= 420) and (xPos <= 420 + 95) and (yPos >= 610) and (yPos <= 610 + 95):
                self.__orderAssigner.clickOnOrder(35)
            # Order 36    
            elif (xPos >= 515) and (xPos <= 515 + 95) and (yPos >= 610) and (yPos <= 610 + 95):
                self.__orderAssigner.clickOnOrder(36)
            # Order 37    
            elif (xPos >= 610) and (xPos <= 610 + 95) and (yPos >= 610) and (yPos <= 610 + 95):
                self.__orderAssigner.clickOnOrder(37)
            # Order 38    
            elif (xPos >= 705) and (xPos <= 705 + 95) and (yPos >= 610) and (yPos <= 610 + 95):
                self.__orderAssigner.clickOnOrder(38)
            # Order 39    
            elif (xPos >= 800) and (xPos <= 800 + 95) and (yPos >= 610) and (yPos <= 610 + 95):
                self.__orderAssigner.clickOnOrder(39)
            # Order 40    
            elif (xPos >= 895) and (xPos <= 895 + 95) and (yPos >= 610) and (yPos <= 610 + 95):
                self.__orderAssigner.clickOnOrder(40)
        
        elif self.__state == eRestaurantState.ORDER_SELECTION:
            if (xPos >= 160) and (xPos <= 160 + 410) and (yPos >= 100) and (yPos <= 100 + 80):
                self.__orderSelector.clickOrder1()
            elif (xPos >= 160) and (xPos <= 160 + 410) and (yPos >= 185) and (yPos <= 185 + 80):
                self.__orderSelector.clickOrder2()
            elif (xPos >= 160) and (xPos <= 160 + 410) and (yPos >= 270) and (yPos <= 270 + 80):
                self.__orderSelector.clickOrder3()
            elif (xPos >= 160) and (xPos <= 160 + 410) and (yPos >= 355) and (yPos <= 355 + 80):
                self.__orderSelector.clickOrder4()
            elif (xPos >= 160) and (xPos <= 160 + 410) and (yPos >= 440) and (yPos <= 440 + 80):
                self.__orderSelector.clickOrder5()
            elif (xPos >= 160) and (xPos <= 160 + 410) and (yPos >= 525) and (yPos <= 525 + 80):
                self.__orderSelector.clickOrder6()
            elif (xPos >= 160) and (xPos <= 160 + 410) and (yPos >= 610) and (yPos <= 610 + 80):
                self.__orderSelector.clickOrder7()
            elif (xPos >= 160) and (xPos <= 160 + 410) and (yPos >= 695) and (yPos <= 695 + 80):
                self.__orderSelector.clickOrder8()
                    
        elif self.__state == eRestaurantState.RECIPE_MAKER:
            
            # Dish Ready Button
            if (xPos >= 875) and (xPos <= 875 + 320) and (yPos >= 740) and (yPos <= 740 + 86):
                self.__recipeMaker.clickButtonDishReady()
                return
            
            # Cancel
            elif (xPos >= 710) and (xPos <= 710 + 160) and (yPos >= 760) and (yPos <= 760 + 56):
                
                # Si no estamos en modo tutorial
                if(GlobalsController.SHOW_TUTORIAL == False):
                    
                    # Indicamos que ahora se debe visualizar la cocina
                    self.__state = eRestaurantState.RESTAURANT
                    AudioController.playSound(eSound.FRIDGE, 1)
                    
                    # Cancelamos la creacion de la receta
                    self.__chef.cancelIngredientsPicking()
                    
                    # Reiniciamos el selector de Ingredientes para un uso posterior
                    self.__recipeMaker.doReset()
                    
                    # Reproducimos la musica de fondo correspondiente
                    AudioController.playMusic(eMusic.RESTAURANT)
                    return
                
            # Tabs
            elif (xPos >= 248) and (xPos <= 503) and (yPos >= 10) and (yPos <= 80):
                self.__recipeMaker.clickTabIngredients()
                
                # Le avisamos al tutorial que avance al siguiente paso
                self.__tutorialManager.nextStep(15)
                return
            
            elif (xPos >= 504) and (xPos <= 702) and (yPos >= 10) and (yPos <= 76):
                self.__recipeMaker.clickTabRecipe()
                
                # Le avisamos al tutorial que avance al siguiente paso
                self.__tutorialManager.nextStep(12)
                return
                
            # Arrows
            elif (xPos >= 135) and (xPos <= 200) and (yPos >= 350) and (yPos <= 445):
                self.__recipeMaker.clickArrowLeft()
                
                # Le avisamos al tutorial que avance al siguiente paso
                self.__tutorialManager.nextStep(10)
                return
            
            elif (xPos >= 625) and (xPos <= 690) and (yPos >= 350) and (yPos <= 445):
                self.__recipeMaker.clickArrowRight()
                
                # Le avisamos al tutorial que avance al siguiente paso
                self.__tutorialManager.nextStep(9)
                self.__tutorialManager.nextStep(14)
                return
                
            # Selected Items to Delete
            elif (xPos >= 800) and (xPos <= 800 + 54) and (yPos >= 110) and (yPos <= 110 + 54):
                self.__recipeMaker.clickDeleteSeletedItem1()
                
                # Le avisamos al tutorial que avance al siguiente paso
                self.__tutorialManager.nextStep(11)
                return
            
            elif (xPos >= 960) and (xPos <= 960 + 54) and (yPos >= 110) and (yPos <= 110 + 54):
                self.__recipeMaker.clickDeleteSeletedItem2()
                return
            elif (xPos >= 1120) and (xPos <= 1120 + 54) and (yPos >= 110) and (yPos <= 110 + 54):
                self.__recipeMaker.clickDeleteSeletedItem3()
                return
            elif (xPos >= 800) and (xPos <= 800 + 54) and (yPos >= 260) and (yPos <= 260 + 54):
                self.__recipeMaker.clickDeleteSeletedItem4()
                return
            elif (xPos >= 960) and (xPos <= 960 + 54) and (yPos >= 260) and (yPos <= 260 + 54):
                self.__recipeMaker.clickDeleteSeletedItem5()
                return
            elif (xPos >= 1120) and (xPos <= 1120 + 54) and (yPos >= 260) and (yPos <= 260 + 54):
                self.__recipeMaker.clickDeleteSeletedItem6()
                return
            elif (xPos >= 800) and (xPos <= 800 + 54) and (yPos >= 410) and (yPos <= 410 + 54):
                self.__recipeMaker.clickDeleteSeletedItem7()
                return
            elif (xPos >= 960) and (xPos <= 960 + 54) and (yPos >= 410) and (yPos <= 410 + 54):
                self.__recipeMaker.clickDeleteSeletedItem8()
                return
            elif (xPos >= 1120) and (xPos <= 1120 + 54) and (yPos >= 410) and (yPos <= 410 + 54):
                self.__recipeMaker.clickDeleteSeletedItem9()
                return
                
            if self.__recipeMaker.getCurrentTab() == eIngredientsTab.INGREDIENTS:
                
                # Groups Button
                if (xPos >= 250 + (55 * 0)) and (xPos <= 250 + (55 * 0) + 50) and (yPos >= 90) and (yPos <= 90 + 50):
                    self.__recipeMaker.clickGroups1Button()
                elif (xPos >= 250 + (55 * 1)) and (xPos <= 250 + (55 * 1) + 50) and (yPos >= 90) and (yPos <= 90 + 50):
                    self.__recipeMaker.clickGroups2Button()
                elif (xPos >= 250 + (55 * 2)) and (xPos <= 250 + (55 * 2) + 50) and (yPos >= 90) and (yPos <= 90 + 50):
                    self.__recipeMaker.clickGroups3Button()
                elif (xPos >= 250 + (55 * 3)) and (xPos <= 250 + (55 * 3) + 50) and (yPos >= 90) and (yPos <= 90 + 50):
                    self.__recipeMaker.clickGroups4Button()
                elif (xPos >= 250 + (55 * 4)) and (xPos <= 250 + (55 * 4) + 50) and (yPos >= 90) and (yPos <= 90 + 50):
                    self.__recipeMaker.clickGroups5Button()
                                    
                    # Le avisamos al tutorial que avance al siguiente paso
                    self.__tutorialManager.nextStep(7)
                    
                elif (xPos >= 250 + (55 * 5)) and (xPos <= 250 + (55 * 5) + 50) and (yPos >= 90) and (yPos <= 90 + 50):
                    self.__recipeMaker.clickGroups6Button()
                elif (xPos >= 250 + (55 * 6)) and (xPos <= 250 + (55 * 6) + 50) and (yPos >= 90) and (yPos <= 90 + 50):
                    self.__recipeMaker.clickGroups7Button()
                elif (xPos >= 250 + (55 * 7)) and (xPos <= 250 + (55 * 7) + 50) and (yPos >= 90) and (yPos <= 90 + 50):
                    self.__recipeMaker.clickGroups8Button()
                    
                # Available Items
                elif (xPos >= 220) and (xPos <= 328) and (yPos >= 210) and (yPos <= 320):
                    self.__recipeMaker.clickAvailableItem1()
                elif (xPos >= 220) and (xPos <= 328) and (yPos >= 330) and (yPos <= 440):
                    self.__recipeMaker.clickAvailableItem2()
                    
                    # Le avisamos al tutorial que avance al siguiente paso
                    self.__tutorialManager.nextStep(8)
                    
                elif (xPos >= 220) and (xPos <= 328) and (yPos >= 450) and (yPos <= 560):
                    self.__recipeMaker.clickAvailableItem3()

            elif self.__recipeMaker.getCurrentTab() == eIngredientsTab.RECIPES:
                
                # Letters
                if (xPos >= 263) and (xPos <= 290) and (yPos >= 86) and (yPos <= 86 + 32):
                    self.__recipeMaker.clickLetter('A')
                    self.__tutorialManager.nextStep(13) # Le avisamos al tutorial que avance al siguiente paso
                elif (xPos >= 290) and (xPos <= 320) and (yPos >= 86) and (yPos <= 86 + 32):
                    self.__recipeMaker.clickLetter('B')
                    self.__tutorialManager.nextStep(13)
                elif (xPos >= 320) and (xPos <= 350) and (yPos >= 86) and (yPos <= 86 + 32):
                    self.__recipeMaker.clickLetter('C')
                    self.__tutorialManager.nextStep(13)
                elif (xPos >= 350) and (xPos <= 378) and (yPos >= 86) and (yPos <= 86 + 32):
                    self.__recipeMaker.clickLetter('D')
                    self.__tutorialManager.nextStep(13)
                elif (xPos >= 378) and (xPos <= 407) and (yPos >= 86) and (yPos <= 86 + 32):
                    self.__recipeMaker.clickLetter('E')
                    self.__tutorialManager.nextStep(13)
                elif (xPos >= 407) and (xPos <= 436) and (yPos >= 86) and (yPos <= 86 + 32):
                    self.__recipeMaker.clickLetter('F')
                    self.__tutorialManager.nextStep(13)
                elif (xPos >= 436) and (xPos <= 465) and (yPos >= 86) and (yPos <= 86 + 32):
                    self.__recipeMaker.clickLetter('G')
                    self.__tutorialManager.nextStep(13)
                elif (xPos >= 465) and (xPos <= 494) and (yPos >= 86) and (yPos <= 86 + 32):
                    self.__recipeMaker.clickLetter('H')
                    self.__tutorialManager.nextStep(13)
                elif (xPos >= 494) and (xPos <= 522) and (yPos >= 86) and (yPos <= 86 + 32):
                    self.__recipeMaker.clickLetter('I')
                    self.__tutorialManager.nextStep(13)
                elif (xPos >= 522) and (xPos <= 548) and (yPos >= 86) and (yPos <= 86 + 32):
                    self.__recipeMaker.clickLetter('J')
                    self.__tutorialManager.nextStep(13)
                elif (xPos >= 548) and (xPos <= 577) and (yPos >= 86) and (yPos <= 86 + 32):
                    self.__recipeMaker.clickLetter('K')
                    self.__tutorialManager.nextStep(13)
                elif (xPos >= 577) and (xPos <= 609) and (yPos >= 86) and (yPos <= 86 + 32):
                    self.__recipeMaker.clickLetter('L')
                    self.__tutorialManager.nextStep(13)
                elif (xPos >= 609) and (xPos <= 644) and (yPos >= 86) and (yPos <= 86 + 32):
                    self.__recipeMaker.clickLetter('M')
                    self.__tutorialManager.nextStep(13)
                elif (xPos >= 644) and (xPos <= 674) and (yPos >= 86) and (yPos <= 86 + 32):
                    self.__recipeMaker.clickLetter('N')
                    self.__tutorialManager.nextStep(13)
                elif (xPos >= 272) and (xPos <= 298) and (yPos >= 117) and (yPos <= 117 + 32):
                    self.__recipeMaker.clickLetter('Ñ')
                    self.__tutorialManager.nextStep(13)
                elif (xPos >= 298) and (xPos <= 332) and (yPos >= 117) and (yPos <= 117 + 32):
                    self.__recipeMaker.clickLetter('O')
                    self.__tutorialManager.nextStep(13)
                elif (xPos >= 332) and (xPos <= 363) and (yPos >= 117) and (yPos <= 117 + 32):
                    self.__recipeMaker.clickLetter('P')
                    self.__tutorialManager.nextStep(13)
                elif (xPos >= 363) and (xPos <= 393) and (yPos >= 117) and (yPos <= 117 + 32):
                    self.__recipeMaker.clickLetter('Q')
                    self.__tutorialManager.nextStep(13)
                elif (xPos >= 393) and (xPos <= 424) and (yPos >= 117) and (yPos <= 117 + 32):
                    self.__recipeMaker.clickLetter('R')
                    self.__tutorialManager.nextStep(13)
                elif (xPos >= 424) and (xPos <= 455) and (yPos >= 117) and (yPos <= 117 + 32):
                    self.__recipeMaker.clickLetter('S')
                    self.__tutorialManager.nextStep(13)
                elif (xPos >= 455) and (xPos <= 485) and (yPos >= 117) and (yPos <= 117 + 32):
                    self.__recipeMaker.clickLetter('T')
                    self.__tutorialManager.nextStep(13)
                elif (xPos >= 485) and (xPos <= 514) and (yPos >= 117) and (yPos <= 117 + 32):
                    self.__recipeMaker.clickLetter('U')
                    self.__tutorialManager.nextStep(13)
                elif (xPos >= 514) and (xPos <= 546) and (yPos >= 117) and (yPos <= 117 + 32):
                    self.__recipeMaker.clickLetter('V')
                    self.__tutorialManager.nextStep(13)
                elif (xPos >= 546) and (xPos <= 582) and (yPos >= 117) and (yPos <= 117 + 32):
                    self.__recipeMaker.clickLetter('W')
                    self.__tutorialManager.nextStep(13)
                elif (xPos >= 582) and (xPos <= 617) and (yPos >= 117) and (yPos <= 117 + 32):
                    self.__recipeMaker.clickLetter('X')
                    self.__tutorialManager.nextStep(13)
                elif (xPos >= 617) and (xPos <= 649) and (yPos >= 117) and (yPos <= 117 + 32):
                    self.__recipeMaker.clickLetter('Y')
                    self.__tutorialManager.nextStep(13)
                elif (xPos >= 649) and (xPos <= 678) and (yPos >= 117) and (yPos <= 117 + 32):
                    self.__recipeMaker.clickLetter('Z')
                    self.__tutorialManager.nextStep(13)
                    
        elif self.__state == eRestaurantState.TRIVIA:
            
            # Answer 1    
            if (xPos >= 0) and (xPos <= 400) and (yPos >= 150) and (yPos <= 150 + 574):
                self.__triviaManager.clickOnAnswer(eQuestionAnswer.ANSWER_A)
            # Answer 2
            elif (xPos >= 400) and (xPos <= 800) and (yPos >= 150) and (yPos <= 150 + 574):
                self.__triviaManager.clickOnAnswer(eQuestionAnswer.ANSWER_B)
            # Answer 3
            elif (xPos >= 800) and (xPos <= 1200) and (yPos >= 150) and (yPos <= 150 + 574):
                self.__triviaManager.clickOnAnswer(eQuestionAnswer.ANSWER_C)
            
    def __doKeyAction(self, event):
        
        if event.key == pygame.K_LEFT:
            self.__chef.startDancing()
            pass
        
        elif event.key == pygame.K_RIGHT:
            self.__chef.startDancing()
            pass
        
        elif event.key == pygame.K_UP:
            self.__chef.startDancing()
            pass
        
        elif event.key == pygame.K_DOWN:
            self.__chef.startDancing()
            pass

    def __getClientById(self, clientId):
        for client in self.__clients:
            if client.id == clientId:
                return client 

    def __resetHover(self):
        
        self.__hoverCloseGame = False
        self.__hoverCancel = False
        
        index = 0
        while index < len(self.__hoverTriviaManager):
            self.__hoverTriviaManager[index] = False
            index = index + 1
      
        index = 0
        while index < len(self.__hoverOrderAssignment):
            self.__hoverOrderAssignment[index] = False
            index = index + 1
        
        index = 0
        while index < len(self.__hoverOrderSelection):
            self.__hoverOrderSelection[index] = False
            index = index + 1
      
        index = 0
        while index < len(self.__hoverRecipeMaker):
            self.__hoverRecipeMaker[index] = False
            index = index + 1            


class TextBox:

    def __init__(self, posX, posY, width, maxChars, font, isPassword):
        
        self.__posX = posX
        self.__posY = posY
        
        self.__focusBorderColor = (255, 255, 0)
        self.__normalBorderColor = (48, 116, 135)
        self.__contentColor = (147, 212, 192)
        self.__textColor = (38, 95, 110)
        
        self.__textReal = Label("", font, self.__textColor, (posX, posY))
        self.__textPassword = Label("", font, self.__textColor, (posX, posY))
        
        self.__maxChars = maxChars
        self.__focus = False
        self.__uppercase = False
        self.__isPassword = isPassword
        
        if font == FontController.font10:
            fontValue = 10
        elif font == FontController.font15:
            fontValue = 15
        elif font == FontController.font20:
            fontValue = 20
        elif font == FontController.font25:
            fontValue = 25
        elif font == FontController.font27:
            fontValue = 27
        elif font == FontController.font30:
            fontValue = 30
        elif font == FontController.font35:
            fontValue = 35
        elif font == FontController.font40:
            fontValue = 40
            
        self.__height = fontValue * 1.5
        self.__width = width
        
        self.__normalBorderWidth = 4
        self.__focusBorderWidth = self.__normalBorderWidth * 2
        
    def getText(self):
        return self.__textReal.text
        
    def doTask(self):
        pass
    
    def doPaint(self, displaySurface):
        
        # Borde de Foco
        if self.__focus == True:
            pygame.draw.rect(displaySurface, self.__focusBorderColor, pygame.Rect(self.__posX - self.__focusBorderWidth, self.__posY - self.__focusBorderWidth, self.__width + (self.__focusBorderWidth * 2), self.__height + (self.__focusBorderWidth * 2)))
        
        # Borde
        pygame.draw.rect(displaySurface, self.__normalBorderColor, pygame.Rect(self.__posX - self.__normalBorderWidth, self.__posY - self.__normalBorderWidth, self.__width + (self.__normalBorderWidth * 2), self.__height + (self.__normalBorderWidth * 2)))
        
        # Contenido
        pygame.draw.rect(displaySurface, self.__contentColor, pygame.Rect(self.__posX, self.__posY, self.__width, self.__height))
        
        # Texto ingresado
        if self.__isPassword == False:
            self.__textReal.doPaint(displaySurface)
        else:
            self.__textPassword.doPaint(displaySurface)
            
    def takeFocus(self):
        self.__focus = True
    
    def quitFocus(self):
        self.__focus = False

    def doMouseAction(self, event):
        
        # Detectamos la posicion en X y Y del click
        xPos, yPos = event.pos
        
        if (xPos >= self.__posX) and (xPos <= self.__posX + self.__width) and (yPos >= self.__posY) and (yPos <= self.__posY + self.__height):
            self.__focus = True
        else:
            self.__focus = False

    def doKeyAction(self, event):
        if self.__focus == True:

            # Teclas no permitidas                
            if event.key == pygame.K_TAB:
                pass
            elif event.key == pygame.K_CAPSLOCK:
                pass
            elif event.key == pygame.K_RETURN:
                pass
            
            # Eliminacion de un caracter
            elif event.key == pygame.K_BACKSPACE:
                self.__textReal.delLastChar()
                self.__textPassword.delLastChar()
                
            # Letra valida presionada
            elif event.key <= 255 and (self.__textReal.getTextLen() < self.__maxChars):
                
                # Obtenemos la letra
                charToAdd = chr(event.key)
                
                # Mayusculas
                if self.__uppercase == True:
                    charToAdd = charToAdd.upper()
                    # self.__uppercase = False
                
                # Añadimos la letra a la cadena
                self.__textReal.addChar(charToAdd)
                self.__textPassword.addChar("*")
                
    def switchCase(self):
        if self.__uppercase == True:
            self.__uppercase = False
        else:
            self.__uppercase = True
