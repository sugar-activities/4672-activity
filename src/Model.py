#!/usr/bin/python
# -*- coding: latin-1 -*-

"""
Rigoberto Sáenz Imbacuán
Desarrollador para Dispositivos Móviles - Colombia Games
Ingeniero de Sistemas y Computación - Universidad Nacional de Colombia
http://www.rigobertosaenz.com/
"""
from copy import deepcopy
from random import randrange
from src.Controller import eIngredientsTab, eIngredientGroup, FontController, \
    ResourceController, AudioController, eSound, GlobalsController, eCharacterGender, \
    eChefMainState, eMotionBlock, eMotionDirection, eChefServiceState, eChefLevel, \
    eChefCommand, eChefCookingState, eClientServiceState, eMotionRow, eMotionColumn, \
    eClientOrderState, eClientPerson, eRecipeFoodTime, eRecipeId, eIngredientId, \
    eRecipePreparation, eQuestionAnswer, eTriviaQuestionId
import random


class TutorialManager:

    def __init__(self):
        
        # Steps
        self.__step = 0
        self.__originX = 0
        self.__originY = 0
        
        # Image
        self.__messageBackground = None
        self.__transparentTotalTime = 10
        self.__transparentCurrentTime = 1

        # Text
        self.__message1 = Label("" , FontController.font18, (120, 100, 70), (0, 0))
        self.__message2 = Label("" , FontController.font18, (120, 100, 70), (0, 0))
        self.__message3 = Label("" , FontController.font18, (120, 100, 70), (0, 0))
        self.__message4 = Label("" , FontController.font18, (120, 100, 70), (0, 0))
        self.__message5 = Label("" , FontController.font18, (120, 100, 70), (0, 0))
        self.__message6 = Label("" , FontController.font18, (120, 100, 70), (0, 0))
        
        # Inicializamos correctamente las variables anteriores
        self.nextStep(1)
        
    def doPaint(self, displaySurface):
        
        if GlobalsController.SHOW_TUTORIAL == True:
            
            if self.__transparentCurrentTime < self.__transparentTotalTime:
                self.__transparentCurrentTime = self.__transparentCurrentTime + 1
                
                # Background
                displaySurface.blit(ResourceController.background_Transparent, (0, 0))
                
                # Si estamos en el ultimo paso del tutorial
                if self.__step == 22:
                    
                    # Title
                    displaySurface.blit(ResourceController.game_ChefNewLevel, (600 - 310, 50))
                    
                    # Chef
                    if GlobalsController.CHEF_GENDER == eCharacterGender.MALE:
                        displaySurface.blit(ResourceController.input_GenderMale_On, (600 - 195, 150))
                    else:
                        displaySurface.blit(ResourceController.input_GenderFemale_On, (600 - 195, 200))
                        
                    # Finlizamos el tutorial
                    if self.__transparentCurrentTime == self.__transparentTotalTime:
                        GlobalsController.SHOW_TUTORIAL = False
                
            # Message
            displaySurface.blit(self.__messageBackground, (self.__originX, self.__originY))
            self.__message1.doPaint(displaySurface)
            self.__message2.doPaint(displaySurface)
            self.__message3.doPaint(displaySurface)
            self.__message4.doPaint(displaySurface)
            self.__message5.doPaint(displaySurface)
            self.__message6.doPaint(displaySurface)
        
    def nextStep(self, stepWanted):
        
        if GlobalsController.SHOW_TUTORIAL == True:
            
            # Avanzamos al siguiente paso
            if stepWanted == (self.__step + 1):
                self.__step = self.__step + 1
                self.__transparentCurrentTime = 1
                
                # Configuramos todo de acuerdo al nuevo paso
                if self.__step == 1:
                    self.__originX = 170
                    self.__originY = 310
                    self.__messageBackground = ResourceController.game_TutorialStepF
                    self.__message1.setText("Bienvenido(a) al Tutorial, aquí te")
                    self.__message2.setText("enseñaremos como jugar Super Chef.")
                    self.__message3.setText("")
                    self.__message4.setText("Selecciona una mesa ocupada por un")
                    self.__message5.setText("cliente para ofrecerle la lista de")
                    self.__message6.setText("recetas disponibles para el desayuno.")
                    
                elif self.__step == 2:
                    self.__originX = 310
                    self.__originY = 400
                    self.__messageBackground = ResourceController.game_TutorialStepB
                    self.__message1.setText("")
                    self.__message2.setText("Esta es la lista de recetas que le")
                    self.__message3.setText("puedes ofrecer al cliente para el")
                    self.__message4.setText("desayuno.")
                    self.__message5.setText("")
                    self.__message6.setText("Selecciona cualquiera receta.")
                    
                elif self.__step == 3:
                    self.__originX = 240
                    self.__originY = 155
                    self.__messageBackground = ResourceController.game_TutorialStepB
                    self.__message1.setText("Es hora de preparar la receta, pero")
                    self.__message2.setText("antes debemos lavarnos las manos,")
                    self.__message3.setText("así evitamos contraer muchas")
                    self.__message4.setText("enfermedades.")
                    self.__message5.setText("")
                    self.__message6.setText("Selecciona el lavamanos.")
                    
                elif self.__step == 4:
                    self.__originX = 540
                    self.__originY = 200
                    self.__messageBackground = ResourceController.game_TutorialStepB
                    self.__message1.setText("")
                    self.__message2.setText("Ya con las manos limpias, podemos")
                    self.__message3.setText("seleccionar los ingredientes para")
                    self.__message4.setText("preparar la receta.")
                    self.__message5.setText("")
                    self.__message6.setText("Selecciona la nevera.")
                    
                elif self.__step == 5:
                    self.__originX = 580
                    self.__originY = -10
                    self.__messageBackground = ResourceController.game_TutorialStepJ
                    self.__message1.setText("Es posible que tengamos más de una")
                    self.__message2.setText("receta lista para ser preparada, por")
                    self.__message3.setText("lo tanto tenemos que selecionar cuál")
                    self.__message4.setText("vamos a preparar.")
                    self.__message5.setText("")
                    self.__message6.setText("Selecciona la primera receta.")
                    
                elif self.__step == 6:
                    self.__originX = 515
                    self.__originY = 14
                    self.__messageBackground = ResourceController.game_TutorialStepL
                    self.__message1.setText("Éstos botones representan los grupos")
                    self.__message2.setText("alimenticios, si seleccionas uno se")
                    self.__message3.setText("mostrarán los alimentos que")
                    self.__message4.setText("pertenecen al grupo.")
                    self.__message5.setText("")
                    self.__message6.setText("Selecciona el grupo Lácteos.")
                
                elif self.__step == 7:
                    self.__originX = 145
                    self.__originY = 430
                    self.__messageBackground = ResourceController.game_TutorialStepC
                    self.__message1.setText("")
                    self.__message2.setText("Estos son algunos de los alimentos")
                    self.__message3.setText("que pertenecen al grupo Lácteos.")
                    self.__message4.setText("")
                    self.__message5.setText("Selecciona el alimento.")
                    self.__message6.setText("")
                
                elif self.__step == 8:
                    self.__originX = 530
                    self.__originY = 440
                    self.__messageBackground = ResourceController.game_TutorialStepC
                    self.__message1.setText("")
                    self.__message2.setText("Puedes ver los demás alimentos que")
                    self.__message3.setText("pertenecen al grupo alimenticio")
                    self.__message4.setText("utilizando las flechas de navegación.")
                    self.__message5.setText("")
                    self.__message6.setText("Selecciona la flecha derecha.")
                                
                elif self.__step == 9:
                    self.__originX = 50
                    self.__originY = 440
                    self.__messageBackground = ResourceController.game_TutorialStepC
                    self.__message1.setText("")
                    self.__message2.setText("Recuerda utilizar las flechas, sino no")
                    self.__message3.setText("podrás ver todos los alimentos que")
                    self.__message4.setText("componen un grupo alimenticio...")
                    self.__message5.setText("")
                    self.__message6.setText("Selecciona la flecha izquierda.")
                                
                elif self.__step == 10:
                    self.__originX = 705
                    self.__originY = 185
                    self.__messageBackground = ResourceController.game_TutorialStepC
                    self.__message1.setText("Si elegiste un alimento por error,")
                    self.__message2.setText("puedes removerlo de la lista de")
                    self.__message3.setText("alimentos seleccionados, presionando")
                    self.__message4.setText("el botón de eliminación.")
                    self.__message5.setText("")
                    self.__message6.setText("Selecciona el botón con la equis.")
                                                                
                elif self.__step == 11:
                    self.__originX = 470
                    self.__originY = 75
                    self.__messageBackground = ResourceController.game_TutorialStepC
                    self.__message1.setText("Ya sabes COMO elegir los alimentos")
                    self.__message2.setText("necesarios para una receta, ahora")
                    self.__message3.setText("necesitamos saber CUALES deben")
                    self.__message4.setText("ser seleccionados...")
                    self.__message5.setText("")
                    self.__message6.setText("Selecciona la pestaña Recetas.")
                                                                
                elif self.__step == 12:
                    self.__originX = 685
                    self.__originY = 15
                    self.__messageBackground = ResourceController.game_TutorialStepL
                    self.__message1.setText("El índice te ayudará a buscar la")
                    self.__message2.setText("receta a preparar más rapido. Solo")
                    self.__message3.setText("debes buscar y seleccionar la letra")
                    self.__message4.setText("inicial del nombre de la receta.")
                    self.__message5.setText("")
                    self.__message6.setText("Selecciona la letra correspondiente.")
                                
                elif self.__step == 13:
                    self.__originX = 685
                    self.__originY = 295
                    self.__messageBackground = ResourceController.game_TutorialStepL
                    self.__message1.setText("Es posible que más de una receta")
                    self.__message2.setText("comience con la misma letra, por lo")
                    self.__message3.setText("tanto puedes usar las flechas de")
                    self.__message4.setText("navegación para buscarla.")
                    self.__message5.setText("")
                    self.__message6.setText("Selecciona la flecha derecha.")
                                
                elif self.__step == 14:
                    self.__originX = 490
                    self.__originY = 105
                    self.__messageBackground = ResourceController.game_TutorialStepD
                    self.__message1.setText("Cuando hayas encontrado la receta,")
                    self.__message2.setText("debes seleccionar los ingredientes que")
                    self.__message3.setText("la componen. Lo bueno es que ya")
                    self.__message4.setText("sabes como seleccionarlos...")
                    self.__message5.setText("")
                    self.__message6.setText("Selecciona la pestaña Alimentos.")
                                
                elif self.__step == 15:
                    self.__originX = 735
                    self.__originY = 375
                    self.__messageBackground = ResourceController.game_TutorialStepG
                    self.__message1.setText("")
                    self.__message2.setText("Debes ubicar y seleccionar todos los")
                    self.__message3.setText("alimentos de la receta, cuando los")
                    self.__message4.setText("encuentres todos el botón Plato Listo")
                    self.__message5.setText("se activará y deberás seleccionarlo...")
                    self.__message6.setText("")
                                
                elif self.__step == 16:
                    self.__originX = 240
                    self.__originY = 155
                    self.__messageBackground = ResourceController.game_TutorialStepB
                    self.__message1.setText("")
                    self.__message2.setText("Ya tienes los ingredientes listos pero")
                    self.__message3.setText("antes debes lavarlos para evitar que")
                    self.__message4.setText("te enfermen.")
                    self.__message5.setText("")
                    self.__message6.setText("Selecciona el lavamanos.")
                                
                elif self.__step == 17:
                    self.__originX = 60
                    self.__originY = 200
                    self.__messageBackground = ResourceController.game_TutorialStepC
                    self.__message1.setText("Ya tenemos todos los ingredientes")
                    self.__message2.setText("listos, es tiempo de preparar la")
                    self.__message3.setText("receta. Recuerda que el aseo del área")
                    self.__message4.setText("de preparación es importante.")
                    self.__message5.setText("")
                    self.__message6.setText("Selecciona el área de preparación.")
                                
                elif self.__step == 18:
                    self.__originX = 300
                    self.__originY = 0
                    self.__messageBackground = ResourceController.game_TutorialStepL
                    self.__message1.setText("Mientras la receta es preparada")
                    self.__message2.setText("puedes atender a los demás clientes")
                    self.__message3.setText("o simplemente esperar a que ")
                    self.__message4.setText("termine la preparación...")
                    self.__message5.setText("")
                    self.__message6.setText("Selecciona el área de preparación.")
                    
                elif self.__step == 19:
                    self.__originX = 170
                    self.__originY = 310
                    self.__messageBackground = ResourceController.game_TutorialStepF
                    self.__message1.setText("")
                    self.__message2.setText("La receta está lista, ahora debemos")
                    self.__message3.setText("entregarla al cliente que la solicitó.")
                    self.__message4.setText("")
                    self.__message5.setText("Selecciona el cliente que pidió la")
                    self.__message6.setText("receta.")
                    
                elif self.__step == 20:
                    self.__originX = 740
                    self.__originY = 360
                    self.__messageBackground = ResourceController.game_TutorialStepP
                    self.__message1.setText("Mientras el cliente come puedes")
                    self.__message2.setText("atender a otros clientes o puedes")
                    self.__message3.setText("esperar a que termine de comer.")
                    self.__message4.setText("Cuando acabe deberás recoger los")
                    self.__message5.setText("platos sucios...")
                    self.__message6.setText("")
                
                elif self.__step == 21:
                    self.__originX = 680
                    self.__originY = 155
                    self.__messageBackground = ResourceController.game_TutorialStepA
                    self.__message1.setText("Por haber recogido los platos sucios")
                    self.__message2.setText("y haber atendido bien al cliente has")
                    self.__message3.setText("ganado las estrellas que este tenía.")
                    self.__message4.setText("Ahora hay que lavar los platos sucios.")
                    self.__message5.setText("")
                    self.__message6.setText("Selecciona el lavaplatos")
                
                elif self.__step == 22:
                    self.__originX = 10
                    self.__originY = 170
                    self.__messageBackground = ResourceController.game_TutorialStepF
                    self.__message1.setText("")
                    self.__message2.setText("Haz completado el tutorial, ahora")
                    self.__message3.setText("atiende a todos los clientes de tu")
                    self.__message4.setText("restaurante y conviértete en un")
                    self.__message5.setText("Super Chef!!!")
                    self.__message6.setText("")
                
                # Asignamos la nueva posicion a los elementos del proximo paso
                self.__message1.setPosition((self.__originX + 65, self.__originY + 65 + (30 * 0)))
                self.__message2.setPosition((self.__originX + 65, self.__originY + 65 + (25 * 1)))
                self.__message3.setPosition((self.__originX + 65, self.__originY + 65 + (25 * 2)))
                self.__message4.setPosition((self.__originX + 65, self.__originY + 65 + (25 * 3)))
                self.__message5.setPosition((self.__originX + 65, self.__originY + 65 + (25 * 4)))
                self.__message6.setPosition((self.__originX + 65, self.__originY + 65 + (25 * 5)))
            
            
class TriviaManager:
    
    def __init__(self):
        
        self.__optionA_title = Label("Opción 1", FontController.font35, (120, 100, 70), (200 - 90, 250))
        self.__optionA_1 = Label("", FontController.font22, (160, 133, 100), (40, 320 + (28 * 0)))
        self.__optionA_2 = Label("", FontController.font22, (160, 133, 100), (40, 320 + (28 * 1)))
        self.__optionA_3 = Label("", FontController.font22, (160, 133, 100), (40, 320 + (28 * 2)))
        self.__optionA_4 = Label("", FontController.font22, (160, 133, 100), (40, 320 + (28 * 3)))
        self.__optionA_5 = Label("", FontController.font22, (160, 133, 100), (40, 320 + (28 * 4)))
        self.__optionA_6 = Label("", FontController.font22, (160, 133, 100), (40, 320 + (28 * 5)))
        self.__optionA_7 = Label("", FontController.font22, (160, 133, 100), (40, 320 + (28 * 6)))
    
        self.__optionB_title = Label("Opción 2", FontController.font35, (120, 100, 70), (600 - 90, 250))
        self.__optionB_1 = Label("", FontController.font22, (160, 133, 100), (440, 320 + (28 * 0)))
        self.__optionB_2 = Label("", FontController.font22, (160, 133, 100), (440, 320 + (28 * 1)))
        self.__optionB_3 = Label("", FontController.font22, (160, 133, 100), (440, 320 + (28 * 2)))
        self.__optionB_4 = Label("", FontController.font22, (160, 133, 100), (440, 320 + (28 * 3)))
        self.__optionB_5 = Label("", FontController.font22, (160, 133, 100), (440, 320 + (28 * 4)))
        self.__optionB_6 = Label("", FontController.font22, (160, 133, 100), (440, 320 + (28 * 5)))
        self.__optionB_7 = Label("", FontController.font22, (160, 133, 100), (440, 320 + (28 * 6)))
    
        self.__optionC_title = Label("Opción 3", FontController.font35, (120, 100, 70), (1000 - 90, 250))
        self.__optionC_1 = Label("", FontController.font22, (160, 133, 100), (840, 320 + (28 * 0)))
        self.__optionC_2 = Label("", FontController.font22, (160, 133, 100), (840, 320 + (28 * 1)))
        self.__optionC_3 = Label("", FontController.font22, (160, 133, 100), (840, 320 + (28 * 2)))
        self.__optionC_4 = Label("", FontController.font22, (160, 133, 100), (840, 320 + (28 * 3)))
        self.__optionC_5 = Label("", FontController.font22, (160, 133, 100), (840, 320 + (28 * 4)))
        self.__optionC_6 = Label("", FontController.font22, (160, 133, 100), (840, 320 + (28 * 5)))
        self.__optionC_7 = Label("", FontController.font22, (160, 133, 100), (840, 320 + (28 * 6)))
        
        # Message
        self.__messageTitle1 = Label("Haz ganado 5 estrellas", FontController.font40, (255, 255, 0), (0, 300))
        self.__messageTitle1.setPosition((600 - (self.__messageTitle1.getTextRenderLen() / 2), self.__messageTitle1.getPosition()[1]))
        
        self.__messageTitle2 = Label("Recuerda:", FontController.font40, (255, 255, 255), (0, 390))
        self.__messageTitle2.setPosition((600 - (self.__messageTitle2.getTextRenderLen() / 2), self.__messageTitle2.getPosition()[1]))
        
        # Recomendation
        self.__recomendation1 = Label("", FontController.font26, (255, 255, 255), (200, 450 + (34 * 0)))
        self.__recomendation2 = Label("", FontController.font26, (255, 255, 255), (200, 450 + (34 * 1)))
        self.__recomendation3 = Label("", FontController.font26, (255, 255, 255), (200, 450 + (34 * 2)))
        self.__recomendation4 = Label("", FontController.font26, (255, 255, 255), (200, 450 + (34 * 3)))
        
        # Question
        self.__correctAnswer = None
        self.__isSelectedAnswerRight = None
        
        # Time
        self.__currentTime = 1
        self.__totalTime = 50
        
        # Manager Flag
        self.__wasTriviaAnswered = False
    
    def doTask(self):
        if self.__isSelectedAnswerRight == True:
            # Conteo regresivo para desactivar el este manager...
            if self.__currentTime <= self.__totalTime:
                self.__currentTime = self.__currentTime + 1
            else:
                self.__wasTriviaAnswered = True
    
    def doPaint(self, displaySurface, hoverList):
        
        # Background
        displaySurface.blit(ResourceController.background_Transparent, (0, 0))
        
        if self.__isSelectedAnswerRight == True:
            
            # Wood            
            displaySurface.blit(ResourceController.background_Answer, (600 - (966 / 2), 0))
            
            # Congratulation Message
            displaySurface.blit(ResourceController.game_ChefNewLevel, (600 - (620 / 2), 160))
            
            # Message
            self.__messageTitle1.doPaint(displaySurface)
            self.__messageTitle2.doPaint(displaySurface)
            
            # Recomendation
            self.__recomendation1.doPaint(displaySurface)
            self.__recomendation2.doPaint(displaySurface)
            self.__recomendation3.doPaint(displaySurface)
            self.__recomendation4.doPaint(displaySurface)
            
            # Chefs
            displaySurface.blit(ResourceController.input_GenderFemale_Off, (200, 420))
            displaySurface.blit(ResourceController.input_GenderMale_Off, (600, 420))
            
        else:
            # Trivia Text
            displaySurface.blit(ResourceController.game_TriviaTitle, (600 - (270 / 2), 10))
            displaySurface.blit(ResourceController.game_TriviaText, (600 - (1108 / 2), 80))
            
            # Options Background
            if hoverList[0] == True:
                displaySurface.blit(ResourceController.input_TriviaOption_On, (200 - (390 / 2), 150))
            else:
                displaySurface.blit(ResourceController.input_TriviaOption_Off, (200 - (390 / 2), 150))
            
            if hoverList[1] == True:
                displaySurface.blit(ResourceController.input_TriviaOption_On, (600 - (390 / 2), 150))
            else:
                displaySurface.blit(ResourceController.input_TriviaOption_Off, (600 - (390 / 2), 150))
                
            if hoverList[2] == True:
                displaySurface.blit(ResourceController.input_TriviaOption_On, (1000 - (390 / 2), 150))
            else:
                displaySurface.blit(ResourceController.input_TriviaOption_Off, (1000 - (390 / 2), 150))
                
            # Options Text
            self.__optionA_title.doPaint(displaySurface)
            self.__optionA_1.doPaint(displaySurface)
            self.__optionA_2.doPaint(displaySurface)
            self.__optionA_3.doPaint(displaySurface)
            self.__optionA_4.doPaint(displaySurface)
            self.__optionA_5.doPaint(displaySurface)
            self.__optionA_6.doPaint(displaySurface)
            self.__optionA_7.doPaint(displaySurface)
    
            self.__optionB_title.doPaint(displaySurface)
            self.__optionB_1.doPaint(displaySurface)
            self.__optionB_2.doPaint(displaySurface)
            self.__optionB_3.doPaint(displaySurface)
            self.__optionB_4.doPaint(displaySurface)
            self.__optionB_5.doPaint(displaySurface)
            self.__optionB_6.doPaint(displaySurface)
            self.__optionB_7.doPaint(displaySurface)
            
            self.__optionC_title.doPaint(displaySurface)
            self.__optionC_1.doPaint(displaySurface)
            self.__optionC_2.doPaint(displaySurface)
            self.__optionC_3.doPaint(displaySurface)
            self.__optionC_4.doPaint(displaySurface)
            self.__optionC_5.doPaint(displaySurface)
            self.__optionC_6.doPaint(displaySurface)
            self.__optionC_7.doPaint(displaySurface)
    
    def doReset(self, foodTime):
        
        # Cargamos la lista de trivias de acuerdo al tiempo de comida
        allTrivias = None
        
        if foodTime == eRecipeFoodTime.BREAKFAST:
            allTrivias = InformationTrivias.breakfastTrivia
        elif foodTime == eRecipeFoodTime.DINNER:
            allTrivias = InformationTrivias.dinnerTrivia
        elif foodTime == eRecipeFoodTime.LUNCH:
            allTrivias = InformationTrivias.lunchTrivia
        else:
            allTrivias = InformationTrivias.refreshmentTrivia
            
        # Cargamos un trivia de manera aleatoria    
        selectedTrivia = random.choice(allTrivias)
        
        # Cargamos toda su informacion
        self.__optionA_1.setText(selectedTrivia.optionA[0])
        self.__optionA_2.setText(selectedTrivia.optionA[1])
        self.__optionA_3.setText(selectedTrivia.optionA[2])
        self.__optionA_4.setText(selectedTrivia.optionA[3])
        self.__optionA_5.setText(selectedTrivia.optionA[4])
        self.__optionA_6.setText(selectedTrivia.optionA[5])
        self.__optionA_7.setText(selectedTrivia.optionA[6])

        self.__optionB_1.setText(selectedTrivia.optionB[0])
        self.__optionB_2.setText(selectedTrivia.optionB[1])
        self.__optionB_3.setText(selectedTrivia.optionB[2])
        self.__optionB_4.setText(selectedTrivia.optionB[3])
        self.__optionB_5.setText(selectedTrivia.optionB[4])
        self.__optionB_6.setText(selectedTrivia.optionB[5])
        self.__optionB_7.setText(selectedTrivia.optionB[6])

        self.__optionC_1.setText(selectedTrivia.optionC[0])
        self.__optionC_2.setText(selectedTrivia.optionC[1])
        self.__optionC_3.setText(selectedTrivia.optionC[2])
        self.__optionC_4.setText(selectedTrivia.optionC[3])
        self.__optionC_5.setText(selectedTrivia.optionC[4])
        self.__optionC_6.setText(selectedTrivia.optionC[5])
        self.__optionC_7.setText(selectedTrivia.optionC[6])
        
        self.__recomendation1.setText(selectedTrivia.recomendation[0])
        self.__recomendation1.setPosition((600 - (self.__recomendation1.getTextRenderLen() / 2), self.__recomendation1.getPosition()[1]))
        
        self.__recomendation2.setText(selectedTrivia.recomendation[1])
        self.__recomendation2.setPosition((600 - (self.__recomendation2.getTextRenderLen() / 2), self.__recomendation2.getPosition()[1]))
        
        self.__recomendation3.setText(selectedTrivia.recomendation[2])
        self.__recomendation3.setPosition((600 - (self.__recomendation3.getTextRenderLen() / 2), self.__recomendation3.getPosition()[1]))
        
        self.__recomendation4.setText(selectedTrivia.recomendation[3])
        self.__recomendation4.setPosition((600 - (self.__recomendation4.getTextRenderLen() / 2), self.__recomendation4.getPosition()[1]))
        
        # Question
        self.__correctAnswer = selectedTrivia.answer
        self.__isSelectedAnswerRight = None
        
        # Time
        self.__currentTime = 1
        
        # Manager Flag
        self.__wasTriviaAnswered = False
        
    def wasTriviaAnswered(self):
        return self.__wasTriviaAnswered
    
    def clickOnAnswer(self, selectedAnswer):
        
        if self.__isSelectedAnswerRight != True:
        
            if self.__correctAnswer == selectedAnswer:
                
                self.__isSelectedAnswerRight = True
                
                # Sonido de Victoria
                AudioController.stopMusic()
                AudioController.playSound(eSound.LEVEL_PASSED, 1)
                
            else:
                self.__isSelectedAnswerRight = False
                
                # Sonido de error
                AudioController.playSound(eSound.INGREDIENT_DELETE, 2)


class OrderAssigner:

    def __init__(self):
        
        # Control
        self.__currentFoodTime = None
        self.__orderWasSelected = False
        self.__selectedOrder = None
        self.__availableRecipes = None
        self.__disabledRecipes = None
        
        # Labels
        self.__title = Label("Lista de recetas adecuadas para el", FontController.font28, (120, 100, 70), (245, 100))
        self.__recipeName = Label("", FontController.font20, (160, 133, 100), (245, 155))
        
    def doTask(self):
        pass

    def doPaint(self, displaySurface, hoverList):
        
        # Background
        displaySurface.blit(ResourceController.background_Transparent, (0, 0))
        displaySurface.blit(ResourceController.background_RecipeAssign, (600 - 410, (825 / 2) - 340))
        
        # Limpiamos el nombre de la receta actual
        self.__recipeName.setText("")
        
        # Pintamos todas las recetas disponibles segun el tiempo de comida actual
        xPos = 0
        yPos = 0
        
        index = 0
        while index < len(self.__availableRecipes):
            
            if (index >= 0) and (index < 8):
                xPos = index * 95
            elif (index >= 8) and (index < 16):
                factorX = index - (8 * 1)
                xPos = factorX * 95
            elif (index >= 16) and (index < 24):
                factorX = index - (8 * 2)
                xPos = factorX * 95
            elif (index >= 24) and (index < 32):
                factorX = index - (8 * 3)
                xPos = factorX * 95
            elif (index >= 32) and (index < 40):
                factorX = index - (8 * 4)
                xPos = factorX * 95
            
            if index == (8 * 1):
                yPos = 100 * 1
            elif index == (8 * 2):
                yPos = 100 * 2
            elif index == (8 * 3):
                yPos = 100 * 3
            elif index == (8 * 4):
                yPos = 100 * 4
            elif index == (8 * 5):
                yPos = 100 * 5

            # Determinamos si el indice actual corresponde a una receta desabilitada o no
            isDisabled = True                
            try:
                self.__disabledRecipes.index(index)
            except:
                # Ocurre una excepcion si el indice no corresponde a una receta desabilitada
                isDisabled = False
                
            if isDisabled == False:
                # Image
                displaySurface.blit(self.__availableRecipes[index].image, (xPos + 240, yPos + 210))
            else:
                # Disabled Image
                displaySurface.blit(self.__availableRecipes[index].imageDisabled, (xPos + 240, yPos + 210))
                
            # Hover
            if hoverList[index] == True:
                
                # Hover Selector
                displaySurface.blit(ResourceController.input_AssignSelector, (xPos + 240 - 15, yPos + 210 - 15))
                
                # Recipe Name
                self.__recipeName.setText(self.__availableRecipes[index].name)
                
            index = index + 1
            
        self.__title.doPaint(displaySurface)
        self.__recipeName.doPaint(displaySurface)
            
    def doReset(self):
        self.__currentFoodTime = None
        self.__orderWasSelected = False
        self.__selectedOrder = None
        self.__availableRecipes = None
        self.__disabledRecipes = None 
    
    def wasOrderSelected(self):
        return self.__orderWasSelected
    
    def clickOnOrder(self, orderNo):
        
        # Si esta dentro de la lista de ordenes disponibles
        if orderNo <= len(self.__availableRecipes):
            
            # Determinamos si el indice actual corresponde a una receta desabilitada o no
            isDisabled = True                
            try:
                self.__disabledRecipes.index(orderNo - 1)
                
            except:
                # Ocurre una excepcion si el indice no corresponde a una receta desabilitada
                isDisabled = False

            # Si la receta no esta desabilitada
            if isDisabled == False:
            
                # Referenciamos la orden seleccionada
                self.__selectedOrder = self.__availableRecipes[orderNo - 1]
                
                # Alzamos la bandera correspondiente
                self.__orderWasSelected = True
    
    def setRecipeFoodTime(self, currentFoodTime, activeClients):
        
        # Guardamos el tiempo de comida actual
        self.__currentFoodTime = currentFoodTime
        
        # Creamos una lista solo con las recetas que pertenezcan a la franja horaria actual
        self.__availableRecipes = list()
        for recipeToCheck in InformationRecipes.allRecipesList:
            
            recipeOnTimeZone = False
            for foodTime in recipeToCheck.foodTimes:
                if foodTime == self.__currentFoodTime:
                    recipeOnTimeZone = True
                    break
            
            if recipeOnTimeZone == True:
                self.__availableRecipes.append(recipeToCheck)
            
        # Determinamos la lista de recetas que no se pueden seleccionar porque ya estan seleccionadas por clientes activos
        self.__disabledRecipes = list()
        
        for activeClient in activeClients:
            try:
                # Buscamos el indice de las receta asignada al cliente activo actual
                index = self.__availableRecipes.index(activeClient.getRecipeWanted())
                
                # Si dicho indice es encontrado, lo agregamos a la lista de recetas a mostrar como desabilitadas
                self.__disabledRecipes.append(index)
                
            except:
                # Ocurre una excepcion si los clientes tienen asignadas recetas de la zona horaria anterior
                pass
            
        # Modificamos el titulo de acuerdo al tiempo de comida actual
        if self.__currentFoodTime == eRecipeFoodTime.REFRESHMENT_AFTERNOON:
            self.__title.setText("Lista de recetas adecuadas para las")
        elif self.__currentFoodTime == eRecipeFoodTime.DINNER:
            self.__title.setText("Lista de recetas adecuadas para la")
        else:
            self.__title.setText("Lista de recetas adecuadas para el")

    def getSelectedOrder(self):
        return self.__selectedOrder


class OrderSelector:

    def __init__(self):
        self.__clientsWithActiveOrders = list()
        self.__selectedClient = None
        self.__orderSelected = False
        
        # Labels
        self.__textPerson = Label("Selecciona la orden a atender:", FontController.font25, (120, 100, 70), (160, 50))
        self.__recipeName = Label("", FontController.font18, (160, 133, 100), (0, 0))
        self.__messageTitle = Label("Los alimentos nos aportan:", FontController.font25, (255, 255, 0), (820, 325))
        self.__message1 = Label("", FontController.font22, (255, 255, 255), (800, 350 + (24 * 1)))
        self.__message2 = Label("", FontController.font22, (255, 255, 255), (800, 350 + (24 * 2)))
        self.__message3 = Label("", FontController.font22, (255, 255, 255), (800, 350 + (24 * 3)))
        self.__message4 = Label("", FontController.font22, (255, 255, 255), (800, 350 + (24 * 4)))
        self.__message5 = Label("", FontController.font22, (255, 255, 255), (800, 350 + (24 * 5)))
        self.__message6 = Label("", FontController.font22, (255, 255, 255), (800, 350 + (24 * 6)))
        
        # Message
        self.__changeMessage()
            
    def doTask(self):
        pass

    def doPaint(self, displaySurface, hoverList):
        
        # Background
        displaySurface.blit(ResourceController.background_Transparent, (0, 0))
        
        # Orders List Back
        displaySurface.blit(ResourceController.background_SelectOrder, (100, -15))
        
        # Title
        self.__textPerson.doPaint(displaySurface)
        
        # Message
        if GlobalsController.CHEF_GENDER == eCharacterGender.MALE:
            displaySurface.blit(ResourceController.game_MessageBackground_Male, (580, 180))
        else:
            displaySurface.blit(ResourceController.game_MessageBackground_Female, (580, 180))

        self.__messageTitle.doPaint(displaySurface)
        self.__message1.doPaint(displaySurface)
        self.__message2.doPaint(displaySurface)
        self.__message3.doPaint(displaySurface)
        self.__message4.doPaint(displaySurface)
        self.__message5.doPaint(displaySurface)
        self.__message6.doPaint(displaySurface)    
        
        # Orders List Items
        index = 0
        xPos = 160
        yPos = 100
        
        for client in self.__clientsWithActiveOrders:
            
            recipeWanted = client.getRecipeWanted()
            if recipeWanted != None:
                
                # Image
                displaySurface.blit(recipeWanted.getImage(), (xPos, yPos + (85 * index)))
                
                # Text
                self.__recipeName.setText(recipeWanted.getName())
                self.__recipeName.setPosition((xPos + 80, yPos + (85 * index) + 20))
                self.__recipeName.doPaint(displaySurface)
                
                # Hover
                if hoverList[index] == True:
                    displaySurface.blit(ResourceController.input_OrderSelector, (xPos - 10, yPos + (85 * index) - 5))
                    
                index = index + 1
                
    def doUpdateImage(self):
        pass
            
    def doReset(self):
        self.__orderSelected = False
        self.__clientsWithActiveOrders = list()
        self.__changeMessage()
            
    def __changeMessage(self):
        self.messageId = random.randint(0, 3)
        if self.messageId == 0:
            self.__message1.setText("Energía: Que el organismo")
            self.__message2.setText("necesita para desarrollar las")
            self.__message3.setText("actividades diarias como")
            self.__message4.setText("estudiar, correr, caminar")
            self.__message5.setText("y leer.")
            self.__message6.setText("")
        elif self.messageId == 1:
            self.__message1.setText("Proteínas: Que ayudan en la")
            self.__message2.setText("formación de huesos, tejidos, y")
            self.__message3.setText("sangre.")
            self.__message4.setText("")
            self.__message5.setText("")
            self.__message6.setText("")
        elif self.messageId == 2:
            self.__message1.setText("Minerales: Que cumplen")
            self.__message2.setText("funciones de formación de")
            self.__message3.setText("tejidos como la sangre y los")
            self.__message4.setText("huesos, también facilitan el")
            self.__message5.setText("aprovechamiento de sustancias")
            self.__message6.setText("benéficas.")
        elif self.messageId == 3:
            self.__message1.setText("Vitaminas: Sson sustancias")
            self.__message2.setText("muy valiosas para el organismo.")
            self.__message3.setText("Ayudan en la construcción del")
            self.__message4.setText("sistema de defensas, y asi")
            self.__message5.setText("protegen el cuerpo contra")
            self.__message6.setText("muchas enfermedades.")

    def setClientsWithActiveOrders(self, clientsWithActiveOrders):
        self.__clientsWithActiveOrders = clientsWithActiveOrders
    
    def wasOrderSelected(self):
        return self.__orderSelected
    
    def getSelectedClient(self):
        return self.__selectedClient
        
    def clickOrder1(self):
        if len(self.__clientsWithActiveOrders) >= 1:
            self.__selectedClient = self.__clientsWithActiveOrders[0]
            self.__orderSelected = True
        
    def clickOrder2(self):
        if len(self.__clientsWithActiveOrders) >= 2:
            self.__selectedClient = self.__clientsWithActiveOrders[1]
            self.__orderSelected = True
        
    def clickOrder3(self):
        if len(self.__clientsWithActiveOrders) >= 3:
            self.__selectedClient = self.__clientsWithActiveOrders[2]
            self.__orderSelected = True
        
    def clickOrder4(self):
        if len(self.__clientsWithActiveOrders) >= 4:
            self.__selectedClient = self.__clientsWithActiveOrders[3]
            self.__orderSelected = True
        
    def clickOrder5(self):
        if len(self.__clientsWithActiveOrders) >= 5:
            self.__selectedClient = self.__clientsWithActiveOrders[4]
            self.__orderSelected = True
        
    def clickOrder6(self):
        if len(self.__clientsWithActiveOrders) >= 6:
            self.__selectedClient = self.__clientsWithActiveOrders[5]
            self.__orderSelected = True
                
    def clickOrder7(self):
        if len(self.__clientsWithActiveOrders) >= 7:
            self.__selectedClient = self.__clientsWithActiveOrders[6]
            self.__orderSelected = True
                
    def clickOrder8(self):
        if len(self.__clientsWithActiveOrders) >= 8:
            self.__selectedClient = self.__clientsWithActiveOrders[7]
            self.__orderSelected = True


class RecipeMaker:

    def __init__(self):
        
        # Ingredients
        self.__selectedIngredients = list()
        
        # Flags
        self.__ingredientsMakeRecipe = False
        self.__dishReadyButtonClicked = False
        
        # Selection
        self.__selectedClient = None
        
        # GUI Control
        self.__currentTab = eIngredientsTab.INGREDIENTS
        self.__currentIngredientGroup = eIngredientGroup.GROUP_1_CEREALES
        self.__currentIngredientPage = 0
        self.__currentRecipesPage = 0
        self.__noOfItemsToShow = 3
        
        # Selected Recipe
        self.__recipeToPrepare1 = Label("Receta a preparar:" , FontController.font20, (255, 255, 255), (710, 610))
        self.__recipeToPrepare2 = Label("" , FontController.font25, (255, 255, 0), (710, 600 + 50))
        
        # Ingredients Text
        self.__groupNumber = Label("" , FontController.font18, (255, 255, 255), (225, 145))
        self.__groupName = Label("" , FontController.font28, (255, 255, 0), (225, 165))
        self.__itemName = Label("" , FontController.font25, (235, 235, 235), (0, 0))
        self.__itemNutrition = Label("" , FontController.font20, (200, 200, 200), (0, 0))
        self.__totalNutrition = Label("" , FontController.font30, (255, 255, 255), (730, 590))
        self.__totalVariety = Label("" , FontController.font30, (255, 255, 255), (730, 600 + 50))
        
        # Last Selected Ingredient
        self.__lastSelectedIngredientName = Label("" , FontController.font25, (120, 100, 70), (255, 585))
        self.__lastSelectedIngredientLine1 = Label("" , FontController.font20, (160, 133, 100), (255, 600 + (25 * 1)))
        self.__lastSelectedIngredientLine2 = Label("" , FontController.font20, (160, 133, 100), (255, 600 + (25 * 2)))
        self.__lastSelectedIngredientLine3 = Label("" , FontController.font20, (160, 133, 100), (255, 600 + (25 * 3)))
        self.__lastSelectedIngredientLine4 = Label("" , FontController.font20, (160, 133, 100), (255, 600 + (25 * 4)))
        self.__lastSelectedIngredientLine5 = Label("" , FontController.font20, (160, 133, 100), (255, 600 + (25 * 5)))
        self.__lastSelectedIngredientLine6 = Label("" , FontController.font20, (160, 133, 100), (255, 600 + (25 * 6)))
        self.__lastSelectedIngredientLine7 = Label("" , FontController.font20, (160, 133, 100), (255, 600 + (25 * 7)))
        
        # Current Recipe
        self.__recipeName = Label("" , FontController.font21, (120, 100, 70), (230, 180))
        
        self.__recipeIngredient1 = Label("" , FontController.font20, (160, 133, 100), (230, 220 + (26 * 0)))
        self.__recipeIngredient2 = Label("" , FontController.font20, (160, 133, 100), (230, 220 + (26 * 1)))
        self.__recipeIngredient3 = Label("" , FontController.font20, (160, 133, 100), (230, 220 + (26 * 2)))
        self.__recipeIngredient4 = Label("" , FontController.font20, (160, 133, 100), (230, 220 + (26 * 3)))
        self.__recipeIngredient5 = Label("" , FontController.font20, (160, 133, 100), (230, 220 + (26 * 4)))
        self.__recipeIngredient6 = Label("" , FontController.font20, (160, 133, 100), (230, 220 + (26 * 5)))
        self.__recipeIngredient7 = Label("" , FontController.font20, (160, 133, 100), (230, 220 + (26 * 6)))
        self.__recipeIngredient8 = Label("" , FontController.font20, (160, 133, 100), (230, 220 + (26 * 7)))
        self.__recipeIngredient9 = Label("" , FontController.font20, (160, 133, 100), (230, 220 + (26 * 8)))
        
        self.__recipeDescriptionLine1 = Label("" , FontController.font20, (160, 133, 100), (230, 460 + (26 * 0)))
        self.__recipeDescriptionLine2 = Label("" , FontController.font20, (160, 133, 100), (230, 460 + (26 * 1)))
        self.__recipeDescriptionLine3 = Label("" , FontController.font20, (160, 133, 100), (230, 460 + (26 * 2)))
        self.__recipeDescriptionLine4 = Label("" , FontController.font20, (160, 133, 100), (230, 460 + (26 * 3)))
        self.__recipeDescriptionLine5 = Label("" , FontController.font20, (160, 133, 100), (230, 460 + (26 * 4)))
        self.__recipeDescriptionLine6 = Label("" , FontController.font20, (160, 133, 100), (230, 460 + (26 * 5)))
        self.__recipeDescriptionLine7 = Label("" , FontController.font20, (160, 133, 100), (230, 460 + (26 * 6)))
        self.__recipeDescriptionLine8 = Label("" , FontController.font20, (160, 133, 100), (230, 460 + (26 * 7)))
        self.__recipeDescriptionLine9 = Label("" , FontController.font20, (160, 133, 100), (230, 460 + (26 * 8)))
        self.__recipeDescriptionLine10 = Label("" , FontController.font20, (160, 133, 100), (230, 460 + (26 * 9)))
        self.__recipeDescriptionLine11 = Label("" , FontController.font20, (160, 133, 100), (230, 460 + (26 * 10)))
        self.__recipeDescriptionLine12 = Label("" , FontController.font20, (160, 133, 100), (230, 460 + (26 * 11)))
        
        self.doUpdateImage()
        
    def doUpdateImage(self):
        
        # Contenido de la receta
        recipeToShow = InformationRecipes.allRecipesList[self.__currentRecipesPage]
        
        self.__recipeImage = recipeToShow.image
        
        self.__recipeName.setText(recipeToShow.name)
        
        if recipeToShow.ingredients[0] != None:
            self.__recipeIngredient1.setText("- " + recipeToShow.ingredients[0].name)
        else:
            self.__recipeIngredient1.setText("")
            
        if recipeToShow.ingredients[1] != None:
            self.__recipeIngredient2.setText("- " + recipeToShow.ingredients[1].name)
        else:
            self.__recipeIngredient2.setText("")
            
        if recipeToShow.ingredients[2] != None:
            self.__recipeIngredient3.setText("- " + recipeToShow.ingredients[2].name)
        else:
            self.__recipeIngredient3.setText("")
            
        if recipeToShow.ingredients[3] != None:
            self.__recipeIngredient4.setText("- " + recipeToShow.ingredients[3].name)
        else:
            self.__recipeIngredient4.setText("")
            
        if recipeToShow.ingredients[4] != None:
            self.__recipeIngredient5.setText("- " + recipeToShow.ingredients[4].name)
        else:
            self.__recipeIngredient5.setText("")
            
        if recipeToShow.ingredients[5] != None:
            self.__recipeIngredient6.setText("- " + recipeToShow.ingredients[5].name)
        else:
            self.__recipeIngredient6.setText("")
            
        if recipeToShow.ingredients[6] != None:
            self.__recipeIngredient7.setText("- " + recipeToShow.ingredients[6].name)
        else:
            self.__recipeIngredient7.setText("")
            
        if recipeToShow.ingredients[7] != None:
            self.__recipeIngredient8.setText("- " + recipeToShow.ingredients[7].name)
        else:
            self.__recipeIngredient8.setText("")
            
        if recipeToShow.ingredients[8] != None:
            self.__recipeIngredient9.setText("- " + recipeToShow.ingredients[8].name)
        else:
            self.__recipeIngredient9.setText("")
        
        self.__recipeDescriptionLine1.setText(recipeToShow.description[0])
        self.__recipeDescriptionLine2.setText(recipeToShow.description[1])
        self.__recipeDescriptionLine3.setText(recipeToShow.description[2])
        self.__recipeDescriptionLine4.setText(recipeToShow.description[3])
        self.__recipeDescriptionLine5.setText(recipeToShow.description[4])
        self.__recipeDescriptionLine6.setText(recipeToShow.description[5])
        self.__recipeDescriptionLine7.setText(recipeToShow.description[6])
        self.__recipeDescriptionLine8.setText(recipeToShow.description[7])
        self.__recipeDescriptionLine9.setText(recipeToShow.description[8])
        self.__recipeDescriptionLine10.setText(recipeToShow.description[9])
        self.__recipeDescriptionLine11.setText(recipeToShow.description[10])
        self.__recipeDescriptionLine12.setText(recipeToShow.description[11])
            
    def doTask(self):
        pass
    
    def doPaint(self, displaySurface, hoverList):
        
        # Transparent Background
        displaySurface.blit(ResourceController.background_Transparent, (0, 0))
        
        # Tabs
        if self.__currentTab == eIngredientsTab.INGREDIENTS:
            displaySurface.blit(ResourceController.input_TabRecipes_Off, (465, 10))
            displaySurface.blit(ResourceController.input_TabIngredients_On, (245, 10))

        elif self.__currentTab == eIngredientsTab.RECIPES:
            displaySurface.blit(ResourceController.input_TabIngredients_Off, (245, 10))
            displaySurface.blit(ResourceController.input_TabRecipes_On, (465, 10))
        
        # Board
        displaySurface.blit(ResourceController.background_PickIngredients, (0, 0))
        
        # Ingredient List
        if self.__currentTab == eIngredientsTab.INGREDIENTS:
            
            # Group Name
            if self.__currentIngredientGroup == eIngredientGroup.GROUP_1_CEREALES:
                groupNumber = "Grupo 1 :"
                groupName = "Cereales, Tubérculos, Raíces"
                groupColor = (255, 255, 255)  # (224, 173, 111)
            elif self.__currentIngredientGroup == eIngredientGroup.GROUP_2_VERDURAS:
                groupNumber = "Grupo 2 :"
                groupName = "Verduras, Leguminosas Verdes"
                groupColor = (255, 255, 255)  # (102, 255, 0)
            elif self.__currentIngredientGroup == eIngredientGroup.GROUP_3_FRUTAS:
                groupNumber = "Grupo 3 :"
                groupName = "Frutas"
                groupColor = (255, 255, 255)  # (239, 145, 3)
            elif self.__currentIngredientGroup == eIngredientGroup.GROUP_4_CARNES:
                groupNumber = "Grupo 4 :"
                groupName = "Carnes, Leguminosas Secas"
                groupColor = (255, 255, 255)  # (255, 66, 0)
            elif self.__currentIngredientGroup == eIngredientGroup.GROUP_5_LACTEOS:
                groupNumber = "Grupo 5 :"
                groupName = "Lácteos"
                groupColor = (255, 255, 255)  # (107, 244, 244)
            elif self.__currentIngredientGroup == eIngredientGroup.GROUP_6_GRASAS:
                groupNumber = "Grupo 6 :"
                groupName = "Grasas"
                groupColor = (255, 255, 255)  # (246, 255, 98)
            elif self.__currentIngredientGroup == eIngredientGroup.GROUP_7_AZUCARES:
                groupNumber = "Grupo 7 :"
                groupName = "Azúcares"
                groupColor = (255, 255, 255)  # (255, 255, 255)
            elif self.__currentIngredientGroup == eIngredientGroup.GROUP_8_OTROS:
                groupNumber = ""
                groupName = "Otros"
                groupColor = (255, 255, 255)  # (159, 159, 159)
                
            self.__groupName.setText(groupName)
            self.__groupName.setColor(groupColor)
            
            self.__groupNumber.setText(groupNumber)
            self.__groupNumber.setColor(groupColor)
            
            self.__groupNumber.doPaint(displaySurface)
            self.__groupName.doPaint(displaySurface)
            
            # Group Buttons Mini
            displaySurface.blit(ResourceController.input_Button1Cereales, (250 + (55 * 0), 90))
            displaySurface.blit(ResourceController.input_Button2Verduras, (250 + (55 * 1), 90))
            displaySurface.blit(ResourceController.input_Button3Frutas, (250 + (55 * 2), 90))
            displaySurface.blit(ResourceController.input_Button4Carnes, (250 + (55 * 3), 90))
            displaySurface.blit(ResourceController.input_Button5Lacteos, (250 + (55 * 4), 90))
            displaySurface.blit(ResourceController.input_Button6Grasas, (250 + (55 * 5), 90))
            displaySurface.blit(ResourceController.input_Button7Azucares, (250 + (55 * 6), 90))
            displaySurface.blit(ResourceController.input_Button8Otros, (250 + (55 * 7), 90))
            
            # Groups Buttons Big (Hover)
            if hoverList[0] == True:
                displaySurface.blit(ResourceController.input_Back1Cereales, (225 + (55 * 0), 65))
                displaySurface.blit(ResourceController.game_Ingredient08Pan, (230 + (55 * 0), 70))
                
            if hoverList[1] == True:
                displaySurface.blit(ResourceController.input_Back2Verduras, (225 + (55 * 1), 65))
                displaySurface.blit(ResourceController.game_Ingredient24Espinaca, (230 + (55 * 1), 70))
                
            if hoverList[2] == True:
                displaySurface.blit(ResourceController.input_Back3Frutas, (225 + (55 * 2), 65))
                displaySurface.blit(ResourceController.game_Ingredient40Mandarina, (230 + (55 * 2), 70))
                
            if hoverList[3] == True:
                displaySurface.blit(ResourceController.input_Back4Carnes, (225 + (55 * 3), 65))
                displaySurface.blit(ResourceController.game_Ingredient56Higado, (230 + (55 * 3), 70))
                
            if hoverList[4] == True:
                displaySurface.blit(ResourceController.input_Back5Lacteos, (225 + (55 * 4), 65))
                displaySurface.blit(ResourceController.game_Ingredient65Leche, (230 + (55 * 4), 70))
                
            if hoverList[5] == True:
                displaySurface.blit(ResourceController.input_Back6Grasas, (225 + (55 * 5), 65))
                displaySurface.blit(ResourceController.game_Ingredient70Margarina, (230 + (55 * 5), 70))
                
            if hoverList[6] == True:
                displaySurface.blit(ResourceController.input_Back7Azucares, (225 + (55 * 6), 65))
                displaySurface.blit(ResourceController.game_Ingredient71Azucar, (230 + (55 * 6), 70))
                
            if hoverList[7] == True:
                displaySurface.blit(ResourceController.input_Back8Otros, (225 + (55 * 7), 65))
                displaySurface.blit(ResourceController.game_Ingredient68Aceite, (230 + (55 * 7), 70))

            # Determinamos el conjunto de ingredientes a mostrar de acuerdo al grupo seleccionado
            ingredientsByGroupToShow = list()
            if self.__currentIngredientGroup == eIngredientGroup.GROUP_1_CEREALES:
                ingredientsByGroupToShow = InformationIngredients.group1Cereales
            elif self.__currentIngredientGroup == eIngredientGroup.GROUP_2_VERDURAS:
                ingredientsByGroupToShow = InformationIngredients.group2Verduras
            elif self.__currentIngredientGroup == eIngredientGroup.GROUP_3_FRUTAS:
                ingredientsByGroupToShow = InformationIngredients.group3Frutas
            elif self.__currentIngredientGroup == eIngredientGroup.GROUP_4_CARNES:
                ingredientsByGroupToShow = InformationIngredients.group4Carnes
            elif self.__currentIngredientGroup == eIngredientGroup.GROUP_5_LACTEOS:
                ingredientsByGroupToShow = InformationIngredients.group5Lacteos
            elif self.__currentIngredientGroup == eIngredientGroup.GROUP_6_GRASAS:
                ingredientsByGroupToShow = InformationIngredients.group6Grasas
            elif self.__currentIngredientGroup == eIngredientGroup.GROUP_7_AZUCARES:
                ingredientsByGroupToShow = InformationIngredients.group7Azucares
            elif self.__currentIngredientGroup == eIngredientGroup.GROUP_8_OTROS:
                ingredientsByGroupToShow = InformationIngredients.group8Otros
                
            # Determinamos los indice correctos dentro del grupo de ingredientes a mostrar
            lowLimit = self.__currentIngredientPage * self.__noOfItemsToShow
            upLimit = (self.__currentIngredientPage * self.__noOfItemsToShow) + self.__noOfItemsToShow
            if upLimit > (len(ingredientsByGroupToShow)):
                upLimit = (len(ingredientsByGroupToShow))
                
            # Obtenemos una lista, que incluye los ingredientes a mostrar
            threeIngredientsList = ingredientsByGroupToShow[lowLimit : upLimit]
            
            # Recorremos la lista de los 5 ingredientes a mostrar
            index = 0
            for ingredient in threeIngredientsList:
                
                # Determinamos si existe el ingrediente
                if (index + 1) <= len(threeIngredientsList):
                    
                    # Fondo de acuerdo al grupo
                    group = ingredient.group
                    if group == eIngredientGroup.GROUP_1_CEREALES:
                        displaySurface.blit(ResourceController.input_Back1Cereales, (220, 210 + (120 * index)))
                    elif group == eIngredientGroup.GROUP_2_VERDURAS:
                        displaySurface.blit(ResourceController.input_Back2Verduras, (220, 210 + (120 * index)))
                    elif group == eIngredientGroup.GROUP_3_FRUTAS:
                        displaySurface.blit(ResourceController.input_Back3Frutas, (220, 210 + (120 * index)))                        
                    elif group == eIngredientGroup.GROUP_4_CARNES:
                        displaySurface.blit(ResourceController.input_Back4Carnes, (220, 210 + (120 * index)))
                    elif group == eIngredientGroup.GROUP_5_LACTEOS:
                        displaySurface.blit(ResourceController.input_Back5Lacteos, (220, 210 + (120 * index)))
                    elif group == eIngredientGroup.GROUP_6_GRASAS:
                        displaySurface.blit(ResourceController.input_Back6Grasas, (220, 210 + (120 * index)))
                    elif group == eIngredientGroup.GROUP_7_AZUCARES:
                        displaySurface.blit(ResourceController.input_Back7Azucares, (220, 210 + (120 * index)))
                    elif group == eIngredientGroup.GROUP_8_OTROS:
                        displaySurface.blit(ResourceController.input_Back8Otros, (220, 210 + (120 * index)))
                        
                    # Icono del ingrediente                        
                    displaySurface.blit(threeIngredientsList[index].image, (220, 210 + (120 * index)))

                    # Nombre del ingrediente
                    self.__itemName.setPosition((340, 230 + (120 * index)))
                    self.__itemName.setText(threeIngredientsList[index].name)
                    self.__itemName.doPaint(displaySurface)
                    
                index = index + 1
                
            # Determinamos si es necesario mostrar las flechas
            
            # - Flecha Izquierda
            lowLimit = (self.__currentIngredientPage - 1) * self.__noOfItemsToShow
            if lowLimit >= 0:
                displaySurface.blit(ResourceController.input_ArrowLeft, (140, 350))
                    
            # - Flecha Derecha
            ingredientsByGroupToShow = list()
            if self.__currentIngredientGroup == eIngredientGroup.GROUP_1_CEREALES:
                ingredientsByGroupToShow = InformationIngredients.group1Cereales
            elif self.__currentIngredientGroup == eIngredientGroup.GROUP_2_VERDURAS:
                ingredientsByGroupToShow = InformationIngredients.group2Verduras
            elif self.__currentIngredientGroup == eIngredientGroup.GROUP_3_FRUTAS:
                ingredientsByGroupToShow = InformationIngredients.group3Frutas
            elif self.__currentIngredientGroup == eIngredientGroup.GROUP_4_CARNES:
                ingredientsByGroupToShow = InformationIngredients.group4Carnes
            elif self.__currentIngredientGroup == eIngredientGroup.GROUP_5_LACTEOS:
                ingredientsByGroupToShow = InformationIngredients.group5Lacteos
            elif self.__currentIngredientGroup == eIngredientGroup.GROUP_6_GRASAS:
                ingredientsByGroupToShow = InformationIngredients.group6Grasas
            elif self.__currentIngredientGroup == eIngredientGroup.GROUP_7_AZUCARES:
                ingredientsByGroupToShow = InformationIngredients.group7Azucares
            elif self.__currentIngredientGroup == eIngredientGroup.GROUP_8_OTROS:
                ingredientsByGroupToShow = InformationIngredients.group8Otros
            
            lowLimit = (self.__currentIngredientPage + 1) * self.__noOfItemsToShow
            if lowLimit < len(ingredientsByGroupToShow):
                displaySurface.blit(ResourceController.input_ArrowRight, (630, 350))
                
            # Ingredient Information
            displaySurface.blit(ResourceController.background_IngredientInfo, (210, 565))
            
            self.__lastSelectedIngredientName.doPaint(displaySurface)
            self.__lastSelectedIngredientLine1.doPaint(displaySurface)
            self.__lastSelectedIngredientLine2.doPaint(displaySurface)
            self.__lastSelectedIngredientLine3.doPaint(displaySurface)
            self.__lastSelectedIngredientLine4.doPaint(displaySurface)
            self.__lastSelectedIngredientLine5.doPaint(displaySurface)
            self.__lastSelectedIngredientLine6.doPaint(displaySurface)
            self.__lastSelectedIngredientLine7.doPaint(displaySurface)
            
        elif self.__currentTab == eIngredientsTab.RECIPES:
            
            # Recipes Background
            displaySurface.blit(ResourceController.input_RecipeIndex, (245, 82))
            displaySurface.blit(ResourceController.background_Recipes, (185, 160))
            
            # Contenido de la receta
            self.__recipeName.doPaint(displaySurface)
            
            self.__recipeIngredient1.doPaint(displaySurface)
            self.__recipeIngredient2.doPaint(displaySurface)
            self.__recipeIngredient3.doPaint(displaySurface)
            self.__recipeIngredient4.doPaint(displaySurface)
            self.__recipeIngredient5.doPaint(displaySurface)
            self.__recipeIngredient6.doPaint(displaySurface)
            self.__recipeIngredient7.doPaint(displaySurface)
            self.__recipeIngredient8.doPaint(displaySurface)
            self.__recipeIngredient9.doPaint(displaySurface)
            
            self.__recipeDescriptionLine1.doPaint(displaySurface)
            self.__recipeDescriptionLine2.doPaint(displaySurface)
            self.__recipeDescriptionLine3.doPaint(displaySurface)
            self.__recipeDescriptionLine4.doPaint(displaySurface)
            self.__recipeDescriptionLine5.doPaint(displaySurface)
            self.__recipeDescriptionLine6.doPaint(displaySurface)
            self.__recipeDescriptionLine7.doPaint(displaySurface)
            self.__recipeDescriptionLine8.doPaint(displaySurface)
            self.__recipeDescriptionLine9.doPaint(displaySurface)
            self.__recipeDescriptionLine10.doPaint(displaySurface)
            self.__recipeDescriptionLine11.doPaint(displaySurface)
            self.__recipeDescriptionLine12.doPaint(displaySurface)
            
            # Flecha Izquierda
            displaySurface.blit(ResourceController.input_ArrowLeft, (140, 350))
            
            # Flecha Derecha
            displaySurface.blit(ResourceController.input_ArrowRight, (630, 350))
        
        # Selected Ingredients Spaces
        displaySurface.blit(ResourceController.game_IngredientSpace, (720, 120))
        displaySurface.blit(ResourceController.game_IngredientSpace, (880, 120))
        displaySurface.blit(ResourceController.game_IngredientSpace, (1040, 120))
        displaySurface.blit(ResourceController.game_IngredientSpace, (720, 120 + (150 * 1)))
        displaySurface.blit(ResourceController.game_IngredientSpace, (880, 120 + (150 * 1)))
        displaySurface.blit(ResourceController.game_IngredientSpace, (1040, 120 + (150 * 1)))
        displaySurface.blit(ResourceController.game_IngredientSpace, (720, 120 + (150 * 2)))
        displaySurface.blit(ResourceController.game_IngredientSpace, (880, 120 + (150 * 2)))
        displaySurface.blit(ResourceController.game_IngredientSpace, (1040, 120 + (150 * 2)))
        
        # Selected Ingredients
        index = 0
        for selectedIngredient in self.__selectedIngredients:
            
            # Calculamos en cual espacio se debe pintar cada uno de los ingredientes
            ingredientCoords = (0, 0)
            crossCoords = (0, 0)
            
            if index == 0:
                ingredientCoords = (730, 130 + (150 * 0))
                crossCoords = (800, 110)
            elif index == 1:
                ingredientCoords = (890, 130 + (150 * 0))
                crossCoords = (960, 110)
            elif index == 2:
                ingredientCoords = (1050, 130 + (150 * 0))
                crossCoords = (1120, 110)
                
            elif index == 3:
                ingredientCoords = (730, 130 + (150 * 1))
                crossCoords = (800, 110 + (150 * 1))
            elif index == 4:
                ingredientCoords = (890, 130 + (150 * 1))
                crossCoords = (960, 110 + (150 * 1))
            elif index == 5:
                ingredientCoords = (1050, 130 + (150 * 1))
                crossCoords = (1120, 110 + (150 * 1))
                
            elif index == 6:
                ingredientCoords = (730, 130 + (150 * 2))
                crossCoords = (800, 110 + (150 * 2))
            elif index == 7:
                ingredientCoords = (890, 130 + (150 * 2))
                crossCoords = (960, 110 + (150 * 2))
            elif index == 8:
                ingredientCoords = (1050, 130 + (150 * 2))
                crossCoords = (1120, 110 + (150 * 2))
                
            # Realizamos el pintado del grupo
            group = selectedIngredient.group
            if group == eIngredientGroup.GROUP_1_CEREALES:
                displaySurface.blit(ResourceController.input_Back1Cereales, ingredientCoords)
            elif group == eIngredientGroup.GROUP_2_VERDURAS:
                displaySurface.blit(ResourceController.input_Back2Verduras, ingredientCoords)
            elif group == eIngredientGroup.GROUP_3_FRUTAS:
                displaySurface.blit(ResourceController.input_Back3Frutas, ingredientCoords)
            elif group == eIngredientGroup.GROUP_4_CARNES:
                displaySurface.blit(ResourceController.input_Back4Carnes, ingredientCoords)
            elif group == eIngredientGroup.GROUP_5_LACTEOS:
                displaySurface.blit(ResourceController.input_Back5Lacteos, ingredientCoords)                                                                
            elif group == eIngredientGroup.GROUP_6_GRASAS:
                displaySurface.blit(ResourceController.input_Back6Grasas, ingredientCoords)
            elif group == eIngredientGroup.GROUP_7_AZUCARES:
                displaySurface.blit(ResourceController.input_Back7Azucares, ingredientCoords)
            elif group == eIngredientGroup.GROUP_8_OTROS:
                displaySurface.blit(ResourceController.input_Back8Otros, ingredientCoords)
            
            # Realizamos el pintado del ingrediente y su equis para eliminarlo
            displaySurface.blit(selectedIngredient.image, ingredientCoords)
            displaySurface.blit(ResourceController.input_Cross, crossCoords)
            
            index = index + 1
            
        self.__recipeToPrepare1.doPaint(displaySurface)
        self.__recipeToPrepare2.doPaint(displaySurface)
        
        # Buttons with Hover
        if hoverList[8] == True:
            displaySurface.blit(ResourceController.input_Cancel_On, (710, 760))
        else:
            displaySurface.blit(ResourceController.input_Cancel_Off, (710, 760))
        
        # Dish Ready Button
        if self.__ingredientsMakeRecipe == True:
            displaySurface.blit(ResourceController.input_ReadyDish_On, (875, 740))
        else:
            displaySurface.blit(ResourceController.input_ReadyDish_Off, (875, 740))

    def doReset(self):
        self.__selectedIngredients = list()
        self.__ingredientsMakeRecipe = False
        self.__dishReadyButtonClicked = False
        self.__selectedClient = None
        
        self.__currentTab = eIngredientsTab.INGREDIENTS
        self.__currentIngredientGroup = eIngredientGroup.GROUP_1_CEREALES
        self.__currentIngredientPage = 0
        self.__currentRecipesPage = 0
        
        self.doUpdateImage()
        
    def orderSelected(self, selectedClient):
        self.__selectedClient = selectedClient
        
        self.__lastSelectedIngredientName.setText("Recuerda:")
        self.__lastSelectedIngredientLine1.setText("Si no conoces los ingredientes que ")
        self.__lastSelectedIngredientLine2.setText("componen la receta, de la orden que ")
        self.__lastSelectedIngredientLine3.setText("elegiste, haz click en la pestaña ")
        self.__lastSelectedIngredientLine4.setText("Recetas y consulta el recetario...")
        self.__lastSelectedIngredientLine5.setText("")
        self.__lastSelectedIngredientLine6.setText("")
        self.__lastSelectedIngredientLine7.setText("")
        
        self.__recipeToPrepare2.setText(self.__selectedClient.getRecipeWanted().name)

    def ingredientsMarkedAsReady(self):
        return self.__dishReadyButtonClicked
    
    def getCurrentTab(self):
        return self.__currentTab
        
    def clickButtonDishReady(self):
        if self.__ingredientsMakeRecipe == True:
            self.__dishReadyButtonClicked = True
    
    def clickTabIngredients(self):
        if self.__dishReadyButtonClicked == False:
            if self.__currentTab == eIngredientsTab.RECIPES: 
                self.__currentTab = eIngredientsTab.INGREDIENTS
                AudioController.playSound(eSound.CLICK_INGREDIENT_SELECTION, 1)
    
    def clickTabRecipe(self):
        if self.__dishReadyButtonClicked == False:
            if self.__currentTab == eIngredientsTab.INGREDIENTS: 
                self.__currentTab = eIngredientsTab.RECIPES
                AudioController.playSound(eSound.CLICK_INGREDIENT_SELECTION, 1)
                
    def clickLetter(self, letter):
        if self.__dishReadyButtonClicked == False:
            if self.__currentTab == eIngredientsTab.RECIPES:
                if letter == 'A':
                    self.__currentRecipesPage = 0
                elif letter == 'B':
                    self.__currentRecipesPage = 9
                elif letter == 'C':
                    self.__currentRecipesPage = 12
                elif letter == 'D':
                    pass
                elif letter == 'E':
                    self.__currentRecipesPage = 16
                elif letter == 'F':
                    pass
                elif letter == 'G':
                    self.__currentRecipesPage = 25
                elif letter == 'H':
                    self.__currentRecipesPage = 28
                elif letter == 'I':
                    pass
                elif letter == 'J':
                    self.__currentRecipesPage = 30
                elif letter == 'K':
                    pass
                elif letter == 'L':
                    self.__currentRecipesPage = 32
                elif letter == 'M':
                    self.__currentRecipesPage = 34
                elif letter == 'N':
                    pass
                elif letter == 'Ñ':
                    pass
                elif letter == 'O':
                    pass
                elif letter == 'P':
                    self.__currentRecipesPage = 35
                elif letter == 'Q':
                    self.__currentRecipesPage = 44
                elif letter == 'R':
                    self.__currentRecipesPage = 45
                elif letter == 'S':
                    self.__currentRecipesPage = 46
                elif letter == 'T':
                    self.__currentRecipesPage = 51
                elif letter == 'U':
                    pass
                elif letter == 'V':
                    pass
                elif letter == 'W':
                    pass
                elif letter == 'X':
                    pass
                elif letter == 'Y':
                    pass
                elif letter == 'Z':
                    self.__currentRecipesPage = 61
                    
                self.doUpdateImage()
                
                AudioController.playSound(eSound.CLICK_INGREDIENT_SELECTION, 1)
    
    def clickArrowLeft(self):
        if self.__dishReadyButtonClicked == False:
            
            if self.__currentTab == eIngredientsTab.INGREDIENTS:
                
                lowLimit = (self.__currentIngredientPage - 1) * self.__noOfItemsToShow
                if lowLimit >= 0:
                    self.__currentIngredientPage = self.__currentIngredientPage - 1
                    AudioController.playSound(eSound.CLICK_INGREDIENT_SELECTION, 1)
                    
            elif self.__currentTab == eIngredientsTab.RECIPES:
                
                self.__currentRecipesPage = self.__currentRecipesPage - 1
                
                if self.__currentRecipesPage < 0:
                    self.__currentRecipesPage = len(InformationRecipes.allRecipesList) - 1
                    
                self.doUpdateImage()
                
                AudioController.playSound(eSound.CLICK_INGREDIENT_SELECTION, 1)
    
    def clickArrowRight(self):
        if self.__dishReadyButtonClicked == False:
            
            if self.__currentTab == eIngredientsTab.INGREDIENTS:
                
                ingredientsByGroupToShow = list()
                if self.__currentIngredientGroup == eIngredientGroup.GROUP_1_CEREALES:
                    ingredientsByGroupToShow = InformationIngredients.group1Cereales
                elif self.__currentIngredientGroup == eIngredientGroup.GROUP_2_VERDURAS:
                    ingredientsByGroupToShow = InformationIngredients.group2Verduras
                elif self.__currentIngredientGroup == eIngredientGroup.GROUP_3_FRUTAS:
                    ingredientsByGroupToShow = InformationIngredients.group3Frutas
                elif self.__currentIngredientGroup == eIngredientGroup.GROUP_4_CARNES:
                    ingredientsByGroupToShow = InformationIngredients.group4Carnes
                elif self.__currentIngredientGroup == eIngredientGroup.GROUP_5_LACTEOS:
                    ingredientsByGroupToShow = InformationIngredients.group5Lacteos
                elif self.__currentIngredientGroup == eIngredientGroup.GROUP_6_GRASAS:
                    ingredientsByGroupToShow = InformationIngredients.group6Grasas
                elif self.__currentIngredientGroup == eIngredientGroup.GROUP_7_AZUCARES:
                    ingredientsByGroupToShow = InformationIngredients.group7Azucares
                elif self.__currentIngredientGroup == eIngredientGroup.GROUP_8_OTROS:
                    ingredientsByGroupToShow = InformationIngredients.group8Otros
                
                lowLimit = (self.__currentIngredientPage + 1) * self.__noOfItemsToShow
                if lowLimit < len(ingredientsByGroupToShow):
                    self.__currentIngredientPage = self.__currentIngredientPage + 1
                    AudioController.playSound(eSound.CLICK_INGREDIENT_SELECTION, 1)
                    
            elif self.__currentTab == eIngredientsTab.RECIPES:
                
                self.__currentRecipesPage = self.__currentRecipesPage + 1
                
                if self.__currentRecipesPage > len(InformationRecipes.allRecipesList) - 1:
                    self.__currentRecipesPage = 0
                    
                self.doUpdateImage()
                
                AudioController.playSound(eSound.CLICK_INGREDIENT_SELECTION, 1)
            
    def clickGroups1Button(self):
        if self.__dishReadyButtonClicked == False:
            if self.__currentTab == eIngredientsTab.INGREDIENTS:
                self.__currentIngredientGroup = eIngredientGroup.GROUP_1_CEREALES
                self.__currentIngredientPage = 0
                AudioController.playSound(eSound.CLICK_INGREDIENT_SELECTION, 1)
                    
    def clickGroups2Button(self):
        if self.__dishReadyButtonClicked == False:
            if self.__currentTab == eIngredientsTab.INGREDIENTS:
                self.__currentIngredientGroup = eIngredientGroup.GROUP_2_VERDURAS
                self.__currentIngredientPage = 0
                AudioController.playSound(eSound.CLICK_INGREDIENT_SELECTION, 1)
                    
    def clickGroups3Button(self):
        if self.__dishReadyButtonClicked == False:
            if self.__currentTab == eIngredientsTab.INGREDIENTS:
                self.__currentIngredientGroup = eIngredientGroup.GROUP_3_FRUTAS
                self.__currentIngredientPage = 0
                AudioController.playSound(eSound.CLICK_INGREDIENT_SELECTION, 1)
                    
    def clickGroups4Button(self):
        if self.__dishReadyButtonClicked == False:
            if self.__currentTab == eIngredientsTab.INGREDIENTS:
                self.__currentIngredientGroup = eIngredientGroup.GROUP_4_CARNES
                self.__currentIngredientPage = 0
                AudioController.playSound(eSound.CLICK_INGREDIENT_SELECTION, 1)
                    
    def clickGroups5Button(self):
        if self.__dishReadyButtonClicked == False:
            if self.__currentTab == eIngredientsTab.INGREDIENTS:
                self.__currentIngredientGroup = eIngredientGroup.GROUP_5_LACTEOS
                self.__currentIngredientPage = 0
                AudioController.playSound(eSound.CLICK_INGREDIENT_SELECTION, 1)
                    
    def clickGroups6Button(self):
        if self.__dishReadyButtonClicked == False:
            if self.__currentTab == eIngredientsTab.INGREDIENTS:
                self.__currentIngredientGroup = eIngredientGroup.GROUP_6_GRASAS
                self.__currentIngredientPage = 0
                AudioController.playSound(eSound.CLICK_INGREDIENT_SELECTION, 1)
                    
    def clickGroups7Button(self):
        if self.__dishReadyButtonClicked == False:
            if self.__currentTab == eIngredientsTab.INGREDIENTS:
                self.__currentIngredientGroup = eIngredientGroup.GROUP_7_AZUCARES
                self.__currentIngredientPage = 0
                AudioController.playSound(eSound.CLICK_INGREDIENT_SELECTION, 1)
        
    def clickGroups8Button(self):
        if self.__dishReadyButtonClicked == False:
            if self.__currentTab == eIngredientsTab.INGREDIENTS:
                self.__currentIngredientGroup = eIngredientGroup.GROUP_8_OTROS
                self.__currentIngredientPage = 0
                AudioController.playSound(eSound.CLICK_INGREDIENT_SELECTION, 1)
                
    def __checkIfIngredientsMakeWantedRecipe(self):
        
        # Dado que la lista de ingredientes seleccionados sera modificada, la duplicamos
        ingredientsFromRecipe = deepcopy(self.__selectedClient.getRecipeWanted().getIngredients())

        # Verificamos si la longitud de ambos conjuntos de ingredientes es la misma        
        if len(self.__selectedIngredients) == len(ingredientsFromRecipe):
            
            # Recorremos la lista de ingredientes de la receta (lo que queden...)
            while len(ingredientsFromRecipe) > 0:
                
                flag = False
                
                # Obtenemos el ingrediente actual de la receta
                recipeIngredient = ingredientsFromRecipe[0]
                
                # Recorremos la lista de ingredientes seleccionados
                for selectedIngredient in self.__selectedIngredients:
                    
                    # Los comparamos
                    if recipeIngredient.id == selectedIngredient.id:
                        flag = True
                
                # Si el ingrediente actual de la receta fue encontrado
                if flag == True:
                    
                    # Lo retiramos de la lista para evitar problemas de duplicidad
                    ingredientsFromRecipe.remove(recipeIngredient)
                    
                else:
                    # Un ingrediente de la receta no fue seleccionado...
                    self.__ingredientsMakeRecipe = False
                    return
                
            # Todos los ingredientes de la receta fueron seleccionados
            self.__ingredientsMakeRecipe = True
            AudioController.playSound(eSound.INGREDIENTS_MAKE_RECIPE, 1)
            
        else:
            # La cantidad de ingredientes seleccionados no corresponde
            self.__ingredientsMakeRecipe = False
    
    def clickAvailableItem1(self):
        if self.__dishReadyButtonClicked == False:
            if self.__currentTab == eIngredientsTab.INGREDIENTS:
            
                # Si aun no se han llenado todos los espacios disponibles para seleccion
                if len(self.__selectedIngredients) < 9:
                    
                    # Determinamos el conjunto de ingredientes a mostrar de acuerdo al grupo seleccionado
                    ingredientsByGroupToShow = list()
                    if self.__currentIngredientGroup == eIngredientGroup.GROUP_1_CEREALES:
                        ingredientsByGroupToShow = InformationIngredients.group1Cereales
                    elif self.__currentIngredientGroup == eIngredientGroup.GROUP_2_VERDURAS:
                        ingredientsByGroupToShow = InformationIngredients.group2Verduras
                    elif self.__currentIngredientGroup == eIngredientGroup.GROUP_3_FRUTAS:
                        ingredientsByGroupToShow = InformationIngredients.group3Frutas
                    elif self.__currentIngredientGroup == eIngredientGroup.GROUP_4_CARNES:
                        ingredientsByGroupToShow = InformationIngredients.group4Carnes
                    elif self.__currentIngredientGroup == eIngredientGroup.GROUP_5_LACTEOS:
                        ingredientsByGroupToShow = InformationIngredients.group5Lacteos
                    elif self.__currentIngredientGroup == eIngredientGroup.GROUP_6_GRASAS:
                        ingredientsByGroupToShow = InformationIngredients.group6Grasas
                    elif self.__currentIngredientGroup == eIngredientGroup.GROUP_7_AZUCARES:
                        ingredientsByGroupToShow = InformationIngredients.group7Azucares
                    elif self.__currentIngredientGroup == eIngredientGroup.GROUP_8_OTROS:
                        ingredientsByGroupToShow = InformationIngredients.group8Otros
                        
                    # Determinamos los indice correctos dentro del grupo de ingredientes a mostrar
                    lowLimit = self.__currentIngredientPage * self.__noOfItemsToShow
                    upLimit = (self.__currentIngredientPage * self.__noOfItemsToShow) + self.__noOfItemsToShow
                    if upLimit > (len(ingredientsByGroupToShow)):
                        upLimit = (len(ingredientsByGroupToShow))
                    
                    # Obtenemos una lista, que incluye los ingredientes a mostrar
                    threeIngredientsList = ingredientsByGroupToShow[lowLimit : upLimit]
    
                    # Si el item existe
                    if len(threeIngredientsList) >= 1:
                        
                        # Obtengo el item seleccionado
                        selectedItem = threeIngredientsList[0]
                        
                        # Muestro la informacion del ingrediente seleccionado
                        self.__lastSelectedIngredientName.setText(selectedItem.name)
                        self.__lastSelectedIngredientLine1.setText(selectedItem.description[0])
                        self.__lastSelectedIngredientLine2.setText(selectedItem.description[1])
                        self.__lastSelectedIngredientLine3.setText(selectedItem.description[2])
                        self.__lastSelectedIngredientLine4.setText(selectedItem.description[3])
                        self.__lastSelectedIngredientLine5.setText(selectedItem.description[4])
                        self.__lastSelectedIngredientLine6.setText(selectedItem.description[5])
                        self.__lastSelectedIngredientLine7.setText(selectedItem.description[6])
                        
                        # Agregamos el item obtenido
                        self.__selectedIngredients.append(selectedItem)
                        AudioController.playSound(eSound.INGREDIENT_SELECT, 1)
                        
        # Determinamos si los ingredientes seleccionados conforman la receta de la orden que se esta atendiendo 
        self.__checkIfIngredientsMakeWantedRecipe()
            
    def clickAvailableItem2(self):
        if self.__dishReadyButtonClicked == False:
            if self.__currentTab == eIngredientsTab.INGREDIENTS:
            
                # Si aun no se han llenado todos los espacios disponibles para seleccion
                if len(self.__selectedIngredients) < 9:
                    
                    # Determinamos el conjunto de ingredientes a mostrar de acuerdo al grupo seleccionado
                    ingredientsByGroupToShow = list()
                    if self.__currentIngredientGroup == eIngredientGroup.GROUP_1_CEREALES:
                        ingredientsByGroupToShow = InformationIngredients.group1Cereales
                    elif self.__currentIngredientGroup == eIngredientGroup.GROUP_2_VERDURAS:
                        ingredientsByGroupToShow = InformationIngredients.group2Verduras
                    elif self.__currentIngredientGroup == eIngredientGroup.GROUP_3_FRUTAS:
                        ingredientsByGroupToShow = InformationIngredients.group3Frutas
                    elif self.__currentIngredientGroup == eIngredientGroup.GROUP_4_CARNES:
                        ingredientsByGroupToShow = InformationIngredients.group4Carnes
                    elif self.__currentIngredientGroup == eIngredientGroup.GROUP_5_LACTEOS:
                        ingredientsByGroupToShow = InformationIngredients.group5Lacteos
                    elif self.__currentIngredientGroup == eIngredientGroup.GROUP_6_GRASAS:
                        ingredientsByGroupToShow = InformationIngredients.group6Grasas
                    elif self.__currentIngredientGroup == eIngredientGroup.GROUP_7_AZUCARES:
                        ingredientsByGroupToShow = InformationIngredients.group7Azucares
                    elif self.__currentIngredientGroup == eIngredientGroup.GROUP_8_OTROS:
                        ingredientsByGroupToShow = InformationIngredients.group8Otros
                        
                    # Determinamos los indice correctos dentro del grupo de ingredientes a mostrar
                    lowLimit = self.__currentIngredientPage * self.__noOfItemsToShow
                    upLimit = (self.__currentIngredientPage * self.__noOfItemsToShow) + self.__noOfItemsToShow
                    if upLimit > (len(ingredientsByGroupToShow)):
                        upLimit = (len(ingredientsByGroupToShow))
                    
                    # Obtenemos una lista, que incluye los ingredientes a mostrar
                    threeIngredientsList = ingredientsByGroupToShow[lowLimit : upLimit]
    
                    # Si el item existe
                    if len(threeIngredientsList) >= 2:
                        
                        # Obtengo el item seleccionado
                        selectedItem = threeIngredientsList[1]
                        
                        # Muestro la informacion del ingrediente seleccionado
                        self.__lastSelectedIngredientName.setText(selectedItem.name)
                        self.__lastSelectedIngredientLine1.setText(selectedItem.description[0])
                        self.__lastSelectedIngredientLine2.setText(selectedItem.description[1])
                        self.__lastSelectedIngredientLine3.setText(selectedItem.description[2])
                        self.__lastSelectedIngredientLine4.setText(selectedItem.description[3])
                        self.__lastSelectedIngredientLine5.setText(selectedItem.description[4])
                        self.__lastSelectedIngredientLine6.setText(selectedItem.description[5])
                        self.__lastSelectedIngredientLine7.setText(selectedItem.description[6])
                        
                        # Agregamos el item obtenido
                        self.__selectedIngredients.append(selectedItem)
                        AudioController.playSound(eSound.INGREDIENT_SELECT, 1)
                        
        # Determinamos si los ingredientes seleccionados conforman la receta de la orden que se esta atendiendo 
        self.__checkIfIngredientsMakeWantedRecipe()
    
    def clickAvailableItem3(self):
        if self.__dishReadyButtonClicked == False:
            if self.__currentTab == eIngredientsTab.INGREDIENTS:
            
                # Si aun no se han llenado todos los espacios disponibles para seleccion
                if len(self.__selectedIngredients) < 9:
                    
                    # Determinamos el conjunto de ingredientes a mostrar de acuerdo al grupo seleccionado
                    ingredientsByGroupToShow = list()
                    if self.__currentIngredientGroup == eIngredientGroup.GROUP_1_CEREALES:
                        ingredientsByGroupToShow = InformationIngredients.group1Cereales
                    elif self.__currentIngredientGroup == eIngredientGroup.GROUP_2_VERDURAS:
                        ingredientsByGroupToShow = InformationIngredients.group2Verduras
                    elif self.__currentIngredientGroup == eIngredientGroup.GROUP_3_FRUTAS:
                        ingredientsByGroupToShow = InformationIngredients.group3Frutas
                    elif self.__currentIngredientGroup == eIngredientGroup.GROUP_4_CARNES:
                        ingredientsByGroupToShow = InformationIngredients.group4Carnes
                    elif self.__currentIngredientGroup == eIngredientGroup.GROUP_5_LACTEOS:
                        ingredientsByGroupToShow = InformationIngredients.group5Lacteos
                    elif self.__currentIngredientGroup == eIngredientGroup.GROUP_6_GRASAS:
                        ingredientsByGroupToShow = InformationIngredients.group6Grasas
                    elif self.__currentIngredientGroup == eIngredientGroup.GROUP_7_AZUCARES:
                        ingredientsByGroupToShow = InformationIngredients.group7Azucares
                    elif self.__currentIngredientGroup == eIngredientGroup.GROUP_8_OTROS:
                        ingredientsByGroupToShow = InformationIngredients.group8Otros
                        
                    # Determinamos los indice correctos dentro del grupo de ingredientes a mostrar
                    lowLimit = self.__currentIngredientPage * self.__noOfItemsToShow
                    upLimit = (self.__currentIngredientPage * self.__noOfItemsToShow) + self.__noOfItemsToShow
                    if upLimit > (len(ingredientsByGroupToShow)):
                        upLimit = (len(ingredientsByGroupToShow))
                    
                    # Obtenemos una lista, que incluye los ingredientes a mostrar
                    threeIngredientsList = ingredientsByGroupToShow[lowLimit : upLimit]
    
                    # Si el item existe
                    if len(threeIngredientsList) >= 3:
                        
                        # Obtengo el item seleccionado
                        selectedItem = threeIngredientsList[2]
                        
                        # Muestro la informacion del ingrediente seleccionado
                        self.__lastSelectedIngredientName.setText(selectedItem.name)
                        self.__lastSelectedIngredientLine1.setText(selectedItem.description[0])
                        self.__lastSelectedIngredientLine2.setText(selectedItem.description[1])
                        self.__lastSelectedIngredientLine3.setText(selectedItem.description[2])
                        self.__lastSelectedIngredientLine4.setText(selectedItem.description[3])
                        self.__lastSelectedIngredientLine5.setText(selectedItem.description[4])
                        self.__lastSelectedIngredientLine6.setText(selectedItem.description[5])
                        self.__lastSelectedIngredientLine7.setText(selectedItem.description[6])
                        
                        # Agregamos el item obtenido
                        self.__selectedIngredients.append(selectedItem)
                        AudioController.playSound(eSound.INGREDIENT_SELECT, 1)
                        
        # Determinamos si los ingredientes seleccionados conforman la receta de la orden que se esta atendiendo 
        self.__checkIfIngredientsMakeWantedRecipe()
                
    def clickDeleteSeletedItem1(self):
        if self.__dishReadyButtonClicked == False:
            if len(self.__selectedIngredients) > 0:
                del self.__selectedIngredients[0]
                AudioController.playSound(eSound.INGREDIENT_DELETE, 1)
        self.__checkIfIngredientsMakeWantedRecipe()
    
    def clickDeleteSeletedItem2(self):
        if self.__dishReadyButtonClicked == False:
            if len(self.__selectedIngredients) > 1:
                del self.__selectedIngredients[1]
                AudioController.playSound(eSound.INGREDIENT_DELETE, 1)
        self.__checkIfIngredientsMakeWantedRecipe()
    
    def clickDeleteSeletedItem3(self):
        if self.__dishReadyButtonClicked == False:
            if len(self.__selectedIngredients) > 2:
                del self.__selectedIngredients[2]
                AudioController.playSound(eSound.INGREDIENT_DELETE, 1)
        self.__checkIfIngredientsMakeWantedRecipe()
    
    def clickDeleteSeletedItem4(self):
        if self.__dishReadyButtonClicked == False:
            if len(self.__selectedIngredients) > 3:
                del self.__selectedIngredients[3]
                AudioController.playSound(eSound.INGREDIENT_DELETE, 1)
        self.__checkIfIngredientsMakeWantedRecipe()
    
    def clickDeleteSeletedItem5(self):
        if self.__dishReadyButtonClicked == False:
            if len(self.__selectedIngredients) > 4:
                del self.__selectedIngredients[4]
                AudioController.playSound(eSound.INGREDIENT_DELETE, 1)
        self.__checkIfIngredientsMakeWantedRecipe()
    
    def clickDeleteSeletedItem6(self):
        if self.__dishReadyButtonClicked == False:
            if len(self.__selectedIngredients) > 5:
                del self.__selectedIngredients[5]
                AudioController.playSound(eSound.INGREDIENT_DELETE, 1)
        self.__checkIfIngredientsMakeWantedRecipe()

    def clickDeleteSeletedItem7(self):
        if self.__dishReadyButtonClicked == False:
            if len(self.__selectedIngredients) > 6:
                del self.__selectedIngredients[6]
                AudioController.playSound(eSound.INGREDIENT_DELETE, 1)
        self.__checkIfIngredientsMakeWantedRecipe()
                
    def clickDeleteSeletedItem8(self):
        if self.__dishReadyButtonClicked == False:
            if len(self.__selectedIngredients) > 7:
                del self.__selectedIngredients[7]
                AudioController.playSound(eSound.INGREDIENT_DELETE, 1)
        self.__checkIfIngredientsMakeWantedRecipe()
                    
    def clickDeleteSeletedItem9(self):
        if self.__dishReadyButtonClicked == False:
            if len(self.__selectedIngredients) > 8:
                del self.__selectedIngredients[8]
                AudioController.playSound(eSound.INGREDIENT_DELETE, 1)
        self.__checkIfIngredientsMakeWantedRecipe()


class Chef:

    def __init__(self):
        
        # Movimiento
        self.__motionPoints = InformationMotionPoints.allPoints
        self.__mainState = eChefMainState.NO_MOTION
        self.__currentMotionPointId = eMotionBlock.ROW1_STOVE
        self.__targetMotionPointId = None
        self.__nextMotionPointId = None
        self.__chefToTargetInitDirection = None
        self.__positionXY = self.__getMotionPointPosition(self.__currentMotionPointId)
        
        # Caracteristicas
        self.__gender = GlobalsController.CHEF_GENDER
        self.__command = None
        self.__direction = eMotionDirection.DOWN
        self.__serviceState = eChefServiceState.READY
        self.__cookingState = None
        
        # Level
        self.stars = 0
        self.level = eChefLevel.LEVEL_0_NONE
        self.__level1Announced = False
        self.__level2Announced = False
        self.__level3Announced = False
        
        # Flags
        self.__hasCleanHands = False
        self.isSelectingOrder = False
        self.__isPickingIngredients = False
        self.hasReachNewlevel = False
        self.isAssigningOrder = False
        
        # Clientes
        self.__clientSelected = None
        self.__clientsWithActiveOrders = list()
        self.__clientFoodIsPreparing = None
        self.__orderToAssign = None
        
        # Tiempos maximos
        self.__cookingStateTotalTime = 2
        
        self.__cookingAnimTotalTime = 38
        self.__cookingAnimTotalFrames = 4
        self.__cookingAnimTotalGap = 2
        
        self.__washingDishesTotalTime = 20
        self.__washingDishesTotalFrames = 2
        self.__washingDishesTotalGap = 2
        
        self.__washIngredientsTotalTime = 10
        self.__washIngredientsTotalFrames = 2
        self.__washIngredientsTotalGap = 2
        
        self.__washHandsTotalTime = 20
        self.__washHandsTotalFrames = 2
        self.__washHandsTotalGap = 2
        
        self.__takingOrderTotalTime = 5
        
        self.__dancingAnimCountdown = 20
        self.__dancingAnimTotalGap = 6
        self.__dancingAnimTotalFrames = 3
        
        # Tiempos actuales
        self.__cookingStateCurrentTime = 1
        
        self.__cookingAnimCurrentTime = 1
        self.__cookingAnimCurrentFrame = 1
        self.__cookingAnimCurrentGap = 1
        
        self.__washingDishesCurrentTime = 1
        self.__washingDishesCurrentFrame = 1
        self.__washingDishesCurrentGap = 1
        
        self.__washIngredientsCurrentTime = 1
        self.__washIngredientsCurrentFrame = 1
        self.__washIngredientsCurrentGap = 1
        
        self.__washHandsCurrentTime = 1
        self.__washHandsCurrentFrame = 1
        self.__washHandsCurrentGap = 1
        
        self.__takingOrderCurrentTime = 1
        
        self.__dancingAnimCurrentGap = 1
        self.__dancingAnimCurrentFrame = 1
        
        # Labels
        self.__textMotionState = Label("", FontController.font40, (120, 100, 70), (776, 20))
        self.__textClientList = Label("x " + str(self.stars), FontController.font20, (255, 255, 255), (900 - 21, 230))
        
        # Imagenes
        self.__imageClient = None
        self.__imageWashingIngredients = None
        self.__imageWashingDishes = None
        self.__imageCooking = None
        
        # Calculamos las imagenes a mostrar al inicio
        self.__doUpdateImage()
    
    def doTask(self, tutorial):
        
        # Si el chef se esta moviendo...
        if self.__mainState is eChefMainState.MOVING:
    
            # Calculamos las coordenadas de las posiciones actual y destino final
            currentPosition = self.__getMotionPointPosition(self.__currentMotionPointId)
            targetPosition = self.__getMotionPointPosition(self.__targetMotionPointId)
            
            # Si aun no hemos llegado al destino final... 
            if self.__positionsAreEqual(currentPosition, targetPosition) == False:
        
                # Si ya se tiene un sub-camino elegido...
                if self.__nextMotionPointId != None:
                    
                    # Nos movemos de acuerdo a la direccion lada
                    self.__move()

                    # Si al habernos movido alcanzamos el punto final del subcamino...
                    nextBlockPosition = self.__getMotionPointPosition(self.__nextMotionPointId)
                    if self.__positionsAreEqual(self.__positionXY, nextBlockPosition) == True:
                        
                        # Se prepara todo para la eleccion de un nuevo subcamino (Si es necesario...)
                        self.__currentMotionPointId = self.__nextMotionPointId
                        self.__nextMotionPointId = None
                    
                else:
                    # Determinamos el sub-camino mas optimo para alcanzar el objetivo final
                    self.__calculateNextStep()
                    
                    # Llamamos recursivamente la funcion para asegurarnos que el Chef se mueva de manera continua
                    # Y no se detenga cuando tenga que realizar el lo de un camino...
                    self.doTask(tutorial)
                
            # LLegamos al punto final    
            else:
                
                # Eliminamos todos los datos de movimiento
                self.__targetMotionPointId = None
                self.__nextMotionPointId = None
                self.__chefToTargetInitDirection = None

                # Si hay alguna orden...
                if self.__command != None:
                    
                    # Comienza la ejecucion de la orden
                    self.__mainState = eChefMainState.DOING_ORDER
                    
                    # Calculamos la direccion de acuerdo a la orden
                    if self.__command == eChefCommand.TAKE_ORDER:
                        self.__direction = eMotionDirection.DOWN
                        
                    elif self.__command == eChefCommand.WASH_HANDS:
                        self.__direction = eMotionDirection.UP
                        self.__serviceState = eChefServiceState.READY
                        AudioController.playSound(eSound.WASHING, 1)
                        
                    elif self.__command == eChefCommand.SELECT_ORDER:
                        self.__direction = eMotionDirection.UP
                        self.isSelectingOrder = True
                        
                    elif self.__command == eChefCommand.PICK_INGREDIENTS:
                        self.__direction = eMotionDirection.UP
                        
                    elif self.__command == eChefCommand.WASH_INGREDIENTS:
                        self.__direction = eMotionDirection.UP
                        AudioController.playSound(eSound.WASHING, 1)
                        
                    elif self.__command == eChefCommand.COOK_INGREDIENTS:
                        self.__direction = eMotionDirection.UP
                        self.__cookingState = eChefCookingState.COOKING
                        
                        # Determinamos el tipo de sonido a reproducir de acuerdo al tipo de preparacion de la receta
                        if self.__clientFoodIsPreparing.getRecipeWanted().preparation == eRecipePreparation.HOT:
                            AudioController.playSound(eSound.COOKING_HOT, 1)
                        else:
                            AudioController.playSound(eSound.COOKING_COLD, 1)
                        
                    elif self.__command == eChefCommand.PICK_PREPARED_FOOD:
                        self.__direction = eMotionDirection.UP
                        
                    elif self.__command == eChefCommand.SERVE_PREPARED_FOOD:
                        self.__direction = eMotionDirection.DOWN
                        
                        # Le avisamos al cliente que su solitud sera atendida
                        if self.__clientSelected != None:
                            self.__clientSelected.chefServesMePreparedFood()
                        
                    elif self.__command == eChefCommand.PICK_DIRTY_DISHES:
                        self.__direction = eMotionDirection.DOWN
                        
                        # Le avisamos al cliente que su solitud sera atendida
                        if self.__clientSelected != None:
                            
                            # Obtenemos las estrellas que tenga el cliente en ese momento
                            self.stars = self.stars + self.__clientSelected.stars
                            
                            # Le indicamos al cliente que se le van a recojer los platos
                            self.__clientSelected.chefPicksMyDirtyDishes()
                            
                            # Determinamos si se ha alcanzado algun nivel de chef
                            if self.level == eChefLevel.LEVEL_0_NONE:
                                if (self.stars >= 25) and (self.__level1Announced == False):
                                    self.__level1Announced = True
                                    self.hasReachNewlevel = True
                                    self.level = eChefLevel.LEVEL_1_JUNIOR
                                    AudioController.playSound(eSound.LEVEL_PASSED, 1)
                                    
                            elif self.level == eChefLevel.LEVEL_1_JUNIOR:
                                if (self.stars >= 50) and (self.__level2Announced == False):
                                    self.__level2Announced = True
                                    self.hasReachNewlevel = True
                                    self.level = eChefLevel.LEVEL_2_SENIOR
                                    AudioController.playSound(eSound.LEVEL_PASSED, 1)
                                    
                            elif self.level == eChefLevel.LEVEL_2_SENIOR:
                                if (self.stars >= 100) and (self.__level3Announced == False):
                                    self.__level3Announced = True
                                    self.hasReachNewlevel = True
                                    self.level = eChefLevel.LEVEL_3_SUPER
                                    AudioController.playSound(eSound.LEVEL_PASSED, 1)
                            
                    elif self.__command == eChefCommand.WASH_DIRTY_DISHES:
                        self.__direction = eMotionDirection.UP
                        AudioController.playSound(eSound.WASHING, 1)
                     
                # No hay orden   
                else:
                    self.__mainState = eChefMainState.NO_MOTION
                    self.__direction = eMotionDirection.DOWN
                
        # Si el chef esta ejecutando la orden dada...
        elif self.__mainState is eChefMainState.DOING_ORDER:
            
            # Actuamos de acuerdo al tipo de orden dada
            if self.__command != None:
                
                if self.__command == eChefCommand.TAKE_ORDER:
                    
                    # Mientras el tiempo en este estado no haya finalizado...
                    if self.__takingOrderCurrentTime < self.__takingOrderTotalTime:
                        self.__takingOrderCurrentTime = self.__takingOrderCurrentTime + 1
                        
                        # Activamos la asignacion de ordenes justo antes de finalizar el tiempo de espera en este estado 
                        if self.__takingOrderCurrentTime == (self.__takingOrderTotalTime - 1):
                            self.isAssigningOrder = True
                            
                    else:
                        # Solo salimos de este estado hasta que sea asignada la orden al cliente
                        if self.isAssigningOrder == False:
                        
                            # Le avisamos al cliente que su solitud sera atendida
                            if self.__clientSelected != None:
                                
                                # Indicarle al cliente la orden seleccionada
                                self.__clientSelected.userAssignMyOrder(self.__orderToAssign)
                            
                            # La ejecucion de la orden ha finalizado
                            self.__takingOrderCurrentTime = 0
                            AudioController.playSound(eSound.ORDER, 1)
                            
                            self.__command = None
                            self.__direction = eMotionDirection.DOWN
                            self.__mainState = eChefMainState.NO_MOTION
                            self.__serviceState = eChefServiceState.READY
                            self.__clientSelected = None
                            self.__hasCleanHands = False
                            self.__deactivateAnyMessage()
                            
                elif self.__command == eChefCommand.WASH_HANDS:
                    
                    # Mientras el tiempo en este estado no haya finalizado...
                    if self.__washHandsCurrentTime < self.__washHandsTotalTime:
                        self.__washHandsCurrentTime = self.__washHandsCurrentTime + 1
                        
                        # Mientras un ciclo de animacion este activo
                        if self.__washHandsCurrentGap < self.__washHandsTotalGap:
                            self.__washHandsCurrentGap = self.__washHandsCurrentGap + 1
                            
                        else:
                            # Unc ciclo de animacion acaba, mostramos la imagen siguiente
                            self.__washHandsCurrentGap = 1
                            
                            # Si aun no se ha mostrado la ultima imagen
                            if self.__washHandsCurrentFrame < self.__washHandsTotalFrames:
                                self.__washHandsCurrentFrame = self.__washHandsCurrentFrame + 1
                            else:
                                self.__washHandsCurrentFrame = 1
                    else:
                        # La ejecucion de la orden ha finalizado
                        self.__washHandsCurrentTime = 1
                        self.__washHandsCurrentFrames = 1
                        self.__washHandsCurrentGap = 1
                        
                        self.__command = None
                        self.__direction = eMotionDirection.DOWN
                        self.__mainState = eChefMainState.NO_MOTION
                        self.__serviceState = eChefServiceState.READY
                        self.__clientSelected = None
                        self.__hasCleanHands = True
                        self.__deactivateAnyMessage()
                        
                        # Le avisamos al tutorial que avance al siguiente paso
                        tutorial.nextStep(4)
                        
                elif self.__command == eChefCommand.SELECT_ORDER:
                    # Esperamos hasta que sean elegidos los ingredientes del plato
                    if self.isSelectingOrder == True:
                        pass  # La orden se esta ejecutando
                    else:
                        # La ejecucion de la orden ha finalizado
                        self.__isPickingIngredients = True
                        
                        self.__command = eChefCommand.PICK_INGREDIENTS
                        self.__direction = eMotionDirection.UP
                        self.__mainState = eChefMainState.DOING_ORDER
                        self.__serviceState = eChefServiceState.READY
                        self.__clientSelected = None
                        self.__hasCleanHands = False
                        self.__deactivateAnyMessage()
                        
                elif self.__command == eChefCommand.PICK_INGREDIENTS:
                    # Esperamos hasta que sean elegidos los ingredientes del plato
                    if self.__isPickingIngredients == True:
                        pass  # La orden se esta ejecutando
                    else:
                        # La ejecucion de la orden ha finalizado
                        self.__command = None
                        self.__direction = eMotionDirection.DOWN
                        self.__mainState = eChefMainState.NO_MOTION
                        self.__serviceState = eChefServiceState.CARRYING_DIRTY_INGREDIENTS
                        self.__clientSelected = None
                        self.__hasCleanHands = False
                        self.__deactivateAnyMessage()
                
                elif self.__command == eChefCommand.WASH_INGREDIENTS:
                    
                    # Mientras el tiempo en este estado no haya finalizado...
                    if self.__washIngredientsCurrentTime < self.__washIngredientsTotalTime:
                        self.__washIngredientsCurrentTime = self.__washIngredientsCurrentTime + 1
                        
                        # Mientras un ciclo de animacion este activo
                        if self.__washIngredientsCurrentGap < self.__washIngredientsTotalGap:
                            self.__washIngredientsCurrentGap = self.__washIngredientsCurrentGap + 1
                            
                        else:
                            # Unc ciclo de animacion acaba, mostramos la imagen siguiente
                            self.__washIngredientsCurrentGap = 1
                            
                            # Si aun no se ha mostrado la ultima imagen
                            if self.__washIngredientsCurrentFrame < self.__washIngredientsTotalFrames:
                                self.__washIngredientsCurrentFrame = self.__washIngredientsCurrentFrame + 1
                            else:
                                self.__washIngredientsCurrentFrame = 1
                    else:
                        # La ejecucion de la orden ha finalizado
                        self.__washIngredientsCurrentTime = 1
                        self.__washIngredientsCurrentFrames = 1
                        self.__washIngredientsCurrentGap = 1
        
                        self.__command = None
                        self.__direction = eMotionDirection.DOWN
                        self.__mainState = eChefMainState.NO_MOTION
                        self.__serviceState = eChefServiceState.CARRYING_CLEAN_INGREDIENTS
                        self.__clientSelected = None
                        self.__hasCleanHands = False
                        self.__deactivateAnyMessage()
                        
                        # Le avisamos al tutorial que avance al siguiente paso
                        tutorial.nextStep(17)
                
                elif self.__command == eChefCommand.COOK_INGREDIENTS:
                    
                    # Mientras el tiempo en este estado no haya finalizado...
                    if self.__cookingStateCurrentTime < self.__cookingStateTotalTime:
                        self.__cookingStateCurrentTime = self.__cookingStateCurrentTime + 1
                        
                    else:
                        # La ejecucion de la orden ha finalizado
                        self.__cookingStateCurrentTime = 1
                        
                        self.__command = None
                        self.__direction = eMotionDirection.DOWN
                        self.__mainState = eChefMainState.NO_MOTION
                        self.__serviceState = eChefServiceState.READY
                        self.__clientSelected = None
                        self.__hasCleanHands = False
                        self.__deactivateAnyMessage()
                        
                        # Le avisamos al tutorial que avance al siguiente paso
                        tutorial.nextStep(18)
                        
                elif self.__command == eChefCommand.PICK_PREPARED_FOOD:
                    
                    # La ejecucion de la orden ha finalizado
                    self.__cookingState = None
                    
                    self.__command = None
                    self.__direction = eMotionDirection.DOWN
                    self.__mainState = eChefMainState.NO_MOTION
                    self.__serviceState = eChefServiceState.CARRYING_PREPARED_FOOD
                    self.__clientSelected = None
                    self.__hasCleanHands = False
                    self.__deactivateAnyMessage()
                    
                    # Le avisamos al tutorial que avance al siguiente paso
                    tutorial.nextStep(19)
                
                elif self.__command == eChefCommand.SERVE_PREPARED_FOOD:
                    
                    # La ejecucion de la orden ha finalizado
                    self.__command = None
                    self.__direction = eMotionDirection.DOWN
                    self.__mainState = eChefMainState.NO_MOTION
                    self.__serviceState = eChefServiceState.READY
                    self.__clientSelected = None
                    self.__hasCleanHands = False
                    self.__deactivateAnyMessage()
                    
                    # Le avisamos al tutorial que avance al siguiente paso
                    tutorial.nextStep(20)
                    
                    AudioController.playSound(eSound.FOOD_SERVED, 1)
                
                elif self.__command == eChefCommand.PICK_DIRTY_DISHES:
                    
                    # La ejecucion de la orden ha finalizado
                    self.__command = None
                    self.__direction = eMotionDirection.DOWN
                    self.__mainState = eChefMainState.NO_MOTION
                    self.__serviceState = eChefServiceState.CARRYING_DIRTY_DISHES
                    self.__clientSelected = None
                    self.__hasCleanHands = False
                    self.__deactivateAnyMessage()
                    
                    # Le avisamos al tutorial que avance al siguiente paso
                    tutorial.nextStep(21)
                    
                    AudioController.playSound(eSound.PICK_DIRTY_DISH, 1)
                
                elif self.__command == eChefCommand.WASH_DIRTY_DISHES:
                    
                    # Mientras el tiempo en este estado no haya finalizado...
                    if self.__washingDishesCurrentTime < self.__washingDishesTotalTime:
                        self.__washingDishesCurrentTime = self.__washingDishesCurrentTime + 1
                        
                        # Mientras un ciclo de animacion este activo
                        if self.__washingDishesCurrentGap < self.__washingDishesTotalGap:
                            self.__washingDishesCurrentGap = self.__washingDishesCurrentGap + 1
                            
                        else:
                            # Unc ciclo de animacion acaba, mostramos la imagen siguiente
                            self.__washingDishesCurrentGap = 1
                            
                            # Si aun no se ha mostrado la ultima imagen
                            if self.__washingDishesCurrentFrame < self.__washingDishesTotalFrames:
                                self.__washingDishesCurrentFrame = self.__washingDishesCurrentFrame + 1
                            else:
                                self.__washingDishesCurrentFrame = 1
                    else:
                        # La ejecucion de la orden ha finalizado
                        self.__washingDishesCurrentTime = 1
                        self.__dishesCurrentFrames = 1
                        self.__washingDishesCurrentGap = 1
                        
                        self.__command = None
                        self.__direction = eMotionDirection.DOWN
                        self.__mainState = eChefMainState.NO_MOTION
                        self.__serviceState = eChefServiceState.READY
                        self.__clientSelected = None
                        self.__hasCleanHands = False
                        self.__deactivateAnyMessage()
                        
                        if self.__gender == eCharacterGender.MALE:
                            AudioController.playSound(eSound.YUJU_BOY, 1)                
                        if self.__gender == eCharacterGender.FEMALE:
                            AudioController.playSound(eSound.YUJU_GIRL, 1)
                        
                        # Le avisamos al tutorial que avance al siguiente paso
                        tutorial.nextStep(22)
                        
        elif self.__mainState is eChefMainState.NO_MOTION:
            
            if self.__dancingAnimCountdown > 0:
                self.__dancingAnimCountdown = self.__dancingAnimCountdown - 1
                
                if self.__gender == eCharacterGender.MALE:
                    AudioController.playSound(eSound.HELLO_BOY, 1)                
                if self.__gender == eCharacterGender.FEMALE:
                    AudioController.playSound(eSound.HELLO_GIRL, 1)    
            else:
            
                # Mientras un ciclo de animacion este activo
                if self.__dancingAnimCurrentGap < self.__dancingAnimTotalGap:
                    self.__dancingAnimCurrentGap = self.__dancingAnimCurrentGap + 1
                    
                else:
                    # Unc ciclo de animacion acaba, mostramos la imagen siguiente
                    self.__dancingAnimCurrentGap = 1
                    
                    # Si aun no se ha mostrado la ultima imagen
                    if self.__dancingAnimCurrentFrame < self.__dancingAnimTotalFrames:
                        self.__dancingAnimCurrentFrame = self.__dancingAnimCurrentFrame + 1
                    else:
                        self.__dancingAnimCurrentFrame = 1
                
                # Determinamos cual imagen se debe mostrar de acuerdo al estado general del chef
                self.__doUpdateImage()
        
            pass
        
        # Esta animacion funciona independiente del estado del chef
        if self.__cookingState == eChefCookingState.COOKING:
            
            # Mientras el tiempo en este estado no haya finalizado...
            if self.__cookingAnimCurrentTime < self.__cookingAnimTotalTime:
                self.__cookingAnimCurrentTime = self.__cookingAnimCurrentTime + 1
                
                # Mientras un ciclo de animacion este activo
                if self.__cookingAnimCurrentGap < self.__cookingAnimTotalGap:
                    self.__cookingAnimCurrentGap = self.__cookingAnimCurrentGap + 1
                    
                else:
                    # Unc ciclo de animacion acaba, mostramos la imagen siguiente
                    self.__cookingAnimCurrentGap = 1
                    
                    # Si aun no se ha mostrado la ultima imagen
                    if self.__cookingAnimCurrentFrame < self.__cookingAnimTotalFrames:
                        self.__cookingAnimCurrentFrame = self.__cookingAnimCurrentFrame + 1
                    else:
                        self.__cookingAnimCurrentFrame = 1
                
            else:
                # La ejecucion de la orden ha finalizado
                self.__cookingAnimCurrentTime = 1
                self.__cookingAnimCurrentFrame = 1
                self.__cookingAnimCurrentGap = 1
                
                AudioController.stopSound(eSound.COOKING_HOT)
                AudioController.stopSound(eSound.COOKING_COLD)
                AudioController.playSound(eSound.BELL, 1)
                
                self.__cookingState = eChefCookingState.DISH_PREPARED_AND_READY_TO_SERVE
            
        # Determinamos cual imagen se debe mostrar de acuerdo al estado general del chef
        self.__doUpdateImage()
    
    def doPaint(self, displaySurface):
        
        if (self.__clientsWithActiveOrders != None) and (len(self.__clientsWithActiveOrders) > 0):
            
            orders = len(self.__clientsWithActiveOrders)
            if self.__command == eChefCommand.TAKE_ORDER:
                orders = orders - 1
            
            if orders > 0:
                self.__textMotionState.setText(str(orders))
                self.__textMotionState.doPaint(displaySurface)
            else:
                self.__textMotionState.setText("")
        
        if self.__imageWashingHands != None:    
            displaySurface.blit(self.__imageWashingHands, (self.__positionXY[0] - 20, self.__positionXY[1] + 103))
        
        if self.__imageWashingIngredients != None:
            displaySurface.blit(self.__imageWashingIngredients, (self.__positionXY[0] - 20, self.__positionXY[1] + 97))

        if self.__imageWashingDishes != None:
            displaySurface.blit(self.__imageWashingDishes, (self.__positionXY[0] - 30, self.__positionXY[1] + 114))

        if self.__cookingState == eChefCookingState.COOKING:
            displaySurface.blit(self.__imageCooking, (62, 40))
        elif self.__cookingState == eChefCookingState.DISH_PREPARED_AND_READY_TO_SERVE:
            displaySurface.blit(ResourceController.game_DishFullBase, (100, 100))
            displaySurface.blit(self.__imageCooking, (145, 75))

        if self.__imageCloud != None:
            displaySurface.blit(self.__imageCloud, (self.__positionXY[0] + 110, self.__positionXY[1] + 50))
            if self.__imageRecipe != None:
                displaySurface.blit(self.__imageRecipe, (self.__positionXY[0] + 117, self.__positionXY[1] + 52))
            
        displaySurface.blit(self.__imageClient, (self.__positionXY[0], self.__positionXY[1]))

    def assignOrderToSelectedClient(self, recipeId):
        self.isAssigningOrder = False
        self.__orderToAssign = recipeId
        
    def __doUpdateImage(self):
        
        if self.__mainState is eChefMainState.NO_MOTION and self.__serviceState == eChefServiceState.READY:
        
            if self.__gender == eCharacterGender.MALE:
                
                if self.level == eChefLevel.LEVEL_0_NONE:
                    if self.__dancingAnimCurrentFrame == 1:
                        self.__imageClient = ResourceController.game_ChefMaleLevel0_FrontDancing_0
                    elif self.__dancingAnimCurrentFrame == 2:
                        self.__imageClient = ResourceController.game_ChefMaleLevel0_FrontDancing_1
                    elif self.__dancingAnimCurrentFrame == 3:
                        self.__imageClient = ResourceController.game_ChefMaleLevel0_FrontDancing_2
                    
                elif self.level == eChefLevel.LEVEL_1_JUNIOR:
                    if self.__dancingAnimCurrentFrame == 1:
                        self.__imageClient = ResourceController.game_ChefMaleLevel1_FrontDancing_0
                    elif self.__dancingAnimCurrentFrame == 2:
                        self.__imageClient = ResourceController.game_ChefMaleLevel1_FrontDancing_1
                    elif self.__dancingAnimCurrentFrame == 3:
                        self.__imageClient = ResourceController.game_ChefMaleLevel1_FrontDancing_2
                    
                elif self.level == eChefLevel.LEVEL_2_SENIOR:
                    if self.__dancingAnimCurrentFrame == 1:
                        self.__imageClient = ResourceController.game_ChefMaleLevel2_FrontDancing_0
                    elif self.__dancingAnimCurrentFrame == 2:
                        self.__imageClient = ResourceController.game_ChefMaleLevel2_FrontDancing_1
                    elif self.__dancingAnimCurrentFrame == 3:
                        self.__imageClient = ResourceController.game_ChefMaleLevel2_FrontDancing_2
                    
                elif self.level == eChefLevel.LEVEL_3_SUPER:
                    if self.__dancingAnimCurrentFrame == 1:
                        self.__imageClient = ResourceController.game_ChefMaleLevel2_FrontDancing_0
                    elif self.__dancingAnimCurrentFrame == 2:
                        self.__imageClient = ResourceController.game_ChefMaleLevel2_FrontDancing_1
                    elif self.__dancingAnimCurrentFrame == 3:
                        self.__imageClient = ResourceController.game_ChefMaleLevel2_FrontDancing_2
                
            elif self.__gender == eCharacterGender.FEMALE:
                
                if self.level == eChefLevel.LEVEL_0_NONE:
                    if self.__dancingAnimCurrentFrame == 1:
                        self.__imageClient = ResourceController.game_ChefFemaleLevel0_FrontDancing_0
                    elif self.__dancingAnimCurrentFrame == 2:
                        self.__imageClient = ResourceController.game_ChefFemaleLevel0_FrontDancing_1
                    elif self.__dancingAnimCurrentFrame == 3:
                        self.__imageClient = ResourceController.game_ChefFemaleLevel0_FrontDancing_2
                    
                elif self.level == eChefLevel.LEVEL_1_JUNIOR:
                    if self.__dancingAnimCurrentFrame == 1:
                        self.__imageClient = ResourceController.game_ChefFemaleLevel1_FrontDancing_0
                    elif self.__dancingAnimCurrentFrame == 2:
                        self.__imageClient = ResourceController.game_ChefFemaleLevel1_FrontDancing_1
                    elif self.__dancingAnimCurrentFrame == 3:
                        self.__imageClient = ResourceController.game_ChefFemaleLevel1_FrontDancing_2
                    
                elif self.level == eChefLevel.LEVEL_2_SENIOR:
                    if self.__dancingAnimCurrentFrame == 1:
                        self.__imageClient = ResourceController.game_ChefFemaleLevel2_FrontDancing_0
                    elif self.__dancingAnimCurrentFrame == 2:
                        self.__imageClient = ResourceController.game_ChefFemaleLevel2_FrontDancing_1
                    elif self.__dancingAnimCurrentFrame == 3:
                        self.__imageClient = ResourceController.game_ChefFemaleLevel2_FrontDancing_2
                    
                elif self.level == eChefLevel.LEVEL_3_SUPER:
                    if self.__dancingAnimCurrentFrame == 1:
                        self.__imageClient = ResourceController.game_ChefFemaleLevel2_FrontDancing_0
                    elif self.__dancingAnimCurrentFrame == 2:
                        self.__imageClient = ResourceController.game_ChefFemaleLevel2_FrontDancing_1
                    elif self.__dancingAnimCurrentFrame == 3:
                        self.__imageClient = ResourceController.game_ChefFemaleLevel2_FrontDancing_2

            
        else:
        
            # Reiniciamos el conteo para mostrar la animacion del baile
            self.__dancingAnimCountdown = 20
            self.__dancingAnimCurrentFrame = 1
            self.__dancingAnimCurrentGap = 1
        
        
            if self.level == eChefLevel.LEVEL_0_NONE:
    
                if self.__gender == eCharacterGender.MALE:
                    if self.__direction == eMotionDirection.RIGHT:
                        if self.__serviceState == eChefServiceState.READY:
                            self.__imageClient = ResourceController.game_ChefMaleLevel0_RightReady
                        elif self.__serviceState == eChefServiceState.TAKING_AN_ORDER:
                            self.__imageClient = ResourceController.game_ChefMaleLevel0_RightTakingAnOrder
                        elif self.__serviceState == eChefServiceState.CARRYING_DIRTY_INGREDIENTS:
                            self.__imageClient = ResourceController.game_ChefMaleLevel0_RightCarryingDirtyIngredients
                        elif self.__serviceState == eChefServiceState.CARRYING_CLEAN_INGREDIENTS:
                            self.__imageClient = ResourceController.game_ChefMaleLevel0_RightCarryingCleanIngredients
                        elif self.__serviceState == eChefServiceState.CARRYING_PREPARED_FOOD:
                            self.__imageClient = ResourceController.game_ChefMaleLevel0_RightCarryingPreparedFood
                        elif self.__serviceState == eChefServiceState.CARRYING_DIRTY_DISHES:
                            self.__imageClient = ResourceController.game_ChefMaleLevel0_RightCarryingDirtyDishes
                            
                    elif self.__direction == eMotionDirection.LEFT:
                        if self.__serviceState == eChefServiceState.READY:
                            self.__imageClient = ResourceController.game_ChefMaleLevel0_LeftReady
                        elif self.__serviceState == eChefServiceState.TAKING_AN_ORDER:
                            self.__imageClient = ResourceController.game_ChefMaleLevel0_LeftTakingAnOrder
                        elif self.__serviceState == eChefServiceState.CARRYING_DIRTY_INGREDIENTS:
                            self.__imageClient = ResourceController.game_ChefMaleLevel0_LeftCarryingDirtyIngredients
                        elif self.__serviceState == eChefServiceState.CARRYING_CLEAN_INGREDIENTS:
                            self.__imageClient = ResourceController.game_ChefMaleLevel0_LeftCarryingCleanIngredients
                        elif self.__serviceState == eChefServiceState.CARRYING_PREPARED_FOOD:
                            self.__imageClient = ResourceController.game_ChefMaleLevel0_LeftCarryingPreparedFood
                        elif self.__serviceState == eChefServiceState.CARRYING_DIRTY_DISHES:
                            self.__imageClient = ResourceController.game_ChefMaleLevel0_LeftCarryingDirtyDishes
                            
                    elif self.__direction == eMotionDirection.UP:
                        if self.__serviceState == eChefServiceState.READY:
                            self.__imageClient = ResourceController.game_ChefMaleLevel0_BackReady
                        elif self.__serviceState == eChefServiceState.TAKING_AN_ORDER:
                            self.__imageClient = ResourceController.game_ChefMaleLevel0_BackTakingAnOrder
                        elif self.__serviceState == eChefServiceState.CARRYING_DIRTY_INGREDIENTS:
                            self.__imageClient = ResourceController.game_ChefMaleLevel0_BackCarryingDirtyIngredients
                        elif self.__serviceState == eChefServiceState.CARRYING_CLEAN_INGREDIENTS:
                            self.__imageClient = ResourceController.game_ChefMaleLevel0_BackCarryingCleanIngredients
                        elif self.__serviceState == eChefServiceState.CARRYING_PREPARED_FOOD:
                            self.__imageClient = ResourceController.game_ChefMaleLevel0_BackCarryingPreparedFood
                        elif self.__serviceState == eChefServiceState.CARRYING_DIRTY_DISHES:
                            self.__imageClient = ResourceController.game_ChefMaleLevel0_BackCarryingDirtyDishes
                            
                    elif self.__direction == eMotionDirection.DOWN:
                        if self.__serviceState == eChefServiceState.READY:
                            self.__imageClient = ResourceController.game_ChefMaleLevel0_FrontReady
                        elif self.__serviceState == eChefServiceState.TAKING_AN_ORDER:
                            self.__imageClient = ResourceController.game_ChefMaleLevel0_FrontTakingAnOrder
                        elif self.__serviceState == eChefServiceState.CARRYING_DIRTY_INGREDIENTS:
                            self.__imageClient = ResourceController.game_ChefMaleLevel0_FrontCarryingDirtyIngredients
                        elif self.__serviceState == eChefServiceState.CARRYING_CLEAN_INGREDIENTS:
                            self.__imageClient = ResourceController.game_ChefMaleLevel0_FrontCarryingCleanIngredients
                        elif self.__serviceState == eChefServiceState.CARRYING_PREPARED_FOOD:
                            self.__imageClient = ResourceController.game_ChefMaleLevel0_FrontCarryingPreparedFood
                        elif self.__serviceState == eChefServiceState.CARRYING_DIRTY_DISHES:
                            self.__imageClient = ResourceController.game_ChefMaleLevel0_FrontCarryingDirtyDishes
                            
                elif self.__gender == eCharacterGender.FEMALE:
                    if self.__direction == eMotionDirection.RIGHT:
                        if self.__serviceState == eChefServiceState.READY:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel0_RightReady
                        elif self.__serviceState == eChefServiceState.TAKING_AN_ORDER:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel0_RightTakingAnOrder
                        elif self.__serviceState == eChefServiceState.CARRYING_DIRTY_INGREDIENTS:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel0_RightCarryingDirtyIngredients
                        elif self.__serviceState == eChefServiceState.CARRYING_CLEAN_INGREDIENTS:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel0_RightCarryingCleanIngredients
                        elif self.__serviceState == eChefServiceState.CARRYING_PREPARED_FOOD:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel0_RightCarryingPreparedFood
                        elif self.__serviceState == eChefServiceState.CARRYING_DIRTY_DISHES:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel0_RightCarryingDirtyDishes
                            
                    elif self.__direction == eMotionDirection.LEFT:
                        if self.__serviceState == eChefServiceState.READY:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel0_LeftReady
                        elif self.__serviceState == eChefServiceState.TAKING_AN_ORDER:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel0_LeftTakingAnOrder
                        elif self.__serviceState == eChefServiceState.CARRYING_DIRTY_INGREDIENTS:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel0_LeftCarryingDirtyIngredients
                        elif self.__serviceState == eChefServiceState.CARRYING_CLEAN_INGREDIENTS:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel0_LeftCarryingCleanIngredients
                        elif self.__serviceState == eChefServiceState.CARRYING_PREPARED_FOOD:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel0_LeftCarryingPreparedFood
                        elif self.__serviceState == eChefServiceState.CARRYING_DIRTY_DISHES:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel0_LeftCarryingDirtyDishes
                            
                    elif self.__direction == eMotionDirection.UP:
                        if self.__serviceState == eChefServiceState.READY:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel0_BackReady
                        elif self.__serviceState == eChefServiceState.TAKING_AN_ORDER:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel0_BackTakingAnOrder
                        elif self.__serviceState == eChefServiceState.CARRYING_DIRTY_INGREDIENTS:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel0_BackCarryingDirtyIngredients
                        elif self.__serviceState == eChefServiceState.CARRYING_CLEAN_INGREDIENTS:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel0_BackCarryingCleanIngredients
                        elif self.__serviceState == eChefServiceState.CARRYING_PREPARED_FOOD:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel0_BackCarryingPreparedFood
                        elif self.__serviceState == eChefServiceState.CARRYING_DIRTY_DISHES:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel0_BackCarryingDirtyDishes
                            
                    elif self.__direction == eMotionDirection.DOWN:
                        if self.__serviceState == eChefServiceState.READY:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel0_FrontReady
                        elif self.__serviceState == eChefServiceState.TAKING_AN_ORDER:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel0_FrontTakingAnOrder
                        elif self.__serviceState == eChefServiceState.CARRYING_DIRTY_INGREDIENTS:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel0_FrontCarryingDirtyIngredients
                        elif self.__serviceState == eChefServiceState.CARRYING_CLEAN_INGREDIENTS:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel0_FrontCarryingCleanIngredients
                        elif self.__serviceState == eChefServiceState.CARRYING_PREPARED_FOOD:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel0_FrontCarryingPreparedFood
                        elif self.__serviceState == eChefServiceState.CARRYING_DIRTY_DISHES:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel0_FrontCarryingDirtyDishes
                      
            
            elif self.level == eChefLevel.LEVEL_1_JUNIOR:
                
                if self.__gender == eCharacterGender.MALE:
                    if self.__direction == eMotionDirection.RIGHT:
                        if self.__serviceState == eChefServiceState.READY:
                            self.__imageClient = ResourceController.game_ChefMaleLevel1_RightReady
                        elif self.__serviceState == eChefServiceState.TAKING_AN_ORDER:
                            self.__imageClient = ResourceController.game_ChefMaleLevel1_RightTakingAnOrder
                        elif self.__serviceState == eChefServiceState.CARRYING_DIRTY_INGREDIENTS:
                            self.__imageClient = ResourceController.game_ChefMaleLevel1_RightCarryingDirtyIngredients
                        elif self.__serviceState == eChefServiceState.CARRYING_CLEAN_INGREDIENTS:
                            self.__imageClient = ResourceController.game_ChefMaleLevel1_RightCarryingCleanIngredients
                        elif self.__serviceState == eChefServiceState.CARRYING_PREPARED_FOOD:
                            self.__imageClient = ResourceController.game_ChefMaleLevel1_RightCarryingPreparedFood
                        elif self.__serviceState == eChefServiceState.CARRYING_DIRTY_DISHES:
                            self.__imageClient = ResourceController.game_ChefMaleLevel1_RightCarryingDirtyDishes
                            
                    elif self.__direction == eMotionDirection.LEFT:
                        if self.__serviceState == eChefServiceState.READY:
                            self.__imageClient = ResourceController.game_ChefMaleLevel1_LeftReady
                        elif self.__serviceState == eChefServiceState.TAKING_AN_ORDER:
                            self.__imageClient = ResourceController.game_ChefMaleLevel1_LeftTakingAnOrder
                        elif self.__serviceState == eChefServiceState.CARRYING_DIRTY_INGREDIENTS:
                            self.__imageClient = ResourceController.game_ChefMaleLevel1_LeftCarryingDirtyIngredients
                        elif self.__serviceState == eChefServiceState.CARRYING_CLEAN_INGREDIENTS:
                            self.__imageClient = ResourceController.game_ChefMaleLevel1_LeftCarryingCleanIngredients
                        elif self.__serviceState == eChefServiceState.CARRYING_PREPARED_FOOD:
                            self.__imageClient = ResourceController.game_ChefMaleLevel1_LeftCarryingPreparedFood
                        elif self.__serviceState == eChefServiceState.CARRYING_DIRTY_DISHES:
                            self.__imageClient = ResourceController.game_ChefMaleLevel1_LeftCarryingDirtyDishes
                            
                    elif self.__direction == eMotionDirection.UP:
                        if self.__serviceState == eChefServiceState.READY:
                            self.__imageClient = ResourceController.game_ChefMaleLevel1_BackReady
                        elif self.__serviceState == eChefServiceState.TAKING_AN_ORDER:
                            self.__imageClient = ResourceController.game_ChefMaleLevel1_BackTakingAnOrder
                        elif self.__serviceState == eChefServiceState.CARRYING_DIRTY_INGREDIENTS:
                            self.__imageClient = ResourceController.game_ChefMaleLevel1_BackCarryingDirtyIngredients
                        elif self.__serviceState == eChefServiceState.CARRYING_CLEAN_INGREDIENTS:
                            self.__imageClient = ResourceController.game_ChefMaleLevel1_BackCarryingCleanIngredients
                        elif self.__serviceState == eChefServiceState.CARRYING_PREPARED_FOOD:
                            self.__imageClient = ResourceController.game_ChefMaleLevel1_BackCarryingPreparedFood
                        elif self.__serviceState == eChefServiceState.CARRYING_DIRTY_DISHES:
                            self.__imageClient = ResourceController.game_ChefMaleLevel1_BackCarryingDirtyDishes
                            
                    elif self.__direction == eMotionDirection.DOWN:
                        if self.__serviceState == eChefServiceState.READY:
                            self.__imageClient = ResourceController.game_ChefMaleLevel1_FrontReady
                        elif self.__serviceState == eChefServiceState.TAKING_AN_ORDER:
                            self.__imageClient = ResourceController.game_ChefMaleLevel1_FrontTakingAnOrder
                        elif self.__serviceState == eChefServiceState.CARRYING_DIRTY_INGREDIENTS:
                            self.__imageClient = ResourceController.game_ChefMaleLevel1_FrontCarryingDirtyIngredients
                        elif self.__serviceState == eChefServiceState.CARRYING_CLEAN_INGREDIENTS:
                            self.__imageClient = ResourceController.game_ChefMaleLevel1_FrontCarryingCleanIngredients
                        elif self.__serviceState == eChefServiceState.CARRYING_PREPARED_FOOD:
                            self.__imageClient = ResourceController.game_ChefMaleLevel1_FrontCarryingPreparedFood
                        elif self.__serviceState == eChefServiceState.CARRYING_DIRTY_DISHES:
                            self.__imageClient = ResourceController.game_ChefMaleLevel1_FrontCarryingDirtyDishes
                            
                elif self.__gender == eCharacterGender.FEMALE:
                    if self.__direction == eMotionDirection.RIGHT:
                        if self.__serviceState == eChefServiceState.READY:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel1_RightReady
                        elif self.__serviceState == eChefServiceState.TAKING_AN_ORDER:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel1_RightTakingAnOrder
                        elif self.__serviceState == eChefServiceState.CARRYING_DIRTY_INGREDIENTS:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel1_RightCarryingDirtyIngredients
                        elif self.__serviceState == eChefServiceState.CARRYING_CLEAN_INGREDIENTS:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel1_RightCarryingCleanIngredients
                        elif self.__serviceState == eChefServiceState.CARRYING_PREPARED_FOOD:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel1_RightCarryingPreparedFood
                        elif self.__serviceState == eChefServiceState.CARRYING_DIRTY_DISHES:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel1_RightCarryingDirtyDishes
                            
                    elif self.__direction == eMotionDirection.LEFT:
                        if self.__serviceState == eChefServiceState.READY:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel1_LeftReady
                        elif self.__serviceState == eChefServiceState.TAKING_AN_ORDER:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel1_LeftTakingAnOrder
                        elif self.__serviceState == eChefServiceState.CARRYING_DIRTY_INGREDIENTS:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel1_LeftCarryingDirtyIngredients
                        elif self.__serviceState == eChefServiceState.CARRYING_CLEAN_INGREDIENTS:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel1_LeftCarryingCleanIngredients
                        elif self.__serviceState == eChefServiceState.CARRYING_PREPARED_FOOD:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel1_LeftCarryingPreparedFood
                        elif self.__serviceState == eChefServiceState.CARRYING_DIRTY_DISHES:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel1_LeftCarryingDirtyDishes
                            
                    elif self.__direction == eMotionDirection.UP:
                        if self.__serviceState == eChefServiceState.READY:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel1_BackReady
                        elif self.__serviceState == eChefServiceState.TAKING_AN_ORDER:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel1_BackTakingAnOrder
                        elif self.__serviceState == eChefServiceState.CARRYING_DIRTY_INGREDIENTS:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel1_BackCarryingDirtyIngredients
                        elif self.__serviceState == eChefServiceState.CARRYING_CLEAN_INGREDIENTS:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel1_BackCarryingCleanIngredients
                        elif self.__serviceState == eChefServiceState.CARRYING_PREPARED_FOOD:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel1_BackCarryingPreparedFood
                        elif self.__serviceState == eChefServiceState.CARRYING_DIRTY_DISHES:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel1_BackCarryingDirtyDishes
                            
                    elif self.__direction == eMotionDirection.DOWN:
                        if self.__serviceState == eChefServiceState.READY:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel1_FrontReady
                        elif self.__serviceState == eChefServiceState.TAKING_AN_ORDER:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel1_FrontTakingAnOrder
                        elif self.__serviceState == eChefServiceState.CARRYING_DIRTY_INGREDIENTS:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel1_FrontCarryingDirtyIngredients
                        elif self.__serviceState == eChefServiceState.CARRYING_CLEAN_INGREDIENTS:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel1_FrontCarryingCleanIngredients
                        elif self.__serviceState == eChefServiceState.CARRYING_PREPARED_FOOD:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel1_FrontCarryingPreparedFood
                        elif self.__serviceState == eChefServiceState.CARRYING_DIRTY_DISHES:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel1_FrontCarryingDirtyDishes
                      
                
            elif self.level == eChefLevel.LEVEL_2_SENIOR:
                
                if self.__gender == eCharacterGender.MALE:
                    if self.__direction == eMotionDirection.RIGHT:
                        if self.__serviceState == eChefServiceState.READY:
                            self.__imageClient = ResourceController.game_ChefMaleLevel2_RightReady
                        elif self.__serviceState == eChefServiceState.TAKING_AN_ORDER:
                            self.__imageClient = ResourceController.game_ChefMaleLevel2_RightTakingAnOrder
                        elif self.__serviceState == eChefServiceState.CARRYING_DIRTY_INGREDIENTS:
                            self.__imageClient = ResourceController.game_ChefMaleLevel2_RightCarryingDirtyIngredients
                        elif self.__serviceState == eChefServiceState.CARRYING_CLEAN_INGREDIENTS:
                            self.__imageClient = ResourceController.game_ChefMaleLevel2_RightCarryingCleanIngredients
                        elif self.__serviceState == eChefServiceState.CARRYING_PREPARED_FOOD:
                            self.__imageClient = ResourceController.game_ChefMaleLevel2_RightCarryingPreparedFood
                        elif self.__serviceState == eChefServiceState.CARRYING_DIRTY_DISHES:
                            self.__imageClient = ResourceController.game_ChefMaleLevel2_RightCarryingDirtyDishes
                            
                    elif self.__direction == eMotionDirection.LEFT:
                        if self.__serviceState == eChefServiceState.READY:
                            self.__imageClient = ResourceController.game_ChefMaleLevel2_LeftReady
                        elif self.__serviceState == eChefServiceState.TAKING_AN_ORDER:
                            self.__imageClient = ResourceController.game_ChefMaleLevel2_LeftTakingAnOrder
                        elif self.__serviceState == eChefServiceState.CARRYING_DIRTY_INGREDIENTS:
                            self.__imageClient = ResourceController.game_ChefMaleLevel2_LeftCarryingDirtyIngredients
                        elif self.__serviceState == eChefServiceState.CARRYING_CLEAN_INGREDIENTS:
                            self.__imageClient = ResourceController.game_ChefMaleLevel2_LeftCarryingCleanIngredients
                        elif self.__serviceState == eChefServiceState.CARRYING_PREPARED_FOOD:
                            self.__imageClient = ResourceController.game_ChefMaleLevel2_LeftCarryingPreparedFood
                        elif self.__serviceState == eChefServiceState.CARRYING_DIRTY_DISHES:
                            self.__imageClient = ResourceController.game_ChefMaleLevel2_LeftCarryingDirtyDishes
                            
                    elif self.__direction == eMotionDirection.UP:
                        if self.__serviceState == eChefServiceState.READY:
                            self.__imageClient = ResourceController.game_ChefMaleLevel2_BackReady
                        elif self.__serviceState == eChefServiceState.TAKING_AN_ORDER:
                            self.__imageClient = ResourceController.game_ChefMaleLevel2_BackTakingAnOrder
                        elif self.__serviceState == eChefServiceState.CARRYING_DIRTY_INGREDIENTS:
                            self.__imageClient = ResourceController.game_ChefMaleLevel2_BackCarryingDirtyIngredients
                        elif self.__serviceState == eChefServiceState.CARRYING_CLEAN_INGREDIENTS:
                            self.__imageClient = ResourceController.game_ChefMaleLevel2_BackCarryingCleanIngredients
                        elif self.__serviceState == eChefServiceState.CARRYING_PREPARED_FOOD:
                            self.__imageClient = ResourceController.game_ChefMaleLevel2_BackCarryingPreparedFood
                        elif self.__serviceState == eChefServiceState.CARRYING_DIRTY_DISHES:
                            self.__imageClient = ResourceController.game_ChefMaleLevel2_BackCarryingDirtyDishes
                            
                    elif self.__direction == eMotionDirection.DOWN:
                        if self.__serviceState == eChefServiceState.READY:
                            self.__imageClient = ResourceController.game_ChefMaleLevel2_FrontReady
                        elif self.__serviceState == eChefServiceState.TAKING_AN_ORDER:
                            self.__imageClient = ResourceController.game_ChefMaleLevel2_FrontTakingAnOrder
                        elif self.__serviceState == eChefServiceState.CARRYING_DIRTY_INGREDIENTS:
                            self.__imageClient = ResourceController.game_ChefMaleLevel2_FrontCarryingDirtyIngredients
                        elif self.__serviceState == eChefServiceState.CARRYING_CLEAN_INGREDIENTS:
                            self.__imageClient = ResourceController.game_ChefMaleLevel2_FrontCarryingCleanIngredients
                        elif self.__serviceState == eChefServiceState.CARRYING_PREPARED_FOOD:
                            self.__imageClient = ResourceController.game_ChefMaleLevel2_FrontCarryingPreparedFood
                        elif self.__serviceState == eChefServiceState.CARRYING_DIRTY_DISHES:
                            self.__imageClient = ResourceController.game_ChefMaleLevel2_FrontCarryingDirtyDishes
                            
                elif self.__gender == eCharacterGender.FEMALE:
                    if self.__direction == eMotionDirection.RIGHT:
                        if self.__serviceState == eChefServiceState.READY:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel2_RightReady
                        elif self.__serviceState == eChefServiceState.TAKING_AN_ORDER:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel2_RightTakingAnOrder
                        elif self.__serviceState == eChefServiceState.CARRYING_DIRTY_INGREDIENTS:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel2_RightCarryingDirtyIngredients
                        elif self.__serviceState == eChefServiceState.CARRYING_CLEAN_INGREDIENTS:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel2_RightCarryingCleanIngredients
                        elif self.__serviceState == eChefServiceState.CARRYING_PREPARED_FOOD:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel2_RightCarryingPreparedFood
                        elif self.__serviceState == eChefServiceState.CARRYING_DIRTY_DISHES:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel2_RightCarryingDirtyDishes
                            
                    elif self.__direction == eMotionDirection.LEFT:
                        if self.__serviceState == eChefServiceState.READY:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel2_LeftReady
                        elif self.__serviceState == eChefServiceState.TAKING_AN_ORDER:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel2_LeftTakingAnOrder
                        elif self.__serviceState == eChefServiceState.CARRYING_DIRTY_INGREDIENTS:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel2_LeftCarryingDirtyIngredients
                        elif self.__serviceState == eChefServiceState.CARRYING_CLEAN_INGREDIENTS:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel2_LeftCarryingCleanIngredients
                        elif self.__serviceState == eChefServiceState.CARRYING_PREPARED_FOOD:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel2_LeftCarryingPreparedFood
                        elif self.__serviceState == eChefServiceState.CARRYING_DIRTY_DISHES:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel2_LeftCarryingDirtyDishes
                            
                    elif self.__direction == eMotionDirection.UP:
                        if self.__serviceState == eChefServiceState.READY:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel2_BackReady
                        elif self.__serviceState == eChefServiceState.TAKING_AN_ORDER:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel2_BackTakingAnOrder
                        elif self.__serviceState == eChefServiceState.CARRYING_DIRTY_INGREDIENTS:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel2_BackCarryingDirtyIngredients
                        elif self.__serviceState == eChefServiceState.CARRYING_CLEAN_INGREDIENTS:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel2_BackCarryingCleanIngredients
                        elif self.__serviceState == eChefServiceState.CARRYING_PREPARED_FOOD:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel2_BackCarryingPreparedFood
                        elif self.__serviceState == eChefServiceState.CARRYING_DIRTY_DISHES:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel2_BackCarryingDirtyDishes
                            
                    elif self.__direction == eMotionDirection.DOWN:
                        if self.__serviceState == eChefServiceState.READY:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel2_FrontReady
                        elif self.__serviceState == eChefServiceState.TAKING_AN_ORDER:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel2_FrontTakingAnOrder
                        elif self.__serviceState == eChefServiceState.CARRYING_DIRTY_INGREDIENTS:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel2_FrontCarryingDirtyIngredients
                        elif self.__serviceState == eChefServiceState.CARRYING_CLEAN_INGREDIENTS:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel2_FrontCarryingCleanIngredients
                        elif self.__serviceState == eChefServiceState.CARRYING_PREPARED_FOOD:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel2_FrontCarryingPreparedFood
                        elif self.__serviceState == eChefServiceState.CARRYING_DIRTY_DISHES:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel2_FrontCarryingDirtyDishes
                      
                   
            elif self.level == eChefLevel.LEVEL_3_SUPER:
            
                if self.__gender == eCharacterGender.MALE:
                    if self.__direction == eMotionDirection.RIGHT:
                        if self.__serviceState == eChefServiceState.READY:
                            self.__imageClient = ResourceController.game_ChefMaleLevel2_RightReady
                        elif self.__serviceState == eChefServiceState.TAKING_AN_ORDER:
                            self.__imageClient = ResourceController.game_ChefMaleLevel2_RightTakingAnOrder
                        elif self.__serviceState == eChefServiceState.CARRYING_DIRTY_INGREDIENTS:
                            self.__imageClient = ResourceController.game_ChefMaleLevel2_RightCarryingDirtyIngredients
                        elif self.__serviceState == eChefServiceState.CARRYING_CLEAN_INGREDIENTS:
                            self.__imageClient = ResourceController.game_ChefMaleLevel2_RightCarryingCleanIngredients
                        elif self.__serviceState == eChefServiceState.CARRYING_PREPARED_FOOD:
                            self.__imageClient = ResourceController.game_ChefMaleLevel2_RightCarryingPreparedFood
                        elif self.__serviceState == eChefServiceState.CARRYING_DIRTY_DISHES:
                            self.__imageClient = ResourceController.game_ChefMaleLevel2_RightCarryingDirtyDishes
                            
                    elif self.__direction == eMotionDirection.LEFT:
                        if self.__serviceState == eChefServiceState.READY:
                            self.__imageClient = ResourceController.game_ChefMaleLevel2_LeftReady
                        elif self.__serviceState == eChefServiceState.TAKING_AN_ORDER:
                            self.__imageClient = ResourceController.game_ChefMaleLevel2_LeftTakingAnOrder
                        elif self.__serviceState == eChefServiceState.CARRYING_DIRTY_INGREDIENTS:
                            self.__imageClient = ResourceController.game_ChefMaleLevel2_LeftCarryingDirtyIngredients
                        elif self.__serviceState == eChefServiceState.CARRYING_CLEAN_INGREDIENTS:
                            self.__imageClient = ResourceController.game_ChefMaleLevel2_LeftCarryingCleanIngredients
                        elif self.__serviceState == eChefServiceState.CARRYING_PREPARED_FOOD:
                            self.__imageClient = ResourceController.game_ChefMaleLevel2_LeftCarryingPreparedFood
                        elif self.__serviceState == eChefServiceState.CARRYING_DIRTY_DISHES:
                            self.__imageClient = ResourceController.game_ChefMaleLevel2_LeftCarryingDirtyDishes
                            
                    elif self.__direction == eMotionDirection.UP:
                        if self.__serviceState == eChefServiceState.READY:
                            self.__imageClient = ResourceController.game_ChefMaleLevel2_BackReady
                        elif self.__serviceState == eChefServiceState.TAKING_AN_ORDER:
                            self.__imageClient = ResourceController.game_ChefMaleLevel2_BackTakingAnOrder
                        elif self.__serviceState == eChefServiceState.CARRYING_DIRTY_INGREDIENTS:
                            self.__imageClient = ResourceController.game_ChefMaleLevel2_BackCarryingDirtyIngredients
                        elif self.__serviceState == eChefServiceState.CARRYING_CLEAN_INGREDIENTS:
                            self.__imageClient = ResourceController.game_ChefMaleLevel2_BackCarryingCleanIngredients
                        elif self.__serviceState == eChefServiceState.CARRYING_PREPARED_FOOD:
                            self.__imageClient = ResourceController.game_ChefMaleLevel2_BackCarryingPreparedFood
                        elif self.__serviceState == eChefServiceState.CARRYING_DIRTY_DISHES:
                            self.__imageClient = ResourceController.game_ChefMaleLevel2_BackCarryingDirtyDishes
                            
                    elif self.__direction == eMotionDirection.DOWN:
                        if self.__serviceState == eChefServiceState.READY:
                            self.__imageClient = ResourceController.game_ChefMaleLevel2_FrontReady
                        elif self.__serviceState == eChefServiceState.TAKING_AN_ORDER:
                            self.__imageClient = ResourceController.game_ChefMaleLevel2_FrontTakingAnOrder
                        elif self.__serviceState == eChefServiceState.CARRYING_DIRTY_INGREDIENTS:
                            self.__imageClient = ResourceController.game_ChefMaleLevel2_FrontCarryingDirtyIngredients
                        elif self.__serviceState == eChefServiceState.CARRYING_CLEAN_INGREDIENTS:
                            self.__imageClient = ResourceController.game_ChefMaleLevel2_FrontCarryingCleanIngredients
                        elif self.__serviceState == eChefServiceState.CARRYING_PREPARED_FOOD:
                            self.__imageClient = ResourceController.game_ChefMaleLevel2_FrontCarryingPreparedFood
                        elif self.__serviceState == eChefServiceState.CARRYING_DIRTY_DISHES:
                            self.__imageClient = ResourceController.game_ChefMaleLevel2_FrontCarryingDirtyDishes
                            
                elif self.__gender == eCharacterGender.FEMALE:
                    if self.__direction == eMotionDirection.RIGHT:
                        if self.__serviceState == eChefServiceState.READY:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel2_RightReady
                        elif self.__serviceState == eChefServiceState.TAKING_AN_ORDER:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel2_RightTakingAnOrder
                        elif self.__serviceState == eChefServiceState.CARRYING_DIRTY_INGREDIENTS:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel2_RightCarryingDirtyIngredients
                        elif self.__serviceState == eChefServiceState.CARRYING_CLEAN_INGREDIENTS:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel2_RightCarryingCleanIngredients
                        elif self.__serviceState == eChefServiceState.CARRYING_PREPARED_FOOD:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel2_RightCarryingPreparedFood
                        elif self.__serviceState == eChefServiceState.CARRYING_DIRTY_DISHES:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel2_RightCarryingDirtyDishes
                            
                    elif self.__direction == eMotionDirection.LEFT:
                        if self.__serviceState == eChefServiceState.READY:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel2_LeftReady
                        elif self.__serviceState == eChefServiceState.TAKING_AN_ORDER:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel2_LeftTakingAnOrder
                        elif self.__serviceState == eChefServiceState.CARRYING_DIRTY_INGREDIENTS:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel2_LeftCarryingDirtyIngredients
                        elif self.__serviceState == eChefServiceState.CARRYING_CLEAN_INGREDIENTS:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel2_LeftCarryingCleanIngredients
                        elif self.__serviceState == eChefServiceState.CARRYING_PREPARED_FOOD:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel2_LeftCarryingPreparedFood
                        elif self.__serviceState == eChefServiceState.CARRYING_DIRTY_DISHES:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel2_LeftCarryingDirtyDishes
                            
                    elif self.__direction == eMotionDirection.UP:
                        if self.__serviceState == eChefServiceState.READY:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel2_BackReady
                        elif self.__serviceState == eChefServiceState.TAKING_AN_ORDER:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel2_BackTakingAnOrder
                        elif self.__serviceState == eChefServiceState.CARRYING_DIRTY_INGREDIENTS:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel2_BackCarryingDirtyIngredients
                        elif self.__serviceState == eChefServiceState.CARRYING_CLEAN_INGREDIENTS:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel2_BackCarryingCleanIngredients
                        elif self.__serviceState == eChefServiceState.CARRYING_PREPARED_FOOD:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel2_BackCarryingPreparedFood
                        elif self.__serviceState == eChefServiceState.CARRYING_DIRTY_DISHES:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel2_BackCarryingDirtyDishes
                            
                    elif self.__direction == eMotionDirection.DOWN:
                        if self.__serviceState == eChefServiceState.READY:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel2_FrontReady
                        elif self.__serviceState == eChefServiceState.TAKING_AN_ORDER:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel2_FrontTakingAnOrder
                        elif self.__serviceState == eChefServiceState.CARRYING_DIRTY_INGREDIENTS:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel2_FrontCarryingDirtyIngredients
                        elif self.__serviceState == eChefServiceState.CARRYING_CLEAN_INGREDIENTS:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel2_FrontCarryingCleanIngredients
                        elif self.__serviceState == eChefServiceState.CARRYING_PREPARED_FOOD:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel2_FrontCarryingPreparedFood
                        elif self.__serviceState == eChefServiceState.CARRYING_DIRTY_DISHES:
                            self.__imageClient = ResourceController.game_ChefFemaleLevel2_FrontCarryingDirtyDishes
                      
                  
        # Calculamos si se debe mostrar la nube con el pedido
        if (self.__serviceState == eChefServiceState.CARRYING_PREPARED_FOOD) and (self.__clientFoodIsPreparing != None):
            self.__imageCloud = ResourceController.game_Cloud
            self.__imageRecipe = self.__clientFoodIsPreparing.getRecipeWanted().image
        else:
            self.__imageCloud = None
            self.__imageRecipe = None
                
        # Calculamos si se debe mostrar la animacion cuando lava las manos
        if (self.__mainState == eChefMainState.DOING_ORDER) and (self.__command == eChefCommand.WASH_HANDS) and (self.__serviceState == eChefServiceState.READY):
            if self.__washHandsCurrentFrame == 1:
                self.__imageWashingHands = ResourceController.game_WashingHands_1
            elif self.__washHandsCurrentFrame == 2:
                self.__imageWashingHands = ResourceController.game_WashingHands_2
                
        else:
            self.__imageWashingHands = None
        
        # Calculamos si se debe mostrar la animacion cuando lava los ingredientes
        if (self.__mainState == eChefMainState.DOING_ORDER) and (self.__command == eChefCommand.WASH_INGREDIENTS) and (self.__serviceState == eChefServiceState.CARRYING_DIRTY_INGREDIENTS):
            if self.__washIngredientsCurrentFrame == 1:
                self.__imageWashingIngredients = ResourceController.game_WashingIngredients_1
            elif self.__washIngredientsCurrentFrame == 2:
                self.__imageWashingIngredients = ResourceController.game_WashingIngredients_2
            
        else:
            self.__imageWashingIngredients = None
            
        # Calculamos si se debe mostrar la animacion cuando lava los platos sucios
        if (self.__mainState == eChefMainState.DOING_ORDER) and (self.__command == eChefCommand.WASH_DIRTY_DISHES) and (self.__serviceState == eChefServiceState.CARRYING_DIRTY_DISHES):
            if self.__washingDishesCurrentFrame == 1:
                self.__imageWashingDishes = ResourceController.game_WashingDishes_1
            elif self.__washingDishesCurrentFrame == 2:
                self.__imageWashingDishes = ResourceController.game_WashingDishes_2
                            
        else:
            self.__imageWashingDishes = None
            
        # Calculamos si se debe mostrar la animacion cuando los ingredientes son cocinados
        if self.__cookingState == eChefCookingState.COOKING:
            
            if self.__clientFoodIsPreparing.getRecipeWanted().preparation == eRecipePreparation.HOT:
                if self.__cookingAnimCurrentFrame == 1:
                    self.__imageCooking = ResourceController.game_CookingHot_1
                elif self.__cookingAnimCurrentFrame == 2:
                    self.__imageCooking = ResourceController.game_CookingHot_2
                elif self.__cookingAnimCurrentFrame == 3:
                    self.__imageCooking = ResourceController.game_CookingHot_3
                elif self.__cookingAnimCurrentFrame == 4:
                    self.__imageCooking = ResourceController.game_CookingHot_4
                    
            elif self.__clientFoodIsPreparing.getRecipeWanted().preparation == eRecipePreparation.COLD:
                if self.__cookingAnimCurrentFrame == 1:
                    self.__imageCooking = ResourceController.game_CookingCold_1
                elif self.__cookingAnimCurrentFrame == 2:
                    self.__imageCooking = ResourceController.game_CookingCold_2
                elif self.__cookingAnimCurrentFrame == 3:
                    self.__imageCooking = ResourceController.game_CookingCold_3
                elif self.__cookingAnimCurrentFrame == 4:
                    self.__imageCooking = ResourceController.game_CookingCold_4
                    
        elif self.__cookingState == eChefCookingState.DISH_PREPARED_AND_READY_TO_SERVE:
            self.__imageCooking = ResourceController.game_DishFull
        else:
            self.__imageCooking = None
    
    def calculateCommand(self, selectedMotionPointId, selectedClientOnTable):
        
        # Definimos el camino a tomar de acuerdo al estado general del chef  
        if self.__mainState == eChefMainState.DOING_ORDER:
            
            # El chef esta ejecutando una orden y no se le puede interrumpir
            return
        
        elif self.__mainState == eChefMainState.MOVING:
            
            # El chef se esta moviendo en el restaurante y no se le puede interrumpir
            return
        
        elif self.__mainState == eChefMainState.NO_MOTION:
            
            # Le indicamos al chef que comience a moverse hacia el bloque objetivo
             
            # Indicamos el nuevo objetivo a alcanzar
            self.__targetMotionPointId = selectedMotionPointId
            
            # Reiniciamos las variables auxiliares del subcamino
            self.__nextMotionPointId = None
            self.__direction = eMotionDirection.DOWN
            
            # Determinamos si el punto objetivo esta la izquierda o derecha del punto actual
            columnStart = self.__motionPoints.get(self.__currentMotionPointId).getColumn()
            columnEnd = self.__motionPoints.get(self.__targetMotionPointId).getColumn()
            
            if columnStart <= columnEnd:
                # Punto objetivo a la derecha
                self.__chefToTargetInitDirection = eMotionDirection.RIGHT
            else:
                # Punto objetivo a la izquierda
                self.__chefToTargetInitDirection = eMotionDirection.LEFT
                
            # Indicamos que el Chef comienza a moverse
            self.__mainState = eChefMainState.MOVING
            
            # Inicialmente no hay orden concreta
            self.__command = None

            # Determinamos si el bloque elegido implica la creacion de una orden, de acuerdo al target y al estado de servicio
                
            # Caso A: Seleccion de Estufa
            if self.__targetMotionPointId == eMotionBlock.ROW1_STOVE:
                if self.__serviceState == eChefServiceState.CARRYING_CLEAN_INGREDIENTS:
                    self.__command = eChefCommand.COOK_INGREDIENTS
                elif (self.__serviceState == eChefServiceState.READY) and (self.__cookingState == eChefCookingState.DISH_PREPARED_AND_READY_TO_SERVE):
                    self.__command = eChefCommand.PICK_PREPARED_FOOD
            
            # Caso B: Seleccion de Lavamanos y Lavaalimentos
            elif self.__targetMotionPointId == eMotionBlock.ROW1_SINK:
                if self.__serviceState == eChefServiceState.CARRYING_DIRTY_INGREDIENTS:
                    self.__command = eChefCommand.WASH_INGREDIENTS
                    
                elif self.__serviceState == eChefServiceState.READY:
                    self.__command = eChefCommand.WASH_HANDS
                    self.__serviceState = eChefServiceState.READY
                        
            # Caso C: Seleccion de Nevera
            elif self.__targetMotionPointId == eMotionBlock.ROW1_FRIDGE:
                if (self.__serviceState == eChefServiceState.READY) and (self.__hasCleanHands == True) and (len(self.__clientsWithActiveOrders) > 0) and (self.__cookingState == None):
                    self.__command = eChefCommand.SELECT_ORDER
                        
            # Caso D: Seleccion de Lavaplatos
            elif self.__targetMotionPointId == eMotionBlock.ROW1_DISHWASHER:
                if self.__serviceState == eChefServiceState.CARRYING_DIRTY_DISHES:
                    self.__command = eChefCommand.WASH_DIRTY_DISHES
            
            # Caso F: Seleccion de cualquier mesa
            elif (selectedMotionPointId == eMotionBlock.ROW2_BLOCK_A) or (selectedMotionPointId == eMotionBlock.ROW2_BLOCK_B) \
                or (selectedMotionPointId == eMotionBlock.ROW2_BLOCK_C) or (selectedMotionPointId == eMotionBlock.ROW2_BLOCK_D) \
                or (selectedMotionPointId == eMotionBlock.ROW3_BLOCK_E) or (selectedMotionPointId == eMotionBlock.ROW3_BLOCK_F) \
                or (selectedMotionPointId == eMotionBlock.ROW3_BLOCK_G) or (selectedMotionPointId == eMotionBlock.ROW3_BLOCK_H):
                
                # En caso de que la mesa tenga un cliente...
                if selectedClientOnTable != None:
                    
                    # Sub-Caso F1: Cliente solicitando servicio
                    if selectedClientOnTable.getServiceState() == eClientServiceState.REQUESTING_FOR_ORDER:
                        
                        # Sub-Caso F1-1: Chef esta disponible para tomar orden
                        if (self.__serviceState == eChefServiceState.READY) or (self.__serviceState == eChefServiceState.TAKING_AN_ORDER):
                            
                            # Si el chef no tiene ya asignado un cliente...
                            if self.__clientSelected == None:
                            
                                # Creamos la orden
                                self.__command = eChefCommand.TAKE_ORDER
                                self.__serviceState = eChefServiceState.TAKING_AN_ORDER
                                self.__clientSelected = selectedClientOnTable
                                self.__clientsWithActiveOrders.append(selectedClientOnTable)
                              
                    # Sub-Caso F2: Cliente esperando por la comida preparada
                    elif selectedClientOnTable.getServiceState() == eClientServiceState.WAITING_FOR_FOOD:
                                 
                        # Sub-Caso F2-1: Chef tiene comida preparada
                        if self.__serviceState == eChefServiceState.CARRYING_PREPARED_FOOD:
                            
                            # Si el plato que se lleva corresponde al cliente que lo pidio
                            if selectedClientOnTable.id == self.__clientFoodIsPreparing.id:
                                
                                # Creamos la orden
                                self.__command = eChefCommand.SERVE_PREPARED_FOOD
                                self.__clientSelected = selectedClientOnTable
                                
                                # Ya no necesitamos la referencia al cliente que pido el plato
                                self.__clientFoodIsPreparing = None
                    
                    # SubCaso F3: Cliente solicitando que retiren los platos
                    elif (selectedClientOnTable.getServiceState() == eClientServiceState.LEAVING) or (selectedClientOnTable.getServiceState() == eClientServiceState.ONLY_DIRTY_DISHES_LEFT):
                    
                        # Sub-Caso F3-1: Chef esta disponible para tomar orden
                        if self.__serviceState == eChefServiceState.READY:
                            
                            # Si el chef no tiene ya asignado un cliente...
                            if self.__clientSelected == None:
                            
                                # Creamos la orden
                                self.__command = eChefCommand.PICK_DIRTY_DISHES
                                self.__clientSelected = selectedClientOnTable
    
    def newLevelAnnounced(self):
        self.hasReachNewlevel = False
            
    def orderSelected(self, selectedClient):
        
        # Si la orden actual es la de seleccionar la orden a atender
        if self.__command == eChefCommand.SELECT_ORDER:
            
            # Indicamos que ya no es necesario mostrar el selector de ordenes a atender
            self.isSelectingOrder = False
            
            # Guardamos la referencia al cliente seleccionado
            self.__clientFoodIsPreparing = selectedClient
            
            # Removemos el cliente de la lista de clientes con ordenes activas
            self.__clientsWithActiveOrders.remove(selectedClient)

    def ingredientsPicked(self):
        
        # Si la orden actual es la de seleccionar los ingredientes
        if self.__command == eChefCommand.PICK_INGREDIENTS:
            
            # Indicamos que ya no es necesario mostrar el selector de ingredientes
            self.__isPickingIngredients = False
            
    def cancelIngredientsPicking(self):

        # Indicamos que ya no es necesario mostrar el selector de ingredientes
        self.__isPickingIngredients = False
        
        # Volvemos a agregar la orden seleccionada a la lista de ordenes disponibles
        self.__clientsWithActiveOrders.append(self.__clientFoodIsPreparing)
        self.__clientFoodIsPreparing = None

        # Cancelamos cualquier orden actual y dejamos el chef en estado de StandBy
        self.__isPickingIngredients = False
        self.isSelectingOrder = False

        self.__command = None
        self.__direction = eMotionDirection.DOWN
        self.__mainState = eChefMainState.NO_MOTION
        self.__serviceState = eChefServiceState.READY
        self.__clientSelected = None
        self.__hasCleanHands = True
        self.__deactivateAnyMessage()
            
    def getClientsWithActiveOrders(self):
        return self.__clientsWithActiveOrders

    def getPositionXY(self):
        return self.__positionXY
    
    def getCurrentBlockId(self):
        return self.__currentMotionPointId
    
    def getCommand(self):
        return self.__command
    
    def __deactivateAnyMessage(self):
        self.__messageState = None
        self.__imageMessageBackground = None
        self.__imageMessageLogo = None
        self.__MessageText = None

    def __move(self):
        
        # Avanzamos hacia el final del subcamino, de acuerdo a la direccion
        if self.__direction == eMotionDirection.UP:
            
            # Verificamos que no sobrepasemos el punto final del sub-camino al movernos
            if (self.__positionXY[1] - GlobalsController.CHEF_MOTION_UNIT) < self.__getMotionPointPosition(self.__nextMotionPointId)[1]:
                # Nos movemos directamente al final del subcamino
                self.__positionXY = (self.__positionXY[0], self.__getMotionPointPosition(self.__nextMotionPointId)[1])
            else:
                # Avanzamos un paso, de acuerdo a MOTION_UNIT
                self.__positionXY = (self.__positionXY[0], self.__positionXY[1] - GlobalsController.CHEF_MOTION_UNIT)
            
        elif self.__direction == eMotionDirection.DOWN:
            
            # Verificamos que no sobrepasemos el punto final del sub-camino al movernos
            if (self.__positionXY[1] + GlobalsController.CHEF_MOTION_UNIT) > self.__getMotionPointPosition(self.__nextMotionPointId)[1]:
                # Nos movemos directamente al final del subcamino
                self.__positionXY = (self.__positionXY[0], self.__getMotionPointPosition(self.__nextMotionPointId)[1])
            else:
                # Avanzamos un paso, de acuerdo a MOTION_UNIT
                self.__positionXY = (self.__positionXY[0], self.__positionXY[1] + GlobalsController.CHEF_MOTION_UNIT)
                
        elif self.__direction == eMotionDirection.LEFT:
            
            # Verificamos que no sobrepasemos el punto final del sub-camino al movernos
            if (self.__positionXY[0] - GlobalsController.CHEF_MOTION_UNIT) < self.__getMotionPointPosition(self.__nextMotionPointId)[0]:
                # Nos movemos directamente al final del subcamino
                self.__positionXY = (self.__getMotionPointPosition(self.__nextMotionPointId)[0], self.__positionXY[1])
            else:
                # Avanzamos un paso, de acuerdo a MOTION_UNIT
                self.__positionXY = (self.__positionXY[0] - GlobalsController.CHEF_MOTION_UNIT, self.__positionXY[1])
            
        elif self.__direction == eMotionDirection.RIGHT:
            
            # Verificamos que no sobrepasemos el punto final del sub-camino al movernos
            if (self.__positionXY[0] + GlobalsController.CHEF_MOTION_UNIT) > self.__getMotionPointPosition(self.__nextMotionPointId)[0]:
                # Nos movemos directamente al final del subcamino
                self.__positionXY = (self.__getMotionPointPosition(self.__nextMotionPointId)[0], self.__positionXY[1])
            else:
                # Avanzamos un paso, de acuerdo a MOTION_UNIT
                self.__positionXY = (self.__positionXY[0] + GlobalsController.CHEF_MOTION_UNIT, self.__positionXY[1])
                
    def __calculateNextStep(self):
        
        # Determinamos si el punto objetivo esta arriba, abajo o en la misma fila que el punto actual
        rowStart = self.__motionPoints.get(self.__currentMotionPointId).getRow()
        rowEnd = self.__motionPoints.get(self.__targetMotionPointId).getRow()
        
        # Caso A: Hacia abajo
        if rowStart < rowEnd:
            
            # Sub-Caso A1: desde fila 1
            if rowStart == eMotionRow.ROW_1:
            
                # Punto objetivo a la derecha
                if self.__chefToTargetInitDirection == eMotionDirection.RIGHT:

                    # 1. Abajo
                    linkToDown = self.__motionPoints.get(self.__currentMotionPointId).getLinkFromDirection(eMotionDirection.DOWN)
                    if linkToDown != None:
                        self.__nextMotionPointId = linkToDown.getTargetBlockId()
                        self.__direction = linkToDown.getDirection()
                    
                    else:
                        # 2. Derecha
                        linkToRight = self.__motionPoints.get(self.__currentMotionPointId).getLinkFromDirection(eMotionDirection.RIGHT)
                        if linkToRight != None:
                            self.__nextMotionPointId = linkToRight.getTargetBlockId()
                            self.__direction = linkToRight.getDirection()
                    
                # Punto objetivo a la izquierda
                else:
                
                    # Buscamos links con estas prioridades:

                    # 1. Abajo
                    linkToDown = self.__motionPoints.get(self.__currentMotionPointId).getLinkFromDirection(eMotionDirection.DOWN)
                    if linkToDown != None:
                        self.__nextMotionPointId = linkToDown.getTargetBlockId()
                        self.__direction = linkToDown.getDirection()
                    
                    else:
                        # 2. Izquierda
                        linkToLeft = self.__motionPoints.get(self.__currentMotionPointId).getLinkFromDirection(eMotionDirection.LEFT)
                        if linkToLeft != None:
                            self.__nextMotionPointId = linkToLeft.getTargetBlockId()
                            self.__direction = linkToLeft.getDirection()
                
            # Sub-Caso A2: desde fila 2
            elif rowStart == eMotionRow.ROW_2:
                
                # Punto objetivo a la derecha
                if self.__chefToTargetInitDirection == eMotionDirection.RIGHT:
                    
                    # Buscamos links con estas prioridades:
                    
                    # 1. Abajo
                    linkToDown = self.__motionPoints.get(self.__currentMotionPointId).getLinkFromDirection(eMotionDirection.DOWN)
                    if linkToDown != None:
                        self.__nextMotionPointId = linkToDown.getTargetBlockId()
                        self.__direction = linkToDown.getDirection()
                    
                    else:
                        # 2. Derecha
                        linkToRight = self.__motionPoints.get(self.__currentMotionPointId).getLinkFromDirection(eMotionDirection.RIGHT)
                        if linkToRight != None:
                            self.__nextMotionPointId = linkToRight.getTargetBlockId()
                            self.__direction = linkToRight.getDirection()
                        
                        else:
                            # 3. Izquierda
                            linkToLeft = self.__motionPoints.get(self.__currentMotionPointId).getLinkFromDirection(eMotionDirection.LEFT)
                            if linkToLeft != None:
                                self.__nextMotionPointId = linkToLeft.getTargetBlockId()
                                self.__direction = linkToLeft.getDirection()
                
                # Punto objetivo a la izquierda
                else:
                
                    # Buscamos links con estas prioridades:
                    
                    # 1. Abajo
                    linkToDown = self.__motionPoints.get(self.__currentMotionPointId).getLinkFromDirection(eMotionDirection.DOWN)
                    if linkToDown != None:
                        self.__nextMotionPointId = linkToDown.getTargetBlockId()
                        self.__direction = linkToDown.getDirection()
                    
                    else:
                        # 2. Izquierda
                        linkToLeft = self.__motionPoints.get(self.__currentMotionPointId).getLinkFromDirection(eMotionDirection.LEFT)
                        if linkToLeft != None:
                            self.__nextMotionPointId = linkToLeft.getTargetBlockId()
                            self.__direction = linkToLeft.getDirection()
                        
                        else:
                            # 3. Derecha
                            linkToRight = self.__motionPoints.get(self.__currentMotionPointId).getLinkFromDirection(eMotionDirection.RIGHT)
                            if linkToRight != None:
                                self.__nextMotionPointId = linkToRight.getTargetBlockId()
                                self.__direction = linkToRight.getDirection()
                
        # Caso B: Hacia arriba
        elif rowStart > rowEnd:
            
            # Sub-Caso B1: desde fila 2
            if rowStart == eMotionRow.ROW_2:
                
                # Punto objetivo a la derecha
                if self.__chefToTargetInitDirection == eMotionDirection.RIGHT:
                    
                    # Buscamos links con estas prioridades:
                    
                    # Excepcion 1: Atajo para subir a la primera fila mas rapido 
                    if self.__currentMotionPointId == eMotionBlock.ROW2_INTERBLOCK_AB:
                                
                        # 1. Izquierda
                        linkToLeft = self.__motionPoints.get(self.__currentMotionPointId).getLinkFromDirection(eMotionDirection.LEFT)
                        if linkToLeft != None:
                            self.__nextMotionPointId = linkToLeft.getTargetBlockId()
                            self.__direction = linkToLeft.getDirection()
                    
                    else:
                        # 1. Arriba
                        linkToUp = self.__motionPoints.get(self.__currentMotionPointId).getLinkFromDirection(eMotionDirection.UP)
                        if linkToUp != None:
                            self.__nextMotionPointId = linkToUp.getTargetBlockId()
                            self.__direction = linkToUp.getDirection()
                        
                        else:
                            # 2. Derecha
                            linkToRight = self.__motionPoints.get(self.__currentMotionPointId).getLinkFromDirection(eMotionDirection.RIGHT)
                            if linkToRight != None:
                                self.__nextMotionPointId = linkToRight.getTargetBlockId()
                                self.__direction = linkToRight.getDirection()
                            
                # Punto objetivo a la izquierda
                else:
                    # Buscamos links con estas prioridades:
                    
                    # Excepcion 1: Atajo para subir a la primera fila mas rapido 
                    if self.__currentMotionPointId == eMotionBlock.ROW2_INTERBLOCK_CD:
                                
                        # 1. Derecha
                        linkToRight = self.__motionPoints.get(self.__currentMotionPointId).getLinkFromDirection(eMotionDirection.RIGHT)
                        if linkToRight != None:
                            self.__nextMotionPointId = linkToRight.getTargetBlockId()
                            self.__direction = linkToRight.getDirection()
                    
                    else:
                        # 1. Arriba
                        linkToUp = self.__motionPoints.get(self.__currentMotionPointId).getLinkFromDirection(eMotionDirection.UP)
                        if linkToUp != None:
                            self.__nextMotionPointId = linkToUp.getTargetBlockId()
                            self.__direction = linkToUp.getDirection()
                            
                        else:
                            # 2. Izquierda
                            linkToLeft = self.__motionPoints.get(self.__currentMotionPointId).getLinkFromDirection(eMotionDirection.LEFT)
                            if linkToLeft != None:
                                self.__nextMotionPointId = linkToLeft.getTargetBlockId()
                                self.__direction = linkToLeft.getDirection()
            
            # Sub-Caso B2: desde fila 3
            elif rowStart == eMotionRow.ROW_3:
                
                # Punto objetivo a la derecha
                if self.__chefToTargetInitDirection == eMotionDirection.RIGHT:
                    
                    # Buscamos links con estas prioridades:
                    
                    # 1. Arriba
                    linkToUp = self.__motionPoints.get(self.__currentMotionPointId).getLinkFromDirection(eMotionDirection.UP)
                    if linkToUp != None:
                        self.__nextMotionPointId = linkToUp.getTargetBlockId()
                        self.__direction = linkToUp.getDirection()
                    
                    else:
                        # 2. Derecha
                        linkToRight = self.__motionPoints.get(self.__currentMotionPointId).getLinkFromDirection(eMotionDirection.RIGHT)
                        if linkToRight != None:
                            self.__nextMotionPointId = linkToRight.getTargetBlockId()
                            self.__direction = linkToRight.getDirection()
                        
                        else:
                            # 3. Izquierda
                            linkToLeft = self.__motionPoints.get(self.__currentMotionPointId).getLinkFromDirection(eMotionDirection.LEFT)
                            if linkToLeft != None:
                                self.__nextMotionPointId = linkToLeft.getTargetBlockId()
                                self.__direction = linkToLeft.getDirection()
                        
                # Punto objetivo a la izquierda
                else:
                
                    # Buscamos links con estas prioridades:
                    
                    # 1. Arriba
                    linkToUp = self.__motionPoints.get(self.__currentMotionPointId).getLinkFromDirection(eMotionDirection.UP)
                    if linkToUp != None:
                        self.__nextMotionPointId = linkToUp.getTargetBlockId()
                        self.__direction = linkToUp.getDirection()
                    
                    else:
                        # 2. Izquierda
                        linkToLeft = self.__motionPoints.get(self.__currentMotionPointId).getLinkFromDirection(eMotionDirection.LEFT)
                        if linkToLeft != None:
                            self.__nextMotionPointId = linkToLeft.getTargetBlockId()
                            self.__direction = linkToLeft.getDirection()
                        
                        else:
                            # 3. Derecha
                            linkToRight = self.__motionPoints.get(self.__currentMotionPointId).getLinkFromDirection(eMotionDirection.RIGHT)
                            if linkToRight != None:
                                self.__nextMotionPointId = linkToRight.getTargetBlockId()
                                self.__direction = linkToRight.getDirection()
        
        # Caso C: Si el punto actual esta en la misma fila que el punto objetivo
        elif rowStart == rowEnd:
            
            # Determinamos si el punto objetivo esta la izquierda o derecha del punto actual
            columnStart = self.__motionPoints.get(self.__currentMotionPointId).getColumn()
            columnEnd = self.__motionPoints.get(self.__targetMotionPointId).getColumn()
        
            # Sub-Caso C1: Hacia la derecha
            if columnStart < columnEnd:
                
                # Buscamos links con estas prioridades:
                
                # 1. Derecha
                linkToRight = self.__motionPoints.get(self.__currentMotionPointId).getLinkFromDirection(eMotionDirection.RIGHT)
                if linkToRight != None:
                    self.__nextMotionPointId = linkToRight.getTargetBlockId()
                    self.__direction = linkToRight.getDirection()

            # Sub-Caso C2: Hacia la izquierda
            elif columnStart > columnEnd:
                
                # Buscamos links con estas prioridades:
                
                # 1. Izquierda
                linkToLeft = self.__motionPoints.get(self.__currentMotionPointId).getLinkFromDirection(eMotionDirection.LEFT)
                if linkToLeft != None:
                    self.__nextMotionPointId = linkToLeft.getTargetBlockId()
                    self.__direction = linkToLeft.getDirection()
            
            # Sub-Caso C3: Si el punto actual esta en la misma columna que el punto objetivo
            elif columnStart == columnEnd:
                
                # Este caso no se da, es detectado antes por este algoritmo...
                pass

    def __positionsAreEqual(self, firstPos, secondPos):
        if firstPos[0] == secondPos[0]:
            if firstPos[1] == secondPos[1]:
                return True
            else:
                return False
        else:
            return False
        
    def getState(self):
        return self.__mainState
    
    def getSelectedClient(self):
        return self.__clientSelected

    def __getMotionPointPosition(self, id):
        pos = self.__motionPoints.get(id).getPositionXY()
        return (pos[0], pos[1])
    
    def startDancing(self):
        if self.__mainState is eChefMainState.NO_MOTION:
            # Reiniciamos el conteo para mostrar la animacion del baile
            self.__dancingAnimCountdown = 0


class Client:

    def __init__(self, id, column, row):
        
        self.id = id
        self.__row = row
        self.__column = column
        
        # Calculamos la posicion de acuerdo a la fila y la columna indicada
        yPos = 0
        if row == eMotionRow.ROW_2:
            yPos = 300
        if row == eMotionRow.ROW_3:
            yPos = 530
        
        xPos = 0
        if column == eMotionColumn.COLUMN_1:
            xPos = -18
        if column == eMotionColumn.COLUMN_3:
            xPos = 292
        if column == eMotionColumn.COLUMN_5:
            xPos = 602
        if column == eMotionColumn.COLUMN_7:
            xPos = 912
            
        self.__positionXY = (xPos, yPos)

        # Caracteristicas
        self.__serviceState = eClientServiceState.NOT_IN_THE_RESTAURANT
        self.__orderState = eClientOrderState.NO_FOOD
        self.__person = eClientPerson.PERSON_A
        self.__direction = eMotionDirection.RIGHT
        self.__recipeWanted = None
        self.stars = 1
        
        # Tiempos maximos
        self.__gettingIntoTotalTime = randrange(5, 100)
        self.__justArrivedTotalTime = randrange(5, 10)
        self.__leavingTotalTime = randrange(50, 150)
        self.__eatingTotalTime = randrange(50, 150)
        self.__menuTotalTime = randrange(5, 30)
        self.__starsTotalTime = randrange(200, 450)
        
        self.__eatingTotalFrames = 3
        self.__menuTotalFrames = 2
        self.__washingDishesTotalFrames = 2
        
        self.__eatingTotalGap = 2
        self.__washingDishesTotalGap = 2
        self.__menuTotalGap = 5
        
        # Tiempos actuales
        self.__currentTime = 1
        self.__starsCurrentTime = 1
        
        self.__eatingCurrentFrame = 1
        self.__washingDishesCurrentFrame = 1
        self.__menuCurrentFrame = 1
        
        self.__eatingCurrentGap = 1
        self.__washingDishesCurrentGap = 1
        self.__menuCurrentGap = 1
        
        # Imagenes
        self.__imageClient = None
        self.__imageDish = None
        self.__imageCloud = None
        self.__imageLetter = None
        self.__imageRecipeWanted = None
    
    def doTask(self):
        
        # Acciones a tomar dependiendo del estado actual del cliente
        if self.__serviceState == eClientServiceState.NOT_IN_THE_RESTAURANT:
            pass
        
        elif self.__serviceState == eClientServiceState.GETTING_INTO_RESTAURANT:
            
            # Verificamos que aun estemos en el rango de tiempo correspondiente a este estado...
            if self.__currentTime < self.__gettingIntoTotalTime:
                self.__currentTime = self.__currentTime + 1
            else:
                # El tiempo en este estado se acabo, cambiamos al estado correspondiente
                self.__serviceState = eClientServiceState.JUST_ARRIVED
                self.__currentTime = 1
        
        elif self.__serviceState == eClientServiceState.JUST_ARRIVED:
            
            # Verificamos que aun estemos en el rango de tiempo correspondiente a este estado...
            if self.__currentTime < self.__justArrivedTotalTime:
                self.__currentTime = self.__currentTime + 1
            else:
                # El tiempo en este estado se acabo, cambiamos al estado correspondiente
                self.__serviceState = eClientServiceState.READING_MENU
                self.__currentTime = 1
            
        elif self.__serviceState == eClientServiceState.READING_MENU:
            
            # Mientras el tiempo en este estado no haya finalizado...
            if self.__currentTime < self.__menuTotalTime:
                self.__currentTime = self.__currentTime + 1
                
                # Mientras un ciclo de animacion este activo
                if self.__menuCurrentGap < self.__menuTotalGap:
                    self.__menuCurrentGap = self.__menuCurrentGap + 1
                    
                else:
                    # Unc ciclo de animacion acaba, mostramos la imagen siguiente
                    self.__menuCurrentGap = 1
                    
                    # Si aun no se ha mostrado la ultima imagen
                    if self.__menuCurrentFrame < self.__menuTotalFrames:
                        self.__menuCurrentFrame = self.__menuCurrentFrame + 1
                    else:
                        self.__menuCurrentFrame = 1
                    
            else:
                # El tiempo en este estado se acabo, cambiamos al estado correspondiente
                self.__serviceState = eClientServiceState.REQUESTING_FOR_ORDER
                self.__currentTime = 1
            
        elif self.__serviceState == eClientServiceState.REQUESTING_FOR_ORDER:
            
            # El conteo de estrellas
            self.__starsCurrentTime = self.__starsCurrentTime + 1
            
            # Si el conteo llega a su fin
            if self.__starsCurrentTime >= self.__starsTotalTime:
                
                # Reiniciamos el conteo
                self.__starsCurrentTime = 1
                
                # Nos aseguramos que no se sobrepase el minimo de estrellas
                if self.stars > 1:
                    
                    # Disminuimos la cantidad de estrellas
                    self.stars = self.stars - 1
            
            # Solo se sale de este estado por orden del chef
            pass 
            
        elif self.__serviceState == eClientServiceState.WAITING_FOR_FOOD:
            
            # El conteo de estrellas
            self.__starsCurrentTime = self.__starsCurrentTime + 1
            
            # Si el conteo llega a su fin
            if self.__starsCurrentTime >= self.__starsTotalTime:
                
                # Reiniciamos el conteo
                self.__starsCurrentTime = 1
                
                # Nos aseguramos que no se sobrepase el minimo de estrellas
                if self.stars > 1:
                    
                    # Disminuimos la cantidad de estrellas
                    self.stars = self.stars - 1
            
            # Solo se sale de este estado por orden del chef
            pass
            
        elif self.__serviceState == eClientServiceState.EATING:
            
            # Mientras el tiempo en este estado no haya finalizado...
            if self.__currentTime < self.__eatingTotalTime:
                self.__currentTime = self.__currentTime + 1
                
                # Mientras un ciclo de animacion este activo
                if self.__eatingCurrentGap < self.__eatingTotalGap:
                    self.__eatingCurrentGap = self.__eatingCurrentGap + 1
                    
                else:
                    # Unc ciclo de animacion acaba, mostramos la imagen siguiente
                    self.__eatingCurrentGap = 1
                    
                    # Si aun no se ha mostrado la ultima imagen
                    if self.__eatingCurrentFrame < self.__eatingTotalFrames:
                        self.__eatingCurrentFrame = self.__eatingCurrentFrame + 1
                    else:
                        self.__eatingCurrentFrame = 1
                    
            else:
                # El tiempo en este estado se acabo, cambiamos al estado correspondiente
                self.__serviceState = eClientServiceState.LEAVING
                self.__orderState = eClientOrderState.DISH_EMPTY
                self.__starsCurrentTime = 1
                self.__currentTime = 1
                AudioController.playSound(eSound.ORDER, 1)
                    
        elif self.__serviceState == eClientServiceState.LEAVING:
            
            # Verificamos que aun estemos en el rango de tiempo correspondiente a este estado...
            if self.__currentTime < self.__leavingTotalTime:
                self.__currentTime = self.__currentTime + 1
            else:
                # El tiempo en este estado se acabo, cambiamos al estado correspondiente
                self.__serviceState = eClientServiceState.ONLY_DIRTY_DISHES_LEFT
                self.__orderState = eClientOrderState.DISH_DIRTY
                self.__starsCurrentTime = 1
                self.__currentTime = 1
                
            # El conteo de estrellas
            self.__starsCurrentTime = self.__starsCurrentTime + 1
            
            # Si el conteo llega a su fin
            if self.__starsCurrentTime >= self.__starsTotalTime:
                
                # Reiniciamos el conteo
                self.__starsCurrentTime = 1
                
                # Nos aseguramos que no se sobrepase el minimo de estrellas
                if self.stars > 1:
                    
                    # Disminuimos la cantidad de estrellas
                    self.stars = self.stars - 1
            
        elif self.__serviceState == eClientServiceState.ONLY_DIRTY_DISHES_LEFT:
            
            # Solo se sale de este estado por orden del chef
        
            # Mientras un ciclo de animacion este activo
            if self.__washingDishesCurrentGap < self.__washingDishesTotalGap:
                self.__washingDishesCurrentGap = self.__washingDishesCurrentGap + 1
                
            else:
                # Unc ciclo de animacion acaba, mostramos la imagen siguiente
                self.__washingDishesCurrentGap = 1
                
                # Si aun no se ha mostrado la ultima imagen
                if self.__washingDishesCurrentFrame < self.__washingDishesTotalFrames:
                    self.__washingDishesCurrentFrame = self.__washingDishesCurrentFrame + 1
                else:
                    self.__washingDishesCurrentFrame = 1
                    
            # El conteo de estrellas
            self.__starsCurrentTime = self.__starsCurrentTime + 1
            
            # Si el conteo llega a su fin
            if self.__starsCurrentTime >= self.__starsTotalTime:
                
                # Reiniciamos el conteo
                self.__starsCurrentTime = 1
                
                # Nos aseguramos que no se sobrepase el minimo de estrellas
                if self.stars > 0:
                    
                    # Disminuimos la cantidad de estrellas
                    self.stars = self.stars - 1
        
        # Determinamos cual imagen se debe mostrar de acuerdo al estado general del cliente
        self.__doUpdateImage()

    def doPaint(self, displaySurface):
        
        if self.__imageDish != None:
            
            if self.__orderState == eClientOrderState.DISH_FULL:
            
                if (self.__person == eClientPerson.PERSON_A) or (self.__person == eClientPerson.PERSON_B):  # Hombre
                    diffX = 0
                    diffY = 4
                elif self.__person == eClientPerson.PERSON_C:  # Mujer
                    diffX = -2
                    diffY = -15
                elif self.__person == eClientPerson.PERSON_D:  # Niño
                    diffX = -35
                    diffY = 15
                elif self.__person == eClientPerson.PERSON_E:  # Niña
                    diffX = -35
                    diffY = 15
                displaySurface.blit(self.__imageDish, (self.__positionXY[0] + 135 + diffX, self.__positionXY[1] + 125 + diffY))
                
            else:
                displaySurface.blit(self.__imageDish, (self.__positionXY[0] + 155, self.__positionXY[1] + 115))
            
        if self.__imageCloud != None:
            
            if (self.__person == eClientPerson.PERSON_A) or (self.__person == eClientPerson.PERSON_B):  # Hombre
                diffX = 0
                diffY = 0
            elif self.__person == eClientPerson.PERSON_C:  # Mujer
                diffX = -8
                diffY = 10
            elif self.__person == eClientPerson.PERSON_D:  # Niño
                diffX = -15
                diffY = 56
            elif self.__person == eClientPerson.PERSON_E:  # Niña
                diffX = -30
                diffY = 56
                
            displaySurface.blit(self.__imageCloud, (self.__positionXY[0] + 160 + diffX, self.__positionXY[1] + 5 + diffY))
            
            if self.__imageRecipeWanted != None:
                displaySurface.blit(self.__imageRecipeWanted, (self.__positionXY[0] + 167 + diffX, self.__positionXY[1] + 7 + diffY))
        
        if self.__imageClient != None:
            displaySurface.blit(self.__imageClient, (self.__positionXY[0], self.__positionXY[1]))
            
        if self.__imageLetter != None:
            displaySurface.blit(self.__imageLetter, (self.__positionXY[0] + 140, self.__positionXY[1] + 80))
            
            if self.__imageRecipeWanted != None:
                displaySurface.blit(self.__imageRecipeWanted, (self.__positionXY[0] + 175, self.__positionXY[1] + 105))
            
        if (self.__serviceState != eClientServiceState.NOT_IN_THE_RESTAURANT) and (self.__serviceState != eClientServiceState.GETTING_INTO_RESTAURANT):
            
            if self.__orderState != eClientOrderState.DISH_DIRTY:
            
                if (self.__person == eClientPerson.PERSON_A) or (self.__person == eClientPerson.PERSON_B):  # Hombre
                    diffX = 0
                    diffY = 0
                elif self.__person == eClientPerson.PERSON_C:  # Mujer
                    diffX = -30
                    diffY = 8
                elif self.__person == eClientPerson.PERSON_D:  # Niño
                    diffX = -20
                    diffY = 60
                elif self.__person == eClientPerson.PERSON_E:  # Niña
                    diffX = -25
                    diffY = 60
                
                if self.stars == 1:
                    displaySurface.blit(ResourceController.game_Star, (self.__positionXY[0] + 50 + diffX + (20 * 2), self.__positionXY[1] - 20 + diffY))
                elif self.stars == 2:
                    displaySurface.blit(ResourceController.game_Star, (self.__positionXY[0] + 50 + diffX + (20 * 1), self.__positionXY[1] - 20 + diffY))
                    displaySurface.blit(ResourceController.game_Star, (self.__positionXY[0] + 50 + diffX + (20 * 2), self.__positionXY[1] - 20 + diffY))
                elif self.stars == 3:
                    displaySurface.blit(ResourceController.game_Star, (self.__positionXY[0] + 50 + diffX + (20 * 1), self.__positionXY[1] - 20 + diffY))
                    displaySurface.blit(ResourceController.game_Star, (self.__positionXY[0] + 50 + diffX + (20 * 2), self.__positionXY[1] - 20 + diffY))
                    displaySurface.blit(ResourceController.game_Star, (self.__positionXY[0] + 50 + diffX + (20 * 3), self.__positionXY[1] - 20 + diffY))
                elif self.stars == 4:
                    displaySurface.blit(ResourceController.game_Star, (self.__positionXY[0] + 50 + diffX + (20 * 0), self.__positionXY[1] - 20 + diffY))
                    displaySurface.blit(ResourceController.game_Star, (self.__positionXY[0] + 50 + diffX + (20 * 1), self.__positionXY[1] - 20 + diffY))
                    displaySurface.blit(ResourceController.game_Star, (self.__positionXY[0] + 50 + diffX + (20 * 2), self.__positionXY[1] - 20 + diffY))
                    displaySurface.blit(ResourceController.game_Star, (self.__positionXY[0] + 50 + diffX + (20 * 3), self.__positionXY[1] - 20 + diffY))
                elif self.stars == 5:
                    displaySurface.blit(ResourceController.game_Star, (self.__positionXY[0] + 50 + diffX + (20 * 0), self.__positionXY[1] - 20 + diffY))
                    displaySurface.blit(ResourceController.game_Star, (self.__positionXY[0] + 50 + diffX + (20 * 1), self.__positionXY[1] - 20 + diffY))
                    displaySurface.blit(ResourceController.game_Star, (self.__positionXY[0] + 50 + diffX + (20 * 2), self.__positionXY[1] - 20 + diffY))
                    displaySurface.blit(ResourceController.game_Star, (self.__positionXY[0] + 50 + diffX + (20 * 3), self.__positionXY[1] - 20 + diffY))
                    displaySurface.blit(ResourceController.game_Star, (self.__positionXY[0] + 50 + diffX + (20 * 4), self.__positionXY[1] - 20 + diffY))
                    
            else:
                if self.stars == 1:                                                                    
                    displaySurface.blit(ResourceController.game_Star, (self.__positionXY[0] + 137 + (20 * 2), self.__positionXY[1] + 75))
                elif self.stars == 2:
                    displaySurface.blit(ResourceController.game_Star, (self.__positionXY[0] + 137 + (20 * 1), self.__positionXY[1] + 75))
                    displaySurface.blit(ResourceController.game_Star, (self.__positionXY[0] + 137 + (20 * 2), self.__positionXY[1] + 75))
                elif self.stars == 3:
                    displaySurface.blit(ResourceController.game_Star, (self.__positionXY[0] + 137 + (20 * 1), self.__positionXY[1] + 75))
                    displaySurface.blit(ResourceController.game_Star, (self.__positionXY[0] + 137 + (20 * 2), self.__positionXY[1] + 75))
                    displaySurface.blit(ResourceController.game_Star, (self.__positionXY[0] + 137 + (20 * 3), self.__positionXY[1] + 75))
                elif self.stars == 4:
                    displaySurface.blit(ResourceController.game_Star, (self.__positionXY[0] + 137 + (20 * 0), self.__positionXY[1] + 75))
                    displaySurface.blit(ResourceController.game_Star, (self.__positionXY[0] + 137 + (20 * 1), self.__positionXY[1] + 75))
                    displaySurface.blit(ResourceController.game_Star, (self.__positionXY[0] + 137 + (20 * 2), self.__positionXY[1] + 75))
                    displaySurface.blit(ResourceController.game_Star, (self.__positionXY[0] + 137 + (20 * 3), self.__positionXY[1] + 75))
                elif self.stars == 5:
                    displaySurface.blit(ResourceController.game_Star, (self.__positionXY[0] + 137 + (20 * 0), self.__positionXY[1] + 75))
                    displaySurface.blit(ResourceController.game_Star, (self.__positionXY[0] + 137 + (20 * 1), self.__positionXY[1] + 75))
                    displaySurface.blit(ResourceController.game_Star, (self.__positionXY[0] + 137 + (20 * 2), self.__positionXY[1] + 75))
                    displaySurface.blit(ResourceController.game_Star, (self.__positionXY[0] + 137 + (20 * 3), self.__positionXY[1] + 75))
                    displaySurface.blit(ResourceController.game_Star, (self.__positionXY[0] + 137 + (20 * 4), self.__positionXY[1] + 75))
        
    def __doUpdateImage(self):
        
        # Calculamos la imagen del cliente a mostrar
        if (self.__serviceState == eClientServiceState.NOT_IN_THE_RESTAURANT) or (self.__serviceState == eClientServiceState.ONLY_DIRTY_DISHES_LEFT):
            self.__imageClient = None
        else:
            if self.__person == eClientPerson.PERSON_A:
                    
                if self.__serviceState == eClientServiceState.JUST_ARRIVED:
                    self.__imageClient = ResourceController.game_ClientALooking
                elif self.__serviceState == eClientServiceState.LEAVING:
                    self.__imageClient = ResourceController.game_ClientALooking
                elif self.__serviceState == eClientServiceState.REQUESTING_FOR_ORDER:
                    self.__imageClient = ResourceController.game_ClientARequesting
                elif self.__serviceState == eClientServiceState.WAITING_FOR_FOOD:
                    self.__imageClient = ResourceController.game_ClientAWaitingForFood
                elif self.__serviceState == eClientServiceState.READING_MENU:
                    if self.__menuCurrentFrame == 1:
                        self.__imageClient = ResourceController.game_ClientAReadingMenu_1
                    elif self.__menuCurrentFrame == 2:
                        self.__imageClient = ResourceController.game_ClientAReadingMenu_2
                elif self.__serviceState == eClientServiceState.EATING:
                    if self.__eatingCurrentFrame == 1:
                        self.__imageClient = ResourceController.game_ClientAEating_1
                    elif self.__eatingCurrentFrame == 2:
                        self.__imageClient = ResourceController.game_ClientAEating_2
                    elif self.__eatingCurrentFrame == 3:
                        self.__imageClient = ResourceController.game_ClientAEating_3
                    
            elif self.__person == eClientPerson.PERSON_B:
                    
                if self.__serviceState == eClientServiceState.JUST_ARRIVED:
                    self.__imageClient = ResourceController.game_ClientBLooking
                elif self.__serviceState == eClientServiceState.LEAVING:
                    self.__imageClient = ResourceController.game_ClientBLooking
                elif self.__serviceState == eClientServiceState.REQUESTING_FOR_ORDER:
                    self.__imageClient = ResourceController.game_ClientBRequesting
                elif self.__serviceState == eClientServiceState.WAITING_FOR_FOOD:
                    self.__imageClient = ResourceController.game_ClientBWaitingForFood
                elif self.__serviceState == eClientServiceState.READING_MENU:
                    if self.__menuCurrentFrame == 1:
                        self.__imageClient = ResourceController.game_ClientBReadingMenu_1
                    elif self.__menuCurrentFrame == 2:
                        self.__imageClient = ResourceController.game_ClientBReadingMenu_2
                elif self.__serviceState == eClientServiceState.EATING:
                    if self.__eatingCurrentFrame == 1:
                        self.__imageClient = ResourceController.game_ClientBEating_1
                    elif self.__eatingCurrentFrame == 2:
                        self.__imageClient = ResourceController.game_ClientBEating_2
                    elif self.__eatingCurrentFrame == 3:
                        self.__imageClient = ResourceController.game_ClientBEating_3
                
            elif self.__person == eClientPerson.PERSON_C:
                    
                if self.__serviceState == eClientServiceState.JUST_ARRIVED:
                    self.__imageClient = ResourceController.game_ClientCLooking
                elif self.__serviceState == eClientServiceState.LEAVING:
                    self.__imageClient = ResourceController.game_ClientCLooking
                elif self.__serviceState == eClientServiceState.REQUESTING_FOR_ORDER:
                    self.__imageClient = ResourceController.game_ClientCRequesting
                elif self.__serviceState == eClientServiceState.WAITING_FOR_FOOD:
                    self.__imageClient = ResourceController.game_ClientCWaitingForFood
                elif self.__serviceState == eClientServiceState.READING_MENU:
                    if self.__menuCurrentFrame == 1:
                        self.__imageClient = ResourceController.game_ClientCReadingMenu_1
                    elif self.__menuCurrentFrame == 2:
                        self.__imageClient = ResourceController.game_ClientCReadingMenu_2
                elif self.__serviceState == eClientServiceState.EATING:
                    if self.__eatingCurrentFrame == 1:
                        self.__imageClient = ResourceController.game_ClientCEating_1
                    elif self.__eatingCurrentFrame == 2:
                        self.__imageClient = ResourceController.game_ClientCEating_2
                    elif self.__eatingCurrentFrame == 3:
                        self.__imageClient = ResourceController.game_ClientCEating_3

            elif self.__person == eClientPerson.PERSON_D:
                    
                if self.__serviceState == eClientServiceState.JUST_ARRIVED:
                    self.__imageClient = ResourceController.game_ClientDLooking
                elif self.__serviceState == eClientServiceState.LEAVING:
                    self.__imageClient = ResourceController.game_ClientDLooking
                elif self.__serviceState == eClientServiceState.REQUESTING_FOR_ORDER:
                    self.__imageClient = ResourceController.game_ClientDRequesting
                elif self.__serviceState == eClientServiceState.WAITING_FOR_FOOD:
                    self.__imageClient = ResourceController.game_ClientDWaitingForFood
                elif self.__serviceState == eClientServiceState.READING_MENU:
                    if self.__menuCurrentFrame == 1:
                        self.__imageClient = ResourceController.game_ClientDReadingMenu_1
                    elif self.__menuCurrentFrame == 2:
                        self.__imageClient = ResourceController.game_ClientDReadingMenu_2
                elif self.__serviceState == eClientServiceState.EATING:
                    if self.__eatingCurrentFrame == 1:
                        self.__imageClient = ResourceController.game_ClientDEating_1
                    elif self.__eatingCurrentFrame == 2:
                        self.__imageClient = ResourceController.game_ClientDEating_2
                    elif self.__eatingCurrentFrame == 3:
                        self.__imageClient = ResourceController.game_ClientDEating_3

            elif self.__person == eClientPerson.PERSON_E:
                    
                if self.__serviceState == eClientServiceState.JUST_ARRIVED:
                    self.__imageClient = ResourceController.game_ClientELooking
                elif self.__serviceState == eClientServiceState.LEAVING:
                    self.__imageClient = ResourceController.game_ClientELooking
                elif self.__serviceState == eClientServiceState.REQUESTING_FOR_ORDER:
                    self.__imageClient = ResourceController.game_ClientERequesting
                elif self.__serviceState == eClientServiceState.WAITING_FOR_FOOD:
                    self.__imageClient = ResourceController.game_ClientEWaitingForFood
                elif self.__serviceState == eClientServiceState.READING_MENU:
                    if self.__menuCurrentFrame == 1:
                        self.__imageClient = ResourceController.game_ClientEReadingMenu_1
                    elif self.__menuCurrentFrame == 2:
                        self.__imageClient = ResourceController.game_ClientEReadingMenu_2
                elif self.__serviceState == eClientServiceState.EATING:
                    if self.__eatingCurrentFrame == 1:
                        self.__imageClient = ResourceController.game_ClientEEating_1
                    elif self.__eatingCurrentFrame == 2:
                        self.__imageClient = ResourceController.game_ClientEEating_2
                    elif self.__eatingCurrentFrame == 3:
                        self.__imageClient = ResourceController.game_ClientEEating_3
            
        # Calculamos la imagen del plato a mostrar
        if self.__orderState == eClientOrderState.NO_FOOD:
            self.__imageDish = None
            
        else:
            if self.__orderState == eClientOrderState.DISH_FULL:
                self.__imageDish = ResourceController.game_DishFull
            elif self.__orderState == eClientOrderState.DISH_EMPTY:
                self.__imageDish = ResourceController.game_DishEmpty
            elif self.__orderState == eClientOrderState.DISH_DIRTY:
                if self.__washingDishesCurrentFrame == 1:
                    self.__imageDish = ResourceController.game_DishDirty_1
                elif self.__washingDishesCurrentFrame == 2:
                    self.__imageDish = ResourceController.game_DishDirty_2

        # Calculamos si se debe mostrar la nube o la carta con el pedido
        if self.__serviceState == eClientServiceState.WAITING_FOR_FOOD:
            self.__imageLetter = ResourceController.game_Letter
            self.__imageRecipeWanted = self.__recipeWanted.getImage()
        else:
            self.__imageLetter = None
            self.__imageRecipeWanted = None
    
    def activate(self, activeClients, timezone, inmediate):
        
        # Creamos la lista de caracteres
        personList = []
        personList.append(eClientPerson.PERSON_A)
        personList.append(eClientPerson.PERSON_B)
        personList.append(eClientPerson.PERSON_C)
        personList.append(eClientPerson.PERSON_D)
        personList.append(eClientPerson.PERSON_E)
        
        personList.append(eClientPerson.PERSON_A)
        personList.append(eClientPerson.PERSON_B)
        personList.append(eClientPerson.PERSON_C)
        personList.append(eClientPerson.PERSON_D)
        personList.append(eClientPerson.PERSON_E)
        
        personList.append(eClientPerson.PERSON_A)
        personList.append(eClientPerson.PERSON_B)
        personList.append(eClientPerson.PERSON_C)
        personList.append(eClientPerson.PERSON_D)
        personList.append(eClientPerson.PERSON_E)

        # Elegimos un caracter a azar
        self.__person = random.choice(personList)
        
        # El cliente acaba de llegar al restaurante
        if inmediate == False:
            self.__serviceState = eClientServiceState.GETTING_INTO_RESTAURANT
        else:
            self.__serviceState = eClientServiceState.JUST_ARRIVED
        self.__orderState = eClientOrderState.NO_FOOD
        self.stars = 5

        # Obtenemos valores aleatorios para los tiempos maximos
        self.__gettingIntoTotalTime = randrange(50, 500)
        self.__justArrivedTotalTime = randrange(5, 10)
        self.__leavingTotalTime = randrange(50, 150)
        self.__eatingTotalTime = randrange(50, 150)
        self.__menuTotalTime = randrange(5, 30)
        self.__starsTotalTime = randrange(200, 450)
        
        # Tiempos actuales
        self.__currentTime = 1
        self.__starsCurrentTime = 1
        
        self.__eatingCurrentFrame = 1
        self.__washingDishesCurrentFrame = 1
        self.__menuCurrentFrame = 1
        
        self.__eatingCurrentGap = 1
        self.__washingDishesCurrentGap = 1
        self.__menuCurrentGap = 1
        
        self.__imageDish = None
        self.__imageClient = None
        self.__imageCloud = None
        self.__imageLetter = None
        self.__imageRecipeWanted = None
        
        self.__doUpdateImage()
       
    def isActive(self):
        if self.__serviceState == eClientServiceState.NOT_IN_THE_RESTAURANT:
            return False
        else:
            return True
        
    def getRecipeWanted(self):
        return self.__recipeWanted
        
    def getServiceState(self):
        return self.__serviceState
    
    def getRow(self):
        return self.__row
            
    def userAssignMyOrder(self, recipe):
        if self.__serviceState == eClientServiceState.REQUESTING_FOR_ORDER:
            self.__serviceState = eClientServiceState.WAITING_FOR_FOOD
            self.__recipeWanted = recipe
            self.__starsCurrentTime = 1
    
    def chefServesMePreparedFood(self):
        if self.__serviceState == eClientServiceState.WAITING_FOR_FOOD:
            self.__serviceState = eClientServiceState.EATING
            self.__orderState = eClientOrderState.DISH_FULL
            self.__starsCurrentTime = 1
    
    def chefPicksMyDirtyDishes(self):
        if (self.__serviceState == eClientServiceState.LEAVING) or (self.__serviceState == eClientServiceState.ONLY_DIRTY_DISHES_LEFT):
            self.__serviceState = eClientServiceState.NOT_IN_THE_RESTAURANT
            self.__orderState = eClientOrderState.NO_FOOD
            self.__starsCurrentTime = 1
            

class MotionLink:

    def __init__(self, direction, targetPointId):
        self.__direction = direction
        self.__targetPointId = targetPointId
        
    def getDirection(self):
        return self.__direction
        
    def getTargetBlockId(self):
        return self.__targetPointId


class MotionPoint:

    def __init__(self, id, column, row):
        self.id = id
        
        self.__column = column
        self.__row = row
        
        # Calculamos la posicion de acuerdo a la fila y la columna indicada
        yPos = 0
        if self.__row == eMotionRow.ROW_1:
            yPos = -30
        if self.__row == eMotionRow.ROW_2:
            yPos = 200
        if self.__row == eMotionRow.ROW_3:
            yPos = 430
        
        xPos = 0
        if self.__column == eMotionColumn.COLUMN_1:
            xPos = 110
        if self.__column == eMotionColumn.COLUMN_2:
            xPos = 220
        if self.__column == eMotionColumn.COLUMN_3:
            xPos = 420
        if self.__column == eMotionColumn.COLUMN_4:
            xPos = 530
        if self.__column == eMotionColumn.COLUMN_5:
            xPos = 730
        if self.__column == eMotionColumn.COLUMN_6:
            xPos = 840
        if self.__column == eMotionColumn.COLUMN_7:
            xPos = 1040
        
        self.__position = (xPos, yPos)
        self.__links = []
        
    def getColumn(self):
        return self.__column
        
    def getRow(self):
        return self.__row
        
    def getPositionXY(self):
        return self.__position
    
    def addLink(self, direction, targetPointId):
        self.__links.append(MotionLink(direction, targetPointId))

    def getLinkFromDirection(self, directionToCheck):
        answer = None
        for link in self.__links:
            if link.getDirection() == directionToCheck:
                answer = link
            
        return answer
             

class FoodTimeBanner:

    def __init__(self):
        
        # Food Time
        self.countdownChange = 1
        self.totalTimeChange = 2000
        self.day = 1
        self.foodTime = eRecipeFoodTime.BREAKFAST

        # GUI        
        self.__image = ResourceController.game_BannerBreakfast_1
        
        # Animation
        self.__animTotalTime = 3
        self.__animCurrentTime = 1
        self.__animCurrentFrame = 1
    
    def doTask(self, isRestaurant):
        
        if isRestaurant == True:
            if GlobalsController.SHOW_TUTORIAL == False:
                
                # El tiempo avanza
                self.countdownChange = self.countdownChange + 1
        
        # Aminacion del banner
        if self.__animCurrentTime < self.__animTotalTime:
            self.__animCurrentTime = self.__animCurrentTime + 1
        else:
            self.__animCurrentTime = 1
            
            # Cambiamos de frame
            if self.__animCurrentFrame == 1:
                self.__animCurrentFrame = 2
            elif self.__animCurrentFrame == 2:
                self.__animCurrentFrame = 1
                
            if self.foodTime == eRecipeFoodTime.REFRESHMENT_MORNING:
                if self.__animCurrentFrame == 1:
                    self.__image = ResourceController.game_BannerRefreshmentMorning_1
                elif self.__animCurrentFrame == 2:
                    self.__image = ResourceController.game_BannerRefreshmentMorning_2
                
            elif self.foodTime == eRecipeFoodTime.LUNCH:
                if self.__animCurrentFrame == 1:
                    self.__image = ResourceController.game_BannerLunch_1
                elif self.__animCurrentFrame == 2:
                    self.__image = ResourceController.game_BannerLunch_2
                
            elif self.foodTime == eRecipeFoodTime.REFRESHMENT_AFTERNOON:
                if self.__animCurrentFrame == 1:
                    self.__image = ResourceController.game_BannerRefreshmentAfternoon_1
                elif self.__animCurrentFrame == 2:
                    self.__image = ResourceController.game_BannerRefreshmentAfternoon_2
                
            elif self.foodTime == eRecipeFoodTime.DINNER:
                if self.__animCurrentFrame == 1:
                    self.__image = ResourceController.game_BannerDinner_1
                elif self.__animCurrentFrame == 2:
                    self.__image = ResourceController.game_BannerDinner_2
                
            elif self.foodTime == eRecipeFoodTime.BREAKFAST:
                if self.__animCurrentFrame == 1:
                    self.__image = ResourceController.game_BannerBreakfast_1
                elif self.__animCurrentFrame == 2:
                    self.__image = ResourceController.game_BannerBreakfast_2
        
        # Si se cumplio el tiempo para cambiar de franja horaria
        if self.countdownChange >= self.totalTimeChange:
            
            # Reiniciamos la animacion
            self.__animCurrentTime = 1
            self.__animCurrentFrame = 1
            
            if self.foodTime == eRecipeFoodTime.BREAKFAST:
                self.foodTime = eRecipeFoodTime.REFRESHMENT_MORNING
                self.__image = ResourceController.game_BannerRefreshmentMorning_1
                AudioController.playSound(eSound.FOOD_TIME_CHANGE, 1)
                
            elif self.foodTime == eRecipeFoodTime.REFRESHMENT_MORNING:
                self.foodTime = eRecipeFoodTime.LUNCH
                self.__image = ResourceController.game_BannerLunch_1
                AudioController.playSound(eSound.FOOD_TIME_CHANGE, 1)
                
            elif self.foodTime == eRecipeFoodTime.LUNCH:
                self.foodTime = eRecipeFoodTime.REFRESHMENT_AFTERNOON
                self.__image = ResourceController.game_BannerRefreshmentAfternoon_1
                AudioController.playSound(eSound.FOOD_TIME_CHANGE, 1)
                
            elif self.foodTime == eRecipeFoodTime.REFRESHMENT_AFTERNOON:
                self.foodTime = eRecipeFoodTime.DINNER
                self.__image = ResourceController.game_BannerDinner_1
                AudioController.playSound(eSound.FOOD_TIME_CHANGE, 1)
                
            elif self.foodTime == eRecipeFoodTime.DINNER:
                self.foodTime = eRecipeFoodTime.BREAKFAST
                self.__image = ResourceController.game_BannerBreakfast_1
                AudioController.playSound(eSound.FOOD_TIME_CHANGE, 1)
                
                self.day = self.day + 1 
                
            self.countdownChange = 1

    def doPaint(self, displaySurface, isRestaurant):
        if isRestaurant == True:
            displaySurface.blit(self.__image, (640 - (183 / 2), 210))
        else:
            displaySurface.blit(self.__image, (795, 82))

            
class Recipe:

    def __init__(self, id):
        
        self.id = id
        
        self.ingredients = list()
        self.ingredients.append(None)
        self.ingredients.append(None)
        self.ingredients.append(None)
        self.ingredients.append(None)
        self.ingredients.append(None)
        self.ingredients.append(None)
        self.ingredients.append(None)
        self.ingredients.append(None)
        self.ingredients.append(None)
        
        self.foodTimes = list()
        
        self.description = list()
        self.description.append("")
        self.description.append("")
        self.description.append("")
        self.description.append("")
        self.description.append("")
        self.description.append("")
        self.description.append("")
        self.description.append("")
        self.description.append("")
        self.description.append("")
        self.description.append("")
        self.description.append("")
        
        # Grupo 1: Cereales, raices, tuberculos y platanos
        if id == eRecipeId._01_ALBONDIGAS:
            self.name = "Albóndigas"
            self.preparation = eRecipePreparation.HOT
            
            self.image = ResourceController.game_Recipe01Albondigas
            self.imageDisabled = ResourceController.game_Recipe01AlbondigasDisabled
            
            self.ingredients[0] = InformationIngredients.allIngredients.get(eIngredientId._54_CARNE_DE_RES)
            self.ingredients[1] = InformationIngredients.allIngredients.get(eIngredientId._53_CARNE_DE_CERDO)
            self.ingredients[2] = InformationIngredients.allIngredients.get(eIngredientId._08_PAN)
            self.ingredients[3] = InformationIngredients.allIngredients.get(eIngredientId._20_CEBOLLA_CABEZONA)
            self.ingredients[4] = InformationIngredients.allIngredients.get(eIngredientId._32_TOMATE)
            self.ingredients[5] = InformationIngredients.allIngredients.get(eIngredientId._57_HUEVO)
            self.ingredients[6] = InformationIngredients.allIngredients.get(eIngredientId._79_SAL)

            self.foodTimes.append(eRecipeFoodTime.LUNCH)
            self.foodTimes.append(eRecipeFoodTime.DINNER)

            self.description[0] = "Moler la carne de res y la"
            self.description[1] = "carne de cerdo, lo mezclas con"
            self.description[2] = "la cebolla larga picada, el"
            self.description[3] = "tomate o pimentón, se agrega la"
            self.description[4] = "miga de pan o el plátano o la "
            self.description[5] = "avena y el huevo y se amasa "
            self.description[6] = "bien."
        
        elif id == eRecipeId._02_AREPA_RELLENA_CON_QUESO:
            self.name = "Arepa rellena con queso"
            self.preparation = eRecipePreparation.HOT
            
            self.image = ResourceController.game_Recipe02ArepaRellenaConQueso
            self.imageDisabled = ResourceController.game_Recipe02ArepaRellenaConQuesoDisabled
            self.ingredients[0] = InformationIngredients.allIngredients.get(eIngredientId._04_HARINA_DE_MAIZ_PRECOCIDA)
            self.ingredients[1] = InformationIngredients.allIngredients.get(eIngredientId._75_AGUA)
            self.ingredients[2] = InformationIngredients.allIngredients.get(eIngredientId._79_SAL)
            self.ingredients[3] = InformationIngredients.allIngredients.get(eIngredientId._68_ACEITE)
            self.ingredients[4] = InformationIngredients.allIngredients.get(eIngredientId._66_QUESO)

            self.foodTimes.append(eRecipeFoodTime.BREAKFAST)
            self.foodTimes.append(eRecipeFoodTime.REFRESHMENT_MORNING)
            self.foodTimes.append(eRecipeFoodTime.REFRESHMENT_AFTERNOON)

            self.description[0] = "Preparar una parrilla caliente"
            self.description[1] = "y engrasada para asar las "
            self.description[2] = "arepas. Luego hacer la masa y"
            self.description[3] = "amasar la arepa con agua un" 
            self.description[4] = "poquito caliente, agregando la"
            self.description[5] = "harina poco a poco mezclando, "
            self.description[6] = "con las manos a medida que la"
            self.description[7] = "agregas. Mezcla la masa con la"
            self.description[8] = "mitad del queso amarillo. Haz "
            self.description[9] = "una bolita, ábrele el centro, "
            self.description[10] = "agrega el queso, forma la arepa"
            self.description[11] = "y colócalas sobre la plancha."

        elif id == eRecipeId._03_ARROZ_A_LA_SUEGRA:
            self.name = "Arroz a la suegra"
            self.preparation = eRecipePreparation.HOT
            
            self.image = ResourceController.game_Recipe03ArrozALaSuegra
            self.imageDisabled = ResourceController.game_Recipe03ArrozALaSuegraDisabled
            self.ingredients[0] = InformationIngredients.allIngredients.get(eIngredientId._02_ARROZ)
            self.ingredients[1] = InformationIngredients.allIngredients.get(eIngredientId._68_ACEITE)
            self.ingredients[2] = InformationIngredients.allIngredients.get(eIngredientId._20_CEBOLLA_CABEZONA)
            self.ingredients[3] = InformationIngredients.allIngredients.get(eIngredientId._75_AGUA)
            self.ingredients[4] = InformationIngredients.allIngredients.get(eIngredientId._57_HUEVO)
            self.ingredients[5] = InformationIngredients.allIngredients.get(eIngredientId._54_CARNE_DE_RES)
            self.ingredients[6] = InformationIngredients.allIngredients.get(eIngredientId._79_SAL)

            self.foodTimes.append(eRecipeFoodTime.LUNCH)
            self.foodTimes.append(eRecipeFoodTime.DINNER)

            self.description[0] = "Dorar la carne picada en "
            self.description[1] = "cubitos y añadir cebolla, dejar"
            self.description[2] = "sofreír, agregar el agua, dejar"
            self.description[3] = "hervir, agregar el cubo de "
            self.description[4] = "caldo y la sal, agregar el "
            self.description[5] = "arroz bien lavado, sudar "
            self.description[6] = "normalmente el arroz; Con los"
            self.description[7] = "huevos, se hace una tortilla y"
            self.description[8] = "se corta en tiras y se revuelve"
            self.description[9] = "con el arroz. Se puede servir"
            self.description[10] = "acompañado de verduras."

        elif id == eRecipeId._04_ARROZ_CAMPESINO:
            self.name = "Arroz campesino"
            self.preparation = eRecipePreparation.HOT
            
            self.image = ResourceController.game_Recipe04ArrozCampesino
            self.imageDisabled = ResourceController.game_Recipe04ArrozCampesinoDisabled
            self.ingredients[0] = InformationIngredients.allIngredients.get(eIngredientId._02_ARROZ)
            self.ingredients[1] = InformationIngredients.allIngredients.get(eIngredientId._06_MAIZ)
            self.ingredients[2] = InformationIngredients.allIngredients.get(eIngredientId._31_PIMENTON)
            self.ingredients[3] = InformationIngredients.allIngredients.get(eIngredientId._20_CEBOLLA_CABEZONA)
            self.ingredients[4] = InformationIngredients.allIngredients.get(eIngredientId._16_AJO)
            self.ingredients[5] = InformationIngredients.allIngredients.get(eIngredientId._32_TOMATE)
            self.ingredients[6] = InformationIngredients.allIngredients.get(eIngredientId._79_SAL)
            self.ingredients[7] = InformationIngredients.allIngredients.get(eIngredientId._68_ACEITE)

            self.foodTimes.append(eRecipeFoodTime.LUNCH)
            self.foodTimes.append(eRecipeFoodTime.DINNER)

            self.description[0] = "Sofreír la cebolla, el pimentón,"
            self.description[1] = "el maíz y el arroz;  luego "
            self.description[2] = "agrega los demás ingredientes" 
            self.description[3] = "(con dos tazas de agua) y tapa"
            self.description[4] = "hasta que salga el anillo de "
            self.description[5] = "vapor y cocina en bajo por 45 "
            self.description[6] = "minutos."
        
        elif id == eRecipeId._05_ARROZ_CON_MENUDENCIAS:
            self.name = "Arroz con menudencias"
            self.preparation = eRecipePreparation.HOT
            
            self.image = ResourceController.game_Recipe05ArrozConMenudencias
            self.imageDisabled = ResourceController.game_Recipe05ArrozConMenudenciasDisabled
            self.ingredients[0] = InformationIngredients.allIngredients.get(eIngredientId._31_PIMENTON)
            self.ingredients[1] = InformationIngredients.allIngredients.get(eIngredientId._17_APIO)
            self.ingredients[2] = InformationIngredients.allIngredients.get(eIngredientId._79_SAL)
            self.ingredients[3] = InformationIngredients.allIngredients.get(eIngredientId._02_ARROZ)
            self.ingredients[4] = InformationIngredients.allIngredients.get(eIngredientId._68_ACEITE)
            self.ingredients[5] = InformationIngredients.allIngredients.get(eIngredientId._20_CEBOLLA_CABEZONA)
            self.ingredients[6] = InformationIngredients.allIngredients.get(eIngredientId._75_AGUA)
            self.ingredients[7] = InformationIngredients.allIngredients.get(eIngredientId._59_MENUDENCIAS)

            self.foodTimes.append(eRecipeFoodTime.LUNCH)
            self.foodTimes.append(eRecipeFoodTime.DINNER)

            self.description[0] = "Cocinar las menudencias con sal"
            self.description[1] = "y aliños, en la olla del arroz "
            self.description[2] = "verter el aceite y dorar las "
            self.description[3] = "verduras (apio y pimentón); "
            self.description[4] = "luego agrega 3 pocillos del"
            self.description[5] = "caldo con las menudencias y el"
            self.description[6] = "arroz. Tapa hasta que salga el"
            self.description[7] = "anillo de vapor y cocina en bajo"
            self.description[8] = "por 45 minutos."
        
        elif id == eRecipeId._06_ARROZ_VEGETARIANO:
            self.name = "Arroz vegetariano"
            self.preparation = eRecipePreparation.HOT
            
            self.image = ResourceController.game_Recipe06ArrozVegetariano
            self.imageDisabled = ResourceController.game_Recipe06ArrozVegetarianoDisabled
            self.ingredients[0] = InformationIngredients.allIngredients.get(eIngredientId._02_ARROZ)
            self.ingredients[1] = InformationIngredients.allIngredients.get(eIngredientId._33_ZANAHORIA)
            self.ingredients[2] = InformationIngredients.allIngredients.get(eIngredientId._27_HABICUELA)
            self.ingredients[3] = InformationIngredients.allIngredients.get(eIngredientId._18_ARVEJA)
            self.ingredients[4] = InformationIngredients.allIngredients.get(eIngredientId._20_CEBOLLA_CABEZONA)
            self.ingredients[5] = InformationIngredients.allIngredients.get(eIngredientId._31_PIMENTON)
            self.ingredients[6] = InformationIngredients.allIngredients.get(eIngredientId._32_TOMATE)
            self.ingredients[7] = InformationIngredients.allIngredients.get(eIngredientId._79_SAL)

            self.foodTimes.append(eRecipeFoodTime.LUNCH)
            self.foodTimes.append(eRecipeFoodTime.DINNER)

            self.description[0] = "Sofreír en aceite la cebolla y"
            self.description[1] = "agregue los demás ingredientes;"
            self.description[2] = "se tapa y se prepara como "
            self.description[3] = "normalmente se hace el arroz."
        
        elif id == eRecipeId._07_ARROZ_VERDE:
            self.name = "Arroz verde"
            self.preparation = eRecipePreparation.HOT
            
            self.image = ResourceController.game_Recipe07ArrozVerde
            self.imageDisabled = ResourceController.game_Recipe07ArrozVerdeDisabled
            self.ingredients[0] = InformationIngredients.allIngredients.get(eIngredientId._02_ARROZ)
            self.ingredients[1] = InformationIngredients.allIngredients.get(eIngredientId._68_ACEITE)
            self.ingredients[2] = InformationIngredients.allIngredients.get(eIngredientId._16_AJO)
            self.ingredients[3] = InformationIngredients.allIngredients.get(eIngredientId._75_AGUA)
            self.ingredients[4] = InformationIngredients.allIngredients.get(eIngredientId._24_ESPINACA)
            self.ingredients[5] = InformationIngredients.allIngredients.get(eIngredientId._79_SAL)

            self.foodTimes.append(eRecipeFoodTime.LUNCH)
            self.foodTimes.append(eRecipeFoodTime.DINNER)

            self.description[0] = "Cocinar la espinaca, licuarla"
            self.description[1] = "y colarla; en el agua "
            self.description[2] = "resultante se debe cocinar el"
            self.description[3] = "arroz junto a los demás "
            self.description[4] = "ingredientes (puedes si quieres"
            self.description[5] = "agregarle al final cilantro,"
            self.description[6] = "perejil y queso rallado). "
        
        elif id == eRecipeId._08_AVENA_EN_HOJUELAS:
            self.name = "Avena en hojuelas"
            self.preparation = eRecipePreparation.HOT
            
            self.image = ResourceController.game_Recipe08AvenaEnHojuelas
            self.imageDisabled = ResourceController.game_Recipe08AvenaEnHojuelasDisabled
            self.ingredients[0] = InformationIngredients.allIngredients.get(eIngredientId._03_AVENA)
            self.ingredients[1] = InformationIngredients.allIngredients.get(eIngredientId._65_LECHE)
            self.ingredients[2] = InformationIngredients.allIngredients.get(eIngredientId._71_AZUCAR)
            self.ingredients[3] = InformationIngredients.allIngredients.get(eIngredientId._79_SAL)

            self.foodTimes.append(eRecipeFoodTime.BREAKFAST)
            self.foodTimes.append(eRecipeFoodTime.REFRESHMENT_MORNING)
            self.foodTimes.append(eRecipeFoodTime.REFRESHMENT_AFTERNOON)

            self.description[0] = "Poner al fuego la leche, agrega"
            self.description[1] = "la avena en hojuelas, una "
            self.description[2] = "de sal, canela y azúcar al "
            self.description[3] = "gusto. Cocina revolviendo "
            self.description[4] = "constantemente y deja hervir de"
            self.description[5] = "3 a 5 minutos."
        
        elif id == eRecipeId._09_BROCHETA_DE_FRUTAS:
            self.name = "Brocheta de frutas"
            self.preparation = eRecipePreparation.COLD
            
            self.image = ResourceController.game_Recipe09BrochetaDeFrutas
            self.imageDisabled = ResourceController.game_Recipe09BrochetaDeFrutasDisabled
            self.ingredients[0] = InformationIngredients.allIngredients.get(eIngredientId._45_MELON)
            self.ingredients[1] = InformationIngredients.allIngredients.get(eIngredientId._37_FRESA)
            self.ingredients[2] = InformationIngredients.allIngredients.get(eIngredientId._41_MANGO)
            self.ingredients[3] = InformationIngredients.allIngredients.get(eIngredientId._67_YOGURT)

            self.foodTimes.append(eRecipeFoodTime.REFRESHMENT_MORNING)
            self.foodTimes.append(eRecipeFoodTime.REFRESHMENT_AFTERNOON)

            self.description[0] = "Colocar en un palillo de pincho"
            self.description[1] = "los trozos de fruta y báñalos "
            self.description[2] = "con yogurt. Si no cuentas con"
            self.description[3] = "palillos, pon todas las frutas"
            self.description[4] = "en una taza y báñalas con el "
            self.description[5] = "yogurt, tendrás una nutritiva"
            self.description[6] = "ensalada de frutas."
        
        elif id == eRecipeId._10_CALDO_DE_PAPA_CON_COSTILLA:
            self.name = "Caldo de papa con costilla"
            self.preparation = eRecipePreparation.HOT
            
            self.image = ResourceController.game_Recipe10CaldoDePapaConCostilla
            self.imageDisabled = ResourceController.game_Recipe10CaldoDePapaConCostillaDisabled
            self.ingredients[0] = InformationIngredients.allIngredients.get(eIngredientId._09_PAPA)
            self.ingredients[1] = InformationIngredients.allIngredients.get(eIngredientId._22_CILANTRO)
            self.ingredients[2] = InformationIngredients.allIngredients.get(eIngredientId._21_CEBOLLA_LARGA)
            self.ingredients[3] = InformationIngredients.allIngredients.get(eIngredientId._75_AGUA)
            self.ingredients[4] = InformationIngredients.allIngredients.get(eIngredientId._79_SAL)
            self.ingredients[5] = InformationIngredients.allIngredients.get(eIngredientId._54_CARNE_DE_RES)

            self.foodTimes.append(eRecipeFoodTime.BREAKFAST)
            self.foodTimes.append(eRecipeFoodTime.DINNER)

            self.description[0] = "Poner la olla express con la"
            self.description[1] = "costilla previamente lavada,"
            self.description[2] = "sal, cebolla y cilantro. Pelar"
            self.description[3] = "la papa y partir en cuadros."
            self.description[4] = "Agregarla al caldo hirviendo."
            self.description[5] = "Dejar cocinar cinco minutos, "
            self.description[6] = "servir caliente, adicionando"
            self.description[7] = "cilantro picado."
        
        elif id == eRecipeId._11_CHANGUA_DE_LECHE_CON_HUEVO:
            self.name = "Changua de leche con huevo"
            self.preparation = eRecipePreparation.HOT
            
            self.image = ResourceController.game_Recipe11ChanguaDeLecheConHuevo
            self.imageDisabled = ResourceController.game_Recipe11ChanguaDeLecheConHuevoDisabled
            self.ingredients[0] = InformationIngredients.allIngredients.get(eIngredientId._57_HUEVO)
            self.ingredients[1] = InformationIngredients.allIngredients.get(eIngredientId._65_LECHE)
            self.ingredients[2] = InformationIngredients.allIngredients.get(eIngredientId._21_CEBOLLA_LARGA)
            self.ingredients[3] = InformationIngredients.allIngredients.get(eIngredientId._22_CILANTRO)
            self.ingredients[4] = InformationIngredients.allIngredients.get(eIngredientId._79_SAL)

            self.foodTimes.append(eRecipeFoodTime.BREAKFAST)
            self.foodTimes.append(eRecipeFoodTime.DINNER)

            self.description[0] = "Poner en una olla mitad leche y"
            self.description[1] = "mitad agua, con la sal, cebolla"
            self.description[2] = "larga picada y cilantro. Cuando"
            self.description[3] = "esté caliente adiciona  el huevo"
            self.description[4] = "sin cáscara, luego el calado y "
            self.description[5] = "deja  hervir hasta que la yema"
            self.description[6] = "de huevo esté dura. Sirve "
            self.description[7] = "adicionando cilantro picado."
        
        elif id == eRecipeId._12_CREMA_DE_CEBOLLA_CABEZONA:
            self.name = "Crema de cebolla cabezona"
            self.preparation = eRecipePreparation.HOT
            
            self.image = ResourceController.game_Recipe12CremaDeCebollaCabezona
            self.imageDisabled = ResourceController.game_Recipe12CremaDeCebollaCabezonaDisabled
            self.ingredients[0] = InformationIngredients.allIngredients.get(eIngredientId._20_CEBOLLA_CABEZONA)
            self.ingredients[1] = InformationIngredients.allIngredients.get(eIngredientId._03_AVENA)
            self.ingredients[2] = InformationIngredients.allIngredients.get(eIngredientId._26_GUASCAS)
            self.ingredients[3] = InformationIngredients.allIngredients.get(eIngredientId._16_AJO)
            self.ingredients[4] = InformationIngredients.allIngredients.get(eIngredientId._68_ACEITE)
            self.ingredients[5] = InformationIngredients.allIngredients.get(eIngredientId._79_SAL)

            self.foodTimes.append(eRecipeFoodTime.LUNCH)
            self.foodTimes.append(eRecipeFoodTime.DINNER)

            self.description[0] = "Se sofreír la cebolla cabezona" 
            self.description[1] = "cortada en rodajas, con el ajo"
            self.description[2] = "y las hojas de guasca; luego "
            self.description[3] = "se licúa esta mezcla y se "
            self.description[4] = "agrega en la olla con la avena"
            self.description[5] = "y tres tazas de agua.  Se debe"
            self.description[6] = "dejar cocinar hasta que hierva."
            self.description[7] = "La puedes servir con papa en "
            self.description[8] = "fosforitos."
        
        elif id == eRecipeId._13_CROQUETAS_DE_ESPINACA:
            self.name = "Croquetas de espinaca"
            self.preparation = eRecipePreparation.COLD
            
            self.image = ResourceController.game_Recipe13CroquetasDeEspinaca
            self.imageDisabled = ResourceController.game_Recipe13CroquetasDeEspinacaDisabled
            self.ingredients[0] = InformationIngredients.allIngredients.get(eIngredientId._09_PAPA)
            self.ingredients[1] = InformationIngredients.allIngredients.get(eIngredientId._79_SAL)
            self.ingredients[2] = InformationIngredients.allIngredients.get(eIngredientId._75_AGUA)
            self.ingredients[3] = InformationIngredients.allIngredients.get(eIngredientId._24_ESPINACA)
            self.ingredients[4] = InformationIngredients.allIngredients.get(eIngredientId._07_MIGA_DE_PAN)
            self.ingredients[5] = InformationIngredients.allIngredients.get(eIngredientId._57_HUEVO)
            self.ingredients[6] = InformationIngredients.allIngredients.get(eIngredientId._70_MARGARINA)

            self.foodTimes.append(eRecipeFoodTime.LUNCH)
            self.foodTimes.append(eRecipeFoodTime.DINNER)

            self.description[0] = "Cocinar la papa y volverla puré."
            self.description[1] = "En una olla pequeña cocina la "
            self.description[2] = "espinaca por 2 minutos. Escurre,"
            self.description[3] = "enfría con agua helada y licúa."
            self.description[4] = "En un colador coloca el licuado,"
            self.description[5] = "con una cuchara presiona hasta"
            self.description[6] = "escurrir muy bien la espinaca."
            self.description[7] = "Mezcla el puré de papa, la miga"
            self.description[8] = "de pan, el huevo, la margarina y"
            self.description[9] = "la espinaca, hasta obtener una"
            self.description[10] = "masa homogénea. Forma bolitas."
            self.description[11] = "En un caldero calienta el aceite."
        
        elif id == eRecipeId._14_ENSALADA_ALBA_HIT:
            self.name = "Ensalada alba hit"
            self.preparation = eRecipePreparation.COLD
            
            self.image = ResourceController.game_Recipe14EnsaladaAlbaHit
            self.imageDisabled = ResourceController.game_Recipe14EnsaladaAlbaHitDisabled
            self.ingredients[0] = InformationIngredients.allIngredients.get(eIngredientId._17_APIO)
            self.ingredients[1] = InformationIngredients.allIngredients.get(eIngredientId._33_ZANAHORIA)
            self.ingredients[2] = InformationIngredients.allIngredients.get(eIngredientId._43_MANZANA_ROJA)
            self.ingredients[3] = InformationIngredients.allIngredients.get(eIngredientId._63_CREMA_DE_LECHE)

            self.foodTimes.append(eRecipeFoodTime.LUNCH)
            self.foodTimes.append(eRecipeFoodTime.DINNER)

            self.description[0] = "Mezclar todos los ingredientes"
            self.description[1] = "en una vasija de plástico."
        
        elif id == eRecipeId._15_ENSALADA_CARLOS:
            self.name = "Ensalada carlos"
            self.preparation = eRecipePreparation.COLD
            
            self.image = ResourceController.game_Recipe15EnsaladaCarlos
            self.imageDisabled = ResourceController.game_Recipe15EnsaladaCarlosDisabled
            self.ingredients[0] = InformationIngredients.allIngredients.get(eIngredientId._28_LECHUGA)
            self.ingredients[1] = InformationIngredients.allIngredients.get(eIngredientId._43_MANZANA_ROJA)
            self.ingredients[2] = InformationIngredients.allIngredients.get(eIngredientId._66_QUESO)
            self.ingredients[3] = InformationIngredients.allIngredients.get(eIngredientId._82_VINAGRETA_DULCE)

            self.foodTimes.append(eRecipeFoodTime.LUNCH)
            self.foodTimes.append(eRecipeFoodTime.DINNER)

            self.description[0] = "Lavar la lechuga hoja por hoja,"
            self.description[1] = "y luego picarla con la mano. La"
            self.description[2] = "manzana y el queso se cortan en"
            self.description[3] = "cuadritos y se agrega la "
            self.description[4] = "vinagreta."
        
        elif id == eRecipeId._16_ENSALADA_CRIOLLA:
            self.name = "Ensalada criolla"
            self.preparation = eRecipePreparation.COLD
            
            self.image = ResourceController.game_Recipe16EnsaladaCriolla
            self.imageDisabled = ResourceController.game_Recipe16EnsaladaCriollaDisabled
            self.ingredients[0] = InformationIngredients.allIngredients.get(eIngredientId._28_LECHUGA)
            self.ingredients[1] = InformationIngredients.allIngredients.get(eIngredientId._24_ESPINACA)
            self.ingredients[2] = InformationIngredients.allIngredients.get(eIngredientId._20_CEBOLLA_CABEZONA)
            self.ingredients[3] = InformationIngredients.allIngredients.get(eIngredientId._22_CILANTRO)
            self.ingredients[4] = InformationIngredients.allIngredients.get(eIngredientId._57_HUEVO)
            self.ingredients[5] = InformationIngredients.allIngredients.get(eIngredientId._34_AGUACATE)
            self.ingredients[6] = InformationIngredients.allIngredients.get(eIngredientId._32_TOMATE)
            self.ingredients[7] = InformationIngredients.allIngredients.get(eIngredientId._82_VINAGRETA_DULCE)

            self.foodTimes.append(eRecipeFoodTime.LUNCH)
            self.foodTimes.append(eRecipeFoodTime.DINNER)

            self.description[0] = "Lava la lechuga y la espinaca,"
            self.description[1] = "cortarlas con la mano y mézclalas"
            self.description[2] = "en una ensaladera junto con el"
            self.description[3] = "cilantro. Pica el aguacate en"
            self.description[4] = "gajos, corta los huevos y el"
            self.description[5] = "tomate en cuartos. Colócalos"
            self.description[6] = "alternadamente, como abanico"
            self.description[7] = "desde el centro de la "
            self.description[8] = "ensaladera. Finalmente, agrega"
            self.description[9] = "la salsa."
        
        elif id == eRecipeId._17_ENSALADA_DE_COLORES:
            self.name = "Ensalada de colores"
            self.preparation = eRecipePreparation.COLD
            
            self.image = ResourceController.game_Recipe17EnsaladaDeColores
            self.imageDisabled = ResourceController.game_Recipe17EnsaladaDeColoresDisabled
            self.ingredients[0] = InformationIngredients.allIngredients.get(eIngredientId._48_PAPAYA)
            self.ingredients[1] = InformationIngredients.allIngredients.get(eIngredientId._45_MELON)
            self.ingredients[2] = InformationIngredients.allIngredients.get(eIngredientId._49_PATILLA)
            self.ingredients[3] = InformationIngredients.allIngredients.get(eIngredientId._42_MANZANA_VERDE)
            self.ingredients[4] = InformationIngredients.allIngredients.get(eIngredientId._43_MANZANA_ROJA)
            self.ingredients[5] = InformationIngredients.allIngredients.get(eIngredientId._46_MORA)
            self.ingredients[6] = InformationIngredients.allIngredients.get(eIngredientId._66_QUESO)

            self.foodTimes.append(eRecipeFoodTime.REFRESHMENT_MORNING)
            self.foodTimes.append(eRecipeFoodTime.REFRESHMENT_AFTERNOON)

            self.description[0] = "Lavar y picar la fruta en" 
            self.description[1] = "cuadros pequeños, la papaya,"
            self.description[2] = "melón, patilla, manzana verde y"
            self.description[3] = "roja. Mézclala y sírvela en una"
            self.description[4] = "copa adornada con queso por "
            self.description[5] = "encima y una mora de adorno."
        
        elif id == eRecipeId._18_ENSALADA_DE_FRUTAS_CON_YOGURT:
            self.name = "Ensalada de frutas con yogurt"
            self.preparation = eRecipePreparation.COLD
            
            self.image = ResourceController.game_Recipe18EnsaladaDeFrutasConYogurt
            self.imageDisabled = ResourceController.game_Recipe18EnsaladaDeFrutasConYogurtDisabled
            self.ingredients[0] = InformationIngredients.allIngredients.get(eIngredientId._41_MANGO)
            self.ingredients[1] = InformationIngredients.allIngredients.get(eIngredientId._48_PAPAYA)
            self.ingredients[2] = InformationIngredients.allIngredients.get(eIngredientId._49_PATILLA)
            self.ingredients[3] = InformationIngredients.allIngredients.get(eIngredientId._35_BANANO)
            self.ingredients[4] = InformationIngredients.allIngredients.get(eIngredientId._42_MANZANA_VERDE)
            self.ingredients[5] = InformationIngredients.allIngredients.get(eIngredientId._67_YOGURT)

            self.foodTimes.append(eRecipeFoodTime.BREAKFAST)
            self.foodTimes.append(eRecipeFoodTime.REFRESHMENT_MORNING)
            self.foodTimes.append(eRecipeFoodTime.REFRESHMENT_AFTERNOON)

            self.description[0] = "Lavar y picar el mango, la"
            self.description[1] = "papaya, patilla sin semilla, el"
            self.description[2] = "banano, la manzana verde en "
            self.description[3] = "gajos. Adiciona  el yogurt y "
            self.description[4] = "sirve en copitas con una uchuva"
            self.description[5] = "de adorno."
        
        elif id == eRecipeId._19_ENSALADA_DE_LA_CASA:
            self.name = "Ensalada de la casa"
            self.preparation = eRecipePreparation.COLD
            
            self.image = ResourceController.game_Recipe19EnsaladaDeLaCasa
            self.imageDisabled = ResourceController.game_Recipe19EnsaladaDeLaCasaDisabled
            self.ingredients[0] = InformationIngredients.allIngredients.get(eIngredientId._28_LECHUGA)
            self.ingredients[1] = InformationIngredients.allIngredients.get(eIngredientId._33_ZANAHORIA)
            self.ingredients[2] = InformationIngredients.allIngredients.get(eIngredientId._20_CEBOLLA_CABEZONA)
            self.ingredients[3] = InformationIngredients.allIngredients.get(eIngredientId._32_TOMATE)
            self.ingredients[4] = InformationIngredients.allIngredients.get(eIngredientId._39_LIMON)
            self.ingredients[5] = InformationIngredients.allIngredients.get(eIngredientId._79_SAL)

            self.foodTimes.append(eRecipeFoodTime.LUNCH)
            self.foodTimes.append(eRecipeFoodTime.DINNER)

            self.description[0] = "Cortar el repollo finamente" 
            self.description[1] = "(puedes rallarlo), lo dejas en"
            self.description[2] = "una vasija con agua y sal. "
            self.description[3] = "Rallar la zanahoria, picar el"
            self.description[4] = "tomate en cuadritos "
            self.description[5] = "(preferiblemente sin cascara y"
            self.description[6] = "sin pepa), la cebolla cabezona"
            self.description[7] = "picada se debe dejar en un taza"
            self.description[8] = "con agua, sal y limón. Después "
            self.description[9] = "de una hora de dejar el repollo"
            self.description[10] = "y la cebolla en agua (aparte),"
            self.description[11] = "se mezclan los ingredientes."
        
        elif id == eRecipeId._20_ENSALADA_DEL_HUERTO:
            self.name = "Ensalada del huerto"
            self.preparation = eRecipePreparation.COLD
            
            self.image = ResourceController.game_Recipe20EnsaladaDelHuerto
            self.imageDisabled = ResourceController.game_Recipe20EnsaladaDelHuertoDisabled
            self.ingredients[0] = InformationIngredients.allIngredients.get(eIngredientId._41_MANGO)
            self.ingredients[1] = InformationIngredients.allIngredients.get(eIngredientId._50_PERA)
            self.ingredients[2] = InformationIngredients.allIngredients.get(eIngredientId._43_MANZANA_ROJA)
            self.ingredients[3] = InformationIngredients.allIngredients.get(eIngredientId._28_LECHUGA)
            self.ingredients[4] = InformationIngredients.allIngredients.get(eIngredientId._82_VINAGRETA_DULCE)

            self.foodTimes.append(eRecipeFoodTime.LUNCH)
            self.foodTimes.append(eRecipeFoodTime.DINNER)

            self.description[0] = "Picar todas las frutas en tiras"
            self.description[1] = "(julianas), la lechuga se corta"
            self.description[2] = "con cuchillo en finas tiras. Se"
            self.description[3] = "mezclan y se agrega la "
            self.description[4] = "vinagreta dulce al gusto."
        
        elif id == eRecipeId._21_ENSALADA_FRIA_DE_PAPA_CON_POLLO:
            self.name = "Ensalada fría de papa con pollo"
            self.preparation = eRecipePreparation.COLD
            
            self.image = ResourceController.game_Recipe21EnsaladaFriaDePapaConPollo
            self.imageDisabled = ResourceController.game_Recipe21EnsaladaFriaDePapaConPolloDisabled
            self.ingredients[0] = InformationIngredients.allIngredients.get(eIngredientId._61_POLLO)
            self.ingredients[1] = InformationIngredients.allIngredients.get(eIngredientId._09_PAPA)
            self.ingredients[2] = InformationIngredients.allIngredients.get(eIngredientId._33_ZANAHORIA)
            self.ingredients[3] = InformationIngredients.allIngredients.get(eIngredientId._27_HABICUELA)
            self.ingredients[4] = InformationIngredients.allIngredients.get(eIngredientId._18_ARVEJA)
            self.ingredients[5] = InformationIngredients.allIngredients.get(eIngredientId._57_HUEVO)
            self.ingredients[6] = InformationIngredients.allIngredients.get(eIngredientId._76_MAYONESA)

            self.foodTimes.append(eRecipeFoodTime.LUNCH)
            self.foodTimes.append(eRecipeFoodTime.DINNER)

            self.description[0] = "Cocinar la pechuga y desmechar."
            self.description[1] = "Aparte, cocinar las papas, "
            self.description[2] = "zanahoria, habichuelas y los "
            self.description[3] = "huevos. Dejar enfriar y cortar"
            self.description[4] = "en cuadritos. Cortar los huevos"
            self.description[5] = "en rodajas o casquitos para "
            self.description[6] = "adornar la ensalada. Mezclar"
            self.description[7] = "todos los aderezos y adicionar"
            self.description[8] = "mayonesa."
        
        elif id == eRecipeId._22_ENSALADA_RANCHERA:
            self.name = "Ensalada ranchera"
            self.preparation = eRecipePreparation.COLD
            
            self.image = ResourceController.game_Recipe22EnsaladaRanchera
            self.imageDisabled = ResourceController.game_Recipe22EnsaladaRancheraDisabled
            self.ingredients[0] = InformationIngredients.allIngredients.get(eIngredientId._28_LECHUGA)
            self.ingredients[1] = InformationIngredients.allIngredients.get(eIngredientId._31_PIMENTON)
            self.ingredients[2] = InformationIngredients.allIngredients.get(eIngredientId._06_MAIZ)
            self.ingredients[3] = InformationIngredients.allIngredients.get(eIngredientId._62_SALCHICHA)

            self.foodTimes.append(eRecipeFoodTime.LUNCH)
            self.foodTimes.append(eRecipeFoodTime.DINNER)

            self.description[0] = "Cocinar el maíz con un poco de"
            self.description[1] = "agua y una pisca de sal, cuando"
            self.description[2] = "ya esté en su punto, se deja "
            self.description[3] = "enfriar. Luego se agrega la "
            self.description[4] = "salchicha que se ha hervido "
            self.description[5] = "previamente, se incluyen los "
            self.description[6] = "demás ingredientes finamente "
            self.description[7] = "picados y se sirve."
        
        elif id == eRecipeId._23_GUARAPO_DE_PINA:
            self.name = "Guarapo de piña"
            self.preparation = eRecipePreparation.COLD
            
            self.image = ResourceController.game_Recipe23GuarapoDePina
            self.imageDisabled = ResourceController.game_Recipe23GuarapoDePinaDisabled
            self.ingredients[0] = InformationIngredients.allIngredients.get(eIngredientId._51_PINA)
            self.ingredients[1] = InformationIngredients.allIngredients.get(eIngredientId._74_PANELA)
            self.ingredients[2] = InformationIngredients.allIngredients.get(eIngredientId._75_AGUA)
            self.ingredients[3] = InformationIngredients.allIngredients.get(eIngredientId._39_LIMON)

            self.foodTimes.append(eRecipeFoodTime.REFRESHMENT_MORNING)
            self.foodTimes.append(eRecipeFoodTime.REFRESHMENT_AFTERNOON)

            self.description[0] = "Licuar el jugo de piña, el agua"
            self.description[1] = "de panela, el jugo de limón y el"
            self.description[2] = "hielo  (puedes también agregarle"
            self.description[3] = "jengibre). Le agregas cuadritos "
            self.description[4] = "de piña a la mezcla final."

        elif id == eRecipeId._24_GUISO_DE_CARNE_Y_VERDURA:
            self.name = "Guiso de carne y verdura"
            self.preparation = eRecipePreparation.HOT
            
            self.image = ResourceController.game_Recipe24GuisoDeCarneYVerdura
            self.imageDisabled = ResourceController.game_Recipe24GuisoDeCarneYVerduraDisabled
            self.ingredients[0] = InformationIngredients.allIngredients.get(eIngredientId._54_CARNE_DE_RES)
            self.ingredients[1] = InformationIngredients.allIngredients.get(eIngredientId._27_HABICUELA)
            self.ingredients[2] = InformationIngredients.allIngredients.get(eIngredientId._33_ZANAHORIA)
            self.ingredients[3] = InformationIngredients.allIngredients.get(eIngredientId._18_ARVEJA)
            self.ingredients[4] = InformationIngredients.allIngredients.get(eIngredientId._20_CEBOLLA_CABEZONA)
            self.ingredients[5] = InformationIngredients.allIngredients.get(eIngredientId._16_AJO)
            self.ingredients[6] = InformationIngredients.allIngredients.get(eIngredientId._79_SAL)

            self.foodTimes.append(eRecipeFoodTime.LUNCH)
            self.foodTimes.append(eRecipeFoodTime.DINNER)

            self.description[0] = "Picar en cuadritos la verdura y"
            self.description[1] = "la carne, se pone a cocinar y "
            self.description[2] = "se mezcla con los aliños y la "
            self.description[3] = "sal al gusto."
        
        elif id == eRecipeId._25_GUISO_DE_HABICHUELA_CON_CARNE:
            self.name = "Guiso de habichuela con carne"
            self.preparation = eRecipePreparation.HOT
            
            self.image = ResourceController.game_Recipe25GuisoDeHabichuelaConCarne
            self.imageDisabled = ResourceController.game_Recipe25GuisoDeHabichuelaConCarneDisabled
            self.ingredients[0] = InformationIngredients.allIngredients.get(eIngredientId._75_AGUA)
            self.ingredients[1] = InformationIngredients.allIngredients.get(eIngredientId._27_HABICUELA)
            self.ingredients[2] = InformationIngredients.allIngredients.get(eIngredientId._54_CARNE_DE_RES)
            self.ingredients[3] = InformationIngredients.allIngredients.get(eIngredientId._32_TOMATE)
            self.ingredients[4] = InformationIngredients.allIngredients.get(eIngredientId._21_CEBOLLA_LARGA)
            self.ingredients[5] = InformationIngredients.allIngredients.get(eIngredientId._31_PIMENTON)
            self.ingredients[6] = InformationIngredients.allIngredients.get(eIngredientId._57_HUEVO)
            self.ingredients[7] = InformationIngredients.allIngredients.get(eIngredientId._79_SAL)

            self.foodTimes.append(eRecipeFoodTime.LUNCH)
            self.foodTimes.append(eRecipeFoodTime.DINNER)

            self.description[0] = "Poner a hervir agua en una olla,"
            self.description[1] = "agregar la habichuela y cocinar"
            self.description[2] = "durante 12 minutos. En una olla"
            self.description[3] = "cocinar la carne, con agua que "
            self.description[4] = "la cubra. Escúrrela y "
            self.description[5] = "desmenúzala. En un sartén pon" 
            self.description[6] = "al fuego lento el tomate, "
            self.description[7] = "cebolla y pimentón durante 3" 
            self.description[8] = "minutos. Adiciona la carne y "
            self.description[9] = "deja 2 minutos. Incorpora  el"
            self.description[10] = "huevo batido, la sal y la "
            self.description[11] = "habichuela. Cocina por 5 mins."

        elif id == eRecipeId._26_HAMBURGUESA:
            self.name = "Hamburguesa"
            self.preparation = eRecipePreparation.HOT
            
            self.image = ResourceController.game_Recipe26Hamburguesa
            self.imageDisabled = ResourceController.game_Recipe26HamburguesaDisabled
            self.ingredients[0] = InformationIngredients.allIngredients.get(eIngredientId._08_PAN)
            self.ingredients[1] = InformationIngredients.allIngredients.get(eIngredientId._54_CARNE_DE_RES)
            self.ingredients[2] = InformationIngredients.allIngredients.get(eIngredientId._20_CEBOLLA_CABEZONA)
            self.ingredients[3] = InformationIngredients.allIngredients.get(eIngredientId._28_LECHUGA)
            self.ingredients[4] = InformationIngredients.allIngredients.get(eIngredientId._32_TOMATE)
            self.ingredients[5] = InformationIngredients.allIngredients.get(eIngredientId._66_QUESO)
            self.ingredients[6] = InformationIngredients.allIngredients.get(eIngredientId._80_SALSA_DE_TOMATE)
            self.ingredients[7] = InformationIngredients.allIngredients.get(eIngredientId._76_MAYONESA)
            self.ingredients[8] = InformationIngredients.allIngredients.get(eIngredientId._77_MOSTAZA)

            self.foodTimes.append(eRecipeFoodTime.LUNCH)
            self.foodTimes.append(eRecipeFoodTime.DINNER)

            self.description[0] = "Sofreír la carne de hamburguesa,"
            self.description[1] = "incluirla en el pan, agregar el"
            self.description[2] = "tomate en rodajas delgadas, la "
            self.description[3] = "lechuga (que debes lavar con "
            self.description[4] = "agua y limón) y la cebolla (que"
            self.description[5] = "debes dejarla al menos 30 "
            self.description[6] = "minutos en agua caliente con" 
            self.description[7] = "sal). Agregas una tajada de "
            self.description[8] = "queso doble crema y las salsas"
            self.description[9] = "que desees."

        elif id == eRecipeId._27_HUEVO_TIBIO:
            self.name = "Huevo tibio"
            self.preparation = eRecipePreparation.HOT
            
            self.image = ResourceController.game_Recipe27HuevoTibio
            self.imageDisabled = ResourceController.game_Recipe27HuevoTibioDisabled
            self.ingredients[0] = InformationIngredients.allIngredients.get(eIngredientId._57_HUEVO)
            self.ingredients[1] = InformationIngredients.allIngredients.get(eIngredientId._75_AGUA)

            self.foodTimes.append(eRecipeFoodTime.BREAKFAST)

            self.description[0] = "Poner al fuego un huevo con agua"
            self.description[1] = "fría en cantidad que lo tape. "
            self.description[2] = "Esperar a que hierva y a partir"
            self.description[3] = "de ese momento, contabilizar 2"
            self.description[4] = "minutos y 30 segundos. Retirar "
            self.description[5] = "del fuego y sacar del agua con "
            self.description[6] = "cuidado inmediatamente."
        
        elif id == eRecipeId._28_JUGO_DE_MARACUYA_Y_ZANAHORIA:
            self.name = "Jugo de maracuyá y zanahoria"
            self.preparation = eRecipePreparation.COLD
            
            self.image = ResourceController.game_Recipe28JugoDeMaracuyaYZanahoria
            self.imageDisabled = ResourceController.game_Recipe28JugoDeMaracuyaYZanahoriaDisabled
            self.ingredients[0] = InformationIngredients.allIngredients.get(eIngredientId._75_AGUA)
            self.ingredients[1] = InformationIngredients.allIngredients.get(eIngredientId._44_MARACUYA)
            self.ingredients[2] = InformationIngredients.allIngredients.get(eIngredientId._33_ZANAHORIA)
            self.ingredients[3] = InformationIngredients.allIngredients.get(eIngredientId._71_AZUCAR)

            self.foodTimes.append(eRecipeFoodTime.BREAKFAST)
            self.foodTimes.append(eRecipeFoodTime.REFRESHMENT_MORNING)
            self.foodTimes.append(eRecipeFoodTime.REFRESHMENT_AFTERNOON)

            self.description[0] = "Licuar el maracuyá con el agua y"
            self.description[1] = "colar. Licuar el jugo de "
            self.description[2] = "maracuyá con la zanahoria y el"
            self.description[3] = "azúcar. Servir frío."
        
        elif id == eRecipeId._29_JUGO_DE_PAPAYA_CON_ZANAHORIA:
            self.name = "Jugo de papaya con zanahoria"
            self.preparation = eRecipePreparation.COLD
            
            self.image = ResourceController.game_Recipe29JugoDePapayaConZanahoria
            self.imageDisabled = ResourceController.game_Recipe29JugoDePapayaConZanahoriaDisabled
            self.ingredients[0] = InformationIngredients.allIngredients.get(eIngredientId._48_PAPAYA)
            self.ingredients[1] = InformationIngredients.allIngredients.get(eIngredientId._33_ZANAHORIA)
            self.ingredients[2] = InformationIngredients.allIngredients.get(eIngredientId._75_AGUA)

            self.foodTimes.append(eRecipeFoodTime.BREAKFAST)
            self.foodTimes.append(eRecipeFoodTime.REFRESHMENT_MORNING)
            self.foodTimes.append(eRecipeFoodTime.REFRESHMENT_AFTERNOON)

            self.description[0] = "Pelar la papaya y la zanahoria," 
            self.description[1] = "picar y licuar con agua. Servir"
            self.description[2] = "inmediatamente."

        elif id == eRecipeId._30_LOMO_DE_CERDO_EN_SALSA_DE_MANGO:
            self.name = "Lomo de cerdo en salsa de mango"
            self.preparation = eRecipePreparation.HOT
            
            self.image = ResourceController.game_Recipe30LomoDeCerdoEnSalsaDeMango
            self.imageDisabled = ResourceController.game_Recipe30LomoDeCerdoEnSalsaDeMangoDisabled
            self.ingredients[0] = InformationIngredients.allIngredients.get(eIngredientId._53_CARNE_DE_CERDO)
            self.ingredients[1] = InformationIngredients.allIngredients.get(eIngredientId._31_PIMENTON)
            self.ingredients[2] = InformationIngredients.allIngredients.get(eIngredientId._20_CEBOLLA_CABEZONA)
            self.ingredients[3] = InformationIngredients.allIngredients.get(eIngredientId._41_MANGO)
            self.ingredients[4] = InformationIngredients.allIngredients.get(eIngredientId._82_VINAGRETA_DULCE)
            self.ingredients[5] = InformationIngredients.allIngredients.get(eIngredientId._74_PANELA)
            self.ingredients[6] = InformationIngredients.allIngredients.get(eIngredientId._69_MANTEQUILLA)
            self.ingredients[7] = InformationIngredients.allIngredients.get(eIngredientId._68_ACEITE)
            self.ingredients[8] = InformationIngredients.allIngredients.get(eIngredientId._79_SAL)

            self.foodTimes.append(eRecipeFoodTime.LUNCH)
            self.foodTimes.append(eRecipeFoodTime.DINNER)

            self.description[0] = "Adobar la carne con los" 
            self.description[1] = "condimentos y la sal desde el"
            self.description[2] = "día anterior; se sofríe en "
            self.description[3] = "aceite bien caliente. "
            self.description[4] = "Los mangos se cocinan durante" 
            self.description[5] = "15 minutos en media taza de "
            self.description[6] = "agua, se cuela. Se agrega el "
            self.description[7] = "vinagre y el azúcar (si tienes"
            self.description[8] = "clavos de canela inclúyelos)."
            self.description[9] = "Se coloca la carne de cerdo en"
            self.description[10] = "la salsa y se tapa bien,se deja"
            self.description[11] = "a fuego alto hasta que espese."

        elif id == eRecipeId._31_LOMO_DE_CERDO_ENCHILADO:
            self.name = "Lomo de cerdo enchilado"
            self.preparation = eRecipePreparation.HOT
            
            self.image = ResourceController.game_Recipe31LomoDeCerdoEnchilado
            self.imageDisabled = ResourceController.game_Recipe31LomoDeCerdoEnchiladoDisabled
            self.ingredients[0] = InformationIngredients.allIngredients.get(eIngredientId._53_CARNE_DE_CERDO)
            self.ingredients[1] = InformationIngredients.allIngredients.get(eIngredientId._39_LIMON)
            self.ingredients[2] = InformationIngredients.allIngredients.get(eIngredientId._17_APIO)
            self.ingredients[3] = InformationIngredients.allIngredients.get(eIngredientId._31_PIMENTON)
            self.ingredients[4] = InformationIngredients.allIngredients.get(eIngredientId._32_TOMATE)
            self.ingredients[5] = InformationIngredients.allIngredients.get(eIngredientId._20_CEBOLLA_CABEZONA)
            self.ingredients[6] = InformationIngredients.allIngredients.get(eIngredientId._16_AJO)
            self.ingredients[7] = InformationIngredients.allIngredients.get(eIngredientId._79_SAL)

            self.foodTimes.append(eRecipeFoodTime.LUNCH)
            self.foodTimes.append(eRecipeFoodTime.DINNER)

            self.description[0] = "Dejar la carne desde el día" 
            self.description[1] = "anterior en el jugo de limón y"
            self.description[2] = "la sal. Licuar todos los aliños"
            self.description[3] = "(apio, pimentón, cebolla, ajo y"
            self.description[4] = "tomate); coloca la carne a "
            self.description[5] = "sofreír y agrega el licuado,"
            self.description[6] = "deja en fuego alto hasta que"
            self.description[7] = "hierva. Luego baja a "
            self.description[8] = "temperatura mínima por hora y"
            self.description[9] = "media pasado este tiempo coloca"
            self.description[10] = "en alto, agrega la maizena "
            self.description[11] = "disuelta, deja que espese."

        elif id == eRecipeId._32_MACARRONES_CON_ATUN:
            self.name = "Macarrones con atún"
            self.preparation = eRecipePreparation.HOT
            
            self.image = ResourceController.game_Recipe32MacarronesConAtun
            self.imageDisabled = ResourceController.game_Recipe32MacarronesConAtunDisabled
            self.ingredients[0] = InformationIngredients.allIngredients.get(eIngredientId._52_ATUN)
            self.ingredients[1] = InformationIngredients.allIngredients.get(eIngredientId._66_QUESO)
            self.ingredients[2] = InformationIngredients.allIngredients.get(eIngredientId._63_CREMA_DE_LECHE)
            self.ingredients[3] = InformationIngredients.allIngredients.get(eIngredientId._81_SOPAS_EN_CREMA)
            self.ingredients[4] = InformationIngredients.allIngredients.get(eIngredientId._69_MANTEQUILLA)
            self.ingredients[5] = InformationIngredients.allIngredients.get(eIngredientId._10_PASTA)
            self.ingredients[6] = InformationIngredients.allIngredients.get(eIngredientId._79_SAL)
            self.ingredients[7] = InformationIngredients.allIngredients.get(eIngredientId._68_ACEITE)

            self.foodTimes.append(eRecipeFoodTime.LUNCH)
            self.foodTimes.append(eRecipeFoodTime.DINNER)

            self.description[0] = "Colocar el agua con sal y aceite"
            self.description[1] = "para cocinar la pasta (te "
            self.description[2] = "sugerimos que sea pasta corta)." 
            self.description[3] = "Cuando ya esté en su punto, se "
            self.description[4] = "escurren bien, se deja en un "
            self.description[5] = "recipiente, se cubre con el "
            self.description[6] = "queso. Prepara la crema de "
            self.description[7] = "champiñones, agrega la anterior" 
            self.description[8] = "mezcla junto con el atún "
            self.description[9] = "desmenuzado y los aliños que" 
            self.description[10] = "prefieras, la crema de leche"
            self.description[11] = "y la mantequilla."

        
        elif id == eRecipeId._33_PASTA_CON_VEGETALES:
            self.name = "Pasta con vegetales"
            self.preparation = eRecipePreparation.HOT
            
            self.image = ResourceController.game_Recipe33PastaConVegetales
            self.imageDisabled = ResourceController.game_Recipe33PastaConVegetalesDisabled
            self.ingredients[0] = InformationIngredients.allIngredients.get(eIngredientId._10_PASTA)
            self.ingredients[1] = InformationIngredients.allIngredients.get(eIngredientId._27_HABICUELA)
            self.ingredients[2] = InformationIngredients.allIngredients.get(eIngredientId._33_ZANAHORIA)
            self.ingredients[3] = InformationIngredients.allIngredients.get(eIngredientId._18_ARVEJA)
            self.ingredients[4] = InformationIngredients.allIngredients.get(eIngredientId._31_PIMENTON)
            self.ingredients[5] = InformationIngredients.allIngredients.get(eIngredientId._32_TOMATE)
            self.ingredients[6] = InformationIngredients.allIngredients.get(eIngredientId._20_CEBOLLA_CABEZONA)
            self.ingredients[7] = InformationIngredients.allIngredients.get(eIngredientId._76_MAYONESA)
            self.ingredients[8] = InformationIngredients.allIngredients.get(eIngredientId._79_SAL)

            self.foodTimes.append(eRecipeFoodTime.LUNCH)
            self.foodTimes.append(eRecipeFoodTime.DINNER)

            self.description[0] = "Cocinar la habichuela y" 
            self.description[1] = "zanahoria picada con la" 
            self.description[2] = "alverja hasta que estén "
            self.description[3] = "blanditas. En otro "
            self.description[4] = "recipiente se cocina la" 
            self.description[5] = "pasta hasta que quede al"
            self.description[6] = "gusto (cocinar con aceite "
            self.description[7] = "y sal). El pimentón se pica en"
            self.description[8] = "tiras delgadas y  la cebolla se"
            self.description[9] = "pica en rodajas. Cuando estén "
            self.description[10] = "listas las verduras y la pasta,"
            self.description[11] = "agrega los demás ingredientes."
        
        elif id == eRecipeId._34_PATACONES_CON_CARNE_DESMECHADA:
            self.name = "Patacones con carne desmechada"
            self.preparation = eRecipePreparation.HOT
            
            self.image = ResourceController.game_Recipe34PataconesConCarneDesmechada
            self.imageDisabled = ResourceController.game_Recipe34PataconesConCarneDesmechadaDisabled
            self.ingredients[0] = InformationIngredients.allIngredients.get(eIngredientId._11_PLATANO)
            self.ingredients[1] = InformationIngredients.allIngredients.get(eIngredientId._54_CARNE_DE_RES)
            self.ingredients[2] = InformationIngredients.allIngredients.get(eIngredientId._20_CEBOLLA_CABEZONA)
            self.ingredients[3] = InformationIngredients.allIngredients.get(eIngredientId._31_PIMENTON)
            self.ingredients[4] = InformationIngredients.allIngredients.get(eIngredientId._32_TOMATE)

            self.foodTimes.append(eRecipeFoodTime.DINNER)

            self.description[0] = "Cocinar y desmechar la carne," 
            self.description[1] = "debes conservar aprox. 1/2 taza" 
            self.description[2] = "de caldo para la salsa. "
            self.description[3] = "Corta los pimientos y las "
            self.description[4] = "cebollas en cuadritos y los pones"
            self.description[5] = "al fuego en una sartén. Agrega el"
            self.description[6] = "tomate machacado y la carne."
            self.description[7] = "Dejar a fuego mediano hasta que"
            self.description[8] = "se evapore el caldo. Sírvelo"
            self.description[9] = "encima de los patacones fritos"
            self.description[10] = "en aceite caliente."
            
        elif id == eRecipeId._35_PEPINOS_RELLENOS:
            self.name = "Pepinos rellenos"
            self.preparation = eRecipePreparation.HOT
            
            self.image = ResourceController.game_Recipe35PepinosRellenos
            self.imageDisabled = ResourceController.game_Recipe35PepinosRellenosDisabled
            self.ingredients[0] = InformationIngredients.allIngredients.get(eIngredientId._69_MANTEQUILLA)
            self.ingredients[1] = InformationIngredients.allIngredients.get(eIngredientId._54_CARNE_DE_RES)
            self.ingredients[2] = InformationIngredients.allIngredients.get(eIngredientId._20_CEBOLLA_CABEZONA)
            self.ingredients[3] = InformationIngredients.allIngredients.get(eIngredientId._32_TOMATE)
            self.ingredients[4] = InformationIngredients.allIngredients.get(eIngredientId._09_PAPA)
            self.ingredients[5] = InformationIngredients.allIngredients.get(eIngredientId._30_PEPINO_COMUN)
            self.ingredients[6] = InformationIngredients.allIngredients.get(eIngredientId._75_AGUA)

            self.foodTimes.append(eRecipeFoodTime.LUNCH)
            self.foodTimes.append(eRecipeFoodTime.DINNER)

            self.description[0] = "Cocinar la carne molida con el"
            self.description[1] = "ahogado. Aparte tritura las "
            self.description[2] = "papas con un tenedor y agrégalas"
            self.description[3] = "a la carne con una taza de caldo."
            self.description[4] = "Deja enfriar y revuelve con el "
            self.description[5] = "queso rallado (opcional). Toma"
            self.description[6] = "los pepinos y retira las semillas"
            self.description[7] = "cuidadosamente. En una olla" 
            self.description[8] = "profunda vierte el agua, la sal"
            self.description[9] = "y cocina los pepinos a fuego "
            self.description[10] = "medio durante 5 minutos."
            self.description[11] = "Rellénalos con la carne."
        
        elif id == eRecipeId._36_PERRO_CALIENTE:
            self.name = "Perro caliente"
            self.preparation = eRecipePreparation.HOT
            
            self.image = ResourceController.game_Recipe36PerroCaliente
            self.imageDisabled = ResourceController.game_Recipe36PerroCalienteDisabled
            self.ingredients[0] = InformationIngredients.allIngredients.get(eIngredientId._08_PAN)
            self.ingredients[1] = InformationIngredients.allIngredients.get(eIngredientId._62_SALCHICHA)
            self.ingredients[2] = InformationIngredients.allIngredients.get(eIngredientId._09_PAPA)
            self.ingredients[3] = InformationIngredients.allIngredients.get(eIngredientId._80_SALSA_DE_TOMATE)
            self.ingredients[4] = InformationIngredients.allIngredients.get(eIngredientId._76_MAYONESA)
            self.ingredients[5] = InformationIngredients.allIngredients.get(eIngredientId._77_MOSTAZA)
            self.ingredients[6] = InformationIngredients.allIngredients.get(eIngredientId._66_QUESO)

            self.foodTimes.append(eRecipeFoodTime.REFRESHMENT_MORNING)
            self.foodTimes.append(eRecipeFoodTime.REFRESHMENT_AFTERNOON)

            self.description[0] = "Hervir la salchicha, incluirla" 
            self.description[1] = "en el pan, agrega papas ralladas"
            self.description[2] = "(de paquete), las salsas y el "
            self.description[3] = "queso rayado."

        elif id == eRecipeId._37_PESCADO_A_LA_PRIMAVERA:
            self.name = "Pescado a la primavera"
            self.preparation = eRecipePreparation.HOT
            
            self.image = ResourceController.game_Recipe37PescadoALaPrimavera
            self.imageDisabled = ResourceController.game_Recipe37PescadoALaPrimaveraDisabled
            self.ingredients[0] = InformationIngredients.allIngredients.get(eIngredientId._60_PESCADO)
            self.ingredients[1] = InformationIngredients.allIngredients.get(eIngredientId._31_PIMENTON)
            self.ingredients[2] = InformationIngredients.allIngredients.get(eIngredientId._20_CEBOLLA_CABEZONA)
            self.ingredients[3] = InformationIngredients.allIngredients.get(eIngredientId._32_TOMATE)
            self.ingredients[4] = InformationIngredients.allIngredients.get(eIngredientId._63_CREMA_DE_LECHE)
            self.ingredients[5] = InformationIngredients.allIngredients.get(eIngredientId._39_LIMON)
            self.ingredients[6] = InformationIngredients.allIngredients.get(eIngredientId._16_AJO)
            self.ingredients[7] = InformationIngredients.allIngredients.get(eIngredientId._79_SAL)

            self.foodTimes.append(eRecipeFoodTime.LUNCH)
            self.foodTimes.append(eRecipeFoodTime.DINNER)

            self.description[0] = "Sazonar los filetes con sal y" 
            self.description[1] = "el jugo de limón. Sofríe el "
            self.description[2] = "pimentón, el ajo y el calabacín,"
            self.description[3] = "agrega el tomate y deja cocinar "
            self.description[4] = "por 10 minutos. Añade la crema "
            self.description[5] = "de leche, los filetes escurridos,"
            self.description[6] = "sazona a tu gusto y deja a fuego"
            self.description[7] = "bajo por 15 minutos."

        elif id == eRecipeId._38_PESCADO_ORIENTAL:
            self.name = "Pescado oriental"
            self.preparation = eRecipePreparation.HOT
            
            self.image = ResourceController.game_Recipe38PescadoOriental
            self.imageDisabled = ResourceController.game_Recipe38PescadoOrientalDisabled
            self.ingredients[0] = InformationIngredients.allIngredients.get(eIngredientId._60_PESCADO)
            self.ingredients[1] = InformationIngredients.allIngredients.get(eIngredientId._20_CEBOLLA_CABEZONA)
            self.ingredients[2] = InformationIngredients.allIngredients.get(eIngredientId._16_AJO)
            self.ingredients[3] = InformationIngredients.allIngredients.get(eIngredientId._57_HUEVO)
            self.ingredients[4] = InformationIngredients.allIngredients.get(eIngredientId._08_PAN)
            self.ingredients[5] = InformationIngredients.allIngredients.get(eIngredientId._68_ACEITE)
            self.ingredients[6] = InformationIngredients.allIngredients.get(eIngredientId._79_SAL)

            self.foodTimes.append(eRecipeFoodTime.LUNCH)
            self.foodTimes.append(eRecipeFoodTime.DINNER)

            self.description[0] = "Aliñar los filetes de pescado"
            self.description[1] = "con la cebolla rallada, el ajo"
            self.description[2] = "machacado, el jugo de limón."
            self.description[3] = "Pásalos por las claras de huevo"
            self.description[4] = "a medio batir, luego por las "
            self.description[5] = "migas de pan. Fríe  en aceite "
            self.description[6] = "bien caliente hasta que estén "
            self.description[7] = "dorados por los dos lados. Los"
            self.description[8] = "puedes bañar con cualquier "
            self.description[9] = "clase de salsa."
        
        elif id == eRecipeId._39_POLLO_A_LA_JARDINERA:
            self.name = "Pollo a la jardinera"
            self.preparation = eRecipePreparation.HOT
            
            self.image = ResourceController.game_Recipe39PolloALaJardinera
            self.imageDisabled = ResourceController.game_Recipe39PolloALaJardineraDisabled
            self.ingredients[0] = InformationIngredients.allIngredients.get(eIngredientId._61_POLLO)
            self.ingredients[1] = InformationIngredients.allIngredients.get(eIngredientId._18_ARVEJA)
            self.ingredients[2] = InformationIngredients.allIngredients.get(eIngredientId._27_HABICUELA)
            self.ingredients[3] = InformationIngredients.allIngredients.get(eIngredientId._33_ZANAHORIA)
            self.ingredients[4] = InformationIngredients.allIngredients.get(eIngredientId._20_CEBOLLA_CABEZONA)
            self.ingredients[5] = InformationIngredients.allIngredients.get(eIngredientId._16_AJO)
            self.ingredients[6] = InformationIngredients.allIngredients.get(eIngredientId._31_PIMENTON)
            self.ingredients[7] = InformationIngredients.allIngredients.get(eIngredientId._32_TOMATE)
            self.ingredients[8] = InformationIngredients.allIngredients.get(eIngredientId._79_SAL)

            self.foodTimes.append(eRecipeFoodTime.LUNCH)
            self.foodTimes.append(eRecipeFoodTime.DINNER)

            self.description[0] = "Picar la zanahoria y la" 
            self.description[1] = "habichuela,  coloca el pollo" 
            self.description[2] = "con poca agua y   agrega las "
            self.description[3] = "verduras, los aliños y la sal "
            self.description[4] = "al gusto. Puedes servir "
            self.description[5] = "acompañado con arroz blanco y"
            self.description[6] = "una tajada de plátano."

        elif id == eRecipeId._40_QUESO_DE_PINA:
            self.name = "Queso de piña"
            self.preparation = eRecipePreparation.COLD
            
            self.image = ResourceController.game_Recipe40QuesoDePina
            self.imageDisabled = ResourceController.game_Recipe40QuesoDePinaDisabled
            self.ingredients[0] = InformationIngredients.allIngredients.get(eIngredientId._51_PINA)
            self.ingredients[1] = InformationIngredients.allIngredients.get(eIngredientId._71_AZUCAR)
            self.ingredients[2] = InformationIngredients.allIngredients.get(eIngredientId._57_HUEVO)
            self.ingredients[3] = InformationIngredients.allIngredients.get(eIngredientId._75_AGUA)

            self.foodTimes.append(eRecipeFoodTime.REFRESHMENT_MORNING)
            self.foodTimes.append(eRecipeFoodTime.REFRESHMENT_AFTERNOON)

            self.description[0] = "Cocinar en agua la cáscara y el"
            self.description[1] = "bagazo de la piña con azúcar, "
            self.description[2] = "hasta que este consistente "
            self.description[3] = "(chicludo). En un plato aparte" 
            self.description[4] = "bates las claras del huevo y las"
            self.description[5] = "vas incorporando poco a poco al"
            self.description[6] = "melado de piña. Lo dejas enfriar"
            self.description[7] = "y a disfrutar de un delicioso y "
            self.description[8] = "económico postre."

        elif id == eRecipeId._41_REFRESCO_DE_MANZANA:
            self.name = "Refresco de manzana"
            self.preparation = eRecipePreparation.COLD
            
            self.image = ResourceController.game_Recipe41RefrescoDeManzana
            self.imageDisabled = ResourceController.game_Recipe41RefrescoDeManzanaDisabled
            self.ingredients[0] = InformationIngredients.allIngredients.get(eIngredientId._42_MANZANA_VERDE)
            self.ingredients[1] = InformationIngredients.allIngredients.get(eIngredientId._39_LIMON)

            self.foodTimes.append(eRecipeFoodTime.REFRESHMENT_MORNING)
            self.foodTimes.append(eRecipeFoodTime.REFRESHMENT_AFTERNOON)

            self.description[0] = "Lavar las manzanas y sin" 
            self.description[1] = "pelarlas partirlas en pedacitos"
            self.description[2] = "pequeños, retirar el corazón." 
            self.description[3] = "Pelar el limón y partirlo en" 
            self.description[4] = "trozos. Pasa por la licuadora"
            self.description[5] = "las frutas y recoge el jugo en"
            self.description[6] = "un jarro, añade cubitos de "
            self.description[7] = "hielo. Mezcla bien con una "
            self.description[8] = "cuchara de madera. Sirvelo"
            self.description[9] = "bien frio."
        
        elif id == eRecipeId._42_SALCHIPAPAS:
            self.name = "Salchipapas"
            self.preparation = eRecipePreparation.HOT
            
            self.image = ResourceController.game_Recipe42Salchipapas
            self.imageDisabled = ResourceController.game_Recipe42SalchipapasDisabled
            self.ingredients[0] = InformationIngredients.allIngredients.get(eIngredientId._09_PAPA)
            self.ingredients[1] = InformationIngredients.allIngredients.get(eIngredientId._62_SALCHICHA)
            self.ingredients[2] = InformationIngredients.allIngredients.get(eIngredientId._68_ACEITE)
            self.ingredients[3] = InformationIngredients.allIngredients.get(eIngredientId._79_SAL)
            self.ingredients[4] = InformationIngredients.allIngredients.get(eIngredientId._80_SALSA_DE_TOMATE)
            self.ingredients[5] = InformationIngredients.allIngredients.get(eIngredientId._76_MAYONESA)
            self.ingredients[6] = InformationIngredients.allIngredients.get(eIngredientId._77_MOSTAZA)

            self.foodTimes.append(eRecipeFoodTime.REFRESHMENT_MORNING)
            self.foodTimes.append(eRecipeFoodTime.REFRESHMENT_AFTERNOON)

            self.description[0] = "Cortar las papas en forma de" 
            self.description[1] = "(las dejas 30 minutos en agua "
            self.description[2] = "con sal y limón), freír en "
            self.description[3] = "abundante aceite. Luego freír"
            self.description[4] = "la salchicha cortada en "
            self.description[5] = "pedacitos. Sirve con salsas."

        elif id == eRecipeId._43_SANDWICH_DE_JAMON_Y_QUESO:
            self.name = "Sándwich de jamón y queso"
            self.preparation = eRecipePreparation.COLD
            
            self.image = ResourceController.game_Recipe43SandwichDeJamonYQueso
            self.imageDisabled = ResourceController.game_Recipe43SandwichDeJamonYQuesoDisabled
            self.ingredients[0] = InformationIngredients.allIngredients.get(eIngredientId._53_CARNE_DE_CERDO)
            self.ingredients[1] = InformationIngredients.allIngredients.get(eIngredientId._66_QUESO)
            self.ingredients[2] = InformationIngredients.allIngredients.get(eIngredientId._08_PAN)

            self.foodTimes.append(eRecipeFoodTime.REFRESHMENT_MORNING)
            self.foodTimes.append(eRecipeFoodTime.REFRESHMENT_AFTERNOON)
            self.foodTimes.append(eRecipeFoodTime.DINNER)

            self.description[0] = "Colocar sobre una tajada de"
            self.description[1] = "pan el queso y el jamón y luego"
            self.description[2] = "poner otra tajada. Poner en "
            self.description[3] = "sanduchera y esperar a que se "
            self.description[4] = "dore. Servirlo caliente."
        
        elif id == eRecipeId._44_SOPA_DE_GARBANZO:
            self.name = "Sopa de garbanzo"
            self.preparation = eRecipePreparation.HOT
            
            self.image = ResourceController.game_Recipe44SopaDeGarbanzo
            self.imageDisabled = ResourceController.game_Recipe44SopaDeGarbanzoDisabled
            self.ingredients[0] = InformationIngredients.allIngredients.get(eIngredientId._55_GARBANZO)
            self.ingredients[1] = InformationIngredients.allIngredients.get(eIngredientId._33_ZANAHORIA)
            self.ingredients[2] = InformationIngredients.allIngredients.get(eIngredientId._09_PAPA)
            self.ingredients[3] = InformationIngredients.allIngredients.get(eIngredientId._54_CARNE_DE_RES)
            self.ingredients[4] = InformationIngredients.allIngredients.get(eIngredientId._20_CEBOLLA_CABEZONA)
            self.ingredients[5] = InformationIngredients.allIngredients.get(eIngredientId._79_SAL)

            self.foodTimes.append(eRecipeFoodTime.LUNCH)
            self.foodTimes.append(eRecipeFoodTime.DINNER)

            self.description[0] = "Dejar el garbanzo con abundante"
            self.description[1] = "agua desde el día anterior."
            self.description[2] = "Cocinar el garbanzo por lo menos"
            self.description[3] = "15 minutos en la olla express,"
            self.description[4] = "le agregas la carne picada, la"
            self.description[5] = "papa en cuadritos y la "
            self.description[6] = "zanahoria rallada. Agregas la" 
            self.description[7] = "sal, la cebolla finamente "
            self.description[8] = "picada y los aliños que desees,"
            self.description[9] = "lo dejas cocinar nuevamente "
            self.description[10] = "hasta que el garbanzo esté "
            self.description[11] = "blando."

        elif id == eRecipeId._45_SOPA_DE_LENTEJAS:
            self.name = "Sopa de lentejas"
            self.preparation = eRecipePreparation.HOT
            
            self.image = ResourceController.game_Recipe45SopaDeLentejas
            self.imageDisabled = ResourceController.game_Recipe45SopaDeLentejasDisabled
            self.ingredients[0] = InformationIngredients.allIngredients.get(eIngredientId._58_LENTEJA)
            self.ingredients[1] = InformationIngredients.allIngredients.get(eIngredientId._09_PAPA)
            self.ingredients[2] = InformationIngredients.allIngredients.get(eIngredientId._54_CARNE_DE_RES)
            self.ingredients[3] = InformationIngredients.allIngredients.get(eIngredientId._20_CEBOLLA_CABEZONA)
            self.ingredients[4] = InformationIngredients.allIngredients.get(eIngredientId._79_SAL)

            self.foodTimes.append(eRecipeFoodTime.LUNCH)
            self.foodTimes.append(eRecipeFoodTime.DINNER)

            self.description[0] = "Agregar 4 tazas de agua en una"
            self.description[1] = "olla, con la carne picada en "
            self.description[2] = "cuadritos, lava muy bien las"
            self.description[3] = "papas, luego córtarlas en" 
            self.description[4] = "cuadritos con la cáscara,"
            self.description[5] = "agregas sal, cebolla finamente"
            self.description[6] = "picada y los aliños que deseen."
            self.description[7] = "Dejas hervir hasta que la "
            self.description[8] = "lenteja esté blandita y tenga"
            self.description[9] = "una textura espesa."
        
        elif id == eRecipeId._46_SOPA_DE_VERDURAS:
            self.name = "Sopa de verduras"
            self.preparation = eRecipePreparation.HOT
            
            self.image = ResourceController.game_Recipe46SopaDeVerduras
            self.imageDisabled = ResourceController.game_Recipe46SopaDeVerdurasDisabled
            self.ingredients[0] = InformationIngredients.allIngredients.get(eIngredientId._33_ZANAHORIA)
            self.ingredients[1] = InformationIngredients.allIngredients.get(eIngredientId._18_ARVEJA)
            self.ingredients[2] = InformationIngredients.allIngredients.get(eIngredientId._27_HABICUELA)
            self.ingredients[3] = InformationIngredients.allIngredients.get(eIngredientId._17_APIO)
            self.ingredients[4] = InformationIngredients.allIngredients.get(eIngredientId._09_PAPA)
            self.ingredients[5] = InformationIngredients.allIngredients.get(eIngredientId._59_MENUDENCIAS)
            self.ingredients[6] = InformationIngredients.allIngredients.get(eIngredientId._20_CEBOLLA_CABEZONA)
            self.ingredients[7] = InformationIngredients.allIngredients.get(eIngredientId._79_SAL)

            self.foodTimes.append(eRecipeFoodTime.LUNCH)
            self.foodTimes.append(eRecipeFoodTime.DINNER)

            self.description[0] = "Cocinar las menudencias con la"
            self.description[1] = "papa en cuadritos, el apio, la"
            self.description[2] = "zanahoria y habichuela en "
            self.description[3] = "cuadritos, y las arverjas."
            self.description[4] = "Agregas la cebolla finamente" 
            self.description[5] = "picada, sal al gusto y los "
            self.description[6] = "aliños que desees."

        elif id == eRecipeId._47_TE_DE_MANGO:
            self.name = "Té de mango"
            self.preparation = eRecipePreparation.COLD
            
            self.image = ResourceController.game_Recipe47TeDeMango
            self.imageDisabled = ResourceController.game_Recipe47TeDeMangoDisabled
            self.ingredients[0] = InformationIngredients.allIngredients.get(eIngredientId._41_MANGO)
            self.ingredients[1] = InformationIngredients.allIngredients.get(eIngredientId._74_PANELA)
            self.ingredients[2] = InformationIngredients.allIngredients.get(eIngredientId._39_LIMON)
            self.ingredients[3] = InformationIngredients.allIngredients.get(eIngredientId._75_AGUA)

            self.foodTimes.append(eRecipeFoodTime.REFRESHMENT_MORNING)
            self.foodTimes.append(eRecipeFoodTime.REFRESHMENT_AFTERNOON)

            self.description[0] = "Poner en infusión las hojas de" 
            self.description[1] = "mango; tapar, dejar reposar y "
            self.description[2] = "filtrar, agregar la panela"
            self.description[3] = "rayada, mezclar y adicionar el"
            self.description[4] = "hielo. Servir en vasos adornados"
            self.description[5] = "con cascaras de limón."
        
        elif id == eRecipeId._48_TERNERA_A_LA_MARINERA:
            self.name = "Ternera a la marinera"
            self.preparation = eRecipePreparation.HOT
            
            self.image = ResourceController.game_Recipe48TerneraALaMarinera
            self.imageDisabled = ResourceController.game_Recipe48TerneraALaMarineraDisabled
            self.ingredients[0] = InformationIngredients.allIngredients.get(eIngredientId._54_CARNE_DE_RES)
            self.ingredients[1] = InformationIngredients.allIngredients.get(eIngredientId._05_HARINA_DE_TRIGO)
            self.ingredients[2] = InformationIngredients.allIngredients.get(eIngredientId._32_TOMATE)
            self.ingredients[3] = InformationIngredients.allIngredients.get(eIngredientId._20_CEBOLLA_CABEZONA)
            self.ingredients[4] = InformationIngredients.allIngredients.get(eIngredientId._81_SOPAS_EN_CREMA)
            self.ingredients[5] = InformationIngredients.allIngredients.get(eIngredientId._75_AGUA)
            self.ingredients[6] = InformationIngredients.allIngredients.get(eIngredientId._79_SAL)

            self.foodTimes.append(eRecipeFoodTime.LUNCH)
            self.foodTimes.append(eRecipeFoodTime.DINNER)

            self.description[0] = "Dorar la carne, espolvorear con"
            self.description[1] = "la harina de trigo añadiendo"
            self.description[2] = "los demás ingredientes. "
            self.description[3] = "Disuelve el sobre de crema (con"
            self.description[4] = "sabor a camarones) en agua o "
            self.description[5] = "leche, y  agrega a la "
            self.description[6] = "preparación.  Puedes acompañar"
            self.description[7] = "con trocitos de queso blanco, "
            self.description[8] = "arroz y verduras."
        
        elif id == eRecipeId._49_TOMATES_RELLENOS:
            self.name = "Tomates rellenos"
            self.preparation = eRecipePreparation.HOT
            
            self.image = ResourceController.game_Recipe49TomatesRellenos
            self.imageDisabled = ResourceController.game_Recipe49TomatesRellenosDisabled
            self.ingredients[0] = InformationIngredients.allIngredients.get(eIngredientId._32_TOMATE)
            self.ingredients[1] = InformationIngredients.allIngredients.get(eIngredientId._06_MAIZ)
            self.ingredients[2] = InformationIngredients.allIngredients.get(eIngredientId._20_CEBOLLA_CABEZONA)
            self.ingredients[3] = InformationIngredients.allIngredients.get(eIngredientId._52_ATUN)
            self.ingredients[4] = InformationIngredients.allIngredients.get(eIngredientId._22_CILANTRO)
            self.ingredients[5] = InformationIngredients.allIngredients.get(eIngredientId._28_LECHUGA)

            self.foodTimes.append(eRecipeFoodTime.LUNCH)
            self.foodTimes.append(eRecipeFoodTime.DINNER)

            self.description[0] = "Lavar los tomates, quitarles la"
            self.description[1] = "tapa superior y ahuecarlos con un"
            self.description[2] = "cuchillo reservando el "
            self.description[3] = "contenido. Pica finamente el"
            self.description[4] = "contenido interior de los"
            self.description[5] = "tomates. Cocina el maíz tierno"
            self.description[6] = "hasta que ablande. Mezcla en una"
            self.description[7] = "taza el atún, el maíz cocido, el"
            self.description[8] = "cilantro, el tomate y la "
            self.description[9] = "cebolla. Adiciona sal. Rellena" 
            self.description[10] = "los tomates ahuecados con ésta "
            self.description[11] = "mezcla."

        elif id == eRecipeId._50_TORTA_DE_AHUYAMA:
            self.name = "Torta de ahuyama"
            self.preparation = eRecipePreparation.HOT
            
            self.image = ResourceController.game_Recipe50TortaDeAhuyama
            self.imageDisabled = ResourceController.game_Recipe50TortaDeAhuyamaDisabled
            self.ingredients[0] = InformationIngredients.allIngredients.get(eIngredientId._15_AHUYAMA)
            self.ingredients[1] = InformationIngredients.allIngredients.get(eIngredientId._57_HUEVO)
            self.ingredients[2] = InformationIngredients.allIngredients.get(eIngredientId._68_ACEITE)
            self.ingredients[3] = InformationIngredients.allIngredients.get(eIngredientId._78_POLVO_DE_HONEAR)
            self.ingredients[4] = InformationIngredients.allIngredients.get(eIngredientId._05_HARINA_DE_TRIGO)
            self.ingredients[5] = InformationIngredients.allIngredients.get(eIngredientId._71_AZUCAR)

            self.foodTimes.append(eRecipeFoodTime.LUNCH)
            self.foodTimes.append(eRecipeFoodTime.DINNER)

            self.description[0] = "Mezclar la ahuyama en forma de"
            self.description[1] = "puré con los huevos, el aceite,"
            self.description[2] = "el azúcar, la harina y el polvo"
            self.description[3] = "de hornear, hasta que sea una "
            self.description[4] = "masa homogénea. Luego engrasas"
            self.description[5] = "un sartén y viertes la mezcla "
            self.description[6] = "por cucharadas, cuando haga "
            self.description[7] = "burbujas volteas la torta y "
            self.description[8] = "después de unos minutos con el"
            self.description[9] = "tenedor verifica que esté lista."  
        
        elif id == eRecipeId._51_TORTA_DE_BANANO:
            self.name = "Torta de banano"
            self.preparation = eRecipePreparation.HOT
            
            self.image = ResourceController.game_Recipe51TortaDeBanano
            self.imageDisabled = ResourceController.game_Recipe51TortaDeBananoDisabled
            self.ingredients[0] = InformationIngredients.allIngredients.get(eIngredientId._35_BANANO)
            self.ingredients[1] = InformationIngredients.allIngredients.get(eIngredientId._57_HUEVO)
            self.ingredients[2] = InformationIngredients.allIngredients.get(eIngredientId._68_ACEITE)
            self.ingredients[3] = InformationIngredients.allIngredients.get(eIngredientId._05_HARINA_DE_TRIGO)
            self.ingredients[4] = InformationIngredients.allIngredients.get(eIngredientId._71_AZUCAR)
            self.ingredients[5] = InformationIngredients.allIngredients.get(eIngredientId._78_POLVO_DE_HONEAR)

            self.foodTimes.append(eRecipeFoodTime.LUNCH)
            self.foodTimes.append(eRecipeFoodTime.DINNER)

            self.description[0] = "Mezclar el banano en forma de" 
            self.description[1] = "puré con los huevos, el aceite,"
            self.description[2] = "el azúcar, la harina y el polvo"
            self.description[3] = "de hornear, hasta que sea una "
            self.description[4] = "masa homogénea. Luego engrasas"
            self.description[5] = "un sartén y viertes la mezcla "
            self.description[6] = "por cucharadas, cuando haga "
            self.description[7] = "burbujas volteas la torta y "
            self.description[8] = "después de unos minutos con el"
            self.description[9] = "tenedor verifica que esté lista."
        
        elif id == eRecipeId._52_TORTA_DE_ZANAHORIA:
            self.name = "Torta de zanahoria"
            self.preparation = eRecipePreparation.HOT
            
            self.image = ResourceController.game_Recipe52TortaDeZanahoria
            self.imageDisabled = ResourceController.game_Recipe52TortaDeZanahoriaDisabled
            self.ingredients[0] = InformationIngredients.allIngredients.get(eIngredientId._33_ZANAHORIA)
            self.ingredients[1] = InformationIngredients.allIngredients.get(eIngredientId._57_HUEVO)
            self.ingredients[2] = InformationIngredients.allIngredients.get(eIngredientId._68_ACEITE)
            self.ingredients[3] = InformationIngredients.allIngredients.get(eIngredientId._05_HARINA_DE_TRIGO)
            self.ingredients[4] = InformationIngredients.allIngredients.get(eIngredientId._71_AZUCAR)
            self.ingredients[5] = InformationIngredients.allIngredients.get(eIngredientId._78_POLVO_DE_HONEAR)

            self.foodTimes.append(eRecipeFoodTime.LUNCH)
            self.foodTimes.append(eRecipeFoodTime.DINNER)

            self.description[0] = "Rallar la zanahoria y mezclar" 
            self.description[1] = "con los huevos, el aceite, el"
            self.description[2] = "azúcar, la harina y el polvo de"
            self.description[3] = "hornear, hasta que sea una masa"
            self.description[4] = "homogénea. Engrasas un sartén y"
            self.description[5] = "viertes la mezcla por "
            self.description[6] = "cucharadas, cuando haga "
            self.description[7] = "burbujas volteas la torta y"
            self.description[8] = "después de unos minutos con el"
            self.description[9] = "tenedor verifica que esté lista."
        
        elif id == eRecipeId._53_TORTILLAS_DE_ACELGAS:
            self.name = "Tortillas de acelgas"
            self.preparation = eRecipePreparation.HOT
            
            self.image = ResourceController.game_Recipe53TortillaDeAcelga
            self.imageDisabled = ResourceController.game_Recipe53TortillaDeAcelgaDisabled
            self.ingredients[0] = InformationIngredients.allIngredients.get(eIngredientId._14_ACELGA)
            self.ingredients[1] = InformationIngredients.allIngredients.get(eIngredientId._57_HUEVO)
            self.ingredients[2] = InformationIngredients.allIngredients.get(eIngredientId._20_CEBOLLA_CABEZONA)
            self.ingredients[3] = InformationIngredients.allIngredients.get(eIngredientId._16_AJO)
            self.ingredients[4] = InformationIngredients.allIngredients.get(eIngredientId._68_ACEITE)
            self.ingredients[5] = InformationIngredients.allIngredients.get(eIngredientId._79_SAL)

            self.foodTimes.append(eRecipeFoodTime.LUNCH)
            self.foodTimes.append(eRecipeFoodTime.DINNER)

            self.description[0] = "Cocinar las acelgas, luego" 
            self.description[1] = "cortarlas en tiras pequeñas, en"
            self.description[2] = "una taza aparte bates los "
            self.description[3] = "huevos y les agregas los aliños"
            self.description[4] = "finamente picados (cebolla, "
            self.description[5] = "ajo) le agregas sal. Luego "
            self.description[6] = "mezclas las acelgas con los"
            self.description[7] = "huevos.  En un sartén engrasado"
            self.description[8] = "agregas las mezcla y verificas"
            self.description[9] = "que quede bien cocinada por "
            self.description[10] = "ambos lados."
        
        elif id == eRecipeId._54_TORTILLAS_DE_ESPINACA:
            self.name = "Tortillas de espinaca"
            self.preparation = eRecipePreparation.HOT
            
            self.image = ResourceController.game_Recipe54TortillaDeEspinaca
            self.imageDisabled = ResourceController.game_Recipe54TortillaDeEspinacaDisabled
            self.ingredients[0] = InformationIngredients.allIngredients.get(eIngredientId._24_ESPINACA)
            self.ingredients[1] = InformationIngredients.allIngredients.get(eIngredientId._57_HUEVO)
            self.ingredients[2] = InformationIngredients.allIngredients.get(eIngredientId._20_CEBOLLA_CABEZONA)
            self.ingredients[3] = InformationIngredients.allIngredients.get(eIngredientId._16_AJO)
            self.ingredients[4] = InformationIngredients.allIngredients.get(eIngredientId._68_ACEITE)
            self.ingredients[5] = InformationIngredients.allIngredients.get(eIngredientId._79_SAL)

            self.foodTimes.append(eRecipeFoodTime.LUNCH)
            self.foodTimes.append(eRecipeFoodTime.DINNER)

            self.description[0] = "Cocinar las espinacas con los"
            self.description[1] = "tallos, luego cortarlas en "
            self.description[2] = "tiras pequeñas, en una taza "
            self.description[3] = "aparte bates los huevos y les"
            self.description[4] = "agregas los aliños finamente"
            self.description[5] = "picados (cebolla, ajo) le "
            self.description[6] = "agregas sal. Luego mezclas las"
            self.description[7] = "espinacas con los huevos. En un"
            self.description[8] = "sartén engrasado agregas las "
            self.description[9] = "mezcla y verificas que quede "
            self.description[10] = "bien cocinada por ambos lados."
        
        elif id == eRecipeId._55_ZAFRESCO:
            self.name = "Zafresco"
            self.preparation = eRecipePreparation.COLD
            
            self.image = ResourceController.game_Recipe55Zafresco
            self.imageDisabled = ResourceController.game_Recipe55ZafrescoDisabled
            self.ingredients[0] = InformationIngredients.allIngredients.get(eIngredientId._40_MANDARINA)
            self.ingredients[1] = InformationIngredients.allIngredients.get(eIngredientId._33_ZANAHORIA)
            self.ingredients[2] = InformationIngredients.allIngredients.get(eIngredientId._30_PEPINO_COMUN)
            self.ingredients[3] = InformationIngredients.allIngredients.get(eIngredientId._75_AGUA)

            self.foodTimes.append(eRecipeFoodTime.REFRESHMENT_MORNING)
            self.foodTimes.append(eRecipeFoodTime.REFRESHMENT_AFTERNOON)

            self.description[0] = "Licuar el jugo de mandarina, de"
            self.description[1] = "zanahoria y de pepino con hielo."
            
            
        elif id == eRecipeId._55_ZAFRESCO:
            self.name = "Zafresco"
            self.preparation = eRecipePreparation.COLD
            
            self.image = ResourceController.game_Recipe55Zafresco
            self.imageDisabled = ResourceController.game_Recipe55ZafrescoDisabled
            self.ingredients[0] = InformationIngredients.allIngredients.get(eIngredientId._40_MANDARINA)
            self.ingredients[1] = InformationIngredients.allIngredients.get(eIngredientId._33_ZANAHORIA)
            self.ingredients[2] = InformationIngredients.allIngredients.get(eIngredientId._30_PEPINO_COMUN)
            self.ingredients[3] = InformationIngredients.allIngredients.get(eIngredientId._75_AGUA)

            self.foodTimes.append(eRecipeFoodTime.REFRESHMENT_MORNING)
            self.foodTimes.append(eRecipeFoodTime.REFRESHMENT_AFTERNOON)

            self.description[0] = "Licuar el jugo de mandarina, de"
            self.description[1] = "zanahoria y de pepino con hielo."
            

        elif id == eRecipeId._56_TORTILLA_DE_MAZORCA:
            self.name = "Tortilla de mazorca"
            self.preparation = eRecipePreparation.HOT
            
            self.image = ResourceController.game_Recipe56TortillaDeMazorca
            self.imageDisabled = ResourceController.game_Recipe56TortillaDeMazorcaDisabled
            self.ingredients[0] = InformationIngredients.allIngredients.get(eIngredientId._57_HUEVO)
            self.ingredients[1] = InformationIngredients.allIngredients.get(eIngredientId._06_MAIZ)
            self.ingredients[2] = InformationIngredients.allIngredients.get(eIngredientId._69_MANTEQUILLA)

            self.foodTimes.append(eRecipeFoodTime.BREAKFAST)

            self.description[0] = "En un recipiente bate los huevos"
            self.description[1] = "de acuerdo a las porciones que"
            self.description[2] = "vayas a preparar, en una sarten"
            self.description[3] = "con una cucharada de mantequilla"
            self.description[4] = "pon a sofreir la mazorca y agrega"
            self.description[5] = "los huevos que tengas revueltos,"
            self.description[6] = "deja a fuego lento por 5 minutos"
            self.description[7] = "y voltea para que dore la otra"
            self.description[8] = "cara de la torta."


        elif id == eRecipeId._57_BATIDO_DE_GUAYABA_Y_AVENA:
            self.name = "Batido de guayaba y avena"
            self.preparation = eRecipePreparation.COLD
            
            self.image = ResourceController.game_Recipe57BatidoDeGuayabaYAvena
            self.imageDisabled = ResourceController.game_Recipe57BatidoDeGuayabaYAvenaDisabled
            self.ingredients[0] = InformationIngredients.allIngredients.get(eIngredientId._65_LECHE)
            self.ingredients[1] = InformationIngredients.allIngredients.get(eIngredientId._38_GUAYABA)
            self.ingredients[2] = InformationIngredients.allIngredients.get(eIngredientId._03_AVENA)
            self.ingredients[3] = InformationIngredients.allIngredients.get(eIngredientId._71_AZUCAR)

            self.foodTimes.append(eRecipeFoodTime.BREAKFAST)
            
            self.description[0] = "Vierte en la licuadora 2 guayabas,"
            self.description[1] = "2 tazas de leche y 2 cucharadas de"
            self.description[2] = "de avena y dos cucharadas de"
            self.description[3] = "azúcar, bate por 3 minutos los"
            self.description[4] = "ingredientes, cuela tu batido y"
            self.description[5] = "empieza tu día con mucha energía."
            

        elif id == eRecipeId._58_BATIDO_DE_YOGURT_FRESAS_Y_AVENA:
            self.name = "Batido de yogurt, fresas y avena"
            self.preparation = eRecipePreparation.COLD
            
            self.image = ResourceController.game_Recipe58BatidoDeYogurtFresasYAvena
            self.imageDisabled = ResourceController.game_Recipe58BatidoDeYogurtFresasYAvenaDisabled
            self.ingredients[0] = InformationIngredients.allIngredients.get(eIngredientId._67_YOGURT)
            self.ingredients[1] = InformationIngredients.allIngredients.get(eIngredientId._37_FRESA)
            self.ingredients[2] = InformationIngredients.allIngredients.get(eIngredientId._03_AVENA)

            self.foodTimes.append(eRecipeFoodTime.BREAKFAST)
            
            self.description[0] = "Vierte en la licuadora una taza"
            self.description[1] = "de yogurt, las fresas y dos"
            self.description[2] = "cucharadas de avena, bate por 3"
            self.description[3] = "minutos hasta que se mezclen"
            self.description[4] = "todos los ingredientes y sirve tu"
            self.description[5] = "delicioso batido para empezar"
            self.description[6] = "el día."
            

        elif id == eRecipeId._59_PANQUEQUES_DE_AVENA:
            self.name = "Panqueques de avena"
            self.preparation = eRecipePreparation.HOT
            
            self.image = ResourceController.game_Recipe59PanquequesDeAvena
            self.imageDisabled = ResourceController.game_Recipe59PanquequesDeAvenaDisabled
            self.ingredients[0] = InformationIngredients.allIngredients.get(eIngredientId._05_HARINA_DE_TRIGO)
            self.ingredients[1] = InformationIngredients.allIngredients.get(eIngredientId._03_AVENA)
            self.ingredients[2] = InformationIngredients.allIngredients.get(eIngredientId._57_HUEVO)
            self.ingredients[3] = InformationIngredients.allIngredients.get(eIngredientId._79_SAL)
            self.ingredients[4] = InformationIngredients.allIngredients.get(eIngredientId._65_LECHE)
            self.ingredients[5] = InformationIngredients.allIngredients.get(eIngredientId._71_AZUCAR)

            self.foodTimes.append(eRecipeFoodTime.BREAKFAST)
            
            self.description[0] = "En la licuadora vierte una taza"
            self.description[1] = "de harina de trigo, 1/2 taza de"
            self.description[2] = "avena, 2 huevos , una pizca de"
            self.description[3] = "sal, y cucharada de azúcar, 1"
            self.description[4] = "taza de leche semidescremada,"
            self.description[5] = "bate por 3 minutos todos los"
            self.description[6] = "ingredientes. Aparte prepara una"
            self.description[7] = "sarten caliente con una gota"
            self.description[8] = "de aceite aceite, e incorpora"
            self.description[9] = "una porción de la mezcla,"
            self.description[10] ="cocina por ambos lados hasta"
            self.description[11] ="que esté dorado tu panqueque."
            

        elif id == eRecipeId._60_TORTILLA_DE_VERDURAS_Y_QUESO:
            self.name = "Tortilla de verduras y queso"
            self.preparation = eRecipePreparation.HOT
            
            self.image = ResourceController.game_Recipe60TortillaDeVerdurasYQueso
            self.imageDisabled = ResourceController.game_Recipe60TortillaDeVerdurasYQuesoDisabled
            self.ingredients[0] = InformationIngredients.allIngredients.get(eIngredientId._57_HUEVO)
            self.ingredients[1] = InformationIngredients.allIngredients.get(eIngredientId._33_ZANAHORIA)
            self.ingredients[2] = InformationIngredients.allIngredients.get(eIngredientId._20_CEBOLLA_CABEZONA)
            self.ingredients[3] = InformationIngredients.allIngredients.get(eIngredientId._31_PIMENTON)
            self.ingredients[4] = InformationIngredients.allIngredients.get(eIngredientId._17_APIO)
            self.ingredients[5] = InformationIngredients.allIngredients.get(eIngredientId._66_QUESO)
            self.ingredients[6] = InformationIngredients.allIngredients.get(eIngredientId._79_SAL)

            self.foodTimes.append(eRecipeFoodTime.BREAKFAST)
            
            self.description[0] = "Ralla la zanahoria y el queso,"
            self.description[1] = "pica finamente la cebolla, el"
            self.description[2] = "pimentón, el tallo del apio con"
            self.description[3] = "algunas hojas, sofrie los"
            self.description[4] = "vegetales por 3 minutos."
            self.description[5] = "Aparte en un recipiente bate 2"
            self.description[6] = "huevos e incorpora todos los"
            self.description[7] = "ingredientes sofreidos y sal al"
            self.description[8] = "gusto. En una sarten calentada"
            self.description[9] = "con una gota de aceite vierte"
            self.description[10] ="la mezcla, tápala y cocina a"
            self.description[11] ="fuego hasta que dore."


        elif id == eRecipeId._61_PANQUEQUES_DE_FRUTA:
            self.name = "Panqueques de fruta"
            self.preparation = eRecipePreparation.COLD
            
            self.image = ResourceController.game_Recipe61PanquequesDeFruta
            self.imageDisabled = ResourceController.game_Recipe61PanquequesDeFrutaDisabled
            self.ingredients[0] = InformationIngredients.allIngredients.get(eIngredientId._05_HARINA_DE_TRIGO)
            self.ingredients[1] = InformationIngredients.allIngredients.get(eIngredientId._57_HUEVO)
            self.ingredients[2] = InformationIngredients.allIngredients.get(eIngredientId._79_SAL)
            self.ingredients[3] = InformationIngredients.allIngredients.get(eIngredientId._65_LECHE)
            self.ingredients[4] = InformationIngredients.allIngredients.get(eIngredientId._71_AZUCAR)
            self.ingredients[5] = InformationIngredients.allIngredients.get(eIngredientId._35_BANANO)
            self.ingredients[6] = InformationIngredients.allIngredients.get(eIngredientId._37_FRESA)

            self.foodTimes.append(eRecipeFoodTime.BREAKFAST)
            
            self.description[0] = "En la licuadora viarte 1 taza"
            self.description[1] = "de harina de trigo, 1 taza de"
            self.description[2] = "leche, 2 huevos, pizca de sal"
            self.description[3] = "y azúcar, bate los ingredientes"
            self.description[4] = "por 3 minutos. Incorpora una"
            self.description[5] = "cucharada de los ingredientes"
            self.description[6] = "en una sarten precalentada con"
            self.description[7] = "una gota de aceite. Mientas se"
            self.description[8] = "cocinan los panqueques pica en"
            self.description[9] = "tajadas el banano y las fresas"
            self.description[10] ="y sirve una porción encima de"
            self.description[11] ="cada uno."


        elif id == eRecipeId._62_AREPAS_DE_MAZORCA:
            self.name = "Arepas de mazorca"
            self.preparation = eRecipePreparation.HOT
            
            self.image = ResourceController.game_Recipe62ArepasDeMazorca
            self.imageDisabled = ResourceController.game_Recipe62ArepasDeMazorcaDisabled
            self.ingredients[0] = InformationIngredients.allIngredients.get(eIngredientId._06_MAIZ)
            self.ingredients[1] = InformationIngredients.allIngredients.get(eIngredientId._65_LECHE)
            self.ingredients[2] = InformationIngredients.allIngredients.get(eIngredientId._71_AZUCAR)
            self.ingredients[3] = InformationIngredients.allIngredients.get(eIngredientId._79_SAL)
            self.ingredients[4] = InformationIngredients.allIngredients.get(eIngredientId._66_QUESO)

            self.foodTimes.append(eRecipeFoodTime.BREAKFAST)
            
            self.description[0] = "Desgrana 4 mazorcas tiernas,"
            self.description[1] = "viertelas a la licuadora junto"
            self.description[2] = "con 1/2 taza de leche, pizca de"
            self.description[3] = "sal y 1/2 cucharada de azúcar."
            self.description[4] = "Licúa por 3 minutos, hasta que"
            self.description[5] = "la mezcla esté espesa."
            self.description[6] = "Precalienta una sarten con una"
            self.description[7] = "gota de aceite para poner a azar"
            self.description[8] = "las arepas, cuanda estén doradas"
            self.description[9] = "por ambos lados pon encima una"
            self.description[10] ="porción de queso."

            

    def getIngredients(self):
        
        ingredientsToReturn = list()
        
        for ingredient in self.ingredients:
            if ingredient != None:
                ingredientsToReturn.append(ingredient)
                
        return ingredientsToReturn
    
    def getImage(self):
        return self.image
    
    def getName(self):
        return self.name
    

class Ingredient:

    def __init__(self, id):
        
        self.id = id
        
        self.description = list()
        self.description.append("")
        self.description.append("")
        self.description.append("")
        self.description.append("")
        self.description.append("")
        self.description.append("")
        self.description.append("")
        
        # Grupo 1: Cereales, raices, tuberculos y platanos
        if id == eIngredientId._01_AREPA:
            self.name = "Arepa"
            self.image = ResourceController.game_Ingredient01Arepa
            self.group = eIngredientGroup.GROUP_1_CEREALES
            self.nutritionValue = 0
            self.description[0] = "La arepa esta hecha de masa de maíz"
            self.description[1] = "molido o de harina de maíz "
            self.description[2] = "precocida, su consumo es muy "
            self.description[3] = "popular en Colombia y Venezuela."
            
        elif id == eIngredientId._02_ARROZ:
            self.name = "Arroz"
            self.image = ResourceController.game_Ingredient02Arroz
            self.group = eIngredientGroup.GROUP_1_CEREALES
            self.nutritionValue = 0
            self.description[0] = "Desde el punto de vista alimenticio"
            self.description[1] = "es el cereal más importante,"
            self.description[2] = "después del trigo. Es un alimento" 
            self.description[3] = "muy rico en hidratos de carbono "
            self.description[4] = "(casi el 80%).Te sugerimos consumir"
            self.description[5] = "arroz integral pues, además tiene"
            self.description[6] = "fibra y vitaminas E y B."
            
        elif id == eIngredientId._03_AVENA:
            self.name = "Avena"
            self.image = ResourceController.game_Ingredient03Avena
            self.group = eIngredientGroup.GROUP_1_CEREALES
            self.nutritionValue = 0
            self.description[0] = "La avena es rica en proteínas de" 
            self.description[1] = "alto valor biológico, grasas y un "
            self.description[2] = "gran número de vitaminas, minerales."
            self.description[3] = "Es el cereal con mayor proporción"
            self.description[4] = "de grasa vegetal."
                        
        elif id == eIngredientId._04_HARINA_DE_MAIZ_PRECOCIDA:
            self.name = "Harina de maíz precocida"
            self.image = ResourceController.game_Ingredient04HarinaDeMaizPrecocida
            self.group = eIngredientGroup.GROUP_1_CEREALES
            self.nutritionValue = 0
            self.description[0] = "Es un alimento base de nuestra" 
            self.description[1] = "cultura alimentaria y hace parte" 
            self.description[2] = "de múltiples preparaciones, la más"
            self.description[3] = "popular, la arepa, en muchas "
            self.description[4] = "variedades."
            
        elif id == eIngredientId._05_HARINA_DE_TRIGO:
            self.name = "Harina de trigo"
            self.image = ResourceController.game_Ingredient05HarinaDeTrigo
            self.group = eIngredientGroup.GROUP_1_CEREALES
            self.nutritionValue = 0
            self.description[0] = "Se obtiene harina de diferentes" 
            self.description[1] = "cereales, la más común es la" 
            self.description[2] = "harina de trigo. Es la base en la" 
            self.description[3] = "elaboración de diferentes alimentos"
            self.description[4] = "entre ellos el pan."
            
        elif id == eIngredientId._06_MAIZ:
            self.name = "Maíz"
            self.image = ResourceController.game_Ingredient06Maiz
            self.group = eIngredientGroup.GROUP_1_CEREALES
            self.nutritionValue = 0
            self.description[0] = "El maíz es el tercer cereal en" 
            self.description[1] = "importancia, después del trigo y"
            self.description[2] = "del arroz."
            
        elif id == eIngredientId._07_MIGA_DE_PAN:
            self.name = "Miga de pan"
            self.image = ResourceController.game_Ingredient07MigaDePan
            self.group = eIngredientGroup.GROUP_1_CEREALES
            self.nutritionValue = 0
            self.description[0] = "Es el pan desmenuzado, que se usa"
            self.description[1] = "como base para recetas."
            
        elif id == eIngredientId._08_PAN:
            self.name = "Pan"
            self.image = ResourceController.game_Ingredient08Pan
            self.group = eIngredientGroup.GROUP_1_CEREALES
            self.nutritionValue = 0
            self.description[0] = "El pan te aporta fibra que ayuda a"
            self.description[1] = "mejorar la digestión. Los panes "
            self.description[2] = "blancos de harinas refinadas son "
            self.description[3] = "los que aportan una menor cantidad,"
            self.description[4] = "el pan denominado como integral "
            self.description[5] = "puede llegar a tener entre tres a "
            self.description[6] = "cuatro veces más de fibra."
            
        elif id == eIngredientId._09_PAPA:
            self.name = "Papa"
            self.image = ResourceController.game_Ingredient09Papa
            self.group = eIngredientGroup.GROUP_1_CEREALES
            self.nutritionValue = 0
            self.description[0] = "La papa es el tubérculo más" 
            self.description[1] = "importante, aportan proteína,"
            self.description[2] = "hierro y es fuente de vitamina C,"
            self.description[3] = "tiamina, niacina y fibra dietética."
            
        elif id == eIngredientId._10_PASTA:
            self.name = "Pasta"
            self.image = ResourceController.game_Ingredient10Pasta
            self.group = eIngredientGroup.GROUP_1_CEREALES
            self.nutritionValue = 0
            self.description[0] = "La pasta aporta calorías a tu" 
            self.description[1] = "cuerpo, gracias a su contenido de"  
            self.description[2] = "hidratos de carbono, proteínas y "
            self.description[3] = "grasas minerales."
            
        elif id == eIngredientId._11_PLATANO:
            self.name = "Plátano"
            self.image = ResourceController.game_Ingredient11Platano
            self.group = eIngredientGroup.GROUP_1_CEREALES
            self.nutritionValue = 0
            self.description[0] = "Es un alimento que ayuda a saciar" 
            self.description[1] = "el hambre rápidamente, por su "
            self.description[2] = "riqueza en potasio ayuda a "
            self.description[3] = "equilibrar el agua en el cuerpo y"
            self.description[4] = "favorece la eliminación de líquidos."
            
        # Grupo 2: Hortalizas, verduras, leguminosas verdes
        elif id == eIngredientId._12_SOYA:
            self.name = "Soya"
            self.image = ResourceController.game_Ingredient12Soya
            self.group = eIngredientGroup.GROUP_1_CEREALES
            self.nutritionValue = 0
            self.description[0] = "Es un alimento muy saludable," 
            self.description[1] = "reduce el nivel de azúcar en la" 
            self.description[2] = "sangre, reduce el colesterol y "
            self.description[3] = "ayuda a evitar la osteoporosis, "
            self.description[4] = "además  es una importante fuente"
            self.description[5] = "de proteína."
            
        elif id == eIngredientId._13_YUCA:
            self.name = "Yuca"
            self.image = ResourceController.game_Ingredient13Yuca
            self.group = eIngredientGroup.GROUP_1_CEREALES
            self.nutritionValue = 0
            self.description[0] = "La Yuca es un alimento muy rico en" 
            self.description[1] = "hidratos de carbono y pobre en "
            self.description[2] = "grasas y proteínas. Es un alimento"
            self.description[3] = "muy digestivo."
            
        elif id == eIngredientId._14_ACELGA:
            self.name = "Acelga"
            self.image = ResourceController.game_Ingredient14Acelga
            self.group = eIngredientGroup.GROUP_2_VERDURAS
            self.nutritionValue = 0
            self.description[0] = "Esta planta de hojas verdes" 
            self.description[1] = "destaca por su gran cantidad de" 
            self.description[2] = "componentes beneficiosos para el" 
            self.description[3] = "organismo y su ausencia de grasas"
            self.description[4] = "y calorías."
            
        elif id == eIngredientId._15_AHUYAMA:
            self.name = "Ahuyama"
            self.image = ResourceController.game_Ingredient15Ahuyama
            self.group = eIngredientGroup.GROUP_2_VERDURAS
            self.nutritionValue = 0
            self.description[0] = "Le ofrece varios beneficios a" 
            self.description[1] = "nuestro organismo, especialmente" 
            self.description[2] = "porque es fuente de beta caroteno,"
            self.description[3] = "un precursor de la vitamina A y "
            self.description[4] = "potente antioxidante que evita el"
            self.description[5] = "envejecimiento de las células."
            
        elif id == eIngredientId._16_AJO:
            self.name = "Ajo"
            self.image = ResourceController.game_Ingredient16Ajo
            self.group = eIngredientGroup.GROUP_2_VERDURAS
            self.nutritionValue = 0
            self.description[0] = "Favorece los procesos digestivos;"
            self.description[1] = "inhibe el virus del resfriado "
            self.description[2] = "común, amebas y otros"
            self.description[3] = "microorganismos relacionados con" 
            self.description[4] = "enfermedades degenerativas como el"
            self.description[5] = "cáncer.  El ajo elimina toxinas "
            self.description[6] = "incluyendo metales como el plomo."
            
        elif id == eIngredientId._17_APIO:
            self.name = "Apio"
            self.image = ResourceController.game_Ingredient17Apio
            self.group = eIngredientGroup.GROUP_2_VERDURAS
            self.nutritionValue = 0
            self.description[0] = "El apio resulta muy positivo en la"
            self.description[1] = "dieta humana debido a su alto "
            self.description[2] = "contenido de fibra dietética, "
            self.description[3] = "vitaminas y minerales, además de" 
            self.description[4] = "ser considerado un buen diurético"
            self.description[5] = "debido al alto porcentaje de agua."
            self.description[6] = "Debes moderar su consumo."
            
        elif id == eIngredientId._18_ARVEJA:
            self.name = "Arveja"
            self.image = ResourceController.game_Ingredient18Arveja
            self.group = eIngredientGroup.GROUP_2_VERDURAS
            self.nutritionValue = 0
            self.description[0] = "La arveja tiene una gran cantidad"
            self.description[1] = "de carbohidratos y, al igual que "
            self.description[2] = "los cereales, es fuente de"
            self.description[3] = "Vitaminas del complejo B. Es rica"
            self.description[4] = "en minerales como fósforo y hierro,"
            self.description[5] = "contiene una alta concentración en"
            self.description[6] = "fibras y son bajas en grasas."
            
        elif id == eIngredientId._19_BROCOLI:
            self.name = "Brócoli"
            self.image = ResourceController.game_Ingredient19Brocoli
            self.group = eIngredientGroup.GROUP_2_VERDURAS
            self.nutritionValue = 0
            self.description[0] = "Es llamado un súper alimento por" 
            self.description[1] = "sus propiedades nutritivas y "
            self.description[2] = "antioxidantes, contiene "
            self.description[3] = "importantes cantidades de" 
            self.description[4] = "vitaminas y minerales."
            
        elif id == eIngredientId._20_CEBOLLA_CABEZONA:
            self.name = "Cebolla cabezona"
            self.image = ResourceController.game_Ingredient20CebollaCabezona
            self.group = eIngredientGroup.GROUP_2_VERDURAS
            self.nutritionValue = 0
            self.description[0] = "La cebolla  estimula el aparato" 
            self.description[1] = "digestivo, limpia el intestino," 
            self.description[2] = "previene algunos tipos de cáncer,"
            self.description[3] = "la hipertensión y el insomnio. Es"
            self.description[4] = "un alimento súper recomendado."
            
        elif id == eIngredientId._21_CEBOLLA_LARGA:
            self.name = "Cebolla larga"
            self.image = ResourceController.game_Ingredient21CebollaLarga
            self.group = eIngredientGroup.GROUP_2_VERDURAS
            self.nutritionValue = 0
            self.description[0] = "Es una verdura que cumple labores"
            self.description[1] = "de especia aportando buen sabor a"
            self.description[2] = "las preparaciones."
            
        elif id == eIngredientId._22_CILANTRO:
            self.name = "Cilantro"
            self.image = ResourceController.game_Ingredient22Cilantro
            self.group = eIngredientGroup.GROUP_2_VERDURAS
            self.nutritionValue = 0
            self.description[0] = "Es una verdura que cumple labores" 
            self.description[1] = "de especia aportando buen sabor a"
            self.description[2] = "las preparaciones."
            
        elif id == eIngredientId._23_COLIFLOR:
            self.name = "Coliflor"
            self.image = ResourceController.game_Ingredient23Coliflor
            self.group = eIngredientGroup.GROUP_2_VERDURAS
            self.nutritionValue = 0
            self.description[0] = "Es un excelente alimento, sus"
            self.description[1] = "propiedades antioxidantes resultan"
            self.description[2] = "benéficas para la prevención de "
            self.description[3] = "enfermedades asociadas con las "
            self.description[4] = "arterias y el corazón."
            
        elif id == eIngredientId._24_ESPINACA:
            self.name = "Espinaca"
            self.image = ResourceController.game_Ingredient24Espinaca
            self.group = eIngredientGroup.GROUP_2_VERDURAS
            self.nutritionValue = 0
            self.description[0] = "Aunque es un alimento rico en "
            self.description[1] = "vitaminas A y E, yodo y varios "
            self.description[2] = "antioxidantes, debe consumirse "
            self.description[3] = "con moderación."
            
        elif id == eIngredientId._25_FRIJOL:
            self.name = "Frijol"
            self.image = ResourceController.game_Ingredient25Frijol
            self.group = eIngredientGroup.GROUP_2_VERDURAS
            self.nutritionValue = 0
            self.description[0] = "Poseen un alto contenido en "
            self.description[1] = "proteínas y en fibra, siendo así" 
            self.description[2] = "mismo una fuente excelente de "
            self.description[3] = "minerales."
            
        elif id == eIngredientId._26_GUASCAS:
            self.name = "Guascas"
            self.image = ResourceController.game_Ingredient26Guascas
            self.group = eIngredientGroup.GROUP_2_VERDURAS
            self.nutritionValue = 0
            self.description[0] = "Estas hojas se utilizan como una "
            self.description[1] = "hierba de especia en la sopa de "
            self.description[2] = "ajiaco. También puede utilizarse"
            self.description[3] = "como ingrediente en diferentes "
            self.description[4] = "ensaladas."
            
        elif id == eIngredientId._27_HABICUELA:
            self.name = "Habichuela"
            self.image = ResourceController.game_Ingredient27Habichuela
            self.group = eIngredientGroup.GROUP_2_VERDURAS
            self.nutritionValue = 0
            self.description[0] = "Poseen un alto contenido en "
            self.description[1] = "proteínas y en fibra, siendo así" 
            self.description[2] = "mismo una fuente excelente de "
            self.description[3] = "minerales."
            
        elif id == eIngredientId._28_LECHUGA:
            self.name = "Lechuga"
            self.image = ResourceController.game_Ingredient28Lechuga
            self.group = eIngredientGroup.GROUP_2_VERDURAS
            self.nutritionValue = 0
            self.description[0] = "Tiene un alto contenido de agua," 
            self.description[1] = "es rica en antioxidantes."

        # Grupo 3: Frutas
        elif id == eIngredientId._29_PEPINO_COHOMBRO:
            self.name = "Pepino cohombro"
            self.image = ResourceController.game_Ingredient29PepinoCohombro
            self.group = eIngredientGroup.GROUP_2_VERDURAS
            self.nutritionValue = 0
            self.description[0] = "Los pepinos son un 95 % de agua,"
            self.description[1] = "por lo tanto están indicados para"
            self.description[2] = "realizar dietas ya que son bajos "
            self.description[3] = "en calorías."
        
        elif id == eIngredientId._30_PEPINO_COMUN:
            self.name = "Pepino común"
            self.image = ResourceController.game_Ingredient30PepinoComun
            self.group = eIngredientGroup.GROUP_2_VERDURAS
            self.nutritionValue = 0
            self.description[0] = "Habitualmente se recolecta aún" 
            self.description[1] = "verde y se consume crudo, "
            self.description[2] = "cocinado o elaborado como "
            self.description[3] = "encurtido, entonces se suele" 
            self.description[4] = "denominar pepinillo. Fresco tiene"
            self.description[5] = "menos nutrientes que en vinagre "
            self.description[6] = "debido a los ingredientes."
        
        elif id == eIngredientId._31_PIMENTON:
            self.name = "Pimentón"
            self.image = ResourceController.game_Ingredient31Pimenton
            self.group = eIngredientGroup.GROUP_2_VERDURAS
            self.nutritionValue = 0
            self.description[0] = "Además de dar un sabor delicioso a"
            self.description[1] = "tus comidas, el pimentón es una "
            self.description[2] = "fuente importante de vitaminas y"
            self.description[3] = "minerales."
        
        elif id == eIngredientId._32_TOMATE:
            self.name = "Tomate"
            self.image = ResourceController.game_Ingredient32Tomate
            self.group = eIngredientGroup.GROUP_2_VERDURAS
            self.nutritionValue = 0
            self.description[0] = "Constituyen un alimento excelente" 
            self.description[1] = "para aquellos que quieran una dieta"
            self.description[2] = "saludable. Están compuestos de una "
            self.description[3] = "serie de alimentos ideales para "
            self.description[4] = "desintoxicar el cuerpo y prevenir" 
            self.description[5] = "enfermedades."
        
        elif id == eIngredientId._33_ZANAHORIA:
            self.name = "Zanahoria"
            self.image = ResourceController.game_Ingredient33Zanahoria
            self.group = eIngredientGroup.GROUP_2_VERDURAS
            self.nutritionValue = 0
            self.description[0] = "Es un alimento excelente gracias a" 
            self.description[1] = "su contenido en vitaminas y "
            self.description[2] = "minerales. El agua es el componente"
            self.description[3] = "más abundante, seguido de los"
            self.description[4] = "hidratos de carbono, siendo estos" 
            self.description[5] = "nutrientes los que aportan energía."
                    
        elif id == eIngredientId._34_AGUACATE:
            self.name = "Aguacate"
            self.image = ResourceController.game_Ingredient34Aguacate
            self.group = eIngredientGroup.GROUP_3_FRUTAS
            self.nutritionValue = 0
            self.description[0] = "Posee un alto contenido en aceites"
            self.description[1] = "vegetales, y se  ha descubierto "
            self.description[2] = "que posee propiedades antioxidantes."
        
        elif id == eIngredientId._35_BANANO:
            self.name = "Banano"
            self.image = ResourceController.game_Ingredient35Banano
            self.group = eIngredientGroup.GROUP_3_FRUTAS
            self.nutritionValue = 0
            self.description[0] = "El banano contiene tres azúcares" 
            self.description[1] = "naturales: sacarosa, fructosa y "
            self.description[2] = "glucosa, que combinados con la "
            self.description[3] = "fibra natural de la fruta nos "
            self.description[4] = "proporciona una abundancia "
            self.description[5] = "inmediata de energía."
        
        elif id == eIngredientId._36_CURUBA:
            self.name = "Curuba"
            self.image = ResourceController.game_Ingredient36Curuba
            self.group = eIngredientGroup.GROUP_3_FRUTAS
            self.nutritionValue = 0
            self.description[0] = "Por sus propiedades sedantes es" 
            self.description[1] = "ideal para aliviar problemas del" 
            self.description[2] = "sistema nervioso y es muy "
            self.description[3] = "aconsejada en trastornos "
            self.description[4] = "intestinales y estomacales."
        
        elif id == eIngredientId._37_FRESA:
            self.name = "Fresa"
            self.image = ResourceController.game_Ingredient37Fresa
            self.group = eIngredientGroup.GROUP_3_FRUTAS
            self.nutritionValue = 0
            self.description[0] = "Poseen grandes cantidades de" 
            self.description[1] = "elementos muy necesarios para "
            self.description[2] = "nuestra salud. Sobre todo, la "
            self.description[3] = "vitamina C, una sustancia "
            self.description[4] = "antioxidante que, además, protege"
            self.description[5] = "al cuerpo fortaleciendo el "
            self.description[6] = "sistema inmune."
        
        elif id == eIngredientId._38_GUAYABA:
            self.name = "Guayaba"
            self.image = ResourceController.game_Ingredient38Guayaba
            self.group = eIngredientGroup.GROUP_3_FRUTAS
            self.nutritionValue = 0
            self.description[0] = "Poseen un alto contenido de agua,"
            self.description[1] = "fibra y contiene 7 veces más "
            self.description[2] = "vitamina C que otras frutas como" 
            self.description[3] = "la naranja."
        
        elif id == eIngredientId._39_LIMON:
            self.name = "Limón"
            self.image = ResourceController.game_Ingredient39Limon
            self.group = eIngredientGroup.GROUP_3_FRUTAS
            self.nutritionValue = 0
            self.description[0] = "El limón ocupa un primer lugar" 
            self.description[1] = "entro los frutos curativos, "
            self.description[2] = "preventivos y de aporte vitamínico," 
            self.description[3] = "transformándolo en un gran"
            self.description[4] = "eliminador de toxinas y un "
            self.description[5] = "poderoso bactericida."
        
        elif id == eIngredientId._40_MANDARINA:
            self.name = "Mandarina"
            self.image = ResourceController.game_Ingredient40Mandarina
            self.group = eIngredientGroup.GROUP_3_FRUTAS
            self.nutritionValue = 0
            self.description[0] = "La mandarina tiene un alto "
            self.description[1] = "contenido en agua; posee una"  
            self.description[2] = "importante cantidad de vitamina C,"
            self.description[3] = "con un aporte calórico del 49%."
        
        elif id == eIngredientId._41_MANGO:
            self.name = "Mango"
            self.image = ResourceController.game_Ingredient41Mango
            self.group = eIngredientGroup.GROUP_3_FRUTAS
            self.nutritionValue = 0
            self.description[0] = "El mango es rico en minerales,"
            self.description[1] = "vitaminas, fibras y anti-oxidantes."
            self.description[2] = "Su principal componente es el agua."
            self.description[3] = "Tiene cualidades diuréticas y "
            self.description[4] = "ayuda en el transito intestinal" 
            self.description[5] = "por su aporte de fibras."
        
        # Grupo 4: Carne, visceras, pollo, pescado, huevo, leguminosas secas
        elif id == eIngredientId._42_MANZANA_VERDE:
            self.name = "Manzana verde"
            self.image = ResourceController.game_Ingredient42ManzanaVerde
            self.group = eIngredientGroup.GROUP_3_FRUTAS
            self.nutritionValue = 0
            self.description[0] = "Estimula el hígado y los riñones," 
            self.description[1] = "y es capaz de limpiar toxinas en"
            self.description[2] = "el organismo; gracias a su "
            self.description[3] = "contenido en fibra mejora el"
            self.description[4] = "transito intestinal y ayuda a la"
            self.description[5] = "digestión."
            
        elif id == eIngredientId._43_MANZANA_ROJA:
            self.name = "Manzana roja"
            self.image = ResourceController.game_Ingredient43ManzanaRoja
            self.group = eIngredientGroup.GROUP_3_FRUTAS
            self.nutritionValue = 0
            self.description[0] = "En general todas sus variedades" 
            self.description[1] = "ofrecen importante aportación de"
            self.description[2] = "vitamina C y otras sustancias"
            self.description[3] = "(fitoquímicos) con propiedades "
            self.description[4] = "anticancerígenas y antioxidantes."
            
        elif id == eIngredientId._44_MARACUYA:
            self.name = "Maracuyá"
            self.image = ResourceController.game_Ingredient44Maracuya
            self.group = eIngredientGroup.GROUP_3_FRUTAS
            self.nutritionValue = 0
            self.description[0] = "Es rica en calcio, hierro y fósforo,"
            self.description[1] = "además de vitaminas A y C."
            
        elif id == eIngredientId._45_MELON:
            self.name = "Melón"
            self.image = ResourceController.game_Ingredient45Melon
            self.group = eIngredientGroup.GROUP_3_FRUTAS
            self.nutritionValue = 0
            self.description[0] = "Tiene buen contenido de vitamina A,"
            self.description[1] = "C y antioxidantes."
            
        elif id == eIngredientId._46_MORA:
            self.name = "Mora"
            self.image = ResourceController.game_Ingredient46Mora
            self.group = eIngredientGroup.GROUP_3_FRUTAS
            self.nutritionValue = 0
            self.description[0] = "Es una fruta rica en hierro, calcio"
            self.description[1] = "y fósforo."
            
        elif id == eIngredientId._47_NARANJA:
            self.name = "Naranja"
            self.image = ResourceController.game_Ingredient47Naranja
            self.group = eIngredientGroup.GROUP_3_FRUTAS
            self.nutritionValue = 0
            self.description[0] = "Su gran riqueza en vitaminas y en" 
            self.description[1] = "oligoelementos la convierten en la"
            self.description[2] = "mejor aliada contra el estrés y la "
            self.description[3] = "depresión."
            
        elif id == eIngredientId._48_PAPAYA:
            self.name = "Papaya"
            self.image = ResourceController.game_Ingredient48Papaya
            self.group = eIngredientGroup.GROUP_3_FRUTAS
            self.nutritionValue = 0
            self.description[0] = "Las papayas destacan por su" 
            self.description[1] = "contenido en vitamina C y vitamina"
            self.description[2] = "A, antioxidantes que retrasan el "
            self.description[3] = "envejecimiento y resultan muy "
            self.description[4] = "beneficiosos en la prevención de"
            self.description[5] = "diversas enfermedades."
            
        elif id == eIngredientId._49_PATILLA:
            self.name = "Patilla"
            self.image = ResourceController.game_Ingredient49Patilla
            self.group = eIngredientGroup.GROUP_3_FRUTAS
            self.nutritionValue = 0
            self.description[0] = "Muy apreciada por ser refrescante,"
            self.description[1] = "rica en agua, sales y antioxidantes."
            
        elif id == eIngredientId._50_PERA:
            self.name = "Pera"
            self.image = ResourceController.game_Ingredient50Pera
            self.group = eIngredientGroup.GROUP_3_FRUTAS
            self.nutritionValue = 0
            self.description[0] = "Tiene un alto contenido de agua," 
            self.description[1] = "fibra y vitaminas B, C y E. Ayuda"
            self.description[2] = "a aliviar los dolores del estómago,"
            self.description[3] = "y favorece la digestión."
            
        elif id == eIngredientId._51_PINA:
            self.name = "Piña"
            self.image = ResourceController.game_Ingredient51Pina
            self.group = eIngredientGroup.GROUP_3_FRUTAS
            self.nutritionValue = 0
            self.description[0] = "La piña facilita la digestión," 
            self.description[1] = "mejora la circulación, ayuda a" 
            self.description[2] = "eliminar agua del cuerpo  y tiene"
            self.description[3] = "propiedades antiinflamatorias por"
            self.description[4] = "lo que resulta útil para disminuir"
            self.description[5] = "el dolor."
            
        elif id == eIngredientId._52_ATUN:
            self.name = "Atún"
            self.image = ResourceController.game_Ingredient52Atun
            self.group = eIngredientGroup.GROUP_4_CARNES
            self.nutritionValue = 0
            self.description[0] = "Contiene grandes cantidades de" 
            self.description[1] = "ácidos grasos omega 3, buenos para"
            self.description[2] = "el corazón y para el buen "
            self.description[3] = "desempeño neural y de las "
            self.description[4] = "articulaciones."
        
        # Grupo 5: Lacteos
        elif id == eIngredientId._53_CARNE_DE_CERDO:
            self.name = "Carne de cerdo"
            self.image = ResourceController.game_Ingredient53CarneDeCerdo
            self.group = eIngredientGroup.GROUP_4_CARNES
            self.nutritionValue = 0
            self.description[0] = "Es una carne rica en grasas"
            self.description[1] = "monoinsaturados esenciales "
            self.description[2] = "para el organismo , además "
            self.description[3] = "contiene hierro, zinc y fosforo."
        
        elif id == eIngredientId._54_CARNE_DE_RES:
            self.name = "Carne de res"
            self.image = ResourceController.game_Ingredient54CarneDeRes
            self.group = eIngredientGroup.GROUP_4_CARNES
            self.nutritionValue = 0
            self.description[0] = "La carne de res es particularmente"
            self.description[1] = "efectiva en imcrementar la "
            self.description[2] = "fortaleza y promover el "
            self.description[3] = "crecimiento muscular."
        
        elif id == eIngredientId._55_GARBANZO:
            self.name = "Garbanzo"
            self.image = ResourceController.game_Ingredient55Garbanzo
            self.group = eIngredientGroup.GROUP_4_CARNES
            self.nutritionValue = 0
            self.description[0] = "El garbanzo es rico en proteínas," 
            self.description[1] = "en almidón y en lípidos (más que "
            self.description[2] = "las otras legumbres) sobre todo de"
            self.description[3] = "ácido oleico y linoleico, que son "
            self.description[4] = "insaturados y carentes de "
            self.description[5] = "colesterol. Del mismo modo el" 
            self.description[6] = "garbanzo es un buen aporte de "
        
        elif id == eIngredientId._56_HIGADO:
            self.name = "Hígado"
            self.image = ResourceController.game_Ingredient56Higado
            self.group = eIngredientGroup.GROUP_4_CARNES
            self.nutritionValue = 0
            self.description[0] = "Es uno de los alimentos más" 
            self.description[1] = "completos, riquísimo en proteínas"
            self.description[2] = "de alta calidad, vitaminas y "
            self.description[3] = "minerales. "
        
        elif id == eIngredientId._57_HUEVO:
            self.name = "Huevo"
            self.image = ResourceController.game_Ingredient57Huevo
            self.group = eIngredientGroup.GROUP_4_CARNES
            self.nutritionValue = 0
            self.description[0] = "El huevo es un alimento bajo en" 
            self.description[1] = "calorías, pero tiene un gran valor"
            self.description[2] = "nutritivo por su aporte de "
            self.description[3] = "proteína de alta calidad biológica,"
            self.description[4] = "ya que contiene todos los "
            self.description[5] = "aminoácidos esenciales."
        
        # Grupo 6: Grasas
        elif id == eIngredientId._58_LENTEJA:
            self.name = "Lenteja"
            self.image = ResourceController.game_Ingredient58Lenteja
            self.group = eIngredientGroup.GROUP_4_CARNES
            self.nutritionValue = 0
            self.description[0] = "Las lentejas ayudan ante las" 
            self.description[1] = "enfermedades cardiacas ya que" 
            self.description[2] = "disminuyen los niveles de "
            self.description[3] = "colesterol y grasas debido a su" 
            self.description[4] = "contenido en fibra, fitatos y al" 
            self.description[5] = "ser muy pobres en lípidos o grasa."
        
        elif id == eIngredientId._59_MENUDENCIAS:
            self.name = "Menudencias"
            self.image = ResourceController.game_Ingredient59Menudencias
            self.group = eIngredientGroup.GROUP_4_CARNES
            self.nutritionValue = 0
            self.description[0] = "Los hombres de las cavernas pronto"
            self.description[1] = "aprendieron que las vísceras de "
            self.description[2] = "los animales que cazaban eran más" 
            self.description[3] = "sustanciosas que la carne, por lo"
            self.description[4] = "que el hígado, los riñones, los "
            self.description[5] = "sesos y el bazo eran lo primero "
            self.description[6] = "que consumían."
        
        elif id == eIngredientId._60_PESCADO:
            self.name = "Pescado"
            self.image = ResourceController.game_Ingredient60Pescado
            self.group = eIngredientGroup.GROUP_4_CARNES
            self.nutritionValue = 0
            self.description[0] = "Aporta  proteínas de gran calidad"
            self.description[1] = "nutricional, vitaminas (en "
            self.description[2] = "especial de la vitamina D) y" 
            self.description[3] = "minerales. A ello suman el aporte"
            self.description[4] = "de ácidos grasos Omega-3, un tipo"
            self.description[5] = "de grasa de demostrado efecto "
            self.description[6] = "protector frente a los riesgos "
        
        # Grupo 7: Azucares
        elif id == eIngredientId._61_POLLO:
            self.name = "Pollo"
            self.image = ResourceController.game_Ingredient61Pollo
            self.group = eIngredientGroup.GROUP_4_CARNES
            self.nutritionValue = 0
            self.description[0] = "Es una de las carnes más" 
            self.description[1] = "recomendadas para incorporar" 
            self.description[2] = "proteínas y nutrientes con un bajo"
            self.description[3] = "contenido de grasa (si se consume "
            self.description[4] = "sin piel)."
        
        elif id == eIngredientId._62_SALCHICHA:
            self.name = "Salchicha"
            self.image = ResourceController.game_Ingredient62Salchicha
            self.group = eIngredientGroup.GROUP_4_CARNES
            self.nutritionValue = 0
            self.description[0] = "Si bien son fuente de proteina, su"
            self.description[1] = "consumo debe ser moderado por su "
            self.description[2] = "alto contenido de sal."
        
        elif id == eIngredientId._63_CREMA_DE_LECHE:
            self.name = "Crema de leche"
            self.image = ResourceController.game_Ingredient63CremaDeLeche
            self.group = eIngredientGroup.GROUP_5_LACTEOS
            self.nutritionValue = 0
            self.description[0] = "Tiene un alto contenido de grasa,"
            self.description[1] = "por lo que su consumo debe ser "
            self.description[2] = "moderado."
        
        elif id == eIngredientId._64_KUMIS:
            self.name = "Kumis"
            self.image = ResourceController.game_Ingredient64Kumis
            self.group = eIngredientGroup.GROUP_5_LACTEOS
            self.nutritionValue = 0
            self.description[0] = "El kumis se hace a partir de unas" 
            self.description[1] = "bacterias que benefician la salud "
            self.description[2] = "humana, a través de un proceso de "
            self.description[3] = "fermentación de la leche entera."
        
        # Grupo 8: Otros
        elif id == eIngredientId._65_LECHE:
            self.name = "Leche"
            self.image = ResourceController.game_Ingredient65Leche
            self.group = eIngredientGroup.GROUP_5_LACTEOS
            self.nutritionValue = 0
            self.description[0] = "Uno de los grandes beneficios de" 
            self.description[1] = "la leche es que se utiliza para "
            self.description[2] = "prevenir la osteoporosis, "
            self.description[3] = "accidentes cerebrovasculares y la"
            self.description[4] = "hipertensión arterial. La leche "
            self.description[5] = "también produce una sustancia que" 
            self.description[6] = "reduce la producción hepática de "
            
        elif id == eIngredientId._66_QUESO:
            self.name = "Queso"
            self.image = ResourceController.game_Ingredient66Queso
            self.group = eIngredientGroup.GROUP_5_LACTEOS
            self.nutritionValue = 0
            self.description[0] = "Los datos nutricionales del queso" 
            self.description[1] = "pueden variar en función de su "
            self.description[2] = "contenido en grasa, pero en "
            self.description[3] = "general se puede decir que es una"
            self.description[4] = "rica fuente de calcio,proteínas, "
            self.description[5] = "y fósforo."
            self.description[6] = ""
            
        elif id == eIngredientId._67_YOGURT:
            self.name = "Yogurt"
            self.image = ResourceController.game_Ingredient67Yogur
            self.group = eIngredientGroup.GROUP_5_LACTEOS
            self.nutritionValue = 0
            self.description[0] = "Es rico en calcio, en proteinas y" 
            self.description[1] = "ayuda a mejorar el transito "
            self.description[2] = "intestinal."
            
        elif id == eIngredientId._68_ACEITE:
            self.name = "Aceite"
            self.image = ResourceController.game_Ingredient68Aceite
            self.group = eIngredientGroup.GROUP_6_GRASAS
            self.nutritionValue = 0
            self.description[0] = "La ingestión moderada de aceites" 
            self.description[1] = "es fuente de ácidos grasos"
            self.description[2] = "esenciales para el organismo." 
            self.description[3] = "Prefiere siempre el aceite de" 
            self.description[4] = "origen vegetal pues es mejor para"
            self.description[5] = "tu salud (Oliva y Soya)."
            
        elif id == eIngredientId._69_MANTEQUILLA:
            self.name = "Mantequilla"
            self.image = ResourceController.game_Ingredient69Mantequilla
            self.group = eIngredientGroup.GROUP_6_GRASAS
            self.nutritionValue = 0
            self.description[0] = "Su consumo debe ser moderado por" 
            self.description[1] = "su alto contenido en grasa."
            
        elif id == eIngredientId._70_MARGARINA:
            self.name = "Margarina"
            self.image = ResourceController.game_Ingredient70Margarina
            self.group = eIngredientGroup.GROUP_6_GRASAS
            self.nutritionValue = 0
            self.description[0] = "Su consumo debe ser espóradico. "
            self.description[1] = "Tiene un alto contenido de acidos"
            self.description[2] = "grasos, aumenta el colesteros y "
            self.description[3] = "favorece la aparición de "
            self.description[4] = "enfermedades coronarias."
            
        elif id == eIngredientId._71_AZUCAR:
            self.name = "Azúcar"
            self.image = ResourceController.game_Ingredient71Azucar
            self.group = eIngredientGroup.GROUP_7_AZUCARES
            self.nutritionValue = 0
            self.description[0] = "El azúcar es imprescindible para" 
            self.description[1] = "nuestra ingesta diaria. Brinda "
            self.description[2] = "energía al organismo permitiendo"
            self.description[3] = "el buen funcionamiento de nuestros"
            self.description[4] = "músculos y cerebro."
            
        elif id == eIngredientId._72_CHOCOLATE:
            self.name = "Chocolate"
            self.image = ResourceController.game_Ingredient72Chocolate
            self.group = eIngredientGroup.GROUP_7_AZUCARES
            self.nutritionValue = 0
            self.description[0] = "Es excelente frente a la tristeza,"
            self.description[1] = "la ansiedad y la irritabilidad. Su"
            self.description[2] = "consumo debe ser moderado por su "
            self.description[3] = "alto contenido de azucar."
            
        elif id == eIngredientId._73_HELADO:
            self.name = "Helado"
            self.image = ResourceController.game_Ingredient73Helado
            self.group = eIngredientGroup.GROUP_7_AZUCARES
            self.nutritionValue = 0
            self.description[0] = "Son deliciosos, pero debe moderar"
            self.description[1] = "su consumo por su alto contenido "
            self.description[2] = "de azucar y grasas."
            
        elif id == eIngredientId._74_PANELA:
            self.name = "Panela"
            self.image = ResourceController.game_Ingredient74Panela
            self.group = eIngredientGroup.GROUP_7_AZUCARES
            self.nutritionValue = 0
            self.description[0] = "La panela es lo que podría" 
            self.description[1] = "llamarse el auténtico azúcar" 
            self.description[2] = "integral de caña y se considera el"
            self.description[3] = "más puro porque se elabora a "
            self.description[4] = "partir de la evaporación del jugo"
            self.description[5] = "de caña a alta temperatura."
            
        elif id == eIngredientId._75_AGUA:
            self.name = "Agua"
            self.image = ResourceController.game_Ingredient75Agua
            self.group = eIngredientGroup.GROUP_8_OTROS
            self.nutritionValue = 0
            self.description[0] = "Sin agua, tu cuerpo dejaría de" 
            self.description[1] = "funcionar correctamente. Más de la"
            self.description[2] = "mitad del cuerpo humano es agua," 
            self.description[3] = "y una persona no puede sobrevivir" 
            self.description[4] = "sin agua más de unos pocos días."
            
        elif id == eIngredientId._76_MAYONESA:
            self.name = "Mayonesa"
            self.image = ResourceController.game_Ingredient76Mayonesa
            self.group = eIngredientGroup.GROUP_8_OTROS
            self.nutritionValue = 0
            self.description[0] = "Debes moderar su consumo pues" 
            self.description[1] = "tiene un alto contenido de grasa."
            
        elif id == eIngredientId._77_MOSTAZA:
            self.name = "Mostaza"
            self.image = ResourceController.game_Ingredient77Mostaza
            self.group = eIngredientGroup.GROUP_8_OTROS
            self.nutritionValue = 0
            self.description[0] = "Debes moderar su consumo pues" 
            self.description[1] = "tiene un alto contenido de grasa."
            
        elif id == eIngredientId._78_POLVO_DE_HONEAR:
            self.name = "Polvo de hornear"
            self.image = ResourceController.game_Ingredient78PolvoDeHornear
            self.group = eIngredientGroup.GROUP_8_OTROS
            self.nutritionValue = 0
            self.description[0] = "Provee de una estructura porosa," 
            self.description[1] = "define la forma y la textura de "
            self.description[2] = "la masa de panes, galletas y "
            self.description[3] = "tortas."
            
        elif id == eIngredientId._79_SAL:
            self.name = "Sal"
            self.image = ResourceController.game_Ingredient79Sal
            self.group = eIngredientGroup.GROUP_8_OTROS
            self.nutritionValue = 0
            self.description[0] = "El consumo de sal modifica "
            self.description[1] = "nuestro comportamiento frente a"
            self.description[2] = "los alimentos ya que es un "
            self.description[3] = "generador del apetito y estimula" 
            self.description[4] = "su ingesta. Se emplea "
            self.description[5] = "fundamentalmente en dos maneras:" 
            self.description[6] = "Condimento y como conservante."
            
        elif id == eIngredientId._80_SALSA_DE_TOMATE:
            self.name = "Salsa de tomate"
            self.image = ResourceController.game_Ingredient80SalsaDeTomate
            self.group = eIngredientGroup.GROUP_8_OTROS
            self.nutritionValue = 0
            self.description[0] = "Salsa elaborada a base de tomate" 
            self.description[1] = "con un alto contenido de azucar, "
            self.description[2] = "su consumo debe ser moderado."
            
        elif id == eIngredientId._81_SOPAS_EN_CREMA:
            self.name = "Sopas en crema"
            self.image = ResourceController.game_Ingredient81SopasEnCrema
            self.group = eIngredientGroup.GROUP_8_OTROS
            self.nutritionValue = 0
            self.description[0] = "Fideos de sémola de trigo, sal," 
            self.description[1] = "almidón de trigo, hortalizas y "
            self.description[2] = "verduras deshidratadas y diversos" 
            self.description[3] = "potenciadores del sabor, "
            self.description[4] = "todos ellos deshidratados para"
            self.description[5] = "evitar el crecimiento de "
            self.description[6] = "microorganismos."
            
        elif id == eIngredientId._82_VINAGRETA_DULCE:
            self.name = "Vinagreta dulce"
            self.image = ResourceController.game_Ingredient82VinagretaDulce
            self.group = eIngredientGroup.GROUP_8_OTROS
            self.nutritionValue = 0
            self.description[0] = "La vinagreta la puedes preparar de"
            self.description[1] = "muchas formas, una de ella es "
            self.description[2] = "mezclando vinagre, aceite de oliva,"
            self.description[3] = "miel y sal."


class Trivia:

    def __init__(self, id):
        
        self.id = id
        
        self.optionA = list()
        self.optionA.append("")
        self.optionA.append("")
        self.optionA.append("")
        self.optionA.append("")
        self.optionA.append("")
        self.optionA.append("")
        self.optionA.append("")
                
        self.optionB = list()
        self.optionB.append("")
        self.optionB.append("")
        self.optionB.append("")
        self.optionB.append("")
        self.optionB.append("")
        self.optionB.append("")
        self.optionB.append("")
        
        self.optionC = list()
        self.optionC.append("")
        self.optionC.append("")
        self.optionC.append("")
        self.optionC.append("")
        self.optionC.append("")
        self.optionC.append("")
        self.optionC.append("")
        
        self.recomendation = list()
        self.recomendation.append("")
        self.recomendation.append("")
        self.recomendation.append("")
        self.recomendation.append("")
        
        if id == eTriviaQuestionId.BREAKFAST_01:
            self.answer = eQuestionAnswer.ANSWER_A
            self.optionA[0] = "1. Avena en hojuela"
            self.optionA[1] = "2. Chocolate"
            self.optionA[2] = "3. Tostadas "

            self.optionB[0] = "1. Jugo de maracuyá y"
            self.optionB[1] = "     zanahoria"
            self.optionB[2] = "2. Tamal"
            self.optionB[3] = "3. Pan francés"

            self.optionC[0] = "1. Changua de leche con"
            self.optionC[1] = "     huevo"
            self.optionC[2] = "2. Café"
            self.optionC[3] = "3. Tostadas con"
            self.optionC[4] = "     mantequilla y"
            self.optionC[5] = "     mermelada"

            self.recomendation[0] = "Un desayuno saludable ayuda a tu corazón a estar sano"
            
        elif id == eTriviaQuestionId.BREAKFAST_02:
            self.answer = eQuestionAnswer.ANSWER_C
            
            self.optionA[0] = "1. Caldo de papa con"
            self.optionA[1] = "     costilla"
            self.optionA[2] = "2. Chocolate en agua"
            self.optionA[3] = "3. Galletas saladas"

            self.optionB[0] = "1. Arepa rellena con queso"
            self.optionB[1] = "2. Chocolate "
            self.optionB[2] = "3. Caldo de papa con"
            self.optionB[3] = "     costilla"

            self.optionC[0] = "1. Ensalada de frutas con"
            self.optionC[1] = "     yogurt"
            self.optionC[2] = "2. Bebida caliente de avena"
            self.optionC[3] = "3. Pan"

            self.recomendation[0] = "El yogurt te ayuda a mantener tus huesos fuertes"
        
        elif id == eTriviaQuestionId.BREAKFAST_03:
            self.answer = eQuestionAnswer.ANSWER_A

            self.optionA[0] = "1. Jugo de papaya con"
            self.optionA[1] = "     zanahoria"
            self.optionA[2] = "2. Huevos batidos con"
            self.optionA[3] = "     tomate y cebolla"
            self.optionA[4] = "3. Agua de panela"

            self.optionB[0] = "1. Caldo de papa con"
            self.optionB[1] = "     costilla"
            self.optionB[2] = "2. Huevos con arroz"
            self.optionB[3] = "3. Pan  tostado"

            self.optionC[0] = "1. Jugo de maracuyá con"
            self.optionC[1] = "     zanahoria"
            self.optionC[2] = "2. Pan con queso"
            self.optionC[3] = "3. Salchichas fritas"
            
            self.recomendation[0] = "Consume diariamente frutas de diferentes colores"
        
        elif id == eTriviaQuestionId.BREAKFAST_04:
            self.answer = eQuestionAnswer.ANSWER_C
            
            self.optionA[0] = "1. Ensalada de frutas con"
            self.optionA[1] = "     yogurt"
            self.optionA[2] = "2. Bebida achocolatada"
            self.optionA[3] = "3. Pan con mortadela"

            self.optionB[0] = "1. Changua de leche con"
            self.optionB[1] = "     huevo"
            self.optionB[2] = "2. Chocolate en agua"
            self.optionB[3] = "3. Tostadas con"
            self.optionB[4] = "    mantequilla y"
            self.optionB[5] = "    mermelada"

            self.optionC[0] = "1. Jugo de maracuyá y"
            self.optionC[1] = "zanahoria"
            self.optionC[2] = "2. Café"
            self.optionC[3] = "3. Mantecada"
            
            self.recomendation[0] = "La zanahoria aporta vitaminas necesarias para tu visión"
        
        elif id == eTriviaQuestionId.BREAKFAST_05:
            self.answer = eQuestionAnswer.ANSWER_B
            
            self.optionA[0] = "1. Avena en hojuela"
            self.optionA[1] = "2. Sandwich de jamón y"
            self.optionA[2] = "     queso"
            self.optionA[3] = "3. Jugo de papaya con"
            self.optionA[4] = "     zanahoria"

            self.optionB[0] = "1. Agua de panela"
            self.optionB[1] = "2. Huevos tibios"
            self.optionB[2] = "3. Galletas saladas"

            self.optionC[0] = "1. Arepa rellena con queso"
            self.optionC[1] = "2. Huevos fritos "
            self.optionC[2] = "3. Chocolate en leche"

            self.recomendation[0] = "Mejora tu nutrición; consume frutas"
            
        elif id == eTriviaQuestionId.BREAKFAST_06:
            self.answer = eQuestionAnswer.ANSWER_A
            
            self.optionA[0] = "1. Avena en hojuela"
            self.optionA[1] = "2. Huevo tibio"
            self.optionA[2] = "3. Pan integral"

            self.optionB[0] = "1. Jugo de maracuyá y"
            self.optionB[1] = "     zanahoria"
            self.optionB[2] = "2. Café con leche"
            self.optionB[3] = "3. Salchichas"

            self.optionC[0] = "1. Changua de leche con"
            self.optionC[1] = "     huevo"
            self.optionC[2] = "2. Agua de panela"
            self.optionC[3] = "3. Arepa con mantequilla"

            self.recomendation[0] = "Diviértete comiendo alimentos saludables"
        
        elif id == eTriviaQuestionId.BREAKFAST_07:
            self.answer = eQuestionAnswer.ANSWER_B
            
            self.optionA[0] = "1. Caldo de papa con"
            self.optionA[1] = "     costilla"
            self.optionA[2] = "2. Café con leche"
            self.optionA[3] = "3. Calado integral"

            self.optionB[0] = "1. Arepa rellena con queso"
            self.optionB[1] = "2. Te en agua"
            self.optionB[2] = "3. Huevos revueltos "

            self.optionC[0] = "1. Ensalada de frutas con"
            self.optionC[1] = "     yogurt"
            self.optionC[2] = "2. Jugo de papaya con"
            self.optionC[3] = "     maracuyá"
            self.optionC[4] = "3. Queso"

            self.recomendation[0] = "Las frutas mejoran tus defensas contra enfermedades"
        
        elif id == eTriviaQuestionId.BREAKFAST_08:
            self.answer = eQuestionAnswer.ANSWER_A
            
            self.optionA[0] = "1. Jugo de papaya con"
            self.optionA[1] = "     zanahoria"
            self.optionA[2] = "2. Queso"
            self.optionA[3] = "3. Pan"

            self.optionB[0] = "1. Caldo de papa con"
            self.optionB[1] = "     costilla"
            self.optionB[2] = "2. Tamal"
            self.optionB[3] = "3. Pan con mantequilla"

            self.optionC[0] = "1. Avena en hojuela"
            self.optionC[1] = "2. Caldo de papa con"
            self.optionC[2] = "     costilla"
            self.optionC[3] = "3. Chocolate en leche"

            self.recomendation[0] = "El queso fortalece tus huesos"
        
        elif id == eTriviaQuestionId.BREAKFAST_09:
            self.answer = eQuestionAnswer.ANSWER_C
            
            self.optionA[0] = "1. Changua de leche con"
            self.optionA[1] = "     huevo"
            self.optionA[2] = "2. Agua de panela"
            self.optionA[3] = "3. Buñuelo"

            self.optionB[0] = "1. Sandwich de jamón y"
            self.optionB[1] = "    queso"
            self.optionB[2] = "2. Chocolate en leche"
            self.optionB[3] = "3. Pan integral con"
            self.optionB[4] = "     mermelada"

            self.optionC[0] = "1. Huevos tibios"
            self.optionC[1] = "2. Bebida caliente de"
            self.optionC[2] = "     avena"
            self.optionC[3] = "3. Arepa rellena con queso"

            self.recomendation[0] = "Este desayuno es muy nutritivo para ti."
        
        elif id == eTriviaQuestionId.BREAKFAST_10:
            self.answer = eQuestionAnswer.ANSWER_B

            self.optionA[0] = "1. Huevos fritos"
            self.optionA[1] = "2. Salchichas "
            self.optionA[2] = "3. Café con leche"

            self.optionB[0] = "1. Bebida achocolatada"
            self.optionB[1] = "2. Porción de queso"
            self.optionB[2] = "3. Galletas saladas"

            self.optionC[0] = "1. Jugo de maracuyá y"
            self.optionC[1] = "     zanahoria"
            self.optionC[2] = "2. Agua de panela"
            self.optionC[3] = "3. Pan "

            self.recomendation[0] = "Comiendo frutas mejoras tu digestión"
        
        elif id == eTriviaQuestionId.BREAKFAST_11:
            self.answer = eQuestionAnswer.ANSWER_C

            self.optionA[0] = "1. Changua de leche con"
            self.optionA[1] = "     huevo"
            self.optionA[2] = "2. Chocolate en leche"
            self.optionA[3] = "3. Pan tostado"

            self.optionB[0] = "1. Caldo de papa con"
            self.optionB[1] = "     costilla"
            self.optionB[2] = "2. Sandwich de jamón y"
            self.optionB[3] = "     queso"
            self.optionB[4] = "3. Café con leche"

            self.optionC[0] = "1. Huevos tibios"
            self.optionC[1] = "2. Jugo de guayaba"
            self.optionC[2] = "3. Arepa rellena con queso"

            self.recomendation[0] = "Consume alimentos cocidos, no fritos"
        
        elif id == eTriviaQuestionId.BREAKFAST_12:
            self.answer = eQuestionAnswer.ANSWER_B
            
            self.optionA[0] = "1. Cereal con leche y fruta"
            self.optionA[1] = "2. Jugo de guayaba en"
            self.optionA[2] = "     agua"
            self.optionA[3] = "3. Torta de zanahoria"

            self.optionB[0] = "1. Huevos revueltos"
            self.optionB[1] = "2. Pan tostado con"
            self.optionB[2] = "     mantequilla"
            self.optionB[3] = "3. Chocolate en leche"

            self.optionC[0] = "1. Torta de banano"
            self.optionC[1] = "2. Jugo de papaya con"
            self.optionC[2] = "     zanahoria"
            self.optionC[3] = "3. Agua de panela"

            self.recomendation[0] = "El huevo es una gran fuente de proteína"
        
        elif id == eTriviaQuestionId.BREAKFAST_13:
            self.answer = eQuestionAnswer.ANSWER_B

            self.optionA[0] = "1. Bebida achocolatada"
            self.optionA[1] = "2. Tostadas"
            self.optionA[2] = "3. Jugo de mango"

            self.optionB[0] = "1. Jugo de maracuyá y"
            self.optionB[1] = "     zanahoria"
            self.optionB[2] = "2. Arepa rellena con queso"

            self.optionC[0] = "1. Caldo de papa con"
            self.optionC[1] = "     costilla"
            self.optionC[2] = "2. Tamal"
            self.optionC[3] = "3. Chocolate en leche"

            self.recomendation[0] = "Un buen desayuno te da energía la que tu cuerpo necesita"
            self.recomendation[1] = "para empezar el día"
        
        elif id == eTriviaQuestionId.BREAKFAST_14:
            self.answer = eQuestionAnswer.ANSWER_B
            
            self.optionA[0] = "1. Huevos fritos"
            self.optionA[1] = "2. Pan con mantequilla"
            self.optionA[2] = "3. Café con leche"

            self.optionB[0] = "1. Cereal con leche"
            self.optionB[1] = "2. Jugo de maracuyá y"
            self.optionB[2] = "     zanahoria"
            self.optionB[3] = "3. Arepa con mantequilla"
            self.optionB[4] = "     y sal"

            self.optionC[0] = "1. Torta de banano"
            self.optionC[1] = "2. Chocolate en leche"
            self.optionC[2] = "3. Huevos revueltos "

            self.recomendation[0] = "La leche fortalece tus huesos"
        
        elif id == eTriviaQuestionId.BREAKFAST_15:
            self.answer = eQuestionAnswer.ANSWER_C

            self.optionA[0] = "1. Changua de leche con"
            self.optionA[1] = "     huevo"
            self.optionA[2] = "2. Arepa rellena con queso"
            self.optionA[3] = "3. Chocolate"

            self.optionB[0] = "1. Ensalada de frutas con"
            self.optionB[1] = "     yogurt"
            self.optionB[2] = "2. Agua de panela"
            self.optionB[3] = "3. Pan"

            self.optionC[0] = "1. Huevo tibio"
            self.optionC[1] = "2. Torta de banano"
            self.optionC[2] = "3. Café"
            
            self.recomendation[0] = "Si desayunas bien, te puedes concentrar mejor en la escuela"
        
        elif id == eTriviaQuestionId.LUNCH_01:
            self.answer = eQuestionAnswer.ANSWER_A
            
            self.optionA[0] = "1. Crema de cebolla"
            self.optionA[1] = "     cabezona"
            self.optionA[2] = "2. Torta de zahanoria"
            self.optionA[3] = "3. Arroz vegetariano"
            self.optionA[4] = "4. Albóndigas"

            self.optionB[0] = "1. Sopa de lentejas"
            self.optionB[1] = "2. Torta de banano"
            self.optionB[2] = "3. Tomates rellenos"
            self.optionB[3] = "4. Arroz blanco"

            self.optionC[0] = "1. Torta de ahuyama"
            self.optionC[1] = "2. Ensalada Carlos"
            self.optionC[2] = "3. Guiso de carne y"
            self.optionC[3] = "     verduras"
            self.optionC[4] = "4. Plátano frito"
            
            self.recomendation[0] = "Las verduras ayudan a los intestinos a funcionar bien"
            
        elif id == eTriviaQuestionId.LUNCH_02:
            self.answer = eQuestionAnswer.ANSWER_A
            
            self.optionA[0] = "1. Tortillas de espinaca"
            self.optionA[1] = "2. Ensalada Alba Hit"
            self.optionA[2] = "3. Pollo a la jardinera"
            self.optionA[3] = "4. Arroz verde"

            self.optionB[0] = "1. Tortillas de acelgas"
            self.optionB[1] = "2. Lomo de cerdo en salsa"
            self.optionB[2] = "     de mango"
            self.optionB[3] = "3. Arroz campesino"
            self.optionB[4] = "4. Pasta con vegetales"

            self.optionC[0] = "1. Sopa de garbanzo"
            self.optionC[1] = "2. Ensalada del huerto"
            self.optionC[2] = "3. Ternera a la marinera"
            self.optionC[3] = "4. Arroz a la suegra"
            
            self.recomendation[0] = "Las verduras tienen muchas vitaminas"
            
        elif id == eTriviaQuestionId.LUNCH_03:
            self.answer = eQuestionAnswer.ANSWER_C
            
            self.optionA[0] = "1. Sopa de verduras"
            self.optionA[1] = "2. Ensalada ranchera"
            self.optionA[2] = "3. Macarrones con atún"
            self.optionA[3] = "4. Patacones"

            self.optionB[0] = "1. Sopa de lentejas"
            self.optionB[1] = "2. Pepinos rellenos"
            self.optionB[2] = "3. Arroz con menudencias"
            self.optionB[3] = "4. Ensalada de la casa"

            self.optionC[0] = "1. Crema de cebolla"
            self.optionC[1] = "     cabezona"
            self.optionC[2] = "2. Guiso de habichuela"
            self.optionC[3] = "     con carne"
            self.optionC[4] = "3. Arroz campesino"
            self.optionC[5] = "4. Croquetas de espinaca"
            
            self.recomendation[0] = "Las verduras ayudan a cuidar el corazón"
            
        elif id == eTriviaQuestionId.LUNCH_04:
            self.answer = eQuestionAnswer.ANSWER_B
            
            self.optionA[0] = "1. Torta de zanahoria"
            self.optionA[1] = "2. Tomates rellenos"
            self.optionA[2] = "3. Albóndigas"
            self.optionA[3] = "4. Pasta con vegetales"

            self.optionB[0] = "1. Sopa de verduras"
            self.optionB[1] = "2. Torta de banano"
            self.optionB[2] = "3. Ensalada Carlos"
            self.optionB[3] = "4. Pescado oriental"

            self.optionC[0] = "1. Hamburguesa"
            self.optionC[1] = "2. Papas a la francesa"
            self.optionC[2] = "3. Ensalada criolla"
            
            self.recomendation[0] = "Es bueno incluir alimentos variados en cada comida"

        elif id == eTriviaQuestionId.LUNCH_05:
            self.answer = eQuestionAnswer.ANSWER_A
  
            self.optionA[0] = "1. Torta de ahuyama"
            self.optionA[1] = "2. Ensalada Alba Hit"
            self.optionA[2] = "3. Pescado a la primavera"

            self.optionB[0] = "1. Tortillas de espinaca"
            self.optionB[1] = "2. Ensalada del huerto"
            self.optionB[2] = "3. Macarrones con atún"
            self.optionB[3] = "4. Arroz con coco"

            self.optionC[0] = "1. Crema de cebolla"
            self.optionC[1] = "     cabezona"
            self.optionC[2] = "2. Ensalada fría de papa"
            self.optionC[3] = "     con pollo"
            self.optionC[4] = "3. Lomo de cerdo"
            self.optionC[5] = "     enchilado"
            self.optionC[6] = "4. Arroz a la suegra"
            
            self.recomendation[0] = "El pescado aporta elementos necesarios para que crezcas"
            
        elif id == eTriviaQuestionId.LUNCH_06:
            self.answer = eQuestionAnswer.ANSWER_B
            
            self.optionA[0] = "1. Sopa de lentejas"
            self.optionA[1] = "2. Ensalada ranchera"
            self.optionA[2] = "3. Pepinos rellenos"
            self.optionA[3] = "4. Arroz con menudencias"
            self.optionA[4] = "5. Croquetas de espinada"

            self.optionB[0] = "1. Sopa de garbanzo"
            self.optionB[1] = "2. Tortillas de acelgas"
            self.optionB[2] = "3. Guiso de carne y verdura"
            self.optionB[3] = "4. Arroz vegetariano"

            self.optionC[0] = "1. Sopa de verduras"
            self.optionC[1] = "2. Ensalada de la casa"
            self.optionC[2] = "3. Lomo de cerdo en salsa"
            self.optionC[3] = "     de mango"
            self.optionC[4] = "4. Arroz con fideos"
            
            self.recomendation[0] = "Tu cuerpo se desarrolla y se mantiene sano con una"
            self.recomendation[1] = "alimentación saludable"
            
        elif id == eTriviaQuestionId.LUNCH_07:
            self.answer = eQuestionAnswer.ANSWER_B
            
            self.optionA[0] = "1. Sopa de garbanzo"
            self.optionA[1] = "2. Ternera a la marinera"
            self.optionA[2] = "3. Ensalada criolla"
            self.optionA[3] = "4. Arroz campesino"
            self.optionA[4] = "5. Patacón"

            self.optionB[0] = "1. Arroz vegetariano"
            self.optionB[1] = "2. Pescado oriental"
            self.optionB[2] = "3. Tomates rellenos"

            self.optionC[0] = "1. Crema de cebolla"
            self.optionC[1] = "    cabezona"
            self.optionC[2] = "2. Pasta con vegetales"
            self.optionC[3] = "3. Torta de ahuyama"
            self.optionC[4] = "4. Macarrones con atún"
            
            self.recomendation[0] = "Consume todos los días verduras de diferentes colores;"
            self.recomendation[1] = "tienen vitaminas"
            
        elif id == eTriviaQuestionId.LUNCH_08:
            self.answer = eQuestionAnswer.ANSWER_C
            
            self.optionA[0] = "1. Tortillas de espinaca"
            self.optionA[1] = "2. Pescado a la primavera"
            self.optionA[2] = "3. Ensalada fría de papa"
            self.optionA[3] = "     con pollo"
            self.optionA[4] = "4. Arroz a la suegra"

            self.optionB[0] = "1. Sopa de verduras"
            self.optionB[1] = "2. Pollo a la jardinera"
            self.optionB[2] = "3. Torta de banano"
            self.optionB[3] = "4. Ensalada Carlos"
            self.optionB[4] = "5. Croquetas de espinaca"

            self.optionC[0] = "1. Tortillas de acelgas"
            self.optionC[1] = "2. Ensalada Alba Hit"
            self.optionC[2] = "3. Albóndigas"
            self.optionC[3] = "4. Arroz con menudencias"

            self.recomendation[0] = "Las verduras le ayudan a tu cuerpo a eliminar el exceso"
            self.recomendation[1] = "de líquidos"
            
        elif id == eTriviaQuestionId.LUNCH_09:
            self.answer = eQuestionAnswer.ANSWER_A

            self.optionA[0] = "1. Crema de cebolla"
            self.optionA[1] = "     cabezona"
            self.optionA[2] = "2. Ensalada del huerto"
            self.optionA[3] = "3. Guiso de carne y"
            self.optionA[4] = "     verduras"
            self.optionA[5] = "4. Arroz verde"

            self.optionB[0] = "1. Torta de zanahoria"
            self.optionB[1] = "2. Ensalada de la casa"
            self.optionB[2] = "3. Lomo de cerdo"
            self.optionB[3] = "     enchilado"
            self.optionB[4] = "4. Arroz campesino"

            self.optionC[0] = "1. Sopa de lentejas"
            self.optionC[1] = "2. Ensalada criolla"
            self.optionC[2] = "3. Pescado a la primavera"
            self.optionC[3] = "4. Pasta con vegetales"
            self.optionC[4] = "5. Yuca frita"
            
            self.recomendation[0] = "Un  buen hábito es comer siempre a la misma hora"
            
        elif id == eTriviaQuestionId.LUNCH_10:
            self.answer = eQuestionAnswer.ANSWER_C
            
            self.optionA[0] = "1. Hamburguesa"
            self.optionA[1] = "2. Patacón"
            self.optionA[2] = "3. Ensalada fría de papa"
            self.optionA[3] = "     con pollo"

            self.optionB[0] = "1. Torta de zanahoria"
            self.optionB[1] = "2. Tomates rellenos"
            self.optionB[2] = "3. Pollo a la jardinera"
            self.optionB[3] = "4. Arroz verde"

            self.optionC[0] = "1. Sopa de verduras"
            self.optionC[1] = "2. Ensalada Carlos"
            self.optionC[2] = "3. Macarrones con atún"
            
            self.recomendation[0] = "Agua a diario debes tomar para siempre sano estar"
            
        elif id == eTriviaQuestionId.LUNCH_11:
            self.answer = eQuestionAnswer.ANSWER_B
            
            self.optionA[0] = "1. Torta de banano"
            self.optionA[1] = "2. Ensalada Alba Hit"
            self.optionA[2] = "3. Lomo de cerdo en salsa"
            self.optionA[3] = "     de mango"
            self.optionA[4] = "4. Arroz campesino"

            self.optionB[0] = "1. Sopa de garbanzo"
            self.optionB[1] = "2. Torta de ahuyama"
            self.optionB[2] = "3. Ternera a la marinera"
            self.optionB[3] = "4. Ensalada criolla"

            self.optionC[0] = "1. Pasta con vegetales"
            self.optionC[1] = "2. Ensalada fría de papa"
            self.optionC[2] = "     con pollo"
            self.optionC[3] = "3. Tortillas de espinaca"
            self.optionC[4] = "4. Pescado a la primavera"
            
            self.recomendation[0] = "Qué divertido es comer en familia!!!"
            
        elif id == eTriviaQuestionId.LUNCH_12:
            self.answer = eQuestionAnswer.ANSWER_A
            
            self.optionA[0] = "1. Tortillas de acelgas"
            self.optionA[1] = "2. Lomo de cerdo"
            self.optionA[2] = "     enchilado"
            self.optionA[3] = "3. Pasta con vegetales"

            self.optionB[0] = "1. Pescado oriental"
            self.optionB[1] = "2. Ensalada del huerto"
            self.optionB[2] = "3. Arroz verde"
            self.optionB[3] = "4. Torta de zanahoria"

            self.optionC[0] = "1. Pasta con vegetales"
            self.optionC[1] = "2. Pepinos rellenos"
            self.optionC[2] = "3. Arroz blanco"
            self.optionC[3] = "4. Torta de banano"
            
            self.recomendation[0] = "La carne de cerdo además de ser sabrosa, es nutritiva"

        elif id == eTriviaQuestionId.LUNCH_13:
            self.answer = eQuestionAnswer.ANSWER_B
            
            self.optionA[0] = "1. Albóndigas"
            self.optionA[1] = "2. Tortillas de espinaca"
            self.optionA[2] = "3. Arroz a la suegra"
            self.optionA[3] = "4. Patacón con guiso"

            self.optionB[0] = "1. Crema de cebolla"
            self.optionB[1] = "     cabezona"
            self.optionB[2] = "2. Guiso de habichuela con"
            self.optionB[3] = "     carne"
            self.optionB[4] = "3. Torta de zanahoria"

            self.optionC[0] = "1. Lomo de cerdo en salsa"
            self.optionC[1] = "     de mango"
            self.optionC[2] = "2. Croquetas de espinaca"
            self.optionC[3] = "3. Arroz vegetariano"
            self.optionC[4] = "4. Yuca frita"
            
            self.recomendation[0] = "Come verduras; ayudan a prevenir enfermedades"
            
        elif id == eTriviaQuestionId.LUNCH_14:
            self.answer = eQuestionAnswer.ANSWER_C

            self.optionA[0] = "1. Sopa de lentejas"
            self.optionA[1] = "2. Ensalada ranchera"
            self.optionA[2] = "3. Pescado a la primavera"
            self.optionA[3] = "4. Papas a la francesa"

            self.optionB[0] = "1. Torta de ahuyama"
            self.optionB[1] = "2. Ensalada de la casa"
            self.optionB[2] = "3. Guiso de habichuela con"
            self.optionB[3] = "     carne"
            self.optionB[4] = "4. Arroz verde"

            self.optionC[0] = "1. Sopa de verduras"
            self.optionC[1] = "2. Pollo a la jardinera"
            self.optionC[2] = "3. Arroz campesino"
            self.optionC[3] = "4. Ensalada Carlos"
            
            self.recomendation[0] = "Un menú balanceado incluye alimentos de por lo menos tres"
            self.recomendation[1] = "grupos diferentes"
            
        elif id == eTriviaQuestionId.LUNCH_15:
            self.answer = eQuestionAnswer.ANSWER_A
            
            self.optionA[0] = "1. Sopa de garbanzo"
            self.optionA[1] = "2. Tortillas de acelgas"
            self.optionA[2] = "3. Albóndigas"
            self.optionA[3] = "4. Arroz con menudencias"

            self.optionB[0] = "1. Sopa de lentejas"
            self.optionB[1] = "2. Torta de ahuyama"
            self.optionB[2] = "3. Macarrones con atún"
            self.optionB[3] = "4. Ensalada criolla"

            self.optionC[0] = "1. Torta de banano"
            self.optionC[1] = "2. Ensalada del huerto"
            self.optionC[2] = "3. Ternera a la marinera"
            self.optionC[3] = "4. Arroz vegetariano"
            
            self.recomendation[0] = "Los garbanzos pertenecen al grupo de las leguminosas"

        elif id == eTriviaQuestionId.LUNCH_16:
            self.answer = eQuestionAnswer.ANSWER_B
            
            self.optionA[0] = "1. Torta de zanahoria"
            self.optionA[1] = "2. Ensalada Alba Hit"
            self.optionA[2] = "3. Pescado oriental"
            self.optionA[3] = "4. Plátano maduro frito"

            self.optionB[0] = "1. Sopa de verduras"
            self.optionB[1] = "2. Tortilla de acelgas"
            self.optionB[2] = "3. Lomo de cerdo"
            self.optionB[3] = "     enchilado"
            self.optionB[4] = "4. Arroz a la suegra"

            self.optionC[0] = "1. Torta de banano"
            self.optionC[1] = "2. Ensalada ranchera"
            self.optionC[2] = "3. Guiso de carne y verdura"
            self.optionC[3] = "4. Arroz campesino"
            
            self.recomendation[0] = "Aliméntate con menús balanceados y nutritivos como este"
            
        elif id == eTriviaQuestionId.LUNCH_17:
            self.answer = eQuestionAnswer.ANSWER_C
            
            self.optionA[0] = "1. Sopa de garbanzo"
            self.optionA[1] = "2. Torta de ahuyama"
            self.optionA[2] = "3. Albóndigas"
            self.optionA[3] = "4. Arroz blanco"

            self.optionB[0] = "1. Tortillas de espinaca"
            self.optionB[1] = "2. Lomo de cerdo"
            self.optionB[2] = "     enchilado"
            self.optionB[3] = "3. Arroz campesino"
            self.optionB[4] = "4. Papa salada"

            self.optionC[0] = "1. Tortillas de acelgas"
            self.optionC[1] = "2. Pescado a la primavera"
            self.optionC[2] = "3. Arroz a la suegra"
            self.optionC[3] = "4. Ensalada Carlos"
            
            self.recomendation[0] = "Para mejorar tu digestión come despacio y mastica bien"
            
        elif id == eTriviaQuestionId.LUNCH_18:
            self.answer = eQuestionAnswer.ANSWER_A
            
            self.optionA[0] = "1. Sopa de lentejas"
            self.optionA[1] = "2. Ensalada de la casa"
            self.optionA[2] = "3. Arroz blanco"
            self.optionA[3] = "4. Ternera a la marinera"

            self.optionB[0] = "1. Sopa de garbanzo"
            self.optionB[1] = "2. Torta de zanahoria"
            self.optionB[2] = "3. Ensalada Carlos"
            self.optionB[3] = "4. Guiso de habichuela con"
            self.optionB[4] = "     carne"

            self.optionC[0] = "1. Crema de cebolla"
            self.optionC[1] = "     cabezona"
            self.optionC[2] = "2. Torta de banano"
            self.optionC[3] = "3. Yuca con guiso"
            self.optionC[4] = "4. Pescado oriental"
            
            self.recomendation[0] = "Un mundo saludable empieza con un plato saludable"
            
        elif id == eTriviaQuestionId.LUNCH_19:
            self.answer = eQuestionAnswer.ANSWER_B

            self.optionA[0] = "1. Pasta con vegetales"
            self.optionA[1] = "2. Ensalada ranchera"
            self.optionA[2] = "3. Pepinos rellenos"
            self.optionA[3] = "4. Arroz a la suegra"

            self.optionB[0] = "1. Sopa de lentejas"
            self.optionB[1] = "2. Torta de ahuyama"
            self.optionB[2] = "3. Tomates rellenos"
            self.optionB[3] = "4. Guiso de carne y"
            self.optionB[4] = "     verduras"

            self.optionC[0] = "1. Tortillas de espinaca"
            self.optionC[1] = "2. Pollo a la jardinera"
            self.optionC[2] = "3. Arroz verde"
            self.optionC[3] = "4. Patacón"
            
            self.recomendation[0] = "Consume poca sal"
            
        elif id == eTriviaQuestionId.LUNCH_20:
            self.answer = eQuestionAnswer.ANSWER_C
            
            self.optionA[0] = "1. Pasta con vegetales"
            self.optionA[1] = "2. Torta de zanahoria"
            self.optionA[2] = "3. Pescado a la primavera"
            self.optionA[3] = "4. Ensalada criolla"

            self.optionB[0] = "1. Sopa de verduras"
            self.optionB[1] = "2. Torta de banano"
            self.optionB[2] = "3. Ensalada de la casa"
            self.optionB[3] = "4. Yuca frita"

            self.optionC[0] = "1. Sopa de garbanzo"
            self.optionC[1] = "2. Ensalada Carlos"
            self.optionC[2] = "3. Pepinos rellenos"
            self.optionC[3] = "4. Arroz campesino"

            self.recomendation[0] = "El garbanzo te da energía y es nutritivo"
        
        elif id == eTriviaQuestionId.DINNER_01:
            self.answer = eQuestionAnswer.ANSWER_A
            
            self.optionA[0] = "1. Tortillas de acelgas"
            self.optionA[1] = "2. Ensalada del huerto"
            self.optionA[2] = "3. Macarrones con atún"

            self.optionB[0] = "1. Croquetas de espinaca"
            self.optionB[1] = "2. Ensalada fría de papa"
            self.optionB[2] = "     con pollo"
            self.optionB[3] = "3. Arroz campesino"

            self.optionC[0] = "1. Torta de ahuyama"
            self.optionC[1] = "2. Ensalada alba Hit"
            self.optionC[2] = "3. Arroz con fideos"
            
            self.recomendation[0] = "Llena la mitad de tu plato con frutas y vegetales"
        
        elif id == eTriviaQuestionId.DINNER_02:
            self.answer = eQuestionAnswer.ANSWER_B
            
            self.optionA[0] = "1. Sopa de garbanzo"
            self.optionA[1] = "2. Torta de ahuyama"
            self.optionA[2] = "3. Yuca frita"

            self.optionB[0] = "1. Sopa de lentejas"
            self.optionB[1] = "2. Torta de zanahoria"
            self.optionB[2] = "3. Guiso de habichuela"
            self.optionB[3] = "     con carne"

            self.optionC[0] = "1. Ensalada criolla"
            self.optionC[1] = "2. Ternera a la marinera"
            self.optionC[2] = "3. Pasta con vegetales"
            
            self.recomendation[0] = "Consume granos enteros (integrales) y así mantendrás"
            self.recomendation[1] = "feliz a tu corazón"
            
        elif id == eTriviaQuestionId.DINNER_03:
            self.answer = eQuestionAnswer.ANSWER_A
            
            self.optionA[0] = "1. Crema de cebolla"
            self.optionA[1] = "     cabezona"
            self.optionA[2] = "2. Torta de banano"
            self.optionA[3] = "3. Arroz con fideos"

            self.optionB[0] = "1. Torta de ahuyama"
            self.optionB[1] = "2. Croquetas de espinaca"
            self.optionB[2] = "3. Macarrones con atún "

            self.optionC[0] = "1. Sopa de garbanzo"
            self.optionC[1] = "2. Torta de zanahoria"
            self.optionC[2] = "3. Guiso de carne y"
            self.optionC[3] = "     verduras"
            
            self.recomendation[0] = "Bebe agua potable"
        
        elif id == eTriviaQuestionId.DINNER_04:
            self.answer = eQuestionAnswer.ANSWER_A
            
            self.optionA[0] = "1. Ensalada ranchera"
            self.optionA[1] = "2. Pollo a la jardinera"
            self.optionA[2] = "3. Arroz verde"

            self.optionB[0] = "1. Pasta con vegetales"
            self.optionB[1] = "2. Torta de banano"
            self.optionB[2] = "3. Lomo de cerdo"
            self.optionB[3] = "     enchilado"

            self.optionC[0] = "1. Sopa de verduras"
            self.optionC[1] = "2. Papa sudada con guiso"
            self.optionC[2] = "3. Macarrones con atún"
            
            self.recomendation[0] = "Aprender a comer es aprender a crecer"
        
        elif id == eTriviaQuestionId.DINNER_05:
            self.answer = eQuestionAnswer.ANSWER_B
            
            self.optionA[0] = "1. Lomo de cerdo en salsa"
            self.optionA[1] = "     de mango"
            self.optionA[2] = "2. Arroz campesino"
            self.optionA[3] = "3. Ensalada fría de papa"
            self.optionA[4] = "     con pollo"

            self.optionB[0] = "1. Tortillas de acelgas"
            self.optionB[1] = "2. Guiso de habichuela con"
            self.optionB[2] = "     carne"
            self.optionB[3] = "3. Arroz blanco"

            self.optionC[0] = "1. Torta de banano"
            self.optionC[1] = "2. Ensalada de la casa"
            self.optionC[2] = "3. Papa sudada"

            self.recomendation[0] = "El arroz, al igual que otros cereales, ayuda a la"
            self.recomendation[1] = "formación de tus músculos"
        
        elif id == eTriviaQuestionId.DINNER_06:
            self.answer = eQuestionAnswer.ANSWER_C
            
            self.optionA[0] = "1. Sopa de verduras"
            self.optionA[1] = "2. Pasta con vegetales"
            self.optionA[2] = "3. Arepa"

            self.optionB[0] = "1. Sopa de garbanzo"
            self.optionB[1] = "2. Guiso de habichuela con"
            self.optionB[2] = "     carne"
            self.optionB[3] = "3. Papas a la francesa"

            self.optionC[0] = "1. Torta de ahuyama"
            self.optionC[1] = "2. Albóndigas"
            self.optionC[2] = "3. Arroz verde"
            
            self.recomendation[0] = "Come pocas grasas y azúcares"
            
        elif id == eTriviaQuestionId.DINNER_07:
            self.answer = eQuestionAnswer.ANSWER_A
            
            self.optionA[0] = "1. Torta de banano"
            self.optionA[1] = "2. Ensalada del huerto"
            self.optionA[2] = "3. Pescado oriental"

            self.optionB[0] = "1. Sopa de verduras"
            self.optionB[1] = "2. Torta de zanahoria"
            self.optionB[2] = "3. Guiso de carne y"
            self.optionB[3] = "     verduras"

            self.optionC[0] = "1. Ensalada fría de papa"
            self.optionC[1] = "     con pollo"
            self.optionC[2] = "2. Ternera a la marinera"
            self.optionC[3] = "3. Pan"
            
            self.recomendation[0] = "Alimentarte bien para crecer sano y fuerte"
        
        elif id == eTriviaQuestionId.DINNER_08:
            self.answer = eQuestionAnswer.ANSWER_B
            
            self.optionA[0] = "1. Sopa de pasta"
            self.optionA[1] = "2. Ensalada de la casa"
            self.optionA[2] = "3. Arroz vegetariano"

            self.optionB[0] = "1. Crema de cebolla"
            self.optionB[1] = "     cabezona"
            self.optionB[2] = "2. Torta de ahuyama"
            self.optionB[3] = "3. Pepinos rellenos"

            self.optionC[0] = "1. Hamburguesa"
            self.optionC[1] = "2. Tortillas de espinaca"
            self.optionC[2] = "3. Papas a la francesa"
            
            self.recomendation[0] = "Buena nutrición es buena salud"
        
        elif id == eTriviaQuestionId.DINNER_09:
            self.answer = eQuestionAnswer.ANSWER_C
            
            self.optionA[0] = "1. Arroz a la suegra"
            self.optionA[1] = "2. Tortillas de acelgas"
            self.optionA[2] = "3. Macarrones con atún"

            self.optionB[0] = "1. Sopa de verduras"
            self.optionB[1] = "2. Ensalada fría de papa"
            self.optionB[2] = "     con pollo"
            self.optionB[3] = "3. Arroz con menudencias"

            self.optionC[0] = "1. Tomates rellenos"
            self.optionC[1] = "2. Ternera a la marinera"
            self.optionC[2] = "3. Papa salada"
            
            self.recomendation[0] = "Menos sal, más vida"
        
        elif id == eTriviaQuestionId.DINNER_10:
            self.answer = eQuestionAnswer.ANSWER_A
            
            self.optionA[0] = "1. Crema de cebolla"
            self.optionA[1] = "     cabezona"
            self.optionA[2] = "2. Tortillas de espinaca"
            self.optionA[3] = "3. Pescado a la primavera"

            self.optionB[0] = "1. Ensalada Carlos"
            self.optionB[1] = "2. Lomo de cerdo"
            self.optionB[2] = "     enchilado"
            self.optionB[3] = "3. Pepinos rellenos"

            self.optionC[0] = "1. Arroz con menudencias"
            self.optionC[1] = "2. Torta de zanahoria"
            self.optionC[2] = "3. Ensalada criolla"
            
            self.recomendation[0] = "Lograrás alimentación balanceada con: verduras, frutas,"
            self.recomendation[1] = "leguminosas, cereales, carnes y lácteos"
        
        elif id == eTriviaQuestionId.DINNER_11:
            self.answer = eQuestionAnswer.ANSWER_B
            
            self.optionA[0] = "1. Sopa de lentejas"
            self.optionA[1] = "2. Ensalada Alba hit"
            self.optionA[2] = "3. Pasta con vegetales"

            self.optionB[0] = "1. Arroz campesino"
            self.optionB[1] = "2. Albóndigas"
            self.optionB[2] = "3. Ensalada del huerto"

            self.optionC[0] = "1. Torta de ahuyama"
            self.optionC[1] = "2. Macarrones con atún"
            self.optionC[2] = "3. Yuca frita"
            
            self.recomendation[0] = "Come verduras crudas y cocinadas"
        
        elif id == eTriviaQuestionId.DINNER_12:
            self.answer = eQuestionAnswer.ANSWER_C
            
            self.optionA[0] = "1. Sopa de garbanzo"
            self.optionA[1] = "2. Pepinos rellenos"
            self.optionA[2] = "3. Torta de banano"

            self.optionB[0] = "1. Sopa de verduras"
            self.optionB[1] = "2. Tortilla de acelgas"
            self.optionB[2] = "3. Guiso de habichuela con"
            self.optionB[3] = "     carne"

            self.optionC[0] = "1. Ensalada de la casa"
            self.optionC[1] = "2. Pollo a la jardinera"
            self.optionC[2] = "3. Arroz verde"
            
            self.recomendation[0] = "Comer frutas aumenta tus defensas contra enfermedades"
            
        elif id == eTriviaQuestionId.DINNER_13:
            self.answer = eQuestionAnswer.ANSWER_A
            
            self.optionA[0] = "1. Pasta con vegetales"
            self.optionA[1] = "2. Albóndigas"
            self.optionA[2] = "3. Zafresco"

            self.optionB[0] = "1. Ensalada del huerto"
            self.optionB[1] = "2. Lomo de cerdo"
            self.optionB[2] = "     enchilado"
            self.optionB[3] = "3. Plátano frito"

            self.optionC[0] = "1. Ensalada criolla"
            self.optionC[1] = "2. Albóndigas"
            self.optionC[2] = "3. Arroz a la suegra"
            self.optionC[3] = "4. Papa sudada con guiso"
            
            self.recomendation[0] = "Las frutas te dan energía"
        
        elif id == eTriviaQuestionId.DINNER_14:
            self.answer = eQuestionAnswer.ANSWER_C
            
            self.optionA[0] = "1. Torta de zanahoria"
            self.optionA[1] = "2. Pasta con leche"
            self.optionA[2] = "3. Ensalada fría de papa"
            self.optionA[3] = "     con pollo"

            self.optionB[0] = "1. Hamburgesa"
            self.optionB[1] = "2. Tomates rellenos"
            self.optionB[2] = "3. Papas a la francesa"

            self.optionC[0] = "1. Sopa de verduras"
            self.optionC[1] = "2. Torta de banano"
            self.optionC[2] = "3. Pollo a la jardinera"
            
            self.recomendation[0] = "Comer es divertido; disfruta la comida"
        
        elif id == eTriviaQuestionId.DINNER_15:
            self.answer = eQuestionAnswer.ANSWER_A
            
            self.optionA[0] = "1. Croquetas de espinaca"
            self.optionA[1] = "2. Guiso de habichuela con"
            self.optionA[2] = "     carne"
            self.optionA[3] = "3. Arroz blanco"

            self.optionB[0] = "1. Crema de cebolla"
            self.optionB[1] = "     cabezona"
            self.optionB[2] = "2. Ensalada ranchera"
            self.optionB[3] = "3. Tortillas de acelgas"

            self.optionC[0] = "1. Arroz a la suegra"
            self.optionC[1] = "2. Tomates rellenos"
            self.optionC[2] = "3. Papa salada"
            
            self.recomendation[0] = "Come fruta y verdura en cada comida"
        
        elif id == eTriviaQuestionId.DINNER_16:
            self.answer = eQuestionAnswer.ANSWER_B
            
            self.optionA[0] = "1. Torta de ahuyama"
            self.optionA[1] = "2. Ensalada Alba Hit"
            self.optionA[2] = "3. Pasta con vegetales"

            self.optionB[0] = "1. Sopa de garbanzo"
            self.optionB[1] = "2. Guiso de carne y"
            self.optionB[2] = "     verduras"
            self.optionB[3] = "3. Torta de ahuyama"

            self.optionC[0] = "1. Sopa de lentejas"
            self.optionC[1] = "2. Torta de zanahoria"
            self.optionC[2] = "3. Ensalada fría de papa"
            self.optionC[3] = "     con pollo"
            
            self.recomendation[0] = "Para mantener una buena digestión, cuida tus dientes. "
        
        elif id == eTriviaQuestionId.DINNER_17:
            self.answer = eQuestionAnswer.ANSWER_C
            
            self.optionA[0] = "1. Ensalada Carlos"
            self.optionA[1] = "2. Plátano frito"
            self.optionA[2] = "3. Arroz verde"

            self.optionB[0] = "1. Hamburgesa"
            self.optionB[1] = "2. Yuca frita"
            self.optionB[2] = "3. Ensalada de la casa"

            self.optionC[0] = "1. Albóndigas"
            self.optionC[1] = "2. Plátano cocinado"
            self.optionC[2] = "3. Tomates rellenos"
            
            self.recomendation[0] = "Si tu salud quieres mantener debes hacer ejercicio y comer"
        
        elif id == eTriviaQuestionId.DINNER_18:
            self.answer = eQuestionAnswer.ANSWER_A
            
            self.optionA[0] = "1. Tortillas de espinaca"
            self.optionA[1] = "2. Pescado a la primavera"
            self.optionA[2] = "3. Arroz a la suegra"

            self.optionB[0] = "1. Patacón con guiso"
            self.optionB[1] = "2. Macarrones con atún"
            self.optionB[2] = "3. Ensalada de la casa"

            self.optionC[0] = "1. Crema de cebolla"
            self.optionC[1] = "     cabezona"
            self.optionC[2] = "2. Tortillas de acelgas"
            self.optionC[3] = "3. Ternera a la marinera"
            
            self.recomendation[0] = "Para calmar tu sed, bebe agua potable"
        
        elif id == eTriviaQuestionId.DINNER_19:
            self.answer = eQuestionAnswer.ANSWER_B
            
            self.optionA[0] = "1. Arroz con fideos"
            self.optionA[1] = "2. Torta de banano"
            self.optionA[2] = "3. Ensalada fría de papa"
            self.optionA[3] = "     con pollo"

            self.optionB[0] = "1. Pasta con vegetales"
            self.optionB[1] = "2. Pescado oriental"

            self.optionC[0] = "1. Sopa de garbanzo"
            self.optionC[1] = "2. Torta de zanahoria"
            self.optionC[2] = "3. Arroz con menudencias"
            
            self.recomendation[0] = "Buena nutrición es buena salud"
        
        elif id == eTriviaQuestionId.DINNER_20:
            self.answer = eQuestionAnswer.ANSWER_C

            self.optionA[0] = "1. Sopa de verduras"
            self.optionA[1] = "2. Torta de ahuyama"
            self.optionA[2] = "3. Arroz campesino"

            self.optionB[0] = "1. Torta de banano"
            self.optionB[1] = "2. Arroz a la suegra"
            self.optionB[2] = "3. Yuca sudada con guiso"

            self.optionC[0] = "1. Torta de ahuyama"
            self.optionC[1] = "2. Guiso de habichuela con"
            self.optionC[2] = "     carne"
            
            self.recomendation[0] = "Buena nutrición es buena salud"

        elif id == eTriviaQuestionId.REFRESHMENT_01:
            self.answer = eQuestionAnswer.ANSWER_A
            
            self.optionA[0] = "1. Zafresco"
            self.optionA[1] = "2. Sandwich de jamón y"
            self.optionA[2] = "     queso"

            self.optionB[0] = "1. Refresco de manzana"
            self.optionB[1] = "2. Empanada de papa"
            self.optionB[2] = "     criolla"

            self.optionC[0] = "1. Guarapo de piña"
            self.optionC[1] = "2. Ensalada de colores"
            
            self.recomendation[0] = "En vez de dulces, come frutas"
        
        elif id == eTriviaQuestionId.REFRESHMENT_02:
            self.answer = eQuestionAnswer.ANSWER_B
            
            self.optionA[0] = "1. Zafresco"
            self.optionA[1] = "2. Perro caliente"

            self.optionB[0] = "1. Te de mango"
            self.optionB[1] = "2. Arepa rellena con queso"

            self.optionC[0] = "1. Ensalada de frutas con"
            self.optionC[1] = "     yogurt"
            self.optionC[2] = "2. Pan con mantequilla"
            
            self.recomendation[0] = "Buen alimento, mejor pensamiento"
            
        elif id == eTriviaQuestionId.REFRESHMENT_03:
            self.answer = eQuestionAnswer.ANSWER_C
            
            self.optionA[0] = "1. Brocheta de frutas"
            self.optionA[1] = "2. Mantecada"

            self.optionB[0] = "1. Refresco de manzana"
            self.optionB[1] = "2. Buñuelo"

            self.optionC[0] = "1. Jugo de maracuyá y"
            self.optionC[1] = "     zanahoria"
            self.optionC[2] = "2. Galletas integrales"
            
            self.recomendation[0] = "Bebe agua en vez de bebidas azucaradas"
            
        elif id == eTriviaQuestionId.REFRESHMENT_04:
            self.answer = eQuestionAnswer.ANSWER_A
            
            self.optionA[0] = "1. Jugo de papaya con"
            self.optionA[1] = "     zanahoria"
            self.optionA[2] = "2. Arepa "

            self.optionB[0] = "1. Refresco de manzana"
            self.optionB[1] = "2. Salchipapas"

            self.optionC[0] = "1. Avena en hojuela"
            self.optionC[1] = "2. Arepa rellena con queso"
            
            self.recomendation[0] = "Las frutas te ofrecen variados sabores y colores"
        
        elif id == eTriviaQuestionId.REFRESHMENT_05:
            self.answer = eQuestionAnswer.ANSWER_B
            
            self.optionA[0] = "1. Guarapo de piña"
            self.optionA[1] = "2. Tostadas con"
            self.optionA[2] = "     mantequilla y"
            self.optionA[3] = "     mermelada"

            self.optionB[0] = "1. Te de mango"
            self.optionB[1] = "2. Torta de arroz con"
            self.optionB[2] = "     huevo"

            self.optionC[0] = "1. Queso de piña"
            self.optionC[1] = "2. Sandwich de jamón y"
            self.optionC[2] = "     queso"
            
            self.recomendation[0] = "Come despacio, disfruta el sabor de cada alimento"
        
        elif id == eTriviaQuestionId.REFRESHMENT_06:
            self.answer = eQuestionAnswer.ANSWER_C

            self.optionA[0] = "1. Zafresco"
            self.optionA[1] = "2. Brocheta de frutas"

            self.optionB[0] = "1. Refresco de manzana"
            self.optionB[1] = "2. Perro caliente"

            self.optionC[0] = "1. Avena en hojuela"
            self.optionC[1] = "2. Banano"
            
            self.recomendation[0] = "Para estar bien haz ejercicio y aliméntate adecuadamente"
            
        elif id == eTriviaQuestionId.REFRESHMENT_07:
            self.answer = eQuestionAnswer.ANSWER_A
            
            self.optionA[0] = "1. Guarapo de piña"
            self.optionA[1] = "2. Sandwich de jamón y"
            self.optionA[2] = "     queso"

            self.optionB[0] = "1. Te de mango"
            self.optionB[1] = "2. Salchipapas"

            self.optionC[0] = "1. Ensalada de frutas con"
            self.optionC[1] = "     yogurt"
            self.optionC[2] = "2. Perro caliente"
            
            self.recomendation[0] = "Cuando comas, no agregues sal a los alimentos"
        
        elif id == eTriviaQuestionId.REFRESHMENT_08:
            self.answer = eQuestionAnswer.ANSWER_B
            
            self.optionA[0] = "1. Jugo de maracuyá y"
            self.optionA[1] = "     zanahoria"
            self.optionA[2] = "2. Pastel de yuca"

            self.optionB[0] = "1. Jugo de papaya con"
            self.optionB[1] = "     zanahoria"
            self.optionB[2] = "2. Queso"

            self.optionC[0] = "1. Ensalada de colores"
            self.optionC[1] = "2. Salchicha frita"

            self.recomendation[0] = "Consume leche y sus derivados para cuidar tus dientes y"
            self.recomendation[1] = "huesos"
        
        elif id == eTriviaQuestionId.REFRESHMENT_09:
            self.answer = eQuestionAnswer.ANSWER_C
            
            self.optionA[0] = "1. Avena en hojuela"
            self.optionA[1] = "2. Torta de pan"

            self.optionB[0] = "1. Jugo de maracuyá y"
            self.optionB[1] = "     zanahoria"
            self.optionB[2] = "2. Roscón con bocadillo"

            self.optionC[0] = "1. Jugo de papaya con"
            self.optionC[1] = "     zanahoria"
            self.optionC[2] = "2. Tostadas integrales"
            
            self.recomendation[0] = "Consume alimentos integrales para mejorar tu digestión"
        
        elif id == eTriviaQuestionId.REFRESHMENT_10:
            self.answer = eQuestionAnswer.ANSWER_A
            
            self.optionA[0] = "1. Jugo de guayaba"
            self.optionA[1] = "2. Sandwich de jamón y"
            self.optionA[2] = "     queso"

            self.optionB[0] = "1. Queso de piña"
            self.optionB[1] = "2. Limonada"

            self.optionC[0] = "1. Gaseosa"
            self.optionC[1] = "2. Perro caliente"
            
            self.recomendation[0] = "El banano es una fruta deliciosa para niños y adultos"
        
        elif id == eTriviaQuestionId.REFRESHMENT_11:
            self.answer = eQuestionAnswer.ANSWER_B
            
            self.optionA[0] = "1. Ensalada de frutas con"
            self.optionA[1] = "     yogurt"
            self.optionA[2] = "2. Pan tajado"

            self.optionB[0] = "1. Limonada"
            self.optionB[1] = "2. Torta de banano"

            self.optionC[0] = "1. Ensalada de colores"
            self.optionC[1] = "2. Bocadillo"
            
            self.recomendation[0] = "Naranja: refrescante, llena de jugo y divertida."
            
        elif id == eTriviaQuestionId.REFRESHMENT_12:
            self.answer = eQuestionAnswer.ANSWER_C
            
            self.optionA[0] = "1. Jugo de mango"
            self.optionA[1] = "2. Queso de piña"

            self.optionB[0] = "1. Café con leche"
            self.optionB[1] = "2. Empanada"

            self.optionC[0] = "1. Brocheta de frutas"

            self.recomendation[0] = "La panela te da energía para seguir jugando"
        
        elif id == eTriviaQuestionId.REFRESHMENT_13:
            self.answer = eQuestionAnswer.ANSWER_A

            self.optionA[0] = "1. Sandwich de jamón y"
            self.optionA[1] = "     queso"
            self.optionA[2] = "2. Agua de panela"

            self.optionB[0] = "1. Arepa rellena con queso"
            self.optionB[1] = "2. Gaseosa"

            self.optionC[0] = "1. Zafresco"
            self.optionC[1] = "2. Salchipapas"
            
            self.recomendation[0] = "La piña te quita la sed"
            
        elif id == eTriviaQuestionId.REFRESHMENT_14:
            self.answer = eQuestionAnswer.ANSWER_B
            
            self.optionA[0] = "1. Refresco de manzana"
            self.optionA[1] = "2. Papas a la francesa"

            self.optionB[0] = "1. Guarapo de piña"
            self.optionB[1] = "2. Torta de zanahoria"

            self.optionC[0] = "1. Ensalada de frutas con"
            self.optionC[1] = "     yogurt"
            self.optionC[2] = "2. Te de mango"
            
            self.recomendation[0] = "La zanahoria tiene vitamina A"
            
        elif id == eTriviaQuestionId.REFRESHMENT_15:
            self.answer = eQuestionAnswer.ANSWER_C
            
            self.optionA[0] = "1. Ensalada de colores"
            self.optionA[1] = "2. Arepa rellena con queso"

            self.optionB[0] = "1. Chocolate en leche"
            self.optionB[1] = "2. Roscón"

            self.optionC[0] = "1. Jugo de maracuyá y"
            self.optionC[1] = "     zanahoria"
            self.optionC[2] = "2. Sandwich de jamón y"
            self.optionC[3] = "     queso"
            
            self.recomendation[0] = "El chocolate es delicioso y mejora tu estado de ánimo"
        
        elif id == eTriviaQuestionId.REFRESHMENT_16:
            self.answer = eQuestionAnswer.ANSWER_A
            
            self.optionA[0] = "1. Zafresco"
            self.optionA[1] = "2. Galletas integrales"

            self.optionB[0] = "1. Zafresco de manzana"
            self.optionB[1] = "2. Hamburguesa"

            self.optionC[0] = "1. Guarapo de piña"
            self.optionC[1] = "2. Roscón con bocadillo"
            
            self.recomendation[0] = "Un refrigerio nutritivo te alimenta y te da energía"
            
        elif id == eTriviaQuestionId.REFRESHMENT_17:
            self.answer = eQuestionAnswer.ANSWER_B
            
            self.optionA[0] = "1. Agua de panela"
            self.optionA[1] = "2. Pan"

            self.optionB[0] = "1. Chocolate en leche"
            self.optionB[1] = "2. Arepa rellena con queso"

            self.optionC[0] = "1. Brocheta de frutas"
            self.optionC[1] = "2. Te de mango"
            
            self.recomendation[0] = "El banano tiene vitaminas y minerales"
        
        elif id == eTriviaQuestionId.REFRESHMENT_18:
            self.answer = eQuestionAnswer.ANSWER_C
            
            self.optionA[0] = "1. Perro caliente"
            self.optionA[1] = "2. Limonada"

            self.optionB[0] = "1. Queso de piña"
            self.optionB[1] = "2. Bebida achocolatada"

            self.optionC[0] = "1. Café con leche"
            self.optionC[1] = "2. Sandwich de jamón y"
            self.optionC[2] = "     queso"
            
            self.recomendation[0] = "La mora tiene vitamina A que es buena para tu visión"
        
        elif id == eTriviaQuestionId.REFRESHMENT_19:
            self.answer = eQuestionAnswer.ANSWER_A
            
            self.optionA[0] = "1. Jugo de papaya con"
            self.optionA[1] = "     zanahoria"
            self.optionA[2] = "2. Torta de banano"

            self.optionB[0] = "1. Avena en hojuela"
            self.optionB[1] = "2. Torta de zanahoria"

            self.optionC[0] = "1. Bebida achocolatada"
            self.optionC[1] = "     fría"
            self.optionC[2] = "2. Salchipapas"

            self.recomendation[0] = "Buena nutrición es buena salud"
        
        elif id == eTriviaQuestionId.REFRESHMENT_20:
            self.answer = eQuestionAnswer.ANSWER_B
            
            self.optionA[0] = "1. Jugo de maracuyá y"
            self.optionA[1] = "     zanahoria"
            self.optionA[2] = "2. Queso con bocadillo"

            self.optionB[0] = "1. Jugo de mora"
            self.optionB[1] = "2. Arepa rellena con queso"

            self.optionC[0] = "1. Ensalada de frutas con"
            self.optionC[1] = "     yogurt"
            self.optionC[2] = "2. Tostadas"
            
            self.recomendation[0] = "Buena nutrición es buena salud"

        
class InformationIngredients:
    
    # ----------------------------
    # Contenedores
    # ----------------------------
    allIngredients = dict()
    group1Cereales = list()
    group2Verduras = list()
    group3Frutas = list()
    group4Carnes = list()
    group5Lacteos = list()
    group6Grasas = list()
    group7Azucares = list()
    group8Otros = list()
    
    # ----------------------------
    # Referencias unicas
    # ----------------------------
    # Grupo 1: Cereales, raices, tuberculos y platanos
    ing01 = Ingredient(eIngredientId._01_AREPA)
    ing02 = Ingredient(eIngredientId._02_ARROZ)
    ing03 = Ingredient(eIngredientId._03_AVENA)
    ing04 = Ingredient(eIngredientId._04_HARINA_DE_MAIZ_PRECOCIDA)
    ing05 = Ingredient(eIngredientId._05_HARINA_DE_TRIGO)
    ing06 = Ingredient(eIngredientId._06_MAIZ)
    ing07 = Ingredient(eIngredientId._07_MIGA_DE_PAN)
    ing08 = Ingredient(eIngredientId._08_PAN)
    ing09 = Ingredient(eIngredientId._09_PAPA)
    ing10 = Ingredient(eIngredientId._10_PASTA)
    ing11 = Ingredient(eIngredientId._11_PLATANO)
    ing12 = Ingredient(eIngredientId._12_SOYA)
    ing13 = Ingredient(eIngredientId._13_YUCA)
    
    # Grupo 2: Hortalizas, verduras, leguminosas verdes
    ing14 = Ingredient(eIngredientId._14_ACELGA)
    ing15 = Ingredient(eIngredientId._15_AHUYAMA)
    ing16 = Ingredient(eIngredientId._16_AJO)
    ing17 = Ingredient(eIngredientId._17_APIO)
    ing18 = Ingredient(eIngredientId._18_ARVEJA)
    ing19 = Ingredient(eIngredientId._19_BROCOLI)
    ing20 = Ingredient(eIngredientId._20_CEBOLLA_CABEZONA)
    ing21 = Ingredient(eIngredientId._21_CEBOLLA_LARGA)
    ing22 = Ingredient(eIngredientId._22_CILANTRO)
    ing23 = Ingredient(eIngredientId._23_COLIFLOR)
    ing24 = Ingredient(eIngredientId._24_ESPINACA)
    ing25 = Ingredient(eIngredientId._25_FRIJOL)
    ing26 = Ingredient(eIngredientId._26_GUASCAS)
    ing27 = Ingredient(eIngredientId._27_HABICUELA)
    ing28 = Ingredient(eIngredientId._28_LECHUGA)
    ing29 = Ingredient(eIngredientId._29_PEPINO_COHOMBRO)
    ing30 = Ingredient(eIngredientId._30_PEPINO_COMUN)
    ing31 = Ingredient(eIngredientId._31_PIMENTON)
    ing32 = Ingredient(eIngredientId._32_TOMATE)
    ing33 = Ingredient(eIngredientId._33_ZANAHORIA)

    # Grupo 3: Frutas
    ing34 = Ingredient(eIngredientId._34_AGUACATE)
    ing35 = Ingredient(eIngredientId._35_BANANO)
    ing36 = Ingredient(eIngredientId._36_CURUBA)
    ing37 = Ingredient(eIngredientId._37_FRESA)
    ing38 = Ingredient(eIngredientId._38_GUAYABA)
    ing39 = Ingredient(eIngredientId._39_LIMON)
    ing40 = Ingredient(eIngredientId._40_MANDARINA)
    ing41 = Ingredient(eIngredientId._41_MANGO)
    ing42 = Ingredient(eIngredientId._42_MANZANA_VERDE)
    ing43 = Ingredient(eIngredientId._43_MANZANA_ROJA)
    ing44 = Ingredient(eIngredientId._44_MARACUYA)
    ing45 = Ingredient(eIngredientId._45_MELON)
    ing46 = Ingredient(eIngredientId._46_MORA)
    ing47 = Ingredient(eIngredientId._47_NARANJA)
    ing48 = Ingredient(eIngredientId._48_PAPAYA)
    ing49 = Ingredient(eIngredientId._49_PATILLA)
    ing50 = Ingredient(eIngredientId._50_PERA)
    ing51 = Ingredient(eIngredientId._51_PINA)
    
    # Grupo 4: Carne, visceras, pollo, pescado, huevo, leguminosas secas
    ing52 = Ingredient(eIngredientId._52_ATUN)
    ing53 = Ingredient(eIngredientId._53_CARNE_DE_CERDO)
    ing54 = Ingredient(eIngredientId._54_CARNE_DE_RES)
    ing55 = Ingredient(eIngredientId._55_GARBANZO)
    ing56 = Ingredient(eIngredientId._56_HIGADO)
    ing57 = Ingredient(eIngredientId._57_HUEVO)
    ing58 = Ingredient(eIngredientId._58_LENTEJA)
    ing59 = Ingredient(eIngredientId._59_MENUDENCIAS)
    ing60 = Ingredient(eIngredientId._60_PESCADO)
    ing61 = Ingredient(eIngredientId._61_POLLO)
    ing62 = Ingredient(eIngredientId._62_SALCHICHA)
    
    # Grupo 5: Lacteos
    ing63 = Ingredient(eIngredientId._63_CREMA_DE_LECHE)
    ing64 = Ingredient(eIngredientId._64_KUMIS)
    ing65 = Ingredient(eIngredientId._65_LECHE)
    ing66 = Ingredient(eIngredientId._66_QUESO)
    ing67 = Ingredient(eIngredientId._67_YOGURT)
    
    # Grupo 6: Grasas
    ing68 = Ingredient(eIngredientId._68_ACEITE)
    ing69 = Ingredient(eIngredientId._69_MANTEQUILLA)
    ing70 = Ingredient(eIngredientId._70_MARGARINA)
    
    # Grupo 7: Azucares
    ing71 = Ingredient(eIngredientId._71_AZUCAR)
    ing72 = Ingredient(eIngredientId._72_CHOCOLATE)
    ing73 = Ingredient(eIngredientId._73_HELADO)
    ing74 = Ingredient(eIngredientId._74_PANELA)

    # Grupo 8: Otros
    ing75 = Ingredient(eIngredientId._75_AGUA)
    ing76 = Ingredient(eIngredientId._76_MAYONESA)
    ing77 = Ingredient(eIngredientId._77_MOSTAZA)
    ing78 = Ingredient(eIngredientId._78_POLVO_DE_HONEAR)
    ing79 = Ingredient(eIngredientId._79_SAL)
    ing80 = Ingredient(eIngredientId._80_SALSA_DE_TOMATE)
    ing81 = Ingredient(eIngredientId._81_SOPAS_EN_CREMA)
    ing82 = Ingredient(eIngredientId._82_VINAGRETA_DULCE)
    
    # ----------------------------
    # Diccionario de todos los grupos
    # ----------------------------
    # Grupo 1: Cereales, raices, tuberculos y platanos
    allIngredients[eIngredientId._01_AREPA] = ing01
    allIngredients[eIngredientId._02_ARROZ] = ing02
    allIngredients[eIngredientId._03_AVENA] = ing03
    allIngredients[eIngredientId._04_HARINA_DE_MAIZ_PRECOCIDA] = ing04
    allIngredients[eIngredientId._05_HARINA_DE_TRIGO] = ing05
    allIngredients[eIngredientId._06_MAIZ] = ing06
    allIngredients[eIngredientId._07_MIGA_DE_PAN] = ing07
    allIngredients[eIngredientId._08_PAN] = ing08
    allIngredients[eIngredientId._09_PAPA] = ing09
    allIngredients[eIngredientId._10_PASTA] = ing10
    allIngredients[eIngredientId._11_PLATANO] = ing11
    allIngredients[eIngredientId._12_SOYA] = ing12
    allIngredients[eIngredientId._13_YUCA] = ing13
    
    # Grupo 2: Hortalizas, verduras, leguminosas verdes
    allIngredients[eIngredientId._14_ACELGA] = ing14
    allIngredients[eIngredientId._15_AHUYAMA] = ing15
    allIngredients[eIngredientId._16_AJO] = ing16
    allIngredients[eIngredientId._17_APIO] = ing17
    allIngredients[eIngredientId._18_ARVEJA] = ing18
    allIngredients[eIngredientId._19_BROCOLI] = ing19
    allIngredients[eIngredientId._20_CEBOLLA_CABEZONA] = ing20
    allIngredients[eIngredientId._21_CEBOLLA_LARGA] = ing21
    allIngredients[eIngredientId._22_CILANTRO] = ing22
    allIngredients[eIngredientId._23_COLIFLOR] = ing23
    allIngredients[eIngredientId._24_ESPINACA] = ing24
    allIngredients[eIngredientId._25_FRIJOL] = ing25
    allIngredients[eIngredientId._26_GUASCAS] = ing26
    allIngredients[eIngredientId._27_HABICUELA] = ing27
    allIngredients[eIngredientId._28_LECHUGA] = ing28
    allIngredients[eIngredientId._29_PEPINO_COHOMBRO] = ing29
    allIngredients[eIngredientId._30_PEPINO_COMUN] = ing30
    allIngredients[eIngredientId._31_PIMENTON] = ing31
    allIngredients[eIngredientId._32_TOMATE] = ing32
    allIngredients[eIngredientId._33_ZANAHORIA] = ing33

    # Grupo 3: Frutas
    allIngredients[eIngredientId._34_AGUACATE] = ing34
    allIngredients[eIngredientId._35_BANANO] = ing35
    allIngredients[eIngredientId._36_CURUBA] = ing36
    allIngredients[eIngredientId._37_FRESA] = ing37
    allIngredients[eIngredientId._38_GUAYABA] = ing38
    allIngredients[eIngredientId._39_LIMON] = ing39
    allIngredients[eIngredientId._40_MANDARINA] = ing40
    allIngredients[eIngredientId._41_MANGO] = ing41
    allIngredients[eIngredientId._42_MANZANA_VERDE] = ing42
    allIngredients[eIngredientId._43_MANZANA_ROJA] = ing43
    allIngredients[eIngredientId._44_MARACUYA] = ing44
    allIngredients[eIngredientId._45_MELON] = ing45
    allIngredients[eIngredientId._46_MORA] = ing46
    allIngredients[eIngredientId._47_NARANJA] = ing47
    allIngredients[eIngredientId._48_PAPAYA] = ing48
    allIngredients[eIngredientId._49_PATILLA] = ing49
    allIngredients[eIngredientId._50_PERA] = ing50
    allIngredients[eIngredientId._51_PINA] = ing51
    
    # Grupo 4: Carne, visceras, pollo, pescado, huevo, leguminosas secas
    allIngredients[eIngredientId._52_ATUN] = ing52
    allIngredients[eIngredientId._53_CARNE_DE_CERDO] = ing53
    allIngredients[eIngredientId._54_CARNE_DE_RES] = ing54
    allIngredients[eIngredientId._55_GARBANZO] = ing55
    allIngredients[eIngredientId._56_HIGADO] = ing56
    allIngredients[eIngredientId._57_HUEVO] = ing57
    allIngredients[eIngredientId._58_LENTEJA] = ing58
    allIngredients[eIngredientId._59_MENUDENCIAS] = ing59
    allIngredients[eIngredientId._60_PESCADO] = ing60
    allIngredients[eIngredientId._61_POLLO] = ing61
    allIngredients[eIngredientId._62_SALCHICHA] = ing62
    
    # Grupo 5: Lacteos
    allIngredients[eIngredientId._63_CREMA_DE_LECHE] = ing63
    allIngredients[eIngredientId._64_KUMIS] = ing64
    allIngredients[eIngredientId._65_LECHE] = ing65
    allIngredients[eIngredientId._66_QUESO] = ing66
    allIngredients[eIngredientId._67_YOGURT] = ing67
    
    # Grupo 6: Grasas
    allIngredients[eIngredientId._68_ACEITE] = ing68
    allIngredients[eIngredientId._69_MANTEQUILLA] = ing69
    allIngredients[eIngredientId._70_MARGARINA] = ing70
    
    # Grupo 7: Azucares
    allIngredients[eIngredientId._71_AZUCAR] = ing71
    allIngredients[eIngredientId._72_CHOCOLATE] = ing72
    allIngredients[eIngredientId._73_HELADO] = ing73
    allIngredients[eIngredientId._74_PANELA] = ing74

    # Grupo 8: Otros
    allIngredients[eIngredientId._75_AGUA] = ing75
    allIngredients[eIngredientId._76_MAYONESA] = ing76
    allIngredients[eIngredientId._77_MOSTAZA] = ing77
    allIngredients[eIngredientId._78_POLVO_DE_HONEAR] = ing78
    allIngredients[eIngredientId._79_SAL] = ing79
    allIngredients[eIngredientId._80_SALSA_DE_TOMATE] = ing80
    allIngredients[eIngredientId._81_SOPAS_EN_CREMA] = ing81
    allIngredients[eIngredientId._82_VINAGRETA_DULCE] = ing82

    # ----------------------------
    # Listas por grupo
    # ----------------------------
    # Grupo 1: Cereales, raices, tuberculos y platanos
    group1Cereales.append(ing01)
    group1Cereales.append(ing02)
    group1Cereales.append(ing03)
    group1Cereales.append(ing04)
    group1Cereales.append(ing05)
    group1Cereales.append(ing06)
    group1Cereales.append(ing07)
    group1Cereales.append(ing08)
    group1Cereales.append(ing09)
    group1Cereales.append(ing10)
    group1Cereales.append(ing11)
    group1Cereales.append(ing12)
    group1Cereales.append(ing13)
    
    # Grupo 2: Hortalizas, verduras, leguminosas verdes
    group2Verduras.append(ing14)
    group2Verduras.append(ing15)
    group2Verduras.append(ing16)
    group2Verduras.append(ing17)
    group2Verduras.append(ing18)
    group2Verduras.append(ing19)
    group2Verduras.append(ing20)
    group2Verduras.append(ing21)
    group2Verduras.append(ing22)
    group2Verduras.append(ing23)
    group2Verduras.append(ing24)
    group2Verduras.append(ing25)
    group2Verduras.append(ing26)
    group2Verduras.append(ing27)
    group2Verduras.append(ing28)
    group2Verduras.append(ing29)
    group2Verduras.append(ing30)
    group2Verduras.append(ing31)
    group2Verduras.append(ing32)
    group2Verduras.append(ing33)

    # Grupo 3: Frutas
    group3Frutas.append(ing34)
    group3Frutas.append(ing35)
    group3Frutas.append(ing36)
    group3Frutas.append(ing37)
    group3Frutas.append(ing38)
    group3Frutas.append(ing39)
    group3Frutas.append(ing40)
    group3Frutas.append(ing41)
    group3Frutas.append(ing42)
    group3Frutas.append(ing43)
    group3Frutas.append(ing44)
    group3Frutas.append(ing45)
    group3Frutas.append(ing46)
    group3Frutas.append(ing47)
    group3Frutas.append(ing48)
    group3Frutas.append(ing49)
    group3Frutas.append(ing50)
    group3Frutas.append(ing51)
    
    # Grupo 4: Carne, visceras, pollo, pescado, huevo, leguminosas secas
    group4Carnes.append(ing52)
    group4Carnes.append(ing53)
    group4Carnes.append(ing54)
    group4Carnes.append(ing55)
    group4Carnes.append(ing56)
    group4Carnes.append(ing57)
    group4Carnes.append(ing58)
    group4Carnes.append(ing59)
    group4Carnes.append(ing60)
    group4Carnes.append(ing61)
    group4Carnes.append(ing62)
    
    # Grupo 5: Lacteos
    group5Lacteos.append(ing63)
    group5Lacteos.append(ing64)
    group5Lacteos.append(ing65)
    group5Lacteos.append(ing66)
    group5Lacteos.append(ing67)
    
    # Grupo 6: Grasas
    group6Grasas.append(ing68)
    group6Grasas.append(ing69)
    group6Grasas.append(ing70)
    
    # Grupo 7: Azucares
    group7Azucares.append(ing71)
    group7Azucares.append(ing72)
    group7Azucares.append(ing73)
    group7Azucares.append(ing74)

    # Grupo 8: Otros
    group8Otros.append(ing75)
    group8Otros.append(ing76)
    group8Otros.append(ing77)
    group8Otros.append(ing78)
    group8Otros.append(ing79)
    group8Otros.append(ing80)
    group8Otros.append(ing81)
    group8Otros.append(ing82)
    
    
class InformationRecipes:
    
    # ----------------------------
    # Referencias unicas
    # ----------------------------
    rec01 = Recipe(eRecipeId._01_ALBONDIGAS)
    rec02 = Recipe(eRecipeId._02_AREPA_RELLENA_CON_QUESO)
    rec03 = Recipe(eRecipeId._03_ARROZ_A_LA_SUEGRA)
    rec04 = Recipe(eRecipeId._04_ARROZ_CAMPESINO)
    rec05 = Recipe(eRecipeId._05_ARROZ_CON_MENUDENCIAS)
    rec06 = Recipe(eRecipeId._06_ARROZ_VEGETARIANO)
    rec07 = Recipe(eRecipeId._07_ARROZ_VERDE)
    rec08 = Recipe(eRecipeId._08_AVENA_EN_HOJUELAS)
    rec09 = Recipe(eRecipeId._09_BROCHETA_DE_FRUTAS)
    rec10 = Recipe(eRecipeId._10_CALDO_DE_PAPA_CON_COSTILLA)
    rec11 = Recipe(eRecipeId._11_CHANGUA_DE_LECHE_CON_HUEVO)
    rec12 = Recipe(eRecipeId._12_CREMA_DE_CEBOLLA_CABEZONA)
    rec13 = Recipe(eRecipeId._13_CROQUETAS_DE_ESPINACA)
    rec14 = Recipe(eRecipeId._14_ENSALADA_ALBA_HIT)
    rec15 = Recipe(eRecipeId._15_ENSALADA_CARLOS)
    rec16 = Recipe(eRecipeId._16_ENSALADA_CRIOLLA)
    rec17 = Recipe(eRecipeId._17_ENSALADA_DE_COLORES)
    rec18 = Recipe(eRecipeId._18_ENSALADA_DE_FRUTAS_CON_YOGURT)
    rec19 = Recipe(eRecipeId._19_ENSALADA_DE_LA_CASA)
    rec20 = Recipe(eRecipeId._20_ENSALADA_DEL_HUERTO)
    rec21 = Recipe(eRecipeId._21_ENSALADA_FRIA_DE_PAPA_CON_POLLO)
    rec22 = Recipe(eRecipeId._22_ENSALADA_RANCHERA)
    rec23 = Recipe(eRecipeId._23_GUARAPO_DE_PINA)
    rec24 = Recipe(eRecipeId._24_GUISO_DE_CARNE_Y_VERDURA)
    rec25 = Recipe(eRecipeId._25_GUISO_DE_HABICHUELA_CON_CARNE)
    rec26 = Recipe(eRecipeId._26_HAMBURGUESA)
    rec27 = Recipe(eRecipeId._27_HUEVO_TIBIO)
    rec28 = Recipe(eRecipeId._28_JUGO_DE_MARACUYA_Y_ZANAHORIA)
    rec29 = Recipe(eRecipeId._29_JUGO_DE_PAPAYA_CON_ZANAHORIA)
    rec30 = Recipe(eRecipeId._30_LOMO_DE_CERDO_EN_SALSA_DE_MANGO)
    rec31 = Recipe(eRecipeId._31_LOMO_DE_CERDO_ENCHILADO)
    rec32 = Recipe(eRecipeId._32_MACARRONES_CON_ATUN)
    rec33 = Recipe(eRecipeId._33_PASTA_CON_VEGETALES)
    rec34 = Recipe(eRecipeId._34_PATACONES_CON_CARNE_DESMECHADA)
    rec35 = Recipe(eRecipeId._35_PEPINOS_RELLENOS)
    rec36 = Recipe(eRecipeId._36_PERRO_CALIENTE)
    rec37 = Recipe(eRecipeId._37_PESCADO_A_LA_PRIMAVERA)
    rec38 = Recipe(eRecipeId._38_PESCADO_ORIENTAL)
    rec39 = Recipe(eRecipeId._39_POLLO_A_LA_JARDINERA)
    rec40 = Recipe(eRecipeId._40_QUESO_DE_PINA)
    rec41 = Recipe(eRecipeId._41_REFRESCO_DE_MANZANA)
    rec42 = Recipe(eRecipeId._42_SALCHIPAPAS)
    rec43 = Recipe(eRecipeId._43_SANDWICH_DE_JAMON_Y_QUESO)
    rec44 = Recipe(eRecipeId._44_SOPA_DE_GARBANZO)
    rec45 = Recipe(eRecipeId._45_SOPA_DE_LENTEJAS)
    rec46 = Recipe(eRecipeId._46_SOPA_DE_VERDURAS)
    rec47 = Recipe(eRecipeId._47_TE_DE_MANGO)
    rec48 = Recipe(eRecipeId._48_TERNERA_A_LA_MARINERA)
    rec49 = Recipe(eRecipeId._49_TOMATES_RELLENOS)
    rec50 = Recipe(eRecipeId._50_TORTA_DE_AHUYAMA)
    rec51 = Recipe(eRecipeId._51_TORTA_DE_BANANO)
    rec52 = Recipe(eRecipeId._52_TORTA_DE_ZANAHORIA)
    rec53 = Recipe(eRecipeId._53_TORTILLAS_DE_ACELGAS)
    rec54 = Recipe(eRecipeId._54_TORTILLAS_DE_ESPINACA)
    rec55 = Recipe(eRecipeId._55_ZAFRESCO)
    rec56 = Recipe(eRecipeId._56_TORTILLA_DE_MAZORCA)
    rec57 = Recipe(eRecipeId._57_BATIDO_DE_GUAYABA_Y_AVENA)
    rec58 = Recipe(eRecipeId._58_BATIDO_DE_YOGURT_FRESAS_Y_AVENA)
    rec59 = Recipe(eRecipeId._59_PANQUEQUES_DE_AVENA)
    rec60 = Recipe(eRecipeId._60_TORTILLA_DE_VERDURAS_Y_QUESO)
    rec61 = Recipe(eRecipeId._61_PANQUEQUES_DE_FRUTA)
    rec62 = Recipe(eRecipeId._62_AREPAS_DE_MAZORCA)
    
    # ----------------------------
    # Diccionario
    # ----------------------------
    allRecipesDict = dict()
    allRecipesDict[eRecipeId._01_ALBONDIGAS] = rec01
    allRecipesDict[eRecipeId._02_AREPA_RELLENA_CON_QUESO] = rec02
    allRecipesDict[eRecipeId._03_ARROZ_A_LA_SUEGRA] = rec03
    allRecipesDict[eRecipeId._04_ARROZ_CAMPESINO] = rec04
    allRecipesDict[eRecipeId._05_ARROZ_CON_MENUDENCIAS] = rec05
    allRecipesDict[eRecipeId._06_ARROZ_VEGETARIANO] = rec06
    allRecipesDict[eRecipeId._07_ARROZ_VERDE] = rec07
    allRecipesDict[eRecipeId._08_AVENA_EN_HOJUELAS] = rec08
    allRecipesDict[eRecipeId._09_BROCHETA_DE_FRUTAS] = rec09
    allRecipesDict[eRecipeId._10_CALDO_DE_PAPA_CON_COSTILLA] = rec10
    allRecipesDict[eRecipeId._11_CHANGUA_DE_LECHE_CON_HUEVO] = rec11
    allRecipesDict[eRecipeId._12_CREMA_DE_CEBOLLA_CABEZONA] = rec12
    allRecipesDict[eRecipeId._13_CROQUETAS_DE_ESPINACA] = rec13
    allRecipesDict[eRecipeId._14_ENSALADA_ALBA_HIT] = rec14
    allRecipesDict[eRecipeId._15_ENSALADA_CARLOS] = rec15
    allRecipesDict[eRecipeId._16_ENSALADA_CRIOLLA] = rec16
    allRecipesDict[eRecipeId._17_ENSALADA_DE_COLORES] = rec17
    allRecipesDict[eRecipeId._18_ENSALADA_DE_FRUTAS_CON_YOGURT] = rec18
    allRecipesDict[eRecipeId._19_ENSALADA_DE_LA_CASA] = rec19
    allRecipesDict[eRecipeId._20_ENSALADA_DEL_HUERTO] = rec20
    allRecipesDict[eRecipeId._21_ENSALADA_FRIA_DE_PAPA_CON_POLLO] = rec21
    allRecipesDict[eRecipeId._22_ENSALADA_RANCHERA] = rec22
    allRecipesDict[eRecipeId._23_GUARAPO_DE_PINA] = rec23
    allRecipesDict[eRecipeId._24_GUISO_DE_CARNE_Y_VERDURA] = rec24
    allRecipesDict[eRecipeId._25_GUISO_DE_HABICHUELA_CON_CARNE] = rec25
    allRecipesDict[eRecipeId._26_HAMBURGUESA] = rec26
    allRecipesDict[eRecipeId._27_HUEVO_TIBIO] = rec27
    allRecipesDict[eRecipeId._28_JUGO_DE_MARACUYA_Y_ZANAHORIA] = rec28
    allRecipesDict[eRecipeId._29_JUGO_DE_PAPAYA_CON_ZANAHORIA] = rec29
    allRecipesDict[eRecipeId._30_LOMO_DE_CERDO_EN_SALSA_DE_MANGO] = rec30
    allRecipesDict[eRecipeId._31_LOMO_DE_CERDO_ENCHILADO] = rec31
    allRecipesDict[eRecipeId._32_MACARRONES_CON_ATUN] = rec32
    allRecipesDict[eRecipeId._33_PASTA_CON_VEGETALES] = rec33
    allRecipesDict[eRecipeId._34_PATACONES_CON_CARNE_DESMECHADA] = rec34
    allRecipesDict[eRecipeId._35_PEPINOS_RELLENOS] = rec35
    allRecipesDict[eRecipeId._36_PERRO_CALIENTE] = rec36
    allRecipesDict[eRecipeId._37_PESCADO_A_LA_PRIMAVERA] = rec37
    allRecipesDict[eRecipeId._38_PESCADO_ORIENTAL] = rec38
    allRecipesDict[eRecipeId._39_POLLO_A_LA_JARDINERA] = rec39
    allRecipesDict[eRecipeId._40_QUESO_DE_PINA] = rec40
    allRecipesDict[eRecipeId._41_REFRESCO_DE_MANZANA] = rec41
    allRecipesDict[eRecipeId._42_SALCHIPAPAS] = rec42
    allRecipesDict[eRecipeId._43_SANDWICH_DE_JAMON_Y_QUESO] = rec43
    allRecipesDict[eRecipeId._44_SOPA_DE_GARBANZO] = rec44
    allRecipesDict[eRecipeId._45_SOPA_DE_LENTEJAS] = rec45
    allRecipesDict[eRecipeId._46_SOPA_DE_VERDURAS] = rec46
    allRecipesDict[eRecipeId._47_TE_DE_MANGO] = rec47
    allRecipesDict[eRecipeId._48_TERNERA_A_LA_MARINERA] = rec48
    allRecipesDict[eRecipeId._49_TOMATES_RELLENOS] = rec49
    allRecipesDict[eRecipeId._50_TORTA_DE_AHUYAMA] = rec50
    allRecipesDict[eRecipeId._51_TORTA_DE_BANANO] = rec51
    allRecipesDict[eRecipeId._52_TORTA_DE_ZANAHORIA] = rec52
    allRecipesDict[eRecipeId._53_TORTILLAS_DE_ACELGAS] = rec53
    allRecipesDict[eRecipeId._54_TORTILLAS_DE_ESPINACA] = rec54
    allRecipesDict[eRecipeId._55_ZAFRESCO] = rec55
    allRecipesDict[eRecipeId._56_TORTILLA_DE_MAZORCA] = rec56
    allRecipesDict[eRecipeId._57_BATIDO_DE_GUAYABA_Y_AVENA] = rec57
    allRecipesDict[eRecipeId._58_BATIDO_DE_YOGURT_FRESAS_Y_AVENA] = rec58
    allRecipesDict[eRecipeId._59_PANQUEQUES_DE_AVENA] = rec59
    allRecipesDict[eRecipeId._60_TORTILLA_DE_VERDURAS_Y_QUESO] = rec60
    allRecipesDict[eRecipeId._61_PANQUEQUES_DE_FRUTA] = rec61
    allRecipesDict[eRecipeId._62_AREPAS_DE_MAZORCA] = rec62
    
    # ----------------------------
    # Lista general (En orden alfabetico)
    # ----------------------------
    allRecipesList = list()
    allRecipesList.append(rec01)
    allRecipesList.append(rec62) #
    allRecipesList.append(rec02)
    allRecipesList.append(rec03)
    allRecipesList.append(rec04)
    allRecipesList.append(rec05)
    allRecipesList.append(rec06)
    allRecipesList.append(rec07)
    allRecipesList.append(rec08)
    allRecipesList.append(rec57) #
    allRecipesList.append(rec58) #
    allRecipesList.append(rec09)
    allRecipesList.append(rec10)
    allRecipesList.append(rec11)
    allRecipesList.append(rec12)
    allRecipesList.append(rec13)
    allRecipesList.append(rec14)
    allRecipesList.append(rec15)
    allRecipesList.append(rec16)
    allRecipesList.append(rec17)
    allRecipesList.append(rec18)
    allRecipesList.append(rec19)
    allRecipesList.append(rec20)
    allRecipesList.append(rec21)
    allRecipesList.append(rec22)
    allRecipesList.append(rec23)
    allRecipesList.append(rec24)
    allRecipesList.append(rec25)
    allRecipesList.append(rec26)
    allRecipesList.append(rec27)
    allRecipesList.append(rec28)
    allRecipesList.append(rec29)
    allRecipesList.append(rec30)
    allRecipesList.append(rec31)
    allRecipesList.append(rec32)
    allRecipesList.append(rec61) #
    allRecipesList.append(rec59) #
    allRecipesList.append(rec33)
    allRecipesList.append(rec34)
    allRecipesList.append(rec35)
    allRecipesList.append(rec36)
    allRecipesList.append(rec37)
    allRecipesList.append(rec38)
    allRecipesList.append(rec39)
    allRecipesList.append(rec40)
    allRecipesList.append(rec41)
    allRecipesList.append(rec42)
    allRecipesList.append(rec43)
    allRecipesList.append(rec44)
    allRecipesList.append(rec45)
    allRecipesList.append(rec46)
    allRecipesList.append(rec47)
    allRecipesList.append(rec48)
    allRecipesList.append(rec49)
    allRecipesList.append(rec50)
    allRecipesList.append(rec51)
    allRecipesList.append(rec52)
    allRecipesList.append(rec56) #
    allRecipesList.append(rec60) #
    allRecipesList.append(rec53)
    allRecipesList.append(rec54)
    allRecipesList.append(rec55)
    
    # allRecipesList.append(rec56)
    # allRecipesList.append(rec57)
    # allRecipesList.append(rec58)
    # allRecipesList.append(rec59)
    # allRecipesList.append(rec60)
    # allRecipesList.append(rec61)
    # allRecipesList.append(rec62)
    
    # ----------------------------
    # Lista de Recetas (BREAKFAST)
    # ----------------------------
    breakfastRecipes = list()
    breakfastRecipes.append(rec02)
    breakfastRecipes.append(rec08)
    breakfastRecipes.append(rec10)
    breakfastRecipes.append(rec11)
    breakfastRecipes.append(rec18)
    breakfastRecipes.append(rec27)
    breakfastRecipes.append(rec28)
    breakfastRecipes.append(rec55)
    breakfastRecipes.append(rec56)
    breakfastRecipes.append(rec57)
    breakfastRecipes.append(rec58)
    breakfastRecipes.append(rec59)
    breakfastRecipes.append(rec60)
    breakfastRecipes.append(rec61)
    breakfastRecipes.append(rec62)
    
    # ----------------------------
    # Lista de Recetas (REFRESHMENT_MORNING)
    # ----------------------------
    refrigerioRecipes = list()
    refrigerioRecipes.append(rec02)
    refrigerioRecipes.append(rec08)
    refrigerioRecipes.append(rec09)
    refrigerioRecipes.append(rec17)
    refrigerioRecipes.append(rec18)
    refrigerioRecipes.append(rec23)
    refrigerioRecipes.append(rec28)
    refrigerioRecipes.append(rec36)
    refrigerioRecipes.append(rec40)
    refrigerioRecipes.append(rec41)
    refrigerioRecipes.append(rec42)
    refrigerioRecipes.append(rec43)
    refrigerioRecipes.append(rec47)
    refrigerioRecipes.append(rec55)
    
    # ----------------------------
    # Lista de Recetas (LUNCH)
    # ----------------------------
    almuerzoRecipes = list()
    almuerzoRecipes.append(rec01)
    almuerzoRecipes.append(rec03)
    almuerzoRecipes.append(rec04)
    almuerzoRecipes.append(rec05)
    almuerzoRecipes.append(rec06)
    almuerzoRecipes.append(rec07)
    almuerzoRecipes.append(rec12)
    almuerzoRecipes.append(rec13)
    almuerzoRecipes.append(rec14)
    almuerzoRecipes.append(rec15)
    almuerzoRecipes.append(rec16)
    almuerzoRecipes.append(rec19)
    almuerzoRecipes.append(rec20)
    almuerzoRecipes.append(rec21)
    almuerzoRecipes.append(rec22)
    almuerzoRecipes.append(rec24)
    almuerzoRecipes.append(rec25)
    almuerzoRecipes.append(rec26)
    almuerzoRecipes.append(rec30)
    almuerzoRecipes.append(rec31)
    almuerzoRecipes.append(rec32)
    almuerzoRecipes.append(rec33)
    almuerzoRecipes.append(rec35)
    almuerzoRecipes.append(rec37)
    almuerzoRecipes.append(rec38)
    almuerzoRecipes.append(rec39)
    almuerzoRecipes.append(rec44)
    almuerzoRecipes.append(rec45)
    almuerzoRecipes.append(rec46)
    almuerzoRecipes.append(rec48)
    almuerzoRecipes.append(rec49)
    almuerzoRecipes.append(rec50)
    almuerzoRecipes.append(rec51)
    almuerzoRecipes.append(rec52)
    almuerzoRecipes.append(rec53)
    almuerzoRecipes.append(rec54)
    
    # ----------------------------
    # Lista de Recetas (REFRESHMENT_AFTERNOON)
    # ----------------------------
    oncesRecipes = list()
    oncesRecipes.append(rec02)
    oncesRecipes.append(rec08)
    oncesRecipes.append(rec09)
    oncesRecipes.append(rec17)
    oncesRecipes.append(rec18)
    oncesRecipes.append(rec23)
    oncesRecipes.append(rec28)
    oncesRecipes.append(rec36)
    oncesRecipes.append(rec40)
    oncesRecipes.append(rec41)
    oncesRecipes.append(rec42)
    oncesRecipes.append(rec43)
    oncesRecipes.append(rec47)
    oncesRecipes.append(rec55)
    
    # ----------------------------
    # Lista de Recetas (DINNER)
    # ----------------------------
    comidaRecipes = list()
    comidaRecipes.append(rec01)
    comidaRecipes.append(rec03)
    comidaRecipes.append(rec04)
    comidaRecipes.append(rec05)
    comidaRecipes.append(rec06)
    comidaRecipes.append(rec07)
    comidaRecipes.append(rec10)
    comidaRecipes.append(rec11)
    comidaRecipes.append(rec12)
    comidaRecipes.append(rec13)
    comidaRecipes.append(rec14)
    comidaRecipes.append(rec15)
    comidaRecipes.append(rec16)
    comidaRecipes.append(rec19)
    comidaRecipes.append(rec20)
    comidaRecipes.append(rec21)
    comidaRecipes.append(rec22)
    comidaRecipes.append(rec24)
    comidaRecipes.append(rec25)
    comidaRecipes.append(rec26)
    comidaRecipes.append(rec30)
    comidaRecipes.append(rec31)
    comidaRecipes.append(rec32)
    comidaRecipes.append(rec33)
    comidaRecipes.append(rec34)
    comidaRecipes.append(rec35)
    comidaRecipes.append(rec37)
    comidaRecipes.append(rec38)
    comidaRecipes.append(rec39)
    comidaRecipes.append(rec43)
    comidaRecipes.append(rec44)
    comidaRecipes.append(rec45)
    comidaRecipes.append(rec46)
    comidaRecipes.append(rec48)
    comidaRecipes.append(rec49)
    comidaRecipes.append(rec50)
    comidaRecipes.append(rec51)
    comidaRecipes.append(rec52)
    comidaRecipes.append(rec53)
    comidaRecipes.append(rec54)
    

class InformationMotionPoints:

        # ROW1_STOVE        
        ROW1_STOVE = MotionPoint(eMotionBlock.ROW1_STOVE, eMotionColumn.COLUMN_1, eMotionRow.ROW_1)
        ROW1_STOVE.addLink(eMotionDirection.DOWN, eMotionBlock.ROW2_BLOCK_A)
        ROW1_STOVE.addLink(eMotionDirection.RIGHT, eMotionBlock.ROW1_SINK)
        
        # ROW1_SINK
        ROW1_SINK = MotionPoint(eMotionBlock.ROW1_SINK, eMotionColumn.COLUMN_3, eMotionRow.ROW_1)
        ROW1_SINK.addLink(eMotionDirection.LEFT, eMotionBlock.ROW1_STOVE)
        ROW1_SINK.addLink(eMotionDirection.RIGHT, eMotionBlock.ROW1_FRIDGE)
        
        # ROW1_FRIDGE
        ROW1_FRIDGE = MotionPoint(eMotionBlock.ROW1_FRIDGE, eMotionColumn.COLUMN_5, eMotionRow.ROW_1)
        ROW1_FRIDGE.addLink(eMotionDirection.LEFT, eMotionBlock.ROW1_SINK)
        ROW1_FRIDGE.addLink(eMotionDirection.RIGHT, eMotionBlock.ROW1_DISHWASHER)
        
        # ROW1_DISHWASHER
        ROW1_DISHWASHER = MotionPoint(eMotionBlock.ROW1_DISHWASHER, eMotionColumn.COLUMN_7, eMotionRow.ROW_1)
        ROW1_DISHWASHER.addLink(eMotionDirection.LEFT, eMotionBlock.ROW1_FRIDGE)
        ROW1_DISHWASHER.addLink(eMotionDirection.DOWN, eMotionBlock.ROW2_BLOCK_D)
        
        # ROW2_CLIENT_A
        ROW2_CLIENT_A = MotionPoint(eMotionBlock.ROW2_BLOCK_A, eMotionColumn.COLUMN_1, eMotionRow.ROW_2)
        ROW2_CLIENT_A.addLink(eMotionDirection.UP, eMotionBlock.ROW1_STOVE)
        ROW2_CLIENT_A.addLink(eMotionDirection.RIGHT, eMotionBlock.ROW2_INTERBLOCK_AB)
        
        # ROW2_INTER_AB
        ROW2_INTER_AB = MotionPoint(eMotionBlock.ROW2_INTERBLOCK_AB, eMotionColumn.COLUMN_2, eMotionRow.ROW_2)
        ROW2_INTER_AB.addLink(eMotionDirection.LEFT, eMotionBlock.ROW2_BLOCK_A)
        ROW2_INTER_AB.addLink(eMotionDirection.DOWN, eMotionBlock.ROW3_INTERBLOCK_EF)
        ROW2_INTER_AB.addLink(eMotionDirection.RIGHT, eMotionBlock.ROW2_BLOCK_B)
        
        # ROW2_CLIENT_B
        ROW2_CLIENT_B = MotionPoint(eMotionBlock.ROW2_BLOCK_B, eMotionColumn.COLUMN_3, eMotionRow.ROW_2)
        ROW2_CLIENT_B.addLink(eMotionDirection.LEFT, eMotionBlock.ROW2_INTERBLOCK_AB)
        ROW2_CLIENT_B.addLink(eMotionDirection.RIGHT, eMotionBlock.ROW2_INTERBLOCK_BC)
        
        # ROW2_INTER_BC
        ROW2_INTER_BC = MotionPoint(eMotionBlock.ROW2_INTERBLOCK_BC, eMotionColumn.COLUMN_4, eMotionRow.ROW_2)
        ROW2_INTER_BC.addLink(eMotionDirection.LEFT, eMotionBlock.ROW2_BLOCK_B)
        ROW2_INTER_BC.addLink(eMotionDirection.DOWN, eMotionBlock.ROW3_INTERBLOCK_FG)
        ROW2_INTER_BC.addLink(eMotionDirection.RIGHT, eMotionBlock.ROW2_BLOCK_C)        
        
        # ROW2_CLIENT_C
        ROW2_CLIENT_C = MotionPoint(eMotionBlock.ROW2_BLOCK_C, eMotionColumn.COLUMN_5, eMotionRow.ROW_2)
        ROW2_CLIENT_C.addLink(eMotionDirection.LEFT, eMotionBlock.ROW2_INTERBLOCK_BC)
        ROW2_CLIENT_C.addLink(eMotionDirection.RIGHT, eMotionBlock.ROW2_INTERBLOCK_CD)        
        
        # ROW2_INTER_CD
        ROW2_INTER_CD = MotionPoint(eMotionBlock.ROW2_INTERBLOCK_CD, eMotionColumn.COLUMN_6, eMotionRow.ROW_2)
        ROW2_INTER_CD.addLink(eMotionDirection.LEFT, eMotionBlock.ROW2_BLOCK_C)
        ROW2_INTER_CD.addLink(eMotionDirection.DOWN, eMotionBlock.ROW3_INTERBLOCK_GH)
        ROW2_INTER_CD.addLink(eMotionDirection.RIGHT, eMotionBlock.ROW2_BLOCK_D)        
        
        # ROW2_CLIENT_D
        ROW2_CLIENT_D = MotionPoint(eMotionBlock.ROW2_BLOCK_D, eMotionColumn.COLUMN_7, eMotionRow.ROW_2)
        ROW2_CLIENT_D.addLink(eMotionDirection.LEFT, eMotionBlock.ROW2_INTERBLOCK_CD)
        ROW2_CLIENT_D.addLink(eMotionDirection.UP, eMotionBlock.ROW1_DISHWASHER)        
                
        # ROW3_CLIENT_E
        ROW3_CLIENT_E = MotionPoint(eMotionBlock.ROW3_BLOCK_E, eMotionColumn.COLUMN_1, eMotionRow.ROW_3)
        ROW3_CLIENT_E.addLink(eMotionDirection.RIGHT, eMotionBlock.ROW3_INTERBLOCK_EF)
        
        # ROW3_INTER_EF
        ROW3_INTER_EF = MotionPoint(eMotionBlock.ROW3_INTERBLOCK_EF, eMotionColumn.COLUMN_2, eMotionRow.ROW_3)
        ROW3_INTER_EF.addLink(eMotionDirection.LEFT, eMotionBlock.ROW3_BLOCK_E)
        ROW3_INTER_EF.addLink(eMotionDirection.UP, eMotionBlock.ROW2_INTERBLOCK_AB)
        ROW3_INTER_EF.addLink(eMotionDirection.RIGHT, eMotionBlock.ROW3_BLOCK_F)
        
        # ROW3_CLIENT_F
        ROW3_CLIENT_F = MotionPoint(eMotionBlock.ROW3_BLOCK_F, eMotionColumn.COLUMN_3, eMotionRow.ROW_3)
        ROW3_CLIENT_F.addLink(eMotionDirection.LEFT, eMotionBlock.ROW3_INTERBLOCK_EF)
        ROW3_CLIENT_F.addLink(eMotionDirection.RIGHT, eMotionBlock.ROW3_INTERBLOCK_FG)
        
        # ROW3_INTER_FG
        ROW3_INTER_FG = MotionPoint(eMotionBlock.ROW3_INTERBLOCK_FG, eMotionColumn.COLUMN_4, eMotionRow.ROW_3)
        ROW3_INTER_FG.addLink(eMotionDirection.LEFT, eMotionBlock.ROW3_BLOCK_F)
        ROW3_INTER_FG.addLink(eMotionDirection.UP, eMotionBlock.ROW2_INTERBLOCK_BC)
        ROW3_INTER_FG.addLink(eMotionDirection.RIGHT, eMotionBlock.ROW3_BLOCK_G)        
        
        # ROW3_CLIENT_G
        ROW3_CLIENT_G = MotionPoint(eMotionBlock.ROW3_BLOCK_G, eMotionColumn.COLUMN_5, eMotionRow.ROW_3)
        ROW3_CLIENT_G.addLink(eMotionDirection.LEFT, eMotionBlock.ROW3_INTERBLOCK_FG)
        ROW3_CLIENT_G.addLink(eMotionDirection.RIGHT, eMotionBlock.ROW3_INTERBLOCK_GH)        
        
        # ROW3_INTER_GH
        ROW3_INTER_GH = MotionPoint(eMotionBlock.ROW3_INTERBLOCK_GH, eMotionColumn.COLUMN_6, eMotionRow.ROW_3)
        ROW3_INTER_GH.addLink(eMotionDirection.LEFT, eMotionBlock.ROW3_BLOCK_G)
        ROW3_INTER_GH.addLink(eMotionDirection.UP, eMotionBlock.ROW2_INTERBLOCK_CD)
        ROW3_INTER_GH.addLink(eMotionDirection.RIGHT, eMotionBlock.ROW3_BLOCK_H)        
        
        # ROW3_CLIENT_H
        ROW3_CLIENT_H = MotionPoint(eMotionBlock.ROW3_BLOCK_H, eMotionColumn.COLUMN_7, eMotionRow.ROW_3)
        ROW3_CLIENT_H.addLink(eMotionDirection.LEFT, eMotionBlock.ROW3_INTERBLOCK_GH)
        
        allPoints = dict()
        allPoints[eMotionBlock.ROW1_STOVE] = ROW1_STOVE
        allPoints[eMotionBlock.ROW1_SINK] = ROW1_SINK
        allPoints[eMotionBlock.ROW1_FRIDGE] = ROW1_FRIDGE
        allPoints[eMotionBlock.ROW1_DISHWASHER] = ROW1_DISHWASHER
        
        allPoints[eMotionBlock.ROW2_BLOCK_A] = ROW2_CLIENT_A
        allPoints[eMotionBlock.ROW2_INTERBLOCK_AB] = ROW2_INTER_AB
        allPoints[eMotionBlock.ROW2_BLOCK_B] = ROW2_CLIENT_B
        allPoints[eMotionBlock.ROW2_INTERBLOCK_BC] = ROW2_INTER_BC
        allPoints[eMotionBlock.ROW2_BLOCK_C] = ROW2_CLIENT_C
        allPoints[eMotionBlock.ROW2_INTERBLOCK_CD] = ROW2_INTER_CD
        allPoints[eMotionBlock.ROW2_BLOCK_D] = ROW2_CLIENT_D
        
        allPoints[eMotionBlock.ROW3_BLOCK_E] = ROW3_CLIENT_E
        allPoints[eMotionBlock.ROW3_INTERBLOCK_EF] = ROW3_INTER_EF
        allPoints[eMotionBlock.ROW3_BLOCK_F] = ROW3_CLIENT_F
        allPoints[eMotionBlock.ROW3_INTERBLOCK_FG] = ROW3_INTER_FG
        allPoints[eMotionBlock.ROW3_BLOCK_G] = ROW3_CLIENT_G
        allPoints[eMotionBlock.ROW3_INTERBLOCK_GH] = ROW3_INTER_GH
        allPoints[eMotionBlock.ROW3_BLOCK_H] = ROW3_CLIENT_H
        
        
class InformationTrivias:
    
    # ----------------------------
    # Referencias unicas
    # ----------------------------
    bre01 = Trivia(eTriviaQuestionId.BREAKFAST_01)
    bre02 = Trivia(eTriviaQuestionId.BREAKFAST_02)
    bre03 = Trivia(eTriviaQuestionId.BREAKFAST_03)
    bre04 = Trivia(eTriviaQuestionId.BREAKFAST_04)
    bre05 = Trivia(eTriviaQuestionId.BREAKFAST_05)
    bre06 = Trivia(eTriviaQuestionId.BREAKFAST_06)
    bre07 = Trivia(eTriviaQuestionId.BREAKFAST_07)
    bre08 = Trivia(eTriviaQuestionId.BREAKFAST_08)
    bre09 = Trivia(eTriviaQuestionId.BREAKFAST_09)
    bre10 = Trivia(eTriviaQuestionId.BREAKFAST_10)
    bre11 = Trivia(eTriviaQuestionId.BREAKFAST_11)
    bre12 = Trivia(eTriviaQuestionId.BREAKFAST_12)
    bre13 = Trivia(eTriviaQuestionId.BREAKFAST_13)
    bre14 = Trivia(eTriviaQuestionId.BREAKFAST_14)
    bre15 = Trivia(eTriviaQuestionId.BREAKFAST_15)
            
    lun01 = Trivia(eTriviaQuestionId.LUNCH_01)
    lun02 = Trivia(eTriviaQuestionId.LUNCH_02)
    lun03 = Trivia(eTriviaQuestionId.LUNCH_03)
    lun04 = Trivia(eTriviaQuestionId.LUNCH_04)
    lun05 = Trivia(eTriviaQuestionId.LUNCH_05)
    lun06 = Trivia(eTriviaQuestionId.LUNCH_06)
    lun07 = Trivia(eTriviaQuestionId.LUNCH_07)
    lun08 = Trivia(eTriviaQuestionId.LUNCH_08)
    lun09 = Trivia(eTriviaQuestionId.LUNCH_09)
    lun10 = Trivia(eTriviaQuestionId.LUNCH_10)
    lun11 = Trivia(eTriviaQuestionId.LUNCH_11)
    lun12 = Trivia(eTriviaQuestionId.LUNCH_12)
    lun13 = Trivia(eTriviaQuestionId.LUNCH_13)
    lun14 = Trivia(eTriviaQuestionId.LUNCH_14)
    lun15 = Trivia(eTriviaQuestionId.LUNCH_15)
    lun16 = Trivia(eTriviaQuestionId.LUNCH_16)
    lun17 = Trivia(eTriviaQuestionId.LUNCH_17)
    lun18 = Trivia(eTriviaQuestionId.LUNCH_18)
    lun19 = Trivia(eTriviaQuestionId.LUNCH_19)
    lun20 = Trivia(eTriviaQuestionId.LUNCH_20)
            
    din01 = Trivia(eTriviaQuestionId.DINNER_01)
    din02 = Trivia(eTriviaQuestionId.DINNER_02)
    din03 = Trivia(eTriviaQuestionId.DINNER_03)
    din04 = Trivia(eTriviaQuestionId.DINNER_04)
    din05 = Trivia(eTriviaQuestionId.DINNER_05)
    din06 = Trivia(eTriviaQuestionId.DINNER_06)
    din07 = Trivia(eTriviaQuestionId.DINNER_07)
    din08 = Trivia(eTriviaQuestionId.DINNER_08)
    din09 = Trivia(eTriviaQuestionId.DINNER_09)
    din10 = Trivia(eTriviaQuestionId.DINNER_10)
    din11 = Trivia(eTriviaQuestionId.DINNER_11)
    din12 = Trivia(eTriviaQuestionId.DINNER_12)
    din13 = Trivia(eTriviaQuestionId.DINNER_13)
    din14 = Trivia(eTriviaQuestionId.DINNER_14)
    din15 = Trivia(eTriviaQuestionId.DINNER_15)
    din16 = Trivia(eTriviaQuestionId.DINNER_16)
    din17 = Trivia(eTriviaQuestionId.DINNER_17)
    din18 = Trivia(eTriviaQuestionId.DINNER_18)
    din19 = Trivia(eTriviaQuestionId.DINNER_19)
    din20 = Trivia(eTriviaQuestionId.DINNER_20)
            
    ref01 = Trivia(eTriviaQuestionId.REFRESHMENT_01)
    ref02 = Trivia(eTriviaQuestionId.REFRESHMENT_02)
    ref03 = Trivia(eTriviaQuestionId.REFRESHMENT_03)
    ref04 = Trivia(eTriviaQuestionId.REFRESHMENT_04)
    ref05 = Trivia(eTriviaQuestionId.REFRESHMENT_05)
    ref06 = Trivia(eTriviaQuestionId.REFRESHMENT_06)
    ref07 = Trivia(eTriviaQuestionId.REFRESHMENT_07)
    ref08 = Trivia(eTriviaQuestionId.REFRESHMENT_08)
    ref09 = Trivia(eTriviaQuestionId.REFRESHMENT_09)
    ref10 = Trivia(eTriviaQuestionId.REFRESHMENT_10)
    ref11 = Trivia(eTriviaQuestionId.REFRESHMENT_11)
    ref12 = Trivia(eTriviaQuestionId.REFRESHMENT_12)
    ref13 = Trivia(eTriviaQuestionId.REFRESHMENT_13)
    ref14 = Trivia(eTriviaQuestionId.REFRESHMENT_14)
    ref15 = Trivia(eTriviaQuestionId.REFRESHMENT_15)
    ref16 = Trivia(eTriviaQuestionId.REFRESHMENT_16)
    ref17 = Trivia(eTriviaQuestionId.REFRESHMENT_17)
    ref18 = Trivia(eTriviaQuestionId.REFRESHMENT_18)
    ref19 = Trivia(eTriviaQuestionId.REFRESHMENT_19)
    ref20 = Trivia(eTriviaQuestionId.REFRESHMENT_20)
    
    # ----------------------------
    # Trivias para BREAKFAST
    # ----------------------------
    breakfastTrivia = list()
    breakfastTrivia.append(bre01)
    breakfastTrivia.append(bre02)
    breakfastTrivia.append(bre03)
    breakfastTrivia.append(bre04)
    breakfastTrivia.append(bre05)
    breakfastTrivia.append(bre06)
    breakfastTrivia.append(bre07)
    breakfastTrivia.append(bre08)
    breakfastTrivia.append(bre09)
    breakfastTrivia.append(bre10)
    breakfastTrivia.append(bre11)
    breakfastTrivia.append(bre12)
    breakfastTrivia.append(bre13)
    breakfastTrivia.append(bre14)
    breakfastTrivia.append(bre15)
                              
    # ----------------------------
    # Trivias para LUNCH
    # ----------------------------
    lunchTrivia = list()
    lunchTrivia.append(lun01)
    lunchTrivia.append(lun02)
    lunchTrivia.append(lun03)
    lunchTrivia.append(lun04)
    lunchTrivia.append(lun05)
    lunchTrivia.append(lun06)
    lunchTrivia.append(lun07)
    lunchTrivia.append(lun08)
    lunchTrivia.append(lun09)
    lunchTrivia.append(lun10)
    lunchTrivia.append(lun11)
    lunchTrivia.append(lun12)
    lunchTrivia.append(lun13)
    lunchTrivia.append(lun14)
    lunchTrivia.append(lun15)
    lunchTrivia.append(lun16)
    lunchTrivia.append(lun17)
    lunchTrivia.append(lun18)
    lunchTrivia.append(lun19)
    lunchTrivia.append(lun20)
                
    # ----------------------------
    # Trivias para DINNER
    # ----------------------------
    dinnerTrivia = list()
    dinnerTrivia.append(din01)
    dinnerTrivia.append(din02)
    dinnerTrivia.append(din03)
    dinnerTrivia.append(din04)
    dinnerTrivia.append(din05)
    dinnerTrivia.append(din06)
    dinnerTrivia.append(din07)
    dinnerTrivia.append(din08)
    dinnerTrivia.append(din09)
    dinnerTrivia.append(din10)
    dinnerTrivia.append(din11)
    dinnerTrivia.append(din12)
    dinnerTrivia.append(din13)
    dinnerTrivia.append(din14)
    dinnerTrivia.append(din15)
    dinnerTrivia.append(din16)
    dinnerTrivia.append(din17)
    dinnerTrivia.append(din18)
    dinnerTrivia.append(din19)
    dinnerTrivia.append(din20)
        
    # ----------------------------
    # Trivias para REFRESHMENT
    # ----------------------------
    refreshmentTrivia = list()
    refreshmentTrivia.append(ref01)
    refreshmentTrivia.append(ref02)
    refreshmentTrivia.append(ref03)
    refreshmentTrivia.append(ref04)
    refreshmentTrivia.append(ref05)
    refreshmentTrivia.append(ref06)
    refreshmentTrivia.append(ref07)
    refreshmentTrivia.append(ref08)
    refreshmentTrivia.append(ref09)
    refreshmentTrivia.append(ref10)
    refreshmentTrivia.append(ref11)
    refreshmentTrivia.append(ref12)
    refreshmentTrivia.append(ref13)
    refreshmentTrivia.append(ref14)
    refreshmentTrivia.append(ref15)
    refreshmentTrivia.append(ref16)
    refreshmentTrivia.append(ref17)
    refreshmentTrivia.append(ref18)
    refreshmentTrivia.append(ref19)
    refreshmentTrivia.append(ref20)
    

class Label:
 
    def __init__(self, text, fontAndSize, color, positionXY):
        self.text = text
        self.__font = fontAndSize
        self.__color = color
        self.__positionXY = positionXY
 
    def doPaint(self, displaySurface):
        if self.text != "":
            renderedText = self.__font.render(self.text, 1, self.__color)
            displaySurface.blit(renderedText, (self.__positionXY[0], self.__positionXY[1]))

    def setText(self, newText):
        self.text = newText
        
    def setColor(self, newColor):
        self.__color = newColor
        
    def setPosition(self, positionXY):
        self.__positionXY = positionXY
        
    def getPosition(self):
        return self.__positionXY
        
    def addChar(self, charToAdd):
        self.text = self.text + charToAdd
        
    def delLastChar(self):
        if len(self.text) > 0:
            self.text = self.text[:len(self.text) - 1]        
        
    def getTextLen(self):
        return len(self.text)
    
    def getTextRenderLen(self):
        return self.__font.size(self.text)[0]
