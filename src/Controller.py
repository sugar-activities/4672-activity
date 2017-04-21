#!/usr/bin/python
# -*- coding: latin-1 -*-

"""
Rigoberto Sáenz Imbacuán
Desarrollador para Dispositivos Móviles - Colombia Games
Ingeniero de Sistemas y Computación - Universidad Nacional de Colombia
http://www.rigobertosaenz.com/
"""
import pygame
import threading
import urllib


class eScreen:
    SPLASH_START = 1
    LOGIN = 2
    REGISTRATION = 3
    SELECT_TUTORIAL = 4
    SELECT_GENDER = 5
    SPLASH_INTER = 6
    RESTAURANT = 7
    SPLASH_CLOSE = 8
    
class eLeafUserId:
    MAIN_USER = 0
    PARENTS = 1
    UNCLE = 2
    BROTHER = 3
    COUSIN = 4
    FRIEND = 5

class eConnectionState:
    CONNECTING = 1
    SUCCESS = 2
    FAILURE = 3
    
class eConnectionMethod:
    POST = 1
    GET = 2

class eMusic:
    MIX = 1
    PICKING = 2
    QUIET = 3
    RESTAURANT = 4
    
class eSound:
    BELL = 1
    CLICK_INGREDIENT_SELECTION = 2
    COOKING_HOT = 3
    COOKING_COLD = 4
    FOOD_SERVED = 5
    FOOD_TIME_CHANGE = 6
    FRIDGE = 7
    INGREDIENT_DELETE = 8
    INGREDIENT_SELECT = 9
    INGREDIENTS_MAKE_RECIPE = 10
    LEVEL_PASSED = 11
    ORDER = 12
    PICK_DIRTY_DISH = 13
    WASHING = 14
    WASHING_DISHES = 15
    
    HELLO_BOY = 16
    HELLO_GIRL = 17
    LEVEL_WIN = 18
    YUJU_BOY = 19
    YUJU_GIRL = 20
    
class eQuestionAnswer:
    ANSWER_A = 1
    ANSWER_B = 2
    ANSWER_C = 3

class eTriviaQuestionId:
    BREAKFAST_01 = 1
    BREAKFAST_02 = 2
    BREAKFAST_03 = 3
    BREAKFAST_04 = 4
    BREAKFAST_05 = 5
    BREAKFAST_06 = 6
    BREAKFAST_07 = 7
    BREAKFAST_08 = 8
    BREAKFAST_09 = 9
    BREAKFAST_10 = 10
    BREAKFAST_11 = 11
    BREAKFAST_12 = 12
    BREAKFAST_13 = 13
    BREAKFAST_14 = 14
    BREAKFAST_15 = 15
    # ---------------
    LUNCH_01 = 16
    LUNCH_02 = 17
    LUNCH_03 = 18
    LUNCH_04 = 19
    LUNCH_05 = 20
    LUNCH_06 = 21
    LUNCH_07 = 22
    LUNCH_08 = 23
    LUNCH_09 = 24
    LUNCH_10 = 25
    LUNCH_11 = 26
    LUNCH_12 = 27
    LUNCH_13 = 28
    LUNCH_14 = 29
    LUNCH_15 = 30
    LUNCH_16 = 31
    LUNCH_17 = 32
    LUNCH_18 = 33
    LUNCH_19 = 34
    LUNCH_20 = 35
    # ---------------                   
    DINNER_01 = 36
    DINNER_02 = 37
    DINNER_03 = 38
    DINNER_04 = 39
    DINNER_05 = 40
    DINNER_06 = 41
    DINNER_07 = 42
    DINNER_08 = 43
    DINNER_09 = 44
    DINNER_10 = 45
    DINNER_11 = 46
    DINNER_12 = 47
    DINNER_13 = 48
    DINNER_14 = 49
    DINNER_15 = 50
    DINNER_16 = 51
    DINNER_17 = 52
    DINNER_18 = 53
    DINNER_19 = 54
    DINNER_20 = 55
    # ---------------
    REFRESHMENT_01 = 56
    REFRESHMENT_02 = 57
    REFRESHMENT_03 = 58
    REFRESHMENT_04 = 59
    REFRESHMENT_05 = 60
    REFRESHMENT_06 = 61
    REFRESHMENT_07 = 62
    REFRESHMENT_08 = 63
    REFRESHMENT_09 = 64
    REFRESHMENT_10 = 65
    REFRESHMENT_11 = 66
    REFRESHMENT_12 = 67
    REFRESHMENT_13 = 68
    REFRESHMENT_14 = 69
    REFRESHMENT_15 = 70
    REFRESHMENT_16 = 71
    REFRESHMENT_17 = 72
    REFRESHMENT_18 = 73
    REFRESHMENT_19 = 74
    REFRESHMENT_20 = 75
    
class eChefCommand:
    NO_COMMAND = 1
    # ---------------
    TAKE_ORDER = 2
    WASH_HANDS = 3
    SELECT_ORDER = 4
    # ---------------
    PICK_INGREDIENTS = 5
    WASH_INGREDIENTS = 6
    COOK_INGREDIENTS = 7
    # ---------------
    PICK_PREPARED_FOOD = 8
    SERVE_PREPARED_FOOD = 9
    # ---------------
    PICK_DIRTY_DISHES = 10
    WASH_DIRTY_DISHES = 11
    WASH_DIRTY_POTS = 12

class eChefMainState:
    NO_MOTION = 1
    MOVING = 2
    DOING_ORDER = 3

class eChefCookingState:
    NONE = 1
    COOKING = 2
    DISH_PREPARED_AND_READY_TO_SERVE = 3

class eChefLevel:
    LEVEL_0_NONE = 0
    LEVEL_1_JUNIOR = 1
    LEVEL_2_SENIOR = 2
    LEVEL_3_SUPER = 3

class eChefServiceState:
    READY = 1
    TAKING_AN_ORDER = 2
    CARRYING_DIRTY_INGREDIENTS = 3
    CARRYING_CLEAN_INGREDIENTS = 4
    CARRYING_PREPARED_FOOD = 5
    CARRYING_DIRTY_DISHES = 6

class eClientOrderState:
    NO_FOOD = 1
    DISH_FULL = 2
    DISH_EMPTY = 3
    DISH_DIRTY = 4

class eClientId:
    CLIENT_A_ROW2 = 1
    CLIENT_B_ROW2 = 2
    CLIENT_C_ROW2 = 3
    CLIENT_D_ROW2 = 4
    # ---------------
    CLIENT_E_ROW3 = 5
    CLIENT_F_ROW3 = 6
    CLIENT_G_ROW3 = 7
    CLIENT_H_ROW3 = 8

class eClientPerson:
    PERSON_A = 1
    PERSON_B = 2
    PERSON_C = 3
    PERSON_D = 4
    PERSON_E = 5

class eClientServiceState:
    NOT_IN_THE_RESTAURANT = 1
    GETTING_INTO_RESTAURANT = 2
    JUST_ARRIVED = 3
    READING_MENU = 4
    REQUESTING_FOR_ORDER = 5
    WAITING_FOR_FOOD = 6
    EATING = 7
    LEAVING = 8
    ONLY_DIRTY_DISHES_LEFT = 9

class eMotionDirection:
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4
    
class eMotionBlock:
    ROW1_STOVE = 1
    ROW1_SINK = 2
    ROW1_FRIDGE = 3
    ROW1_DISHWASHER = 4
    # ---------------
    ROW2_BLOCK_A = 5
    ROW2_BLOCK_B = 6
    ROW2_BLOCK_C = 7
    ROW2_BLOCK_D = 8
    # ---------------
    ROW2_INTERBLOCK_AB = 9
    ROW2_INTERBLOCK_BC = 10
    ROW2_INTERBLOCK_CD = 11
    # ---------------
    ROW3_BLOCK_E = 12
    ROW3_BLOCK_F = 13
    ROW3_BLOCK_G = 14
    ROW3_BLOCK_H = 15
    # ---------------
    ROW3_INTERBLOCK_EF = 16
    ROW3_INTERBLOCK_FG = 17
    ROW3_INTERBLOCK_GH = 18

class eMotionColumn:
    COLUMN_1 = 1
    COLUMN_2 = 2
    COLUMN_3 = 3
    COLUMN_4 = 4
    COLUMN_5 = 5
    COLUMN_6 = 6
    COLUMN_7 = 7

class eMotionRow:
    ROW_1 = 1
    ROW_2 = 2
    ROW_3 = 3
    
class eIngredientGroup:
    GROUP_1_CEREALES = 1
    GROUP_2_VERDURAS = 2
    GROUP_3_FRUTAS = 3
    GROUP_4_CARNES = 4
    GROUP_5_LACTEOS = 5
    GROUP_6_GRASAS = 6
    GROUP_7_AZUCARES = 7
    GROUP_8_OTROS = 8
    
class eIngredientsTab:
    INGREDIENTS = 1
    RECIPES = 2

class eIngredientId:
    # Grupo 1: Cereales, raices, tuberculos y platanos
    _01_AREPA = 1
    _02_ARROZ = 2
    _03_AVENA = 3
    _04_HARINA_DE_MAIZ_PRECOCIDA = 4
    _05_HARINA_DE_TRIGO = 5
    _06_MAIZ = 6
    _07_MIGA_DE_PAN = 7
    _08_PAN = 8
    _09_PAPA = 9
    _10_PASTA = 10
    _11_PLATANO = 11
    _12_SOYA = 12
    _13_YUCA = 13
    # Grupo 2: Hortalizas, verduras, leguminosas verdes                                                    
    _14_ACELGA = 14
    _15_AHUYAMA = 15
    _16_AJO = 16
    _17_APIO = 17
    _18_ARVEJA = 18
    _19_BROCOLI = 19
    _20_CEBOLLA_CABEZONA = 20
    _21_CEBOLLA_LARGA = 21
    _22_CILANTRO = 22
    _23_COLIFLOR = 23
    _24_ESPINACA = 24
    _25_FRIJOL = 25
    _26_GUASCAS = 26
    _27_HABICUELA = 27
    _28_LECHUGA = 28
    _29_PEPINO_COHOMBRO = 29
    _30_PEPINO_COMUN = 30
    _31_PIMENTON = 31
    _32_TOMATE = 32
    _33_ZANAHORIA = 33
    # Grupo 3: Frutas                                                                                       
    _34_AGUACATE = 34
    _35_BANANO = 35
    _36_CURUBA = 36
    _37_FRESA = 37
    _38_GUAYABA = 38
    _39_LIMON = 39
    _40_MANDARINA = 40
    _41_MANGO = 41
    _42_MANZANA_VERDE = 42
    _43_MANZANA_ROJA = 43
    _44_MARACUYA = 44
    _45_MELON = 45
    _46_MORA = 46
    _47_NARANJA = 47
    _48_PAPAYA = 48
    _49_PATILLA = 49
    _50_PERA = 50
    _51_PINA = 51
    # Grupo 4: Carne, visceras, pollo, pescado, huevo, leguminosas secas                                    
    _52_ATUN = 52
    _53_CARNE_DE_CERDO = 53
    _54_CARNE_DE_RES = 54
    _55_GARBANZO = 55
    _56_HIGADO = 56
    _57_HUEVO = 57
    _58_LENTEJA = 58
    _59_MENUDENCIAS = 59
    _60_PESCADO = 60
    _61_POLLO = 61
    _62_SALCHICHA = 62
    # Grupo 5: Lacteos                                                                                      
    _63_CREMA_DE_LECHE = 63
    _64_KUMIS = 64
    _65_LECHE = 65
    _66_QUESO = 66
    _67_YOGURT = 67
    # Grupo 6: Grasas                                                                                       
    _68_ACEITE = 68
    _69_MANTEQUILLA = 69
    _70_MARGARINA = 70
    # Grupo 7: Azucares                                                                                     
    _71_AZUCAR = 71
    _72_CHOCOLATE = 72
    _73_HELADO = 73
    _74_PANELA = 74
    # Grupo 8: Otros                                                                                        
    _75_AGUA = 75
    _76_MAYONESA = 76
    _77_MOSTAZA = 77
    _78_POLVO_DE_HONEAR = 78
    _79_SAL = 79
    _80_SALSA_DE_TOMATE = 80
    _81_SOPAS_EN_CREMA = 81
    _82_VINAGRETA_DULCE = 82
    
class eRecipeId:
    _01_ALBONDIGAS = 1
    _02_AREPA_RELLENA_CON_QUESO = 2
    _03_ARROZ_A_LA_SUEGRA = 3
    _04_ARROZ_CAMPESINO = 4
    _05_ARROZ_CON_MENUDENCIAS = 5                               
    _06_ARROZ_VEGETARIANO = 6                               
    _07_ARROZ_VERDE = 7                               
    _08_AVENA_EN_HOJUELAS = 8                               
    _09_BROCHETA_DE_FRUTAS = 9                               
    _10_CALDO_DE_PAPA_CON_COSTILLA = 10                               
    # ---------------                            
    _11_CHANGUA_DE_LECHE_CON_HUEVO = 11                               
    _12_CREMA_DE_CEBOLLA_CABEZONA = 12                               
    _13_CROQUETAS_DE_ESPINACA = 13                               
    _14_ENSALADA_ALBA_HIT = 14                               
    _15_ENSALADA_CARLOS = 15                               
    _16_ENSALADA_CRIOLLA = 16                               
    _17_ENSALADA_DE_COLORES = 17                               
    _18_ENSALADA_DE_FRUTAS_CON_YOGURT = 18                               
    _19_ENSALADA_DE_LA_CASA = 19                               
    _20_ENSALADA_DEL_HUERTO = 20                               
    # ---------------                            
    _21_ENSALADA_FRIA_DE_PAPA_CON_POLLO = 21                               
    _22_ENSALADA_RANCHERA = 22                               
    _23_GUARAPO_DE_PINA = 23                               
    _24_GUISO_DE_CARNE_Y_VERDURA = 24                               
    _25_GUISO_DE_HABICHUELA_CON_CARNE = 25                               
    _26_HAMBURGUESA = 26                               
    _27_HUEVO_TIBIO = 27                               
    _28_JUGO_DE_MARACUYA_Y_ZANAHORIA = 28                               
    _29_JUGO_DE_PAPAYA_CON_ZANAHORIA = 29                               
    _30_LOMO_DE_CERDO_EN_SALSA_DE_MANGO = 30                               
    # ---------------                            
    _31_LOMO_DE_CERDO_ENCHILADO = 31                               
    _32_MACARRONES_CON_ATUN = 32                               
    _33_PASTA_CON_VEGETALES = 33                               
    _34_PATACONES_CON_CARNE_DESMECHADA = 34                               
    _35_PEPINOS_RELLENOS = 35                               
    _36_PERRO_CALIENTE = 36                               
    _37_PESCADO_A_LA_PRIMAVERA = 37                               
    _38_PESCADO_ORIENTAL = 38                               
    _39_POLLO_A_LA_JARDINERA = 39                               
    _40_QUESO_DE_PINA = 40                               
    # ---------------                            
    _41_REFRESCO_DE_MANZANA = 41                               
    _42_SALCHIPAPAS = 42                               
    _43_SANDWICH_DE_JAMON_Y_QUESO = 43                               
    _44_SOPA_DE_GARBANZO = 44                               
    _45_SOPA_DE_LENTEJAS = 45                               
    _46_SOPA_DE_VERDURAS = 46                               
    _47_TE_DE_MANGO = 47                               
    _48_TERNERA_A_LA_MARINERA = 48                               
    _49_TOMATES_RELLENOS = 49                               
    _50_TORTA_DE_AHUYAMA = 50                               
    # ---------------                            
    _51_TORTA_DE_BANANO = 51                               
    _52_TORTA_DE_ZANAHORIA = 52                               
    _53_TORTILLAS_DE_ACELGAS = 53                               
    _54_TORTILLAS_DE_ESPINACA = 54                               
    _55_ZAFRESCO = 55
    _56_TORTILLA_DE_MAZORCA = 56
    _57_BATIDO_DE_GUAYABA_Y_AVENA = 57
    _58_BATIDO_DE_YOGURT_FRESAS_Y_AVENA = 58
    _59_PANQUEQUES_DE_AVENA = 59
    # ---------------
    _60_TORTILLA_DE_VERDURAS_Y_QUESO = 60
    _61_PANQUEQUES_DE_FRUTA = 61
    _62_AREPAS_DE_MAZORCA = 62

class eRecipePreparation:
    HOT = 1
    COLD = 2

class eRecipeFoodTime:
    BREAKFAST = 1
    REFRESHMENT_MORNING = 2
    LUNCH = 3
    REFRESHMENT_AFTERNOON = 4
    DINNER = 5

class eCharacterGender:
    MALE = 1
    FEMALE = 2

class eFoodState:
    RAW_AND_DIRTY = 1
    RAW_AND_CLEAN = 2
    PREPARED = 3
    
class eRestaurantState:
    RESTAURANT = 1
    ORDER_ASSIGNMENT = 2
    ORDER_SELECTION = 3
    RECIPE_MAKER = 4
    TRIVIA = 5

class ResourceController:
    
    # Audio folder
    music_Mix = "res/audio/Mix.ogg"
    music_Picking = "res/audio/Picking.ogg"
    music_Quiet = "res/audio/Quiet.ogg"
    music_Restaurant = "res/audio/Restaurant.ogg"
    
    # -> Sounds
    soundBell = None
    soundClickIngredientSelection = None
    soundCookingHot = None
    soundCookingCold = None
    soundFoodServed = None
    soundFoodTimeChange = None
    soundFridge = None
    soundIngredientDelete = None
    soundIngredientSelect = None
    soundIngredientsMakeRecipe = None
    soundOrder = None
    soundPickDirtyDish = None
    soundWashing = None
    soundWashingDishes = None
    
    soundHelloBoy = None
    soundHelloGirl = None
    soundLevelWin = None
    soundYujuBoy = None
    soundYujuGirl = None
    
    @staticmethod
    def doInit():
        
        # -> Sounds
        ResourceController.soundBell = pygame.mixer.Sound("res/audio/sounds/Bell.ogg")
        ResourceController.soundClickIngredientSelection = pygame.mixer.Sound("res/audio/sounds/ClickIngredientSelection.ogg")
        ResourceController.soundCookingHot = pygame.mixer.Sound("res/audio/sounds/CookingHot.ogg")
        ResourceController.soundCookingCold = pygame.mixer.Sound("res/audio/sounds/CookingCold.ogg")
        ResourceController.soundFoodServed = pygame.mixer.Sound("res/audio/sounds/FoodServed.ogg")
        ResourceController.soundFoodTimeChange = pygame.mixer.Sound("res/audio/sounds/FoodTimeChange.ogg")
        ResourceController.soundFridge = pygame.mixer.Sound("res/audio/sounds/Fridge.ogg")
        ResourceController.soundIngredientDelete = pygame.mixer.Sound("res/audio/sounds/IngredientDelete.ogg")
        ResourceController.soundIngredientSelect = pygame.mixer.Sound("res/audio/sounds/IngredientSelect.ogg")
        ResourceController.soundIngredientsMakeRecipe = pygame.mixer.Sound("res/audio/sounds/IngredientsMakeRecipe.ogg")
        ResourceController.soundLevelPassed = pygame.mixer.Sound("res/audio/sounds/LevelPassed.ogg")
        ResourceController.soundOrder = pygame.mixer.Sound("res/audio/sounds/Order.ogg")
        ResourceController.soundPickDirtyDish = pygame.mixer.Sound("res/audio/sounds/PickDirtyDish.ogg")
        ResourceController.soundWashing = pygame.mixer.Sound("res/audio/sounds/Washing.ogg")
        ResourceController.soundWashingDishes = pygame.mixer.Sound("res/audio/sounds/WashingDishes.ogg")
        
        ResourceController.soundHelloBoy = pygame.mixer.Sound("res/audio/sounds/cheers/HelloBoy.ogg")
        ResourceController.soundHelloGirl = pygame.mixer.Sound("res/audio/sounds/cheers/HelloGirl.ogg")
        ResourceController.soundLevelWin = pygame.mixer.Sound("res/audio/sounds/cheers/LevelWin.ogg")
        ResourceController.soundYujuBoy = pygame.mixer.Sound("res/audio/sounds/cheers/YujuBoy.ogg")
        ResourceController.soundYujuGirl = pygame.mixer.Sound("res/audio/sounds/cheers/YujuGirl.ogg")
    
        ResourceController.soundBell.set_volume(1.0)
        ResourceController.soundClickIngredientSelection.set_volume(1.0)
        ResourceController.soundCookingHot.set_volume(0.15)
        ResourceController.soundCookingCold.set_volume(0.5)
        ResourceController.soundFoodServed.set_volume(1.0)
        ResourceController.soundFoodTimeChange.set_volume(1.0)
        ResourceController.soundFridge.set_volume(1.0)
        ResourceController.soundIngredientDelete.set_volume(1.0)
        ResourceController.soundIngredientSelect.set_volume(1.0)
        ResourceController.soundIngredientsMakeRecipe.set_volume(1.0)
        ResourceController.soundLevelPassed.set_volume(1.0)
        ResourceController.soundOrder.set_volume(1.0)
        ResourceController.soundPickDirtyDish.set_volume(1.0)
        ResourceController.soundWashing.set_volume(1.0)
        ResourceController.soundWashingDishes.set_volume(1.0)
        
        ResourceController.soundHelloBoy.set_volume(1.0)
        ResourceController.soundHelloGirl.set_volume(1.0)
        ResourceController.soundLevelWin.set_volume(1.0)
        ResourceController.soundYujuBoy.set_volume(1.0)
        ResourceController.soundYujuGirl.set_volume(1.0)
        
        # LLamado a funcion convert() y convert_alpha() para aumento de velocidad

        # Background folder
        ResourceController.background_Answer.convert_alpha() #pygame.image.load("res/background/Answer.png")
        ResourceController.background_IngredientInfo.convert_alpha() #pygame.image.load("res/background/IngredientInfo.png")
        ResourceController.background_Kitchen.convert() #pygame.image.load("res/background/Kitchen.png")
        ResourceController.background_Login.convert_alpha() #pygame.image.load("res/background/Login.png")
        ResourceController.background_PickIngredients.convert_alpha() #pygame.image.load("res/background/PickIngredients.png")
        ResourceController.background_RecipeAssign.convert_alpha() #pygame.image.load("res/background/RecipeAssign.png")
        ResourceController.background_Recipes.convert_alpha() #pygame.image.load("res/background/Recipes.png")
        ResourceController.background_Registration.convert_alpha() #pygame.image.load("res/background/Registration.png")
        ResourceController.background_SelectGender.convert_alpha() #pygame.image.load("res/background/SelectGender.png")
        ResourceController.background_SelectOrder.convert_alpha() #pygame.image.load("res/background/SelectOrder.png")
        ResourceController.background_Splash_1.convert() #pygame.image.load("res/background/Splash_1.png")
        ResourceController.background_Splash_2.convert() #pygame.image.load("res/background/Splash_2.png")
        ResourceController.background_Splash_3.convert() #pygame.image.load("res/background/Splash_3.png")
        ResourceController.background_Splash_4.convert() #pygame.image.load("res/background/Splash_4.png")
        ResourceController.background_Splash_5.convert() #pygame.image.load("res/background/Splash_5.png")
        ResourceController.background_Transparent.convert_alpha() #pygame.image.load("res/background/Transparent.png")
        
        # Input folder
        ResourceController.input_Accept_Off.convert_alpha() #pygame.image.load("res/input/Accept_Off.png")
        ResourceController.input_Accept_On.convert_alpha() #pygame.image.load("res/input/Accept_On.png")
        ResourceController.input_ArrowLeft.convert_alpha() #pygame.image.load("res/input/ArrowLeft.png")
        ResourceController.input_ArrowRight.convert_alpha() #pygame.image.load("res/input/ArrowRight.png")
        ResourceController.input_AssignSelector.convert_alpha() #pygame.image.load("res/input/AssignSelector.png")
        ResourceController.input_Back1Cereales.convert_alpha() #pygame.image.load("res/input/Back1Cereales.png")
        ResourceController.input_Back2Verduras.convert_alpha() #pygame.image.load("res/input/Back2Verduras.png")
        ResourceController.input_Back3Frutas.convert_alpha() #pygame.image.load("res/input/Back3Frutas.png")
        ResourceController.input_Back4Carnes.convert_alpha() #pygame.image.load("res/input/Back4Carnes.png") 
        ResourceController.input_Back5Lacteos.convert_alpha() #pygame.image.load("res/input/Back5Lacteos.png")
        ResourceController.input_Back6Grasas.convert_alpha() #pygame.image.load("res/input/Back6Grasas.png")
        ResourceController.input_Back7Azucares.convert_alpha() #pygame.image.load("res/input/Back7Azucares.png")
        ResourceController.input_Back8Otros.convert_alpha() #pygame.image.load("res/input/Back8Otros.png")
        ResourceController.input_Button1Cereales.convert_alpha() #pygame.image.load("res/input/Button1Cereales.png")
        ResourceController.input_Button2Verduras.convert_alpha() #pygame.image.load("res/input/Button2Verduras.png")
        ResourceController.input_Button3Frutas.convert_alpha() #pygame.image.load("res/input/Button3Frutas.png")
        ResourceController.input_Button4Carnes.convert_alpha() #pygame.image.load("res/input/Button4Carnes.png")
        ResourceController.input_Button5Lacteos.convert_alpha() #pygame.image.load("res/input/Button5Lacteos.png")
        ResourceController.input_Button6Grasas.convert_alpha() #pygame.image.load("res/input/Button6Grasas.png")
        ResourceController.input_Button7Azucares.convert_alpha() #pygame.image.load("res/input/Button7Azucares.png")
        ResourceController.input_Button8Otros.convert_alpha() #pygame.image.load("res/input/Button8Otros.png")
        ResourceController.input_Cancel_Off.convert_alpha() #pygame.image.load("res/input/Cancel_Off.png")
        ResourceController.input_Cancel_On.convert_alpha() #pygame.image.load("res/input/Cancel_On.png")
        ResourceController.input_CloseGame_Off.convert_alpha() #pygame.image.load("res/input/CloseGame_Off.png")
        ResourceController.input_CloseGame_On.convert_alpha() #pygame.image.load("res/input/CloseGame_On.png")
        ResourceController.input_Connecting.convert_alpha() #pygame.image.load("res/input/Connecting.png")
        ResourceController.input_Cross.convert_alpha() #pygame.image.load("res/input/Cross.png")
        ResourceController.input_GenderFemale_On.convert_alpha() #pygame.image.load("res/input/GenderFemale_On.png")
        ResourceController.input_GenderFemale_Off.convert_alpha() #pygame.image.load("res/input/GenderFemale_Off.png")
        ResourceController.input_GenderMale_On.convert_alpha() #pygame.image.load("res/input/GenderMale_On.png")
        ResourceController.input_GenderMale_Off.convert_alpha() #pygame.image.load("res/input/GenderMale_Off.png")
        ResourceController.input_Login_Off.convert_alpha() #pygame.image.load("res/input/Login_Off.png")
        ResourceController.input_Login_On.convert_alpha() #pygame.image.load("res/input/Login_On.png")
        ResourceController.input_LoginBrother.convert_alpha() #pygame.image.load("res/input/LoginBrother.png")
        ResourceController.input_LoginCousin.convert_alpha() #pygame.image.load("res/input/LoginCousin.png")
        ResourceController.input_LoginFriend.convert_alpha() #pygame.image.load("res/input/LoginFriend.png")
        ResourceController.input_LoginInput.convert_alpha() #pygame.image.load("res/input/LoginInput.png")
        ResourceController.input_LoginMainUser.convert_alpha() #pygame.image.load("res/input/LoginMainUser.png")
        ResourceController.input_LoginParent.convert_alpha() #pygame.image.load("res/input/LoginParent.png")
        ResourceController.input_LoginUncle.convert_alpha() #pygame.image.load("res/input/LoginUncle.png")
        ResourceController.input_OrderSelector.convert_alpha() #pygame.image.load("res/input/OrderSelector.png")
        ResourceController.input_ReadyDish_On.convert_alpha() #pygame.image.load("res/input/ReadyDish_On.png")
        ResourceController.input_ReadyDish_Off.convert_alpha() #pygame.image.load("res/input/ReadyDish_Off.png")
        ResourceController.input_RecipeIndex.convert_alpha() #pygame.image.load("res/input/RecipeIndex.png")
        ResourceController.input_Registration_On.convert_alpha() #pygame.image.load("res/input/Registration_On.png")
        ResourceController.input_Registration_Off.convert_alpha() #pygame.image.load("res/input/Registration_Off.png")
        ResourceController.input_TabIngredients_On.convert_alpha() #pygame.image.load("res/input/TabIngredients_On.png")
        ResourceController.input_TabIngredients_Off.convert_alpha() #pygame.image.load("res/input/TabIngredients_Off.png")
        ResourceController.input_TabRecipes_On.convert_alpha() #pygame.image.load("res/input/TabRecipes_On.png")
        ResourceController.input_TabRecipes_Off.convert_alpha() #pygame.image.load("res/input/TabRecipes_Off.png")
        ResourceController.input_TriviaOption_Off.convert_alpha() #pygame.image.load("res/input/TriviaOption_Off.png")
        ResourceController.input_TriviaOption_On.convert_alpha() #pygame.image.load("res/input/TriviaOption_On.png")
        ResourceController.input_TutorialNo_Off.convert_alpha() #pygame.image.load("res/input/TutorialNo_Off.png")
        ResourceController.input_TutorialNo_On.convert_alpha() #pygame.image.load("res/input/TutorialNo_On.png")
        ResourceController.input_TutorialYes_Off.convert_alpha() #pygame.image.load("res/input/TutorialYes_Off.png")
        ResourceController.input_TutorialYes_On.convert_alpha() #pygame.image.load("res/input/TutorialYes_On.png")
        
        # Game folder
        ResourceController.game_BannerBreakfast_1.convert_alpha() #pygame.image.load("res/game/BannerBreakfast_1.png")
        ResourceController.game_BannerBreakfast_2.convert_alpha() #pygame.image.load("res/game/BannerBreakfast_2.png")
        ResourceController.game_BannerDinner_1.convert_alpha() #pygame.image.load("res/game/BannerDinner_1.png")
        ResourceController.game_BannerDinner_2.convert_alpha() #pygame.image.load("res/game/BannerDinner_2.png")
        ResourceController.game_BannerLunch_1.convert_alpha() #pygame.image.load("res/game/BannerLunch_1.png")
        ResourceController.game_BannerLunch_2.convert_alpha() #pygame.image.load("res/game/BannerLunch_2.png")
        ResourceController.game_BannerRefreshmentAfternoon_1.convert_alpha() #pygame.image.load("res/game/BannerRefreshmentAfternoon_1.png")
        ResourceController.game_BannerRefreshmentAfternoon_2.convert_alpha() #pygame.image.load("res/game/BannerRefreshmentAfternoon_2.png")
        ResourceController.game_BannerRefreshmentMorning_1.convert_alpha() #pygame.image.load("res/game/BannerRefreshmentMorning_1.png")
        ResourceController.game_BannerRefreshmentMorning_2.convert_alpha() #pygame.image.load("res/game/BannerRefreshmentMorning_2.png")
        ResourceController.game_Chair.convert_alpha() #pygame.image.load("res/game/Chair.png")
        ResourceController.game_ChefHatBronze.convert_alpha() #pygame.image.load("res/game/ChefHatBronze.png")
        ResourceController.game_ChefHatGold.convert_alpha() #pygame.image.load("res/game/ChefHatGold.png")
        ResourceController.game_ChefHatSilver.convert_alpha() #pygame.image.load("res/game/ChefHatSilver.png")
        ResourceController.game_ChefHatMiniNone.convert_alpha() #pygame.image.load("res/game/ChefHatMiniNone.png")
        ResourceController.game_ChefHatMiniBronze.convert_alpha() #pygame.image.load("res/game/ChefHatMiniBronze.png")
        ResourceController.game_ChefHatMiniGold.convert_alpha() #pygame.image.load("res/game/ChefHatMiniGold.png")
        ResourceController.game_ChefHatMiniSilver.convert_alpha() #pygame.image.load("res/game/ChefHatMiniSilver.png")
        ResourceController.game_ChefLevel1.convert_alpha() #pygame.image.load("res/game/ChefLevel1.png")
        ResourceController.game_ChefLevel2.convert_alpha() #pygame.image.load("res/game/ChefLevel2.png")
        ResourceController.game_ChefLevel3.convert_alpha() #pygame.image.load("res/game/ChefLevel3.png")
        ResourceController.game_ChefNewLevel.convert_alpha() #pygame.image.load("res/game/ChefNewLevel.png")
        ResourceController.game_Cloud.convert_alpha() #pygame.image.load("res/game/Cloud.png")
        ResourceController.game_CookingCold_1.convert_alpha() #pygame.image.load("res/game/CookingCold_1.png")
        ResourceController.game_CookingCold_2.convert_alpha() #pygame.image.load("res/game/CookingCold_2.png")
        ResourceController.game_CookingCold_3.convert_alpha() #pygame.image.load("res/game/CookingCold_3.png")
        ResourceController.game_CookingCold_4.convert_alpha() #pygame.image.load("res/game/CookingCold_4.png")
        ResourceController.game_CookingHot_1.convert_alpha() #pygame.image.load("res/game/CookingHot_1.png")
        ResourceController.game_CookingHot_2.convert_alpha() #pygame.image.load("res/game/CookingHot_2.png")
        ResourceController.game_CookingHot_3.convert_alpha() #pygame.image.load("res/game/CookingHot_3.png")
        ResourceController.game_CookingHot_4.convert_alpha() #pygame.image.load("res/game/CookingHot_4.png")
        ResourceController.game_DishDirty_1.convert_alpha() #pygame.image.load("res/game/DishDirty_1.png")
        ResourceController.game_DishDirty_2.convert_alpha() #pygame.image.load("res/game/DishDirty_2.png")
        ResourceController.game_DishEmpty.convert_alpha() #pygame.image.load("res/game/DishEmpty.png")
        ResourceController.game_DishFull.convert_alpha() #pygame.image.load("res/game/DishFull.png")
        ResourceController.game_DishFullBase.convert_alpha() #pygame.image.load("res/game/DishFullBase.png")
        ResourceController.game_IngredientSpace.convert_alpha() #pygame.image.load("res/game/IngredientSpace.png")
        ResourceController.game_Letter.convert_alpha() #pygame.image.load("res/game/Letter.png")
        ResourceController.game_MessageBackground_Female.convert_alpha() #pygame.image.load("res/game/MessageBackground_Female.png")
        ResourceController.game_MessageBackground_Male.convert_alpha() #pygame.image.load("res/game/MessageBackground_Male.png")
        ResourceController.game_Star.convert_alpha() #pygame.image.load("res/game/Star.png")
        ResourceController.game_StarsBackground.convert_alpha() #pygame.image.load("res/game/StarsBackground.png")
        ResourceController.game_Table.convert_alpha() #pygame.image.load("res/game/Table.png")
        ResourceController.game_TriviaText.convert_alpha() #pygame.image.load("res/game/TriviaText.png")
        ResourceController.game_TriviaTitle.convert_alpha() #pygame.image.load("res/game/TriviaTitle.png")
        ResourceController.game_TutorialStepA.convert_alpha() #pygame.image.load("res/game/TutorialStepA.png")
        ResourceController.game_TutorialStepB.convert_alpha() #pygame.image.load("res/game/TutorialStepB.png")
        ResourceController.game_TutorialStepC.convert_alpha() #pygame.image.load("res/game/TutorialStepC.png")
        ResourceController.game_TutorialStepD.convert_alpha() #pygame.image.load("res/game/TutorialStepD.png")
        ResourceController.game_TutorialStepE.convert_alpha() #pygame.image.load("res/game/TutorialStepE.png")
        ResourceController.game_TutorialStepF.convert_alpha() #pygame.image.load("res/game/TutorialStepF.png")
        ResourceController.game_TutorialStepG.convert_alpha() #pygame.image.load("res/game/TutorialStepG.png")
        ResourceController.game_TutorialStepH.convert_alpha() #pygame.image.load("res/game/TutorialStepH.png")
        ResourceController.game_TutorialStepI.convert_alpha() #pygame.image.load("res/game/TutorialStepI.png")
        ResourceController.game_TutorialStepJ.convert_alpha() #pygame.image.load("res/game/TutorialStepJ.png")
        ResourceController.game_TutorialStepK.convert_alpha() #pygame.image.load("res/game/TutorialStepK.png")
        ResourceController.game_TutorialStepL.convert_alpha() #pygame.image.load("res/game/TutorialStepL.png")
        ResourceController.game_TutorialStepM.convert_alpha() #pygame.image.load("res/game/TutorialStepM.png")
        ResourceController.game_TutorialStepN.convert_alpha() #pygame.image.load("res/game/TutorialStepN.png")
        ResourceController.game_TutorialStepO.convert_alpha() #pygame.image.load("res/game/TutorialStepO.png")
        ResourceController.game_TutorialStepP.convert_alpha() #pygame.image.load("res/game/TutorialStepP.png")
        ResourceController.game_TutorialWelcome.convert_alpha() #pygame.image.load("res/game/TutorialWelcome.png")
        ResourceController.game_WashingDishes_1.convert_alpha() #pygame.image.load("res/game/WashingDishes_1.png")
        ResourceController.game_WashingDishes_2.convert_alpha() #pygame.image.load("res/game/WashingDishes_2.png")
        ResourceController.game_WashingHands_1.convert_alpha() #pygame.image.load("res/game/WashingHands_1.png")
        ResourceController.game_WashingHands_2.convert_alpha() #pygame.image.load("res/game/WashingHands_2.png")
        ResourceController.game_WashingIngredients_1.convert_alpha() #pygame.image.load("res/game/WashingIngredients_1.png")
        ResourceController.game_WashingIngredients_2.convert_alpha() #pygame.image.load("res/game/WashingIngredients_2.png")
        
        # -> Chef
        ResourceController.game_ChefFemaleLevel0_BackCarryingCleanIngredients.convert_alpha() #pygame.image.load("res/game/chef/female/level_0/Back_CarryingCleanIngredients.png")
        ResourceController.game_ChefFemaleLevel0_BackCarryingDirtyDishes.convert_alpha() #pygame.image.load("res/game/chef/female/level_0/Back_CarryingDirtyDishes.png")
        ResourceController.game_ChefFemaleLevel0_BackCarryingDirtyIngredients.convert_alpha() #pygame.image.load("res/game/chef/female/level_0/Back_CarryingDirtyIngredients.png")
        ResourceController.game_ChefFemaleLevel0_BackCarryingPreparedFood.convert_alpha() #pygame.image.load("res/game/chef/female/level_0/Back_CarryingPreparedFood.png")
        ResourceController.game_ChefFemaleLevel0_BackReady.convert_alpha() #pygame.image.load("res/game/chef/female/level_0/Back_Ready.png")
        ResourceController.game_ChefFemaleLevel0_BackTakingAnOrder.convert_alpha() #pygame.image.load("res/game/chef/female/level_0/Back_TakingAnOrder.png")
        
        ResourceController.game_ChefFemaleLevel0_FrontCarryingCleanIngredients.convert_alpha() #pygame.image.load("res/game/chef/female/level_0/Front_CarryingCleanIngredients.png")
        ResourceController.game_ChefFemaleLevel0_FrontCarryingDirtyDishes.convert_alpha() #pygame.image.load("res/game/chef/female/level_0/Front_CarryingDirtyDishes.png")
        ResourceController.game_ChefFemaleLevel0_FrontCarryingDirtyIngredients.convert_alpha() #pygame.image.load("res/game/chef/female/level_0/Front_CarryingDirtyIngredients.png")
        ResourceController.game_ChefFemaleLevel0_FrontCarryingPreparedFood.convert_alpha() #pygame.image.load("res/game/chef/female/level_0/Front_CarryingPreparedFood.png")
        ResourceController.game_ChefFemaleLevel0_FrontReady.convert_alpha() #pygame.image.load("res/game/chef/female/level_0/Front_Ready.png")
        ResourceController.game_ChefFemaleLevel0_FrontTakingAnOrder.convert_alpha() #pygame.image.load("res/game/chef/female/level_0/Front_TakingAnOrder.png")
        
        ResourceController.game_ChefFemaleLevel0_LeftCarryingCleanIngredients.convert_alpha() #pygame.image.load("res/game/chef/female/level_0/Left_CarryingCleanIngredients.png")
        ResourceController.game_ChefFemaleLevel0_LeftCarryingDirtyDishes.convert_alpha() #pygame.image.load("res/game/chef/female/level_0/Left_CarryingDirtyDishes.png")
        ResourceController.game_ChefFemaleLevel0_LeftCarryingDirtyIngredients.convert_alpha() #pygame.image.load("res/game/chef/female/level_0/Left_CarryingDirtyIngredients.png")
        ResourceController.game_ChefFemaleLevel0_LeftCarryingPreparedFood.convert_alpha() #pygame.image.load("res/game/chef/female/level_0/Left_CarryingPreparedFood.png")
        ResourceController.game_ChefFemaleLevel0_LeftReady.convert_alpha() #pygame.image.load("res/game/chef/female/level_0/Left_Ready.png")
        ResourceController.game_ChefFemaleLevel0_LeftTakingAnOrder.convert_alpha() #pygame.image.load("res/game/chef/female/level_0/Left_TakingAnOrder.png")
        
        ResourceController.game_ChefFemaleLevel0_RightCarryingCleanIngredients.convert_alpha() #pygame.image.load("res/game/chef/female/level_0/Right_CarryingCleanIngredients.png")
        ResourceController.game_ChefFemaleLevel0_RightCarryingDirtyDishes.convert_alpha() #pygame.image.load("res/game/chef/female/level_0/Right_CarryingDirtyDishes.png")
        ResourceController.game_ChefFemaleLevel0_RightCarryingDirtyIngredients.convert_alpha() #pygame.image.load("res/game/chef/female/level_0/Right_CarryingDirtyIngredients.png")
        ResourceController.game_ChefFemaleLevel0_RightCarryingPreparedFood.convert_alpha() #pygame.image.load("res/game/chef/female/level_0/Right_CarryingPreparedFood.png")
        ResourceController.game_ChefFemaleLevel0_RightReady.convert_alpha() #pygame.image.load("res/game/chef/female/level_0/Right_Ready.png")
        ResourceController.game_ChefFemaleLevel0_RightTakingAnOrder.convert_alpha() #pygame.image.load("res/game/chef/female/level_0/Right_TakingAnOrder.png")
        
        ResourceController.game_ChefMaleLevel0_BackCarryingCleanIngredients.convert_alpha() #pygame.image.load("res/game/chef/male/level_0/Back_CarryingCleanIngredients.png")
        ResourceController.game_ChefMaleLevel0_BackCarryingDirtyDishes.convert_alpha() #pygame.image.load("res/game/chef/male/level_0/Back_CarryingDirtyDishes.png")
        ResourceController.game_ChefMaleLevel0_BackCarryingDirtyIngredients.convert_alpha() #pygame.image.load("res/game/chef/male/level_0/Back_CarryingDirtyIngredients.png")
        ResourceController.game_ChefMaleLevel0_BackCarryingPreparedFood.convert_alpha() #pygame.image.load("res/game/chef/male/level_0/Back_CarryingPreparedFood.png")
        ResourceController.game_ChefMaleLevel0_BackReady.convert_alpha() #pygame.image.load("res/game/chef/male/level_0/Back_Ready.png")
        ResourceController.game_ChefMaleLevel0_BackTakingAnOrder.convert_alpha() #pygame.image.load("res/game/chef/male/level_0/Back_TakingAnOrder.png")
                                                                                       
        ResourceController.game_ChefMaleLevel0_FrontCarryingCleanIngredients.convert_alpha() #pygame.image.load("res/game/chef/male/level_0/Front_CarryingCleanIngredients.png")
        ResourceController.game_ChefMaleLevel0_FrontCarryingDirtyDishes.convert_alpha() #pygame.image.load("res/game/chef/male/level_0/Front_CarryingDirtyDishes.png")
        ResourceController.game_ChefMaleLevel0_FrontCarryingDirtyIngredients.convert_alpha() #pygame.image.load("res/game/chef/male/level_0/Front_CarryingDirtyIngredients.png")
        ResourceController.game_ChefMaleLevel0_FrontCarryingPreparedFood.convert_alpha() #pygame.image.load("res/game/chef/male/level_0/Front_CarryingPreparedFood.png")
        ResourceController.game_ChefMaleLevel0_FrontReady.convert_alpha() #pygame.image.load("res/game/chef/male/level_0/Front_Ready.png")
        ResourceController.game_ChefMaleLevel0_FrontTakingAnOrder.convert_alpha() #pygame.image.load("res/game/chef/male/level_0/Front_TakingAnOrder.png")
                                                                                       
        ResourceController.game_ChefMaleLevel0_LeftCarryingCleanIngredients.convert_alpha() #pygame.image.load("res/game/chef/male/level_0/Left_CarryingCleanIngredients.png")
        ResourceController.game_ChefMaleLevel0_LeftCarryingDirtyDishes.convert_alpha() #pygame.image.load("res/game/chef/male/level_0/Left_CarryingDirtyDishes.png")
        ResourceController.game_ChefMaleLevel0_LeftCarryingDirtyIngredients.convert_alpha() #pygame.image.load("res/game/chef/male/level_0/Left_CarryingDirtyIngredients.png")
        ResourceController.game_ChefMaleLevel0_LeftCarryingPreparedFood.convert_alpha() #pygame.image.load("res/game/chef/male/level_0/Left_CarryingPreparedFood.png")
        ResourceController.game_ChefMaleLevel0_LeftReady.convert_alpha() #pygame.image.load("res/game/chef/male/level_0/Left_Ready.png")
        ResourceController.game_ChefMaleLevel0_LeftTakingAnOrder.convert_alpha() #pygame.image.load("res/game/chef/male/level_0/Left_TakingAnOrder.png")
                                                                                       
        ResourceController.game_ChefMaleLevel0_RightCarryingCleanIngredients.convert_alpha() #pygame.image.load("res/game/chef/male/level_0/Right_CarryingCleanIngredients.png")
        ResourceController.game_ChefMaleLevel0_RightCarryingDirtyDishes.convert_alpha() #pygame.image.load("res/game/chef/male/level_0/Right_CarryingDirtyDishes.png")
        ResourceController.game_ChefMaleLevel0_RightCarryingDirtyIngredients.convert_alpha() #pygame.image.load("res/game/chef/male/level_0/Right_CarryingDirtyIngredients.png")
        ResourceController.game_ChefMaleLevel0_RightCarryingPreparedFood.convert_alpha() #pygame.image.load("res/game/chef/male/level_0/Right_CarryingPreparedFood.png")
        ResourceController.game_ChefMaleLevel0_RightReady.convert_alpha() #pygame.image.load("res/game/chef/male/level_0/Right_Ready.png")
        ResourceController.game_ChefMaleLevel0_RightTakingAnOrder.convert_alpha() #pygame.image.load("res/game/chef/male/level_0/Right_TakingAnOrder.png")
        
        # -> Clients
        ResourceController.game_ClientAEating_1.convert_alpha() #pygame.image.load("res/game/clients/PersonA_Eating_1.png")
        ResourceController.game_ClientAEating_2.convert_alpha() #pygame.image.load("res/game/clients/PersonA_Eating_2.png")
        ResourceController.game_ClientAEating_3.convert_alpha() #pygame.image.load("res/game/clients/PersonA_Eating_3.png")
        ResourceController.game_ClientALooking.convert_alpha() #pygame.image.load("res/game/clients/PersonA_Looking.png")
        ResourceController.game_ClientAReadingMenu_1.convert_alpha() #pygame.image.load("res/game/clients/PersonA_ReadingMenu_1.png")
        ResourceController.game_ClientAReadingMenu_2.convert_alpha() #pygame.image.load("res/game/clients/PersonA_ReadingMenu_2.png")
        ResourceController.game_ClientARequesting.convert_alpha() #pygame.image.load("res/game/clients/PersonA_Requesting.png")
        ResourceController.game_ClientAWaitingForFood.convert_alpha() #pygame.image.load("res/game/clients/PersonA_WaitingForFood.png")
        
        ResourceController.game_ClientBEating_1.convert_alpha() #pygame.image.load("res/game/clients/PersonB_Eating_1.png")
        ResourceController.game_ClientBEating_2.convert_alpha() #pygame.image.load("res/game/clients/PersonB_Eating_2.png")
        ResourceController.game_ClientBEating_3.convert_alpha() #pygame.image.load("res/game/clients/PersonB_Eating_3.png")
        ResourceController.game_ClientBLooking.convert_alpha() #pygame.image.load("res/game/clients/PersonB_Looking.png")
        ResourceController.game_ClientBReadingMenu_1.convert_alpha() #pygame.image.load("res/game/clients/PersonB_ReadingMenu_1.png")
        ResourceController.game_ClientBReadingMenu_2.convert_alpha() #pygame.image.load("res/game/clients/PersonB_ReadingMenu_2.png")
        ResourceController.game_ClientBRequesting.convert_alpha() #pygame.image.load("res/game/clients/PersonB_Requesting.png")
        ResourceController.game_ClientBWaitingForFood.convert_alpha() #pygame.image.load("res/game/clients/PersonB_WaitingForFood.png")
        
        ResourceController.game_ClientCEating_1.convert_alpha() #pygame.image.load("res/game/clients/PersonC_Eating_1.png")
        ResourceController.game_ClientCEating_2.convert_alpha() #pygame.image.load("res/game/clients/PersonC_Eating_2.png")
        ResourceController.game_ClientCEating_3.convert_alpha() #pygame.image.load("res/game/clients/PersonC_Eating_3.png")
        ResourceController.game_ClientCLooking.convert_alpha() #pygame.image.load("res/game/clients/PersonC_Looking.png")
        ResourceController.game_ClientCReadingMenu_1.convert_alpha() #pygame.image.load("res/game/clients/PersonC_ReadingMenu_1.png")
        ResourceController.game_ClientCReadingMenu_2.convert_alpha() #pygame.image.load("res/game/clients/PersonC_ReadingMenu_2.png")
        ResourceController.game_ClientCRequesting.convert_alpha() #pygame.image.load("res/game/clients/PersonC_Requesting.png")
        ResourceController.game_ClientCWaitingForFood.convert_alpha() #pygame.image.load("res/game/clients/PersonC_WaitingForFood.png")
        
        ResourceController.game_ClientDEating_1.convert_alpha() #pygame.image.load("res/game/clients/PersonD_Eating_1.png")
        ResourceController.game_ClientDEating_2.convert_alpha() #pygame.image.load("res/game/clients/PersonD_Eating_2.png")
        ResourceController.game_ClientDEating_3.convert_alpha() #pygame.image.load("res/game/clients/PersonD_Eating_3.png")
        ResourceController.game_ClientDLooking.convert_alpha() #pygame.image.load("res/game/clients/PersonD_Looking.png")
        ResourceController.game_ClientDReadingMenu_1.convert_alpha() #pygame.image.load("res/game/clients/PersonD_ReadingMenu_1.png")
        ResourceController.game_ClientDReadingMenu_2.convert_alpha() #pygame.image.load("res/game/clients/PersonD_ReadingMenu_2.png")
        ResourceController.game_ClientDRequesting.convert_alpha() #pygame.image.load("res/game/clients/PersonD_Requesting.png")
        ResourceController.game_ClientDWaitingForFood.convert_alpha() #pygame.image.load("res/game/clients/PersonD_WaitingForFood.png")
        
        ResourceController.game_ClientEEating_1.convert_alpha() #pygame.image.load("res/game/clients/PersonE_Eating_1.png")
        ResourceController.game_ClientEEating_2.convert_alpha() #pygame.image.load("res/game/clients/PersonE_Eating_2.png")
        ResourceController.game_ClientEEating_3.convert_alpha() #pygame.image.load("res/game/clients/PersonE_Eating_3.png")
        ResourceController.game_ClientELooking.convert_alpha() #pygame.image.load("res/game/clients/PersonE_Looking.png")
        ResourceController.game_ClientEReadingMenu_1.convert_alpha() #pygame.image.load("res/game/clients/PersonE_ReadingMenu_1.png")
        ResourceController.game_ClientEReadingMenu_2.convert_alpha() #pygame.image.load("res/game/clients/PersonE_ReadingMenu_2.png")
        ResourceController.game_ClientERequesting.convert_alpha() #pygame.image.load("res/game/clients/PersonE_Requesting.png")
        ResourceController.game_ClientEWaitingForFood.convert_alpha() #pygame.image.load("res/game/clients/PersonE_WaitingForFood.png")
        
        # -> Ingredients
        ResourceController.game_Ingredient01Arepa.convert_alpha() #pygame.image.load("res/game/ingredients/01Arepa.png")
        ResourceController.game_Ingredient02Arroz.convert_alpha() #pygame.image.load("res/game/ingredients/02Arroz.png")
        ResourceController.game_Ingredient03Avena.convert_alpha() #pygame.image.load("res/game/ingredients/03Avena.png")
        ResourceController.game_Ingredient04HarinaDeMaizPrecocida.convert_alpha() #pygame.image.load("res/game/ingredients/04HarinaDeMaizPrecocida.png")
        ResourceController.game_Ingredient05HarinaDeTrigo.convert_alpha() #pygame.image.load("res/game/ingredients/05HarinaDeTrigo.png")
        ResourceController.game_Ingredient06Maiz.convert_alpha() #pygame.image.load("res/game/ingredients/06Maiz.png")
        ResourceController.game_Ingredient07MigaDePan.convert_alpha() #pygame.image.load("res/game/ingredients/07MigaDePan.png")
        ResourceController.game_Ingredient08Pan.convert_alpha() #pygame.image.load("res/game/ingredients/08Pan.png")
        ResourceController.game_Ingredient09Papa.convert_alpha() #pygame.image.load("res/game/ingredients/09Papa.png")
        ResourceController.game_Ingredient10Pasta.convert_alpha() #pygame.image.load("res/game/ingredients/10Pasta.png")
        ResourceController.game_Ingredient11Platano.convert_alpha() #pygame.image.load("res/game/ingredients/11Platano.png")
        ResourceController.game_Ingredient12Soya.convert_alpha() #pygame.image.load("res/game/ingredients/12Soya.png")
        ResourceController.game_Ingredient13Yuca.convert_alpha() #pygame.image.load("res/game/ingredients/13Yuca.png")
        ResourceController.game_Ingredient14Acelga.convert_alpha() #pygame.image.load("res/game/ingredients/14Acelga.png")
        ResourceController.game_Ingredient15Ahuyama.convert_alpha() #pygame.image.load("res/game/ingredients/15Ahuyama.png")
        ResourceController.game_Ingredient16Ajo.convert_alpha() #pygame.image.load("res/game/ingredients/16Ajo.png")
        ResourceController.game_Ingredient17Apio.convert_alpha() #pygame.image.load("res/game/ingredients/17Apio.png")
        ResourceController.game_Ingredient18Arveja.convert_alpha() #pygame.image.load("res/game/ingredients/18Arveja.png")
        ResourceController.game_Ingredient19Brocoli.convert_alpha() #pygame.image.load("res/game/ingredients/19Brocoli.png")
        ResourceController.game_Ingredient20CebollaCabezona.convert_alpha() #pygame.image.load("res/game/ingredients/20CebollaCabezona.png")
        ResourceController.game_Ingredient21CebollaLarga.convert_alpha() #pygame.image.load("res/game/ingredients/21CebollaLarga.png")
        ResourceController.game_Ingredient22Cilantro.convert_alpha() #pygame.image.load("res/game/ingredients/22Cilantro.png")
        ResourceController.game_Ingredient23Coliflor.convert_alpha() #pygame.image.load("res/game/ingredients/23Coliflor.png")
        ResourceController.game_Ingredient24Espinaca.convert_alpha() #pygame.image.load("res/game/ingredients/24Espinaca.png")
        ResourceController.game_Ingredient25Frijol.convert_alpha() #pygame.image.load("res/game/ingredients/25Frijol.png")
        ResourceController.game_Ingredient26Guascas.convert_alpha() #pygame.image.load("res/game/ingredients/26Guascas.png")
        ResourceController.game_Ingredient27Habichuela.convert_alpha() #pygame.image.load("res/game/ingredients/27Habichuela.png")
        ResourceController.game_Ingredient28Lechuga.convert_alpha() #pygame.image.load("res/game/ingredients/28Lechuga.png")
        ResourceController.game_Ingredient29PepinoCohombro.convert_alpha() #pygame.image.load("res/game/ingredients/29PepinoCohombro.png")
        ResourceController.game_Ingredient30PepinoComun.convert_alpha() #pygame.image.load("res/game/ingredients/30PepinoComun.png")
        ResourceController.game_Ingredient31Pimenton.convert_alpha() #pygame.image.load("res/game/ingredients/31Pimenton.png")
        ResourceController.game_Ingredient32Tomate.convert_alpha() #pygame.image.load("res/game/ingredients/32Tomate.png")
        ResourceController.game_Ingredient33Zanahoria.convert_alpha() #pygame.image.load("res/game/ingredients/33Zanahoria.png")
        ResourceController.game_Ingredient34Aguacate.convert_alpha() #pygame.image.load("res/game/ingredients/34Aguacate.png")
        ResourceController.game_Ingredient35Banano.convert_alpha() #pygame.image.load("res/game/ingredients/35Banano.png")
        ResourceController.game_Ingredient36Curuba.convert_alpha() #pygame.image.load("res/game/ingredients/36Curuba.png")
        ResourceController.game_Ingredient37Fresa.convert_alpha() #pygame.image.load("res/game/ingredients/37Fresa.png")
        ResourceController.game_Ingredient38Guayaba.convert_alpha() #pygame.image.load("res/game/ingredients/38Guayaba.png")
        ResourceController.game_Ingredient39Limon.convert_alpha() #pygame.image.load("res/game/ingredients/39Limon.png")
        ResourceController.game_Ingredient40Mandarina.convert_alpha() #pygame.image.load("res/game/ingredients/40Mandarina.png")
        ResourceController.game_Ingredient41Mango.convert_alpha() #pygame.image.load("res/game/ingredients/41Mango.png")
        ResourceController.game_Ingredient42ManzanaVerde.convert_alpha() #pygame.image.load("res/game/ingredients/42ManzanaVerde.png")
        ResourceController.game_Ingredient43ManzanaRoja.convert_alpha() #pygame.image.load("res/game/ingredients/43ManzanaRoja.png")
        ResourceController.game_Ingredient44Maracuya.convert_alpha() #pygame.image.load("res/game/ingredients/44Maracuya.png")
        ResourceController.game_Ingredient45Melon.convert_alpha() #pygame.image.load("res/game/ingredients/45Melon.png")
        ResourceController.game_Ingredient46Mora.convert_alpha() #pygame.image.load("res/game/ingredients/46Mora.png")
        ResourceController.game_Ingredient47Naranja.convert_alpha() #pygame.image.load("res/game/ingredients/47Naranja.png")
        ResourceController.game_Ingredient48Papaya.convert_alpha() #pygame.image.load("res/game/ingredients/48Papaya.png")
        ResourceController.game_Ingredient49Patilla.convert_alpha() #pygame.image.load("res/game/ingredients/49Patilla.png")
        ResourceController.game_Ingredient50Pera.convert_alpha() #pygame.image.load("res/game/ingredients/50Pera.png")
        ResourceController.game_Ingredient51Pina.convert_alpha() #pygame.image.load("res/game/ingredients/51Pina.png")
        ResourceController.game_Ingredient52Atun.convert_alpha() #pygame.image.load("res/game/ingredients/52Atun.png")
        ResourceController.game_Ingredient53CarneDeCerdo.convert_alpha() #pygame.image.load("res/game/ingredients/53CarneDeCerdo.png")
        ResourceController.game_Ingredient54CarneDeRes.convert_alpha() #pygame.image.load("res/game/ingredients/54CarneDeRes.png")
        ResourceController.game_Ingredient55Garbanzo.convert_alpha() #pygame.image.load("res/game/ingredients/55Garbanzo.png")
        ResourceController.game_Ingredient56Higado.convert_alpha() #pygame.image.load("res/game/ingredients/56Higado.png")
        ResourceController.game_Ingredient57Huevo.convert_alpha() #pygame.image.load("res/game/ingredients/57Huevo.png")
        ResourceController.game_Ingredient58Lenteja.convert_alpha() #pygame.image.load("res/game/ingredients/58Lenteja.png")
        ResourceController.game_Ingredient59Menudencias.convert_alpha() #pygame.image.load("res/game/ingredients/59Menudencias.png")
        ResourceController.game_Ingredient60Pescado.convert_alpha() #pygame.image.load("res/game/ingredients/60Pescado.png")
        ResourceController.game_Ingredient61Pollo.convert_alpha() #pygame.image.load("res/game/ingredients/61Pollo.png")
        ResourceController.game_Ingredient62Salchicha.convert_alpha() #pygame.image.load("res/game/ingredients/62Salchicha.png")
        ResourceController.game_Ingredient63CremaDeLeche.convert_alpha() #pygame.image.load("res/game/ingredients/63CremaDeLeche.png")
        ResourceController.game_Ingredient64Kumis.convert_alpha() #pygame.image.load("res/game/ingredients/64Kumis.png")
        ResourceController.game_Ingredient65Leche.convert_alpha() #pygame.image.load("res/game/ingredients/65Leche.png")
        ResourceController.game_Ingredient66Queso.convert_alpha() #pygame.image.load("res/game/ingredients/66Queso.png")
        ResourceController.game_Ingredient67Yogur.convert_alpha() #pygame.image.load("res/game/ingredients/67Yogur.png")
        ResourceController.game_Ingredient68Aceite.convert_alpha() #pygame.image.load("res/game/ingredients/68Aceite.png")
        ResourceController.game_Ingredient69Mantequilla.convert_alpha() #pygame.image.load("res/game/ingredients/69Mantequilla.png")
        ResourceController.game_Ingredient70Margarina.convert_alpha() #pygame.image.load("res/game/ingredients/70Margarina.png")
        ResourceController.game_Ingredient71Azucar.convert_alpha() #pygame.image.load("res/game/ingredients/71Azucar.png")
        ResourceController.game_Ingredient72Chocolate.convert_alpha() #pygame.image.load("res/game/ingredients/72Chocolate.png")
        ResourceController.game_Ingredient73Helado.convert_alpha() #pygame.image.load("res/game/ingredients/73Helado.png")
        ResourceController.game_Ingredient74Panela.convert_alpha() #pygame.image.load("res/game/ingredients/74Panela.png")
        ResourceController.game_Ingredient75Agua.convert_alpha() #pygame.image.load("res/game/ingredients/75Agua.png")
        ResourceController.game_Ingredient76Mayonesa.convert_alpha() #pygame.image.load("res/game/ingredients/76Mayonesa.png")
        ResourceController.game_Ingredient77Mostaza.convert_alpha() #pygame.image.load("res/game/ingredients/77Mostaza.png")
        ResourceController.game_Ingredient78PolvoDeHornear.convert_alpha() #pygame.image.load("res/game/ingredients/78PolvoDeHornear.png")
        ResourceController.game_Ingredient79Sal.convert_alpha() #pygame.image.load("res/game/ingredients/79Sal.png")
        ResourceController.game_Ingredient80SalsaDeTomate.convert_alpha() #pygame.image.load("res/game/ingredients/80SalsaDeTomate.png")
        ResourceController.game_Ingredient81SopasEnCrema.convert_alpha() #pygame.image.load("res/game/ingredients/81SopasEnCrema.png")
        ResourceController.game_Ingredient82VinagretaDulce.convert_alpha() #pygame.image.load("res/game/ingredients/82VinagretaDulce.png")
        
        # -> Recipes (Enabled)
        ResourceController.game_Recipe01Albondigas.convert_alpha() #pygame.image.load("res/game/recipes/01Albondigas.png")
        ResourceController.game_Recipe02ArepaRellenaConQueso.convert_alpha() #pygame.image.load("res/game/recipes/02ArepaRellenaConQueso.png")
        ResourceController.game_Recipe03ArrozALaSuegra.convert_alpha() #pygame.image.load("res/game/recipes/03ArrozALaSuegra.png")
        ResourceController.game_Recipe04ArrozCampesino.convert_alpha() #pygame.image.load("res/game/recipes/04ArrozCampesino.png")
        ResourceController.game_Recipe05ArrozConMenudencias.convert_alpha() #pygame.image.load("res/game/recipes/05ArrozConMenudencias.png")
        ResourceController.game_Recipe06ArrozVegetariano.convert_alpha() #pygame.image.load("res/game/recipes/06ArrozVegetariano.png")
        ResourceController.game_Recipe07ArrozVerde.convert_alpha() #pygame.image.load("res/game/recipes/07ArrozVerde.png")
        ResourceController.game_Recipe08AvenaEnHojuelas.convert_alpha() #pygame.image.load("res/game/recipes/08AvenaEnHojuelas.png")
        ResourceController.game_Recipe09BrochetaDeFrutas.convert_alpha() #pygame.image.load("res/game/recipes/09BrochetaDeFrutas.png")
        ResourceController.game_Recipe10CaldoDePapaConCostilla.convert_alpha() #pygame.image.load("res/game/recipes/10CaldoDePapaConCostilla.png")
        ResourceController.game_Recipe11ChanguaDeLecheConHuevo.convert_alpha() #pygame.image.load("res/game/recipes/11ChanguaDeLecheConHuevo.png")
        ResourceController.game_Recipe12CremaDeCebollaCabezona.convert_alpha() #pygame.image.load("res/game/recipes/12CremaDeCebollaCabezona.png")
        ResourceController.game_Recipe13CroquetasDeEspinaca.convert_alpha() #pygame.image.load("res/game/recipes/13CroquetasDeEspinaca.png")
        ResourceController.game_Recipe14EnsaladaAlbaHit.convert_alpha() #pygame.image.load("res/game/recipes/14EnsaladaAlbaHit.png")
        ResourceController.game_Recipe15EnsaladaCarlos.convert_alpha() #pygame.image.load("res/game/recipes/15EnsaladaCarlos.png")
        ResourceController.game_Recipe16EnsaladaCriolla.convert_alpha() #pygame.image.load("res/game/recipes/16EnsaladaCriolla.png")
        ResourceController.game_Recipe17EnsaladaDeColores.convert_alpha() #pygame.image.load("res/game/recipes/17EnsaladaDeColores.png")
        ResourceController.game_Recipe18EnsaladaDeFrutasConYogurt.convert_alpha() #pygame.image.load("res/game/recipes/18EnsaladaDeFrutasConYogurt.png")
        ResourceController.game_Recipe19EnsaladaDeLaCasa.convert_alpha() #pygame.image.load("res/game/recipes/19EnsaladaDeLaCasa.png")
        ResourceController.game_Recipe20EnsaladaDelHuerto.convert_alpha() #pygame.image.load("res/game/recipes/20EnsaladaDelHuerto.png")
        ResourceController.game_Recipe21EnsaladaFriaDePapaConPollo.convert_alpha() #pygame.image.load("res/game/recipes/21EnsaladaFriaDePapaConPollo.png")
        ResourceController.game_Recipe22EnsaladaRanchera.convert_alpha() #pygame.image.load("res/game/recipes/22EnsaladaRanchera.png")
        ResourceController.game_Recipe23GuarapoDePina.convert_alpha() #pygame.image.load("res/game/recipes/23GuarapoDePina.png")
        ResourceController.game_Recipe24GuisoDeCarneYVerdura.convert_alpha() #pygame.image.load("res/game/recipes/24GuisoDeCarneYVerdura.png")
        ResourceController.game_Recipe25GuisoDeHabichuelaConCarne.convert_alpha() #pygame.image.load("res/game/recipes/25GuisoDeHabichuelaConCarne.png")
        ResourceController.game_Recipe26Hamburguesa.convert_alpha() #pygame.image.load("res/game/recipes/26Hamburguesa.png")
        ResourceController.game_Recipe27HuevoTibio.convert_alpha() #pygame.image.load("res/game/recipes/27HuevoTibio.png")
        ResourceController.game_Recipe28JugoDeMaracuyaYZanahoria.convert_alpha() #pygame.image.load("res/game/recipes/28JugoDeMaracuyaYZanahoria.png")
        ResourceController.game_Recipe29JugoDePapayaConZanahoria.convert_alpha() #pygame.image.load("res/game/recipes/29JugoDePapayaConZanahoria.png")
        ResourceController.game_Recipe30LomoDeCerdoEnSalsaDeMango.convert_alpha() #pygame.image.load("res/game/recipes/30LomoDeCerdoEnSalsaDeMango.png")
        ResourceController.game_Recipe31LomoDeCerdoEnchilado.convert_alpha() #pygame.image.load("res/game/recipes/31LomoDeCerdoEnchilado.png")
        ResourceController.game_Recipe32MacarronesConAtun.convert_alpha() #pygame.image.load("res/game/recipes/32MacarronesConAtun.png")
        ResourceController.game_Recipe33PastaConVegetales.convert_alpha() #pygame.image.load("res/game/recipes/33PastaConVegetales.png")
        ResourceController.game_Recipe34PataconesConCarneDesmechada.convert_alpha() #pygame.image.load("res/game/recipes/34PataconesConCarneDesmechada.png")
        ResourceController.game_Recipe35PepinosRellenos.convert_alpha() #pygame.image.load("res/game/recipes/35PepinosRellenos.png")
        ResourceController.game_Recipe36PerroCaliente.convert_alpha() #pygame.image.load("res/game/recipes/36PerroCaliente.png")
        ResourceController.game_Recipe37PescadoALaPrimavera.convert_alpha() #pygame.image.load("res/game/recipes/37PescadoALaPrimavera.png")
        ResourceController.game_Recipe38PescadoOriental.convert_alpha() #pygame.image.load("res/game/recipes/38PescadoOriental.png")
        ResourceController.game_Recipe39PolloALaJardinera.convert_alpha() #pygame.image.load("res/game/recipes/39PolloALaJardinera.png")
        ResourceController.game_Recipe40QuesoDePina.convert_alpha() #pygame.image.load("res/game/recipes/40QuesoDePina.png")
        ResourceController.game_Recipe41RefrescoDeManzana.convert_alpha() #pygame.image.load("res/game/recipes/41RefrescoDeManzana.png")
        ResourceController.game_Recipe42Salchipapas.convert_alpha() #pygame.image.load("res/game/recipes/42Salchipapas.png")
        ResourceController.game_Recipe43SandwichDeJamonYQueso.convert_alpha() #pygame.image.load("res/game/recipes/43SandwichDeJamonYQueso.png")
        ResourceController.game_Recipe44SopaDeGarbanzo.convert_alpha() #pygame.image.load("res/game/recipes/44SopaDeGarbanzo.png")
        ResourceController.game_Recipe45SopaDeLentejas.convert_alpha() #pygame.image.load("res/game/recipes/45SopaDeLentejas.png")
        ResourceController.game_Recipe46SopaDeVerduras.convert_alpha() #pygame.image.load("res/game/recipes/46SopaDeVerduras.png")
        ResourceController.game_Recipe47TeDeMango.convert_alpha() #pygame.image.load("res/game/recipes/47TeDeMango.png")
        ResourceController.game_Recipe48TerneraALaMarinera.convert_alpha() #pygame.image.load("res/game/recipes/48TerneraALaMarinera.png")
        ResourceController.game_Recipe49TomatesRellenos.convert_alpha() #pygame.image.load("res/game/recipes/49TomatesRellenos.png")
        ResourceController.game_Recipe50TortaDeAhuyama.convert_alpha() #pygame.image.load("res/game/recipes/50TortaDeAhuyama.png")
        ResourceController.game_Recipe51TortaDeBanano.convert_alpha() #pygame.image.load("res/game/recipes/51TortaDeBanano.png")
        ResourceController.game_Recipe52TortaDeZanahoria.convert_alpha() #pygame.image.load("res/game/recipes/52TortaDeZanahoria.png")
        ResourceController.game_Recipe53TortillaDeAcelga.convert_alpha() #pygame.image.load("res/game/recipes/53TortillaDeAcelga.png")
        ResourceController.game_Recipe54TortillaDeEspinaca.convert_alpha() #pygame.image.load("res/game/recipes/54TortillaDeEspinaca.png")
        ResourceController.game_Recipe55Zafresco.convert_alpha() #pygame.image.load("res/game/recipes/55Zafresco.png")
        
        ResourceController.game_Recipe56TortillaDeMazorca.convert_alpha() #pygame.image.load("res/game/recipes/56TortillaDeMazorca.png")
        ResourceController.game_Recipe57BatidoDeGuayabaYAvena.convert_alpha() #pygame.image.load("res/game/recipes/57BatidoDeGuayabaYAvena.png")
        ResourceController.game_Recipe58BatidoDeYogurtFresasYAvena.convert_alpha() #pygame.image.load("res/game/recipes/58BatidoDeYogurtFresasYAvena.png")
        ResourceController.game_Recipe59PanquequesDeAvena.convert_alpha() #pygame.image.load("res/game/recipes/59PanquequesDeAvena.png")
        ResourceController.game_Recipe60TortillaDeVerdurasYQueso.convert_alpha() #pygame.image.load("res/game/recipes/60TortillaDeVerdurasYQueso.png")
        ResourceController.game_Recipe61PanquequesDeFruta.convert_alpha() #pygame.image.load("res/game/recipes/61PanquequesDeFruta.png")
        ResourceController.game_Recipe62ArepasDeMazorca.convert_alpha() #pygame.image.load("res/game/recipes/62ArepasDeMazorca.png")
        
        
    
        # -> Recipes (Disabled)
        ResourceController.game_Recipe01AlbondigasDisabled.convert_alpha() #pygame.image.load("res/game/recipesDisabled/01Albondigas.png")
        ResourceController.game_Recipe02ArepaRellenaConQuesoDisabled.convert_alpha() #pygame.image.load("res/game/recipesDisabled/02ArepaRellenaConQueso.png")
        ResourceController.game_Recipe03ArrozALaSuegraDisabled.convert_alpha() #pygame.image.load("res/game/recipesDisabled/03ArrozALaSuegra.png")
        ResourceController.game_Recipe04ArrozCampesinoDisabled.convert_alpha() #pygame.image.load("res/game/recipesDisabled/04ArrozCampesino.png")
        ResourceController.game_Recipe05ArrozConMenudenciasDisabled.convert_alpha() #pygame.image.load("res/game/recipesDisabled/05ArrozConMenudencias.png")
        ResourceController.game_Recipe06ArrozVegetarianoDisabled.convert_alpha() #pygame.image.load("res/game/recipesDisabled/06ArrozVegetariano.png")
        ResourceController.game_Recipe07ArrozVerdeDisabled.convert_alpha() #pygame.image.load("res/game/recipesDisabled/07ArrozVerde.png")
        ResourceController.game_Recipe08AvenaEnHojuelasDisabled.convert_alpha() #pygame.image.load("res/game/recipesDisabled/08AvenaEnHojuelas.png")
        ResourceController.game_Recipe09BrochetaDeFrutasDisabled.convert_alpha() #pygame.image.load("res/game/recipesDisabled/09BrochetaDeFrutas.png")
        ResourceController.game_Recipe10CaldoDePapaConCostillaDisabled.convert_alpha() #pygame.image.load("res/game/recipesDisabled/10CaldoDePapaConCostilla.png")
        ResourceController.game_Recipe11ChanguaDeLecheConHuevoDisabled.convert_alpha() #pygame.image.load("res/game/recipesDisabled/11ChanguaDeLecheConHuevo.png")
        ResourceController.game_Recipe12CremaDeCebollaCabezonaDisabled.convert_alpha() #pygame.image.load("res/game/recipesDisabled/12CremaDeCebollaCabezona.png")
        ResourceController.game_Recipe13CroquetasDeEspinacaDisabled.convert_alpha() #pygame.image.load("res/game/recipesDisabled/13CroquetasDeEspinaca.png")
        ResourceController.game_Recipe14EnsaladaAlbaHitDisabled.convert_alpha() #pygame.image.load("res/game/recipesDisabled/14EnsaladaAlbaHit.png")
        ResourceController.game_Recipe15EnsaladaCarlosDisabled.convert_alpha() #pygame.image.load("res/game/recipesDisabled/15EnsaladaCarlos.png")
        ResourceController.game_Recipe16EnsaladaCriollaDisabled.convert_alpha() #pygame.image.load("res/game/recipesDisabled/16EnsaladaCriolla.png")
        ResourceController.game_Recipe17EnsaladaDeColoresDisabled.convert_alpha() #pygame.image.load("res/game/recipesDisabled/17EnsaladaDeColores.png")
        ResourceController.game_Recipe18EnsaladaDeFrutasConYogurtDisabled.convert_alpha() #pygame.image.load("res/game/recipesDisabled/18EnsaladaDeFrutasConYogurt.png")
        ResourceController.game_Recipe19EnsaladaDeLaCasaDisabled.convert_alpha() #pygame.image.load("res/game/recipesDisabled/19EnsaladaDeLaCasa.png")
        ResourceController.game_Recipe20EnsaladaDelHuertoDisabled.convert_alpha() #pygame.image.load("res/game/recipesDisabled/20EnsaladaDelHuerto.png")
        ResourceController.game_Recipe21EnsaladaFriaDePapaConPolloDisabled.convert_alpha() #pygame.image.load("res/game/recipesDisabled/21EnsaladaFriaDePapaConPollo.png")
        ResourceController.game_Recipe22EnsaladaRancheraDisabled.convert_alpha() #pygame.image.load("res/game/recipesDisabled/22EnsaladaRanchera.png")
        ResourceController.game_Recipe23GuarapoDePinaDisabled.convert_alpha() #pygame.image.load("res/game/recipesDisabled/23GuarapoDePina.png")
        ResourceController.game_Recipe24GuisoDeCarneYVerduraDisabled.convert_alpha() #pygame.image.load("res/game/recipesDisabled/24GuisoDeCarneYVerdura.png")
        ResourceController.game_Recipe25GuisoDeHabichuelaConCarneDisabled.convert_alpha() #pygame.image.load("res/game/recipesDisabled/25GuisoDeHabichuelaConCarne.png")
        ResourceController.game_Recipe26HamburguesaDisabled.convert_alpha() #pygame.image.load("res/game/recipesDisabled/26Hamburguesa.png")
        ResourceController.game_Recipe27HuevoTibioDisabled.convert_alpha() #pygame.image.load("res/game/recipesDisabled/27HuevoTibio.png")
        ResourceController.game_Recipe28JugoDeMaracuyaYZanahoriaDisabled.convert_alpha() #pygame.image.load("res/game/recipesDisabled/28JugoDeMaracuyaYZanahoria.png")
        ResourceController.game_Recipe29JugoDePapayaConZanahoriaDisabled.convert_alpha() #pygame.image.load("res/game/recipesDisabled/29JugoDePapayaConZanahoria.png")
        ResourceController.game_Recipe30LomoDeCerdoEnSalsaDeMangoDisabled.convert_alpha() #pygame.image.load("res/game/recipesDisabled/30LomoDeCerdoEnSalsaDeMango.png")
        ResourceController.game_Recipe31LomoDeCerdoEnchiladoDisabled.convert_alpha() #pygame.image.load("res/game/recipesDisabled/31LomoDeCerdoEnchilado.png")
        ResourceController.game_Recipe32MacarronesConAtunDisabled.convert_alpha() #pygame.image.load("res/game/recipesDisabled/32MacarronesConAtun.png")
        ResourceController.game_Recipe33PastaConVegetalesDisabled.convert_alpha() #pygame.image.load("res/game/recipesDisabled/33PastaConVegetales.png")
        ResourceController.game_Recipe34PataconesConCarneDesmechadaDisabled.convert_alpha() #pygame.image.load("res/game/recipesDisabled/34PataconesConCarneDesmechada.png")
        ResourceController.game_Recipe35PepinosRellenosDisabled.convert_alpha() #pygame.image.load("res/game/recipesDisabled/35PepinosRellenos.png")
        ResourceController.game_Recipe36PerroCalienteDisabled.convert_alpha() #pygame.image.load("res/game/recipesDisabled/36PerroCaliente.png")
        ResourceController.game_Recipe37PescadoALaPrimaveraDisabled.convert_alpha() #pygame.image.load("res/game/recipesDisabled/37PescadoALaPrimavera.png")
        ResourceController.game_Recipe38PescadoOrientalDisabled.convert_alpha() #pygame.image.load("res/game/recipesDisabled/38PescadoOriental.png")
        ResourceController.game_Recipe39PolloALaJardineraDisabled.convert_alpha() #pygame.image.load("res/game/recipesDisabled/39PolloALaJardinera.png")
        ResourceController.game_Recipe40QuesoDePinaDisabled.convert_alpha() #pygame.image.load("res/game/recipesDisabled/40QuesoDePina.png")
        ResourceController.game_Recipe41RefrescoDeManzanaDisabled.convert_alpha() #pygame.image.load("res/game/recipesDisabled/41RefrescoDeManzana.png")
        ResourceController.game_Recipe42SalchipapasDisabled.convert_alpha() #pygame.image.load("res/game/recipesDisabled/42Salchipapas.png")
        ResourceController.game_Recipe43SandwichDeJamonYQuesoDisabled.convert_alpha() #pygame.image.load("res/game/recipesDisabled/43SandwichDeJamonYQueso.png")
        ResourceController.game_Recipe44SopaDeGarbanzoDisabled.convert_alpha() #pygame.image.load("res/game/recipesDisabled/44SopaDeGarbanzo.png")
        ResourceController.game_Recipe45SopaDeLentejasDisabled.convert_alpha() #pygame.image.load("res/game/recipesDisabled/45SopaDeLentejas.png")
        ResourceController.game_Recipe46SopaDeVerdurasDisabled.convert_alpha() #pygame.image.load("res/game/recipesDisabled/46SopaDeVerduras.png")
        ResourceController.game_Recipe47TeDeMangoDisabled.convert_alpha() #pygame.image.load("res/game/recipesDisabled/47TeDeMango.png")
        ResourceController.game_Recipe48TerneraALaMarineraDisabled.convert_alpha() #pygame.image.load("res/game/recipesDisabled/48TerneraALaMarinera.png")
        ResourceController.game_Recipe49TomatesRellenosDisabled.convert_alpha() #pygame.image.load("res/game/recipesDisabled/49TomatesRellenos.png")
        ResourceController.game_Recipe50TortaDeAhuyamaDisabled.convert_alpha() #pygame.image.load("res/game/recipesDisabled/50TortaDeAhuyama.png")
        ResourceController.game_Recipe51TortaDeBananoDisabled.convert_alpha() #pygame.image.load("res/game/recipesDisabled/51TortaDeBanano.png")
        ResourceController.game_Recipe52TortaDeZanahoriaDisabled.convert_alpha() #pygame.image.load("res/game/recipesDisabled/52TortaDeZanahoria.png")
        ResourceController.game_Recipe53TortillaDeAcelgaDisabled.convert_alpha() #pygame.image.load("res/game/recipesDisabled/53TortillaDeAcelga.png")
        ResourceController.game_Recipe54TortillaDeEspinacaDisabled.convert_alpha() #pygame.image.load("res/game/recipesDisabled/54TortillaDeEspinaca.png")
        ResourceController.game_Recipe55ZafrescoDisabled.convert_alpha() #pygame.image.load("res/game/recipesDisabled/55Zafresco.png")
    
        ResourceController.game_Recipe56TortillaDeMazorcaDisabled.convert_alpha() #pygame.image.load("res/game/recipesDisabled/56TortillaDeMazorca.png")
        ResourceController.game_Recipe57BatidoDeGuayabaYAvenaDisabled.convert_alpha() #pygame.image.load("res/game/recipesDisabled/57BatidoDeGuayabaYAvena.png")
        ResourceController.game_Recipe58BatidoDeYogurtFresasYAvenaDisabled.convert_alpha() #pygame.image.load("res/game/recipesDisabled/58BatidoDeYogurtFresasYAvena.png")
        ResourceController.game_Recipe59PanquequesDeAvenaDisabled.convert_alpha() #pygame.image.load("res/game/recipesDisabled/59PanquequesDeAvena.png")
        ResourceController.game_Recipe60TortillaDeVerdurasYQuesoDisabled.convert_alpha() #pygame.image.load("res/game/recipesDisabled/60TortillaDeVerdurasYQueso.png")
        ResourceController.game_Recipe61PanquequesDeFrutaDisabled.convert_alpha() #pygame.image.load("res/game/recipesDisabled/61PanquequesDeFruta.png")
        ResourceController.game_Recipe62ArepasDeMazorcaDisabled.convert_alpha() #pygame.image.load("res/game/recipesDisabled/62ArepasDeMazorca.png")

        
    
    # Background folder
    background_Answer = pygame.image.load("res/background/Answer.png")
    background_IngredientInfo = pygame.image.load("res/background/IngredientInfo.png")
    background_Kitchen = pygame.image.load("res/background/Kitchen.png")
    background_Login = pygame.image.load("res/background/Login.png")
    background_PickIngredients = pygame.image.load("res/background/PickIngredients.png")
    background_RecipeAssign = pygame.image.load("res/background/RecipeAssign.png")
    background_Recipes = pygame.image.load("res/background/Recipes.png")
    background_Registration = pygame.image.load("res/background/Registration.png")
    background_SelectGender = pygame.image.load("res/background/SelectGender.png")
    background_SelectOrder = pygame.image.load("res/background/SelectOrder.png")
    background_Splash_1 = pygame.image.load("res/background/Splash_1.png")
    background_Splash_2 = pygame.image.load("res/background/Splash_2.png")
    background_Splash_3 = pygame.image.load("res/background/Splash_3.png")
    background_Splash_4 = pygame.image.load("res/background/Splash_4.png")
    background_Splash_5 = pygame.image.load("res/background/Splash_5.png")
    background_Transparent = pygame.image.load("res/background/Transparent.png")
    
    # Input folder
    input_Accept_Off = pygame.image.load("res/input/Accept_Off.png")
    input_Accept_On = pygame.image.load("res/input/Accept_On.png")
    input_ArrowLeft = pygame.image.load("res/input/ArrowLeft.png")
    input_ArrowRight = pygame.image.load("res/input/ArrowRight.png")
    input_AssignSelector = pygame.image.load("res/input/AssignSelector.png")
    input_Back1Cereales = pygame.image.load("res/input/Back1Cereales.png")
    input_Back2Verduras = pygame.image.load("res/input/Back2Verduras.png")
    input_Back3Frutas = pygame.image.load("res/input/Back3Frutas.png")
    input_Back4Carnes = pygame.image.load("res/input/Back4Carnes.png") 
    input_Back5Lacteos = pygame.image.load("res/input/Back5Lacteos.png")
    input_Back6Grasas = pygame.image.load("res/input/Back6Grasas.png")
    input_Back7Azucares = pygame.image.load("res/input/Back7Azucares.png")
    input_Back8Otros = pygame.image.load("res/input/Back8Otros.png")
    input_Button1Cereales = pygame.image.load("res/input/Button1Cereales.png")
    input_Button2Verduras = pygame.image.load("res/input/Button2Verduras.png")
    input_Button3Frutas = pygame.image.load("res/input/Button3Frutas.png")
    input_Button4Carnes = pygame.image.load("res/input/Button4Carnes.png")
    input_Button5Lacteos = pygame.image.load("res/input/Button5Lacteos.png")
    input_Button6Grasas = pygame.image.load("res/input/Button6Grasas.png")
    input_Button7Azucares = pygame.image.load("res/input/Button7Azucares.png")
    input_Button8Otros = pygame.image.load("res/input/Button8Otros.png")
    input_Cancel_Off = pygame.image.load("res/input/Cancel_Off.png")
    input_Cancel_On = pygame.image.load("res/input/Cancel_On.png")
    input_CloseGame_Off = pygame.image.load("res/input/CloseGame_Off.png")
    input_CloseGame_On = pygame.image.load("res/input/CloseGame_On.png")
    input_Connecting = pygame.image.load("res/input/Connecting.png")
    input_Cross = pygame.image.load("res/input/Cross.png")
    input_GenderFemale_On = pygame.image.load("res/input/GenderFemale_On.png")
    input_GenderFemale_Off = pygame.image.load("res/input/GenderFemale_Off.png")
    input_GenderMale_On = pygame.image.load("res/input/GenderMale_On.png")
    input_GenderMale_Off = pygame.image.load("res/input/GenderMale_Off.png")
    input_Login_Off = pygame.image.load("res/input/Login_Off.png")
    input_Login_On = pygame.image.load("res/input/Login_On.png")
    input_LoginBrother = pygame.image.load("res/input/LoginBrother.png")
    input_LoginCousin = pygame.image.load("res/input/LoginCousin.png")
    input_LoginFriend = pygame.image.load("res/input/LoginFriend.png")
    input_LoginInput = pygame.image.load("res/input/LoginInput.png")
    input_LoginMainUser = pygame.image.load("res/input/LoginMainUser.png")
    input_LoginParent = pygame.image.load("res/input/LoginParent.png")
    input_LoginUncle = pygame.image.load("res/input/LoginUncle.png")
    input_OrderSelector = pygame.image.load("res/input/OrderSelector.png")
    input_ReadyDish_On = pygame.image.load("res/input/ReadyDish_On.png")
    input_ReadyDish_Off = pygame.image.load("res/input/ReadyDish_Off.png")
    input_RecipeIndex = pygame.image.load("res/input/RecipeIndex.png")
    input_Registration_On = pygame.image.load("res/input/Registration_On.png")
    input_Registration_Off = pygame.image.load("res/input/Registration_Off.png")
    input_TabIngredients_On = pygame.image.load("res/input/TabIngredients_On.png")
    input_TabIngredients_Off = pygame.image.load("res/input/TabIngredients_Off.png")
    input_TabRecipes_On = pygame.image.load("res/input/TabRecipes_On.png")
    input_TabRecipes_Off = pygame.image.load("res/input/TabRecipes_Off.png")
    input_TriviaOption_Off = pygame.image.load("res/input/TriviaOption_Off.png")
    input_TriviaOption_On = pygame.image.load("res/input/TriviaOption_On.png")
    input_TutorialNo_Off = pygame.image.load("res/input/TutorialNo_Off.png")
    input_TutorialNo_On = pygame.image.load("res/input/TutorialNo_On.png")
    input_TutorialYes_Off = pygame.image.load("res/input/TutorialYes_Off.png")
    input_TutorialYes_On = pygame.image.load("res/input/TutorialYes_On.png")
            
    # Cursor folder
    cursor_Sugar = "res/cursor/Sugar.xbm"
    cursor_SugarMask = "res/cursor/SugarMask.xbm"
    
    # Font folder
    font_BorisBlackBloxx = "res/font/BorisBlackBloxx.ttf"
    
    # Game folder
    game_BannerBreakfast_1 = pygame.image.load("res/game/BannerBreakfast_1.png")
    game_BannerBreakfast_2 = pygame.image.load("res/game/BannerBreakfast_2.png")
    game_BannerDinner_1 = pygame.image.load("res/game/BannerDinner_1.png")
    game_BannerDinner_2 = pygame.image.load("res/game/BannerDinner_2.png")
    game_BannerLunch_1 = pygame.image.load("res/game/BannerLunch_1.png")
    game_BannerLunch_2 = pygame.image.load("res/game/BannerLunch_2.png")
    game_BannerRefreshmentAfternoon_1 = pygame.image.load("res/game/BannerRefreshmentAfternoon_1.png")
    game_BannerRefreshmentAfternoon_2 = pygame.image.load("res/game/BannerRefreshmentAfternoon_2.png")
    game_BannerRefreshmentMorning_1 = pygame.image.load("res/game/BannerRefreshmentMorning_1.png")
    game_BannerRefreshmentMorning_2 = pygame.image.load("res/game/BannerRefreshmentMorning_2.png")
    game_Chair = pygame.image.load("res/game/Chair.png")
    game_ChefHatBronze = pygame.image.load("res/game/ChefHatBronze.png")
    game_ChefHatGold = pygame.image.load("res/game/ChefHatGold.png")
    game_ChefHatSilver = pygame.image.load("res/game/ChefHatSilver.png")
    game_ChefHatMiniNone = pygame.image.load("res/game/ChefHatMiniNone.png")
    game_ChefHatMiniBronze = pygame.image.load("res/game/ChefHatMiniBronze.png")
    game_ChefHatMiniGold = pygame.image.load("res/game/ChefHatMiniGold.png")
    game_ChefHatMiniSilver = pygame.image.load("res/game/ChefHatMiniSilver.png")
    game_ChefLevel1 = pygame.image.load("res/game/ChefLevel1.png")
    game_ChefLevel2 = pygame.image.load("res/game/ChefLevel2.png")
    game_ChefLevel3 = pygame.image.load("res/game/ChefLevel3.png")
    game_ChefNewLevel = pygame.image.load("res/game/ChefNewLevel.png")
    game_Cloud = pygame.image.load("res/game/Cloud.png")
    game_CookingCold_1 = pygame.image.load("res/game/CookingCold_1.png")
    game_CookingCold_2 = pygame.image.load("res/game/CookingCold_2.png")
    game_CookingCold_3 = pygame.image.load("res/game/CookingCold_3.png")
    game_CookingCold_4 = pygame.image.load("res/game/CookingCold_4.png")
    game_CookingHot_1 = pygame.image.load("res/game/CookingHot_1.png")
    game_CookingHot_2 = pygame.image.load("res/game/CookingHot_2.png")
    game_CookingHot_3 = pygame.image.load("res/game/CookingHot_3.png")
    game_CookingHot_4 = pygame.image.load("res/game/CookingHot_4.png")
    game_DishDirty_1 = pygame.image.load("res/game/DishDirty_1.png")
    game_DishDirty_2 = pygame.image.load("res/game/DishDirty_2.png")
    game_DishEmpty = pygame.image.load("res/game/DishEmpty.png")
    game_DishFull = pygame.image.load("res/game/DishFull.png")
    game_DishFullBase = pygame.image.load("res/game/DishFullBase.png")
    game_IngredientSpace = pygame.image.load("res/game/IngredientSpace.png")
    game_Letter = pygame.image.load("res/game/Letter.png")
    game_MessageBackground_Female = pygame.image.load("res/game/MessageBackground_Female.png")
    game_MessageBackground_Male = pygame.image.load("res/game/MessageBackground_Male.png")
    game_Star = pygame.image.load("res/game/Star.png")
    game_StarsBackground = pygame.image.load("res/game/StarsBackground.png")
    game_Table = pygame.image.load("res/game/Table.png")
    game_TriviaText = pygame.image.load("res/game/TriviaText.png")
    game_TriviaTitle = pygame.image.load("res/game/TriviaTitle.png")
    game_TutorialStepA = pygame.image.load("res/game/TutorialStepA.png")
    game_TutorialStepB = pygame.image.load("res/game/TutorialStepB.png")
    game_TutorialStepC = pygame.image.load("res/game/TutorialStepC.png")
    game_TutorialStepD = pygame.image.load("res/game/TutorialStepD.png")
    game_TutorialStepE = pygame.image.load("res/game/TutorialStepE.png")
    game_TutorialStepF = pygame.image.load("res/game/TutorialStepF.png")
    game_TutorialStepG = pygame.image.load("res/game/TutorialStepG.png")
    game_TutorialStepH = pygame.image.load("res/game/TutorialStepH.png")
    game_TutorialStepI = pygame.image.load("res/game/TutorialStepI.png")
    game_TutorialStepJ = pygame.image.load("res/game/TutorialStepJ.png")
    game_TutorialStepK = pygame.image.load("res/game/TutorialStepK.png")
    game_TutorialStepL = pygame.image.load("res/game/TutorialStepL.png")
    game_TutorialStepM = pygame.image.load("res/game/TutorialStepM.png")
    game_TutorialStepN = pygame.image.load("res/game/TutorialStepN.png")
    game_TutorialStepO = pygame.image.load("res/game/TutorialStepO.png")
    game_TutorialStepP = pygame.image.load("res/game/TutorialStepP.png")
    game_TutorialWelcome = pygame.image.load("res/game/TutorialWelcome.png")
    game_WashingDishes_1 = pygame.image.load("res/game/WashingDishes_1.png")
    game_WashingDishes_2 = pygame.image.load("res/game/WashingDishes_2.png")
    game_WashingHands_1 = pygame.image.load("res/game/WashingHands_1.png")
    game_WashingHands_2 = pygame.image.load("res/game/WashingHands_2.png")
    game_WashingIngredients_1 = pygame.image.load("res/game/WashingIngredients_1.png")
    game_WashingIngredients_2 = pygame.image.load("res/game/WashingIngredients_2.png")
    
    # -> Chef Female
    
    # Level 0
    game_ChefFemaleLevel0_BackCarryingCleanIngredients =       pygame.image.load("res/game/chef/female/level_0/Back_CarryingCleanIngredients.png")
    game_ChefFemaleLevel0_BackCarryingDirtyDishes =            pygame.image.load("res/game/chef/female/level_0/Back_CarryingDirtyDishes.png")
    game_ChefFemaleLevel0_BackCarryingDirtyIngredients =       pygame.image.load("res/game/chef/female/level_0/Back_CarryingDirtyIngredients.png")
    game_ChefFemaleLevel0_BackCarryingPreparedFood =           pygame.image.load("res/game/chef/female/level_0/Back_CarryingPreparedFood.png")
    game_ChefFemaleLevel0_BackReady =                          pygame.image.load("res/game/chef/female/level_0/Back_Ready.png")
    game_ChefFemaleLevel0_BackTakingAnOrder =                  pygame.image.load("res/game/chef/female/level_0/Back_TakingAnOrder.png")
    
    game_ChefFemaleLevel0_FrontCarryingCleanIngredients =      pygame.image.load("res/game/chef/female/level_0/Front_CarryingCleanIngredients.png")
    game_ChefFemaleLevel0_FrontCarryingDirtyDishes =           pygame.image.load("res/game/chef/female/level_0/Front_CarryingDirtyDishes.png")
    game_ChefFemaleLevel0_FrontCarryingDirtyIngredients =      pygame.image.load("res/game/chef/female/level_0/Front_CarryingDirtyIngredients.png")
    game_ChefFemaleLevel0_FrontCarryingPreparedFood =          pygame.image.load("res/game/chef/female/level_0/Front_CarryingPreparedFood.png")
    game_ChefFemaleLevel0_FrontReady =                         pygame.image.load("res/game/chef/female/level_0/Front_Ready.png")
    game_ChefFemaleLevel0_FrontTakingAnOrder =                 pygame.image.load("res/game/chef/female/level_0/Front_TakingAnOrder.png")
    game_ChefFemaleLevel0_FrontDancing_0 =                     pygame.image.load("res/game/chef/female/level_0/Front_Dancing_0.png")
    game_ChefFemaleLevel0_FrontDancing_1 =                     pygame.image.load("res/game/chef/female/level_0/Front_Dancing_1.png")
    game_ChefFemaleLevel0_FrontDancing_2 =                     pygame.image.load("res/game/chef/female/level_0/Front_Dancing_2.png")
    
    game_ChefFemaleLevel0_LeftCarryingCleanIngredients =       pygame.image.load("res/game/chef/female/level_0/Left_CarryingCleanIngredients.png")
    game_ChefFemaleLevel0_LeftCarryingDirtyDishes =            pygame.image.load("res/game/chef/female/level_0/Left_CarryingDirtyDishes.png")
    game_ChefFemaleLevel0_LeftCarryingDirtyIngredients =       pygame.image.load("res/game/chef/female/level_0/Left_CarryingDirtyIngredients.png")
    game_ChefFemaleLevel0_LeftCarryingPreparedFood =           pygame.image.load("res/game/chef/female/level_0/Left_CarryingPreparedFood.png")
    game_ChefFemaleLevel0_LeftReady =                          pygame.image.load("res/game/chef/female/level_0/Left_Ready.png")
    game_ChefFemaleLevel0_LeftTakingAnOrder =                  pygame.image.load("res/game/chef/female/level_0/Left_TakingAnOrder.png")
    
    game_ChefFemaleLevel0_RightCarryingCleanIngredients =      pygame.image.load("res/game/chef/female/level_0/Right_CarryingCleanIngredients.png")
    game_ChefFemaleLevel0_RightCarryingDirtyDishes =           pygame.image.load("res/game/chef/female/level_0/Right_CarryingDirtyDishes.png")
    game_ChefFemaleLevel0_RightCarryingDirtyIngredients =      pygame.image.load("res/game/chef/female/level_0/Right_CarryingDirtyIngredients.png")
    game_ChefFemaleLevel0_RightCarryingPreparedFood =          pygame.image.load("res/game/chef/female/level_0/Right_CarryingPreparedFood.png")
    game_ChefFemaleLevel0_RightReady =                         pygame.image.load("res/game/chef/female/level_0/Right_Ready.png")
    game_ChefFemaleLevel0_RightTakingAnOrder =                 pygame.image.load("res/game/chef/female/level_0/Right_TakingAnOrder.png")
    
    # Level 1
    game_ChefFemaleLevel1_BackCarryingCleanIngredients =       pygame.image.load("res/game/chef/female/level_1/Back_CarryingCleanIngredients.png")
    game_ChefFemaleLevel1_BackCarryingDirtyDishes =            pygame.image.load("res/game/chef/female/level_1/Back_CarryingDirtyDishes.png")
    game_ChefFemaleLevel1_BackCarryingDirtyIngredients =       pygame.image.load("res/game/chef/female/level_1/Back_CarryingDirtyIngredients.png")
    game_ChefFemaleLevel1_BackCarryingPreparedFood =           pygame.image.load("res/game/chef/female/level_1/Back_CarryingPreparedFood.png")
    game_ChefFemaleLevel1_BackReady =                          pygame.image.load("res/game/chef/female/level_1/Back_Ready.png")
    game_ChefFemaleLevel1_BackTakingAnOrder =                  pygame.image.load("res/game/chef/female/level_1/Back_TakingAnOrder.png")

    game_ChefFemaleLevel1_FrontCarryingCleanIngredients =      pygame.image.load("res/game/chef/female/level_1/Front_CarryingCleanIngredients.png")
    game_ChefFemaleLevel1_FrontCarryingDirtyDishes =           pygame.image.load("res/game/chef/female/level_1/Front_CarryingDirtyDishes.png")
    game_ChefFemaleLevel1_FrontCarryingDirtyIngredients =      pygame.image.load("res/game/chef/female/level_1/Front_CarryingDirtyIngredients.png")
    game_ChefFemaleLevel1_FrontCarryingPreparedFood =          pygame.image.load("res/game/chef/female/level_1/Front_CarryingPreparedFood.png")
    game_ChefFemaleLevel1_FrontReady =                         pygame.image.load("res/game/chef/female/level_1/Front_Ready.png")
    game_ChefFemaleLevel1_FrontTakingAnOrder =                 pygame.image.load("res/game/chef/female/level_1/Front_TakingAnOrder.png")
    game_ChefFemaleLevel1_FrontDancing_0 =                     pygame.image.load("res/game/chef/female/level_1/Front_Dancing_0.png")
    game_ChefFemaleLevel1_FrontDancing_1 =                     pygame.image.load("res/game/chef/female/level_1/Front_Dancing_1.png")
    game_ChefFemaleLevel1_FrontDancing_2 =                     pygame.image.load("res/game/chef/female/level_1/Front_Dancing_2.png")

    game_ChefFemaleLevel1_LeftCarryingCleanIngredients =       pygame.image.load("res/game/chef/female/level_1/Left_CarryingCleanIngredients.png")
    game_ChefFemaleLevel1_LeftCarryingDirtyDishes =            pygame.image.load("res/game/chef/female/level_1/Left_CarryingDirtyDishes.png")
    game_ChefFemaleLevel1_LeftCarryingDirtyIngredients =       pygame.image.load("res/game/chef/female/level_1/Left_CarryingDirtyIngredients.png")
    game_ChefFemaleLevel1_LeftCarryingPreparedFood =           pygame.image.load("res/game/chef/female/level_1/Left_CarryingPreparedFood.png")
    game_ChefFemaleLevel1_LeftReady =                          pygame.image.load("res/game/chef/female/level_1/Left_Ready.png")
    game_ChefFemaleLevel1_LeftTakingAnOrder =                  pygame.image.load("res/game/chef/female/level_1/Left_TakingAnOrder.png")

    game_ChefFemaleLevel1_RightCarryingCleanIngredients =      pygame.image.load("res/game/chef/female/level_1/Right_CarryingCleanIngredients.png")
    game_ChefFemaleLevel1_RightCarryingDirtyDishes =           pygame.image.load("res/game/chef/female/level_1/Right_CarryingDirtyDishes.png")
    game_ChefFemaleLevel1_RightCarryingDirtyIngredients =      pygame.image.load("res/game/chef/female/level_1/Right_CarryingDirtyIngredients.png")
    game_ChefFemaleLevel1_RightCarryingPreparedFood =          pygame.image.load("res/game/chef/female/level_1/Right_CarryingPreparedFood.png")
    game_ChefFemaleLevel1_RightReady =                         pygame.image.load("res/game/chef/female/level_1/Right_Ready.png")
    game_ChefFemaleLevel1_RightTakingAnOrder =                 pygame.image.load("res/game/chef/female/level_1/Right_TakingAnOrder.png")
    
    # Level 2
    game_ChefFemaleLevel2_BackCarryingCleanIngredients =       pygame.image.load("res/game/chef/female/level_2/Back_CarryingCleanIngredients.png")
    game_ChefFemaleLevel2_BackCarryingDirtyDishes =            pygame.image.load("res/game/chef/female/level_2/Back_CarryingDirtyDishes.png")
    game_ChefFemaleLevel2_BackCarryingDirtyIngredients =       pygame.image.load("res/game/chef/female/level_2/Back_CarryingDirtyIngredients.png")
    game_ChefFemaleLevel2_BackCarryingPreparedFood =           pygame.image.load("res/game/chef/female/level_2/Back_CarryingPreparedFood.png")
    game_ChefFemaleLevel2_BackReady =                          pygame.image.load("res/game/chef/female/level_2/Back_Ready.png")
    game_ChefFemaleLevel2_BackTakingAnOrder =                  pygame.image.load("res/game/chef/female/level_2/Back_TakingAnOrder.png")

    game_ChefFemaleLevel2_FrontCarryingCleanIngredients =      pygame.image.load("res/game/chef/female/level_2/Front_CarryingCleanIngredients.png")
    game_ChefFemaleLevel2_FrontCarryingDirtyDishes =           pygame.image.load("res/game/chef/female/level_2/Front_CarryingDirtyDishes.png")
    game_ChefFemaleLevel2_FrontCarryingDirtyIngredients =      pygame.image.load("res/game/chef/female/level_2/Front_CarryingDirtyIngredients.png")
    game_ChefFemaleLevel2_FrontCarryingPreparedFood =          pygame.image.load("res/game/chef/female/level_2/Front_CarryingPreparedFood.png")
    game_ChefFemaleLevel2_FrontReady =                         pygame.image.load("res/game/chef/female/level_2/Front_Ready.png")
    game_ChefFemaleLevel2_FrontTakingAnOrder =                 pygame.image.load("res/game/chef/female/level_2/Front_TakingAnOrder.png")
    game_ChefFemaleLevel2_FrontDancing_0 =                     pygame.image.load("res/game/chef/female/level_2/Front_Dancing_0.png")
    game_ChefFemaleLevel2_FrontDancing_1 =                     pygame.image.load("res/game/chef/female/level_2/Front_Dancing_1.png")
    game_ChefFemaleLevel2_FrontDancing_2 =                     pygame.image.load("res/game/chef/female/level_2/Front_Dancing_2.png")

    game_ChefFemaleLevel2_LeftCarryingCleanIngredients =       pygame.image.load("res/game/chef/female/level_2/Left_CarryingCleanIngredients.png")
    game_ChefFemaleLevel2_LeftCarryingDirtyDishes =            pygame.image.load("res/game/chef/female/level_2/Left_CarryingDirtyDishes.png")
    game_ChefFemaleLevel2_LeftCarryingDirtyIngredients =       pygame.image.load("res/game/chef/female/level_2/Left_CarryingDirtyIngredients.png")
    game_ChefFemaleLevel2_LeftCarryingPreparedFood =           pygame.image.load("res/game/chef/female/level_2/Left_CarryingPreparedFood.png")
    game_ChefFemaleLevel2_LeftReady =                          pygame.image.load("res/game/chef/female/level_2/Left_Ready.png")
    game_ChefFemaleLevel2_LeftTakingAnOrder =                  pygame.image.load("res/game/chef/female/level_2/Left_TakingAnOrder.png")

    game_ChefFemaleLevel2_RightCarryingCleanIngredients =      pygame.image.load("res/game/chef/female/level_2/Right_CarryingCleanIngredients.png")
    game_ChefFemaleLevel2_RightCarryingDirtyDishes =           pygame.image.load("res/game/chef/female/level_2/Right_CarryingDirtyDishes.png")
    game_ChefFemaleLevel2_RightCarryingDirtyIngredients =      pygame.image.load("res/game/chef/female/level_2/Right_CarryingDirtyIngredients.png")
    game_ChefFemaleLevel2_RightCarryingPreparedFood =          pygame.image.load("res/game/chef/female/level_2/Right_CarryingPreparedFood.png")
    game_ChefFemaleLevel2_RightReady =                         pygame.image.load("res/game/chef/female/level_2/Right_Ready.png")
    game_ChefFemaleLevel2_RightTakingAnOrder =                 pygame.image.load("res/game/chef/female/level_2/Right_TakingAnOrder.png")
    
    
    # -> Chef Male
    
    # Level 0    
    game_ChefMaleLevel0_BackCarryingCleanIngredients =         pygame.image.load("res/game/chef/male/level_0/Back_CarryingCleanIngredients.png")
    game_ChefMaleLevel0_BackCarryingDirtyDishes =              pygame.image.load("res/game/chef/male/level_0/Back_CarryingDirtyDishes.png")
    game_ChefMaleLevel0_BackCarryingDirtyIngredients =         pygame.image.load("res/game/chef/male/level_0/Back_CarryingDirtyIngredients.png")
    game_ChefMaleLevel0_BackCarryingPreparedFood =             pygame.image.load("res/game/chef/male/level_0/Back_CarryingPreparedFood.png")
    game_ChefMaleLevel0_BackReady =                            pygame.image.load("res/game/chef/male/level_0/Back_Ready.png")
    game_ChefMaleLevel0_BackTakingAnOrder =                    pygame.image.load("res/game/chef/male/level_0/Back_TakingAnOrder.png")
                                                                                   
    game_ChefMaleLevel0_FrontCarryingCleanIngredients =        pygame.image.load("res/game/chef/male/level_0/Front_CarryingCleanIngredients.png")
    game_ChefMaleLevel0_FrontCarryingDirtyDishes =             pygame.image.load("res/game/chef/male/level_0/Front_CarryingDirtyDishes.png")
    game_ChefMaleLevel0_FrontCarryingDirtyIngredients =        pygame.image.load("res/game/chef/male/level_0/Front_CarryingDirtyIngredients.png")
    game_ChefMaleLevel0_FrontCarryingPreparedFood =            pygame.image.load("res/game/chef/male/level_0/Front_CarryingPreparedFood.png")
    game_ChefMaleLevel0_FrontReady =                           pygame.image.load("res/game/chef/male/level_0/Front_Ready.png")
    game_ChefMaleLevel0_FrontTakingAnOrder =                   pygame.image.load("res/game/chef/male/level_0/Front_TakingAnOrder.png")
    game_ChefMaleLevel0_FrontDancing_0 =                       pygame.image.load("res/game/chef/male/level_0/Front_Dancing_0.png")
    game_ChefMaleLevel0_FrontDancing_1 =                       pygame.image.load("res/game/chef/male/level_0/Front_Dancing_1.png")
    game_ChefMaleLevel0_FrontDancing_2 =                       pygame.image.load("res/game/chef/male/level_0/Front_Dancing_2.png")
                                                                                   
    game_ChefMaleLevel0_LeftCarryingCleanIngredients =         pygame.image.load("res/game/chef/male/level_0/Left_CarryingCleanIngredients.png")
    game_ChefMaleLevel0_LeftCarryingDirtyDishes =              pygame.image.load("res/game/chef/male/level_0/Left_CarryingDirtyDishes.png")
    game_ChefMaleLevel0_LeftCarryingDirtyIngredients =         pygame.image.load("res/game/chef/male/level_0/Left_CarryingDirtyIngredients.png")
    game_ChefMaleLevel0_LeftCarryingPreparedFood =             pygame.image.load("res/game/chef/male/level_0/Left_CarryingPreparedFood.png")
    game_ChefMaleLevel0_LeftReady =                            pygame.image.load("res/game/chef/male/level_0/Left_Ready.png")
    game_ChefMaleLevel0_LeftTakingAnOrder =                    pygame.image.load("res/game/chef/male/level_0/Left_TakingAnOrder.png")
                                                                                   
    game_ChefMaleLevel0_RightCarryingCleanIngredients =        pygame.image.load("res/game/chef/male/level_0/Right_CarryingCleanIngredients.png")
    game_ChefMaleLevel0_RightCarryingDirtyDishes =             pygame.image.load("res/game/chef/male/level_0/Right_CarryingDirtyDishes.png")
    game_ChefMaleLevel0_RightCarryingDirtyIngredients =        pygame.image.load("res/game/chef/male/level_0/Right_CarryingDirtyIngredients.png")
    game_ChefMaleLevel0_RightCarryingPreparedFood =            pygame.image.load("res/game/chef/male/level_0/Right_CarryingPreparedFood.png")
    game_ChefMaleLevel0_RightReady =                           pygame.image.load("res/game/chef/male/level_0/Right_Ready.png")
    game_ChefMaleLevel0_RightTakingAnOrder =                   pygame.image.load("res/game/chef/male/level_0/Right_TakingAnOrder.png")
    
    # Level 1
    game_ChefMaleLevel1_BackCarryingCleanIngredients =         pygame.image.load("res/game/chef/male/level_1/Back_CarryingCleanIngredients.png")
    game_ChefMaleLevel1_BackCarryingDirtyDishes =              pygame.image.load("res/game/chef/male/level_1/Back_CarryingDirtyDishes.png")
    game_ChefMaleLevel1_BackCarryingDirtyIngredients =         pygame.image.load("res/game/chef/male/level_1/Back_CarryingDirtyIngredients.png")
    game_ChefMaleLevel1_BackCarryingPreparedFood =             pygame.image.load("res/game/chef/male/level_1/Back_CarryingPreparedFood.png")
    game_ChefMaleLevel1_BackReady =                            pygame.image.load("res/game/chef/male/level_1/Back_Ready.png")
    game_ChefMaleLevel1_BackTakingAnOrder =                    pygame.image.load("res/game/chef/male/level_1/Back_TakingAnOrder.png")

    game_ChefMaleLevel1_FrontCarryingCleanIngredients =        pygame.image.load("res/game/chef/male/level_1/Front_CarryingCleanIngredients.png")
    game_ChefMaleLevel1_FrontCarryingDirtyDishes =             pygame.image.load("res/game/chef/male/level_1/Front_CarryingDirtyDishes.png")
    game_ChefMaleLevel1_FrontCarryingDirtyIngredients =        pygame.image.load("res/game/chef/male/level_1/Front_CarryingDirtyIngredients.png")
    game_ChefMaleLevel1_FrontCarryingPreparedFood =            pygame.image.load("res/game/chef/male/level_1/Front_CarryingPreparedFood.png")
    game_ChefMaleLevel1_FrontReady =                           pygame.image.load("res/game/chef/male/level_1/Front_Ready.png")
    game_ChefMaleLevel1_FrontTakingAnOrder =                   pygame.image.load("res/game/chef/male/level_1/Front_TakingAnOrder.png")
    game_ChefMaleLevel1_FrontDancing_0 =                       pygame.image.load("res/game/chef/male/level_1/Front_Dancing_0.png")
    game_ChefMaleLevel1_FrontDancing_1 =                       pygame.image.load("res/game/chef/male/level_1/Front_Dancing_1.png")
    game_ChefMaleLevel1_FrontDancing_2 =                       pygame.image.load("res/game/chef/male/level_1/Front_Dancing_2.png")

    game_ChefMaleLevel1_LeftCarryingCleanIngredients =         pygame.image.load("res/game/chef/male/level_1/Left_CarryingCleanIngredients.png")
    game_ChefMaleLevel1_LeftCarryingDirtyDishes =              pygame.image.load("res/game/chef/male/level_1/Left_CarryingDirtyDishes.png")
    game_ChefMaleLevel1_LeftCarryingDirtyIngredients =         pygame.image.load("res/game/chef/male/level_1/Left_CarryingDirtyIngredients.png")
    game_ChefMaleLevel1_LeftCarryingPreparedFood =             pygame.image.load("res/game/chef/male/level_1/Left_CarryingPreparedFood.png")
    game_ChefMaleLevel1_LeftReady =                            pygame.image.load("res/game/chef/male/level_1/Left_Ready.png")
    game_ChefMaleLevel1_LeftTakingAnOrder =                    pygame.image.load("res/game/chef/male/level_1/Left_TakingAnOrder.png")

    game_ChefMaleLevel1_RightCarryingCleanIngredients =        pygame.image.load("res/game/chef/male/level_1/Right_CarryingCleanIngredients.png")
    game_ChefMaleLevel1_RightCarryingDirtyDishes =             pygame.image.load("res/game/chef/male/level_1/Right_CarryingDirtyDishes.png")
    game_ChefMaleLevel1_RightCarryingDirtyIngredients =        pygame.image.load("res/game/chef/male/level_1/Right_CarryingDirtyIngredients.png")
    game_ChefMaleLevel1_RightCarryingPreparedFood =            pygame.image.load("res/game/chef/male/level_1/Right_CarryingPreparedFood.png")
    game_ChefMaleLevel1_RightReady =                           pygame.image.load("res/game/chef/male/level_1/Right_Ready.png")
    game_ChefMaleLevel1_RightTakingAnOrder =                   pygame.image.load("res/game/chef/male/level_1/Right_TakingAnOrder.png")
    
    # Level 2
    game_ChefMaleLevel2_BackCarryingCleanIngredients =         pygame.image.load("res/game/chef/male/level_2/Back_CarryingCleanIngredients.png")
    game_ChefMaleLevel2_BackCarryingDirtyDishes =              pygame.image.load("res/game/chef/male/level_2/Back_CarryingDirtyDishes.png")
    game_ChefMaleLevel2_BackCarryingDirtyIngredients =         pygame.image.load("res/game/chef/male/level_2/Back_CarryingDirtyIngredients.png")
    game_ChefMaleLevel2_BackCarryingPreparedFood =             pygame.image.load("res/game/chef/male/level_2/Back_CarryingPreparedFood.png")
    game_ChefMaleLevel2_BackReady =                            pygame.image.load("res/game/chef/male/level_2/Back_Ready.png")
    game_ChefMaleLevel2_BackTakingAnOrder =                    pygame.image.load("res/game/chef/male/level_2/Back_TakingAnOrder.png")

    game_ChefMaleLevel2_FrontCarryingCleanIngredients =        pygame.image.load("res/game/chef/male/level_2/Front_CarryingCleanIngredients.png")
    game_ChefMaleLevel2_FrontCarryingDirtyDishes =             pygame.image.load("res/game/chef/male/level_2/Front_CarryingDirtyDishes.png")
    game_ChefMaleLevel2_FrontCarryingDirtyIngredients =        pygame.image.load("res/game/chef/male/level_2/Front_CarryingDirtyIngredients.png")
    game_ChefMaleLevel2_FrontCarryingPreparedFood =            pygame.image.load("res/game/chef/male/level_2/Front_CarryingPreparedFood.png")
    game_ChefMaleLevel2_FrontReady =                           pygame.image.load("res/game/chef/male/level_2/Front_Ready.png")
    game_ChefMaleLevel2_FrontTakingAnOrder =                   pygame.image.load("res/game/chef/male/level_2/Front_TakingAnOrder.png")
    game_ChefMaleLevel2_FrontDancing_0 =                       pygame.image.load("res/game/chef/male/level_2/Front_Dancing_0.png")
    game_ChefMaleLevel2_FrontDancing_1 =                       pygame.image.load("res/game/chef/male/level_2/Front_Dancing_1.png")
    game_ChefMaleLevel2_FrontDancing_2 =                       pygame.image.load("res/game/chef/male/level_2/Front_Dancing_2.png")

    game_ChefMaleLevel2_LeftCarryingCleanIngredients =         pygame.image.load("res/game/chef/male/level_2/Left_CarryingCleanIngredients.png")
    game_ChefMaleLevel2_LeftCarryingDirtyDishes =              pygame.image.load("res/game/chef/male/level_2/Left_CarryingDirtyDishes.png")
    game_ChefMaleLevel2_LeftCarryingDirtyIngredients =         pygame.image.load("res/game/chef/male/level_2/Left_CarryingDirtyIngredients.png")
    game_ChefMaleLevel2_LeftCarryingPreparedFood =             pygame.image.load("res/game/chef/male/level_2/Left_CarryingPreparedFood.png")
    game_ChefMaleLevel2_LeftReady =                            pygame.image.load("res/game/chef/male/level_2/Left_Ready.png")
    game_ChefMaleLevel2_LeftTakingAnOrder =                    pygame.image.load("res/game/chef/male/level_2/Left_TakingAnOrder.png")

    game_ChefMaleLevel2_RightCarryingCleanIngredients =        pygame.image.load("res/game/chef/male/level_2/Right_CarryingCleanIngredients.png")
    game_ChefMaleLevel2_RightCarryingDirtyDishes =             pygame.image.load("res/game/chef/male/level_2/Right_CarryingDirtyDishes.png")
    game_ChefMaleLevel2_RightCarryingDirtyIngredients =        pygame.image.load("res/game/chef/male/level_2/Right_CarryingDirtyIngredients.png")
    game_ChefMaleLevel2_RightCarryingPreparedFood =            pygame.image.load("res/game/chef/male/level_2/Right_CarryingPreparedFood.png")
    game_ChefMaleLevel2_RightReady =                           pygame.image.load("res/game/chef/male/level_2/Right_Ready.png")
    game_ChefMaleLevel2_RightTakingAnOrder =                   pygame.image.load("res/game/chef/male/level_2/Right_TakingAnOrder.png")
    
    
    # -> Clients
    game_ClientAEating_1 = pygame.image.load("res/game/clients/PersonA_Eating_1.png")
    game_ClientAEating_2 = pygame.image.load("res/game/clients/PersonA_Eating_2.png")
    game_ClientAEating_3 = pygame.image.load("res/game/clients/PersonA_Eating_3.png")
    game_ClientALooking = pygame.image.load("res/game/clients/PersonA_Looking.png")
    game_ClientAReadingMenu_1 = pygame.image.load("res/game/clients/PersonA_ReadingMenu_1.png")
    game_ClientAReadingMenu_2 = pygame.image.load("res/game/clients/PersonA_ReadingMenu_2.png")
    game_ClientARequesting = pygame.image.load("res/game/clients/PersonA_Requesting.png")
    game_ClientAWaitingForFood = pygame.image.load("res/game/clients/PersonA_WaitingForFood.png")
    
    game_ClientBEating_1 = pygame.image.load("res/game/clients/PersonB_Eating_1.png")
    game_ClientBEating_2 = pygame.image.load("res/game/clients/PersonB_Eating_2.png")
    game_ClientBEating_3 = pygame.image.load("res/game/clients/PersonB_Eating_3.png")
    game_ClientBLooking = pygame.image.load("res/game/clients/PersonB_Looking.png")
    game_ClientBReadingMenu_1 = pygame.image.load("res/game/clients/PersonB_ReadingMenu_1.png")
    game_ClientBReadingMenu_2 = pygame.image.load("res/game/clients/PersonB_ReadingMenu_2.png")
    game_ClientBRequesting = pygame.image.load("res/game/clients/PersonB_Requesting.png")
    game_ClientBWaitingForFood = pygame.image.load("res/game/clients/PersonB_WaitingForFood.png")
    
    game_ClientCEating_1 = pygame.image.load("res/game/clients/PersonC_Eating_1.png")
    game_ClientCEating_2 = pygame.image.load("res/game/clients/PersonC_Eating_2.png")
    game_ClientCEating_3 = pygame.image.load("res/game/clients/PersonC_Eating_3.png")
    game_ClientCLooking = pygame.image.load("res/game/clients/PersonC_Looking.png")
    game_ClientCReadingMenu_1 = pygame.image.load("res/game/clients/PersonC_ReadingMenu_1.png")
    game_ClientCReadingMenu_2 = pygame.image.load("res/game/clients/PersonC_ReadingMenu_2.png")
    game_ClientCRequesting = pygame.image.load("res/game/clients/PersonC_Requesting.png")
    game_ClientCWaitingForFood = pygame.image.load("res/game/clients/PersonC_WaitingForFood.png")
    
    game_ClientDEating_1 = pygame.image.load("res/game/clients/PersonD_Eating_1.png")
    game_ClientDEating_2 = pygame.image.load("res/game/clients/PersonD_Eating_2.png")
    game_ClientDEating_3 = pygame.image.load("res/game/clients/PersonD_Eating_3.png")
    game_ClientDLooking = pygame.image.load("res/game/clients/PersonD_Looking.png")
    game_ClientDReadingMenu_1 = pygame.image.load("res/game/clients/PersonD_ReadingMenu_1.png")
    game_ClientDReadingMenu_2 = pygame.image.load("res/game/clients/PersonD_ReadingMenu_2.png")
    game_ClientDRequesting = pygame.image.load("res/game/clients/PersonD_Requesting.png")
    game_ClientDWaitingForFood = pygame.image.load("res/game/clients/PersonD_WaitingForFood.png")
    
    game_ClientEEating_1 = pygame.image.load("res/game/clients/PersonE_Eating_1.png")
    game_ClientEEating_2 = pygame.image.load("res/game/clients/PersonE_Eating_2.png")
    game_ClientEEating_3 = pygame.image.load("res/game/clients/PersonE_Eating_3.png")
    game_ClientELooking = pygame.image.load("res/game/clients/PersonE_Looking.png")
    game_ClientEReadingMenu_1 = pygame.image.load("res/game/clients/PersonE_ReadingMenu_1.png")
    game_ClientEReadingMenu_2 = pygame.image.load("res/game/clients/PersonE_ReadingMenu_2.png")
    game_ClientERequesting = pygame.image.load("res/game/clients/PersonE_Requesting.png")
    game_ClientEWaitingForFood = pygame.image.load("res/game/clients/PersonE_WaitingForFood.png")
    
    # -> Ingredients
    game_Ingredient01Arepa = pygame.image.load("res/game/ingredients/01Arepa.png")
    game_Ingredient02Arroz = pygame.image.load("res/game/ingredients/02Arroz.png")
    game_Ingredient03Avena = pygame.image.load("res/game/ingredients/03Avena.png")
    game_Ingredient04HarinaDeMaizPrecocida = pygame.image.load("res/game/ingredients/04HarinaDeMaizPrecocida.png")
    game_Ingredient05HarinaDeTrigo = pygame.image.load("res/game/ingredients/05HarinaDeTrigo.png")
    game_Ingredient06Maiz = pygame.image.load("res/game/ingredients/06Maiz.png")
    game_Ingredient07MigaDePan = pygame.image.load("res/game/ingredients/07MigaDePan.png")
    game_Ingredient08Pan = pygame.image.load("res/game/ingredients/08Pan.png")
    game_Ingredient09Papa = pygame.image.load("res/game/ingredients/09Papa.png")
    game_Ingredient10Pasta = pygame.image.load("res/game/ingredients/10Pasta.png")
    game_Ingredient11Platano = pygame.image.load("res/game/ingredients/11Platano.png")
    game_Ingredient12Soya = pygame.image.load("res/game/ingredients/12Soya.png")
    game_Ingredient13Yuca = pygame.image.load("res/game/ingredients/13Yuca.png")
    game_Ingredient14Acelga = pygame.image.load("res/game/ingredients/14Acelga.png")
    game_Ingredient15Ahuyama = pygame.image.load("res/game/ingredients/15Ahuyama.png")
    game_Ingredient16Ajo = pygame.image.load("res/game/ingredients/16Ajo.png")
    game_Ingredient17Apio = pygame.image.load("res/game/ingredients/17Apio.png")
    game_Ingredient18Arveja = pygame.image.load("res/game/ingredients/18Arveja.png")
    game_Ingredient19Brocoli = pygame.image.load("res/game/ingredients/19Brocoli.png")
    game_Ingredient20CebollaCabezona = pygame.image.load("res/game/ingredients/20CebollaCabezona.png")
    game_Ingredient21CebollaLarga = pygame.image.load("res/game/ingredients/21CebollaLarga.png")
    game_Ingredient22Cilantro = pygame.image.load("res/game/ingredients/22Cilantro.png")
    game_Ingredient23Coliflor = pygame.image.load("res/game/ingredients/23Coliflor.png")
    game_Ingredient24Espinaca = pygame.image.load("res/game/ingredients/24Espinaca.png")
    game_Ingredient25Frijol = pygame.image.load("res/game/ingredients/25Frijol.png")
    game_Ingredient26Guascas = pygame.image.load("res/game/ingredients/26Guascas.png")
    game_Ingredient27Habichuela = pygame.image.load("res/game/ingredients/27Habichuela.png")
    game_Ingredient28Lechuga = pygame.image.load("res/game/ingredients/28Lechuga.png")
    game_Ingredient29PepinoCohombro = pygame.image.load("res/game/ingredients/29PepinoCohombro.png")
    game_Ingredient30PepinoComun = pygame.image.load("res/game/ingredients/30PepinoComun.png")
    game_Ingredient31Pimenton = pygame.image.load("res/game/ingredients/31Pimenton.png")
    game_Ingredient32Tomate = pygame.image.load("res/game/ingredients/32Tomate.png")
    game_Ingredient33Zanahoria = pygame.image.load("res/game/ingredients/33Zanahoria.png")
    game_Ingredient34Aguacate = pygame.image.load("res/game/ingredients/34Aguacate.png")
    game_Ingredient35Banano = pygame.image.load("res/game/ingredients/35Banano.png")
    game_Ingredient36Curuba = pygame.image.load("res/game/ingredients/36Curuba.png")
    game_Ingredient37Fresa = pygame.image.load("res/game/ingredients/37Fresa.png")
    game_Ingredient38Guayaba = pygame.image.load("res/game/ingredients/38Guayaba.png")
    game_Ingredient39Limon = pygame.image.load("res/game/ingredients/39Limon.png")
    game_Ingredient40Mandarina = pygame.image.load("res/game/ingredients/40Mandarina.png")
    game_Ingredient41Mango = pygame.image.load("res/game/ingredients/41Mango.png")
    game_Ingredient42ManzanaVerde = pygame.image.load("res/game/ingredients/42ManzanaVerde.png")
    game_Ingredient43ManzanaRoja = pygame.image.load("res/game/ingredients/43ManzanaRoja.png")
    game_Ingredient44Maracuya = pygame.image.load("res/game/ingredients/44Maracuya.png")
    game_Ingredient45Melon = pygame.image.load("res/game/ingredients/45Melon.png")
    game_Ingredient46Mora = pygame.image.load("res/game/ingredients/46Mora.png")
    game_Ingredient47Naranja = pygame.image.load("res/game/ingredients/47Naranja.png")
    game_Ingredient48Papaya = pygame.image.load("res/game/ingredients/48Papaya.png")
    game_Ingredient49Patilla = pygame.image.load("res/game/ingredients/49Patilla.png")
    game_Ingredient50Pera = pygame.image.load("res/game/ingredients/50Pera.png")
    game_Ingredient51Pina = pygame.image.load("res/game/ingredients/51Pina.png")
    game_Ingredient52Atun = pygame.image.load("res/game/ingredients/52Atun.png")
    game_Ingredient53CarneDeCerdo = pygame.image.load("res/game/ingredients/53CarneDeCerdo.png")
    game_Ingredient54CarneDeRes = pygame.image.load("res/game/ingredients/54CarneDeRes.png")
    game_Ingredient55Garbanzo = pygame.image.load("res/game/ingredients/55Garbanzo.png")
    game_Ingredient56Higado = pygame.image.load("res/game/ingredients/56Higado.png")
    game_Ingredient57Huevo = pygame.image.load("res/game/ingredients/57Huevo.png")
    game_Ingredient58Lenteja = pygame.image.load("res/game/ingredients/58Lenteja.png")
    game_Ingredient59Menudencias = pygame.image.load("res/game/ingredients/59Menudencias.png")
    game_Ingredient60Pescado = pygame.image.load("res/game/ingredients/60Pescado.png")
    game_Ingredient61Pollo = pygame.image.load("res/game/ingredients/61Pollo.png")
    game_Ingredient62Salchicha = pygame.image.load("res/game/ingredients/62Salchicha.png")
    game_Ingredient63CremaDeLeche = pygame.image.load("res/game/ingredients/63CremaDeLeche.png")
    game_Ingredient64Kumis = pygame.image.load("res/game/ingredients/64Kumis.png")
    game_Ingredient65Leche = pygame.image.load("res/game/ingredients/65Leche.png")
    game_Ingredient66Queso = pygame.image.load("res/game/ingredients/66Queso.png")
    game_Ingredient67Yogur = pygame.image.load("res/game/ingredients/67Yogur.png")
    game_Ingredient68Aceite = pygame.image.load("res/game/ingredients/68Aceite.png")
    game_Ingredient69Mantequilla = pygame.image.load("res/game/ingredients/69Mantequilla.png")
    game_Ingredient70Margarina = pygame.image.load("res/game/ingredients/70Margarina.png")
    game_Ingredient71Azucar = pygame.image.load("res/game/ingredients/71Azucar.png")
    game_Ingredient72Chocolate = pygame.image.load("res/game/ingredients/72Chocolate.png")
    game_Ingredient73Helado = pygame.image.load("res/game/ingredients/73Helado.png")
    game_Ingredient74Panela = pygame.image.load("res/game/ingredients/74Panela.png")
    game_Ingredient75Agua = pygame.image.load("res/game/ingredients/75Agua.png")
    game_Ingredient76Mayonesa = pygame.image.load("res/game/ingredients/76Mayonesa.png")
    game_Ingredient77Mostaza = pygame.image.load("res/game/ingredients/77Mostaza.png")
    game_Ingredient78PolvoDeHornear = pygame.image.load("res/game/ingredients/78PolvoDeHornear.png")
    game_Ingredient79Sal = pygame.image.load("res/game/ingredients/79Sal.png")
    game_Ingredient80SalsaDeTomate = pygame.image.load("res/game/ingredients/80SalsaDeTomate.png")
    game_Ingredient81SopasEnCrema = pygame.image.load("res/game/ingredients/81SopasEnCrema.png")
    game_Ingredient82VinagretaDulce = pygame.image.load("res/game/ingredients/82VinagretaDulce.png")
    
    # -> Recipes (Enabled)
    game_Recipe01Albondigas = pygame.image.load("res/game/recipes/01Albondigas.png")
    game_Recipe02ArepaRellenaConQueso = pygame.image.load("res/game/recipes/02ArepaRellenaConQueso.png")
    game_Recipe03ArrozALaSuegra = pygame.image.load("res/game/recipes/03ArrozALaSuegra.png")
    game_Recipe04ArrozCampesino = pygame.image.load("res/game/recipes/04ArrozCampesino.png")
    game_Recipe05ArrozConMenudencias = pygame.image.load("res/game/recipes/05ArrozConMenudencias.png")
    game_Recipe06ArrozVegetariano = pygame.image.load("res/game/recipes/06ArrozVegetariano.png")
    game_Recipe07ArrozVerde = pygame.image.load("res/game/recipes/07ArrozVerde.png")
    game_Recipe08AvenaEnHojuelas = pygame.image.load("res/game/recipes/08AvenaEnHojuelas.png")
    game_Recipe09BrochetaDeFrutas = pygame.image.load("res/game/recipes/09BrochetaDeFrutas.png")
    game_Recipe10CaldoDePapaConCostilla = pygame.image.load("res/game/recipes/10CaldoDePapaConCostilla.png")
    game_Recipe11ChanguaDeLecheConHuevo = pygame.image.load("res/game/recipes/11ChanguaDeLecheConHuevo.png")
    game_Recipe12CremaDeCebollaCabezona = pygame.image.load("res/game/recipes/12CremaDeCebollaCabezona.png")
    game_Recipe13CroquetasDeEspinaca = pygame.image.load("res/game/recipes/13CroquetasDeEspinaca.png")
    game_Recipe14EnsaladaAlbaHit = pygame.image.load("res/game/recipes/14EnsaladaAlbaHit.png")
    game_Recipe15EnsaladaCarlos = pygame.image.load("res/game/recipes/15EnsaladaCarlos.png")
    game_Recipe16EnsaladaCriolla = pygame.image.load("res/game/recipes/16EnsaladaCriolla.png")
    game_Recipe17EnsaladaDeColores = pygame.image.load("res/game/recipes/17EnsaladaDeColores.png")
    game_Recipe18EnsaladaDeFrutasConYogurt = pygame.image.load("res/game/recipes/18EnsaladaDeFrutasConYogurt.png")
    game_Recipe19EnsaladaDeLaCasa = pygame.image.load("res/game/recipes/19EnsaladaDeLaCasa.png")
    game_Recipe20EnsaladaDelHuerto = pygame.image.load("res/game/recipes/20EnsaladaDelHuerto.png")
    game_Recipe21EnsaladaFriaDePapaConPollo = pygame.image.load("res/game/recipes/21EnsaladaFriaDePapaConPollo.png")
    game_Recipe22EnsaladaRanchera = pygame.image.load("res/game/recipes/22EnsaladaRanchera.png")
    game_Recipe23GuarapoDePina = pygame.image.load("res/game/recipes/23GuarapoDePina.png")
    game_Recipe24GuisoDeCarneYVerdura = pygame.image.load("res/game/recipes/24GuisoDeCarneYVerdura.png")
    game_Recipe25GuisoDeHabichuelaConCarne = pygame.image.load("res/game/recipes/25GuisoDeHabichuelaConCarne.png")
    game_Recipe26Hamburguesa = pygame.image.load("res/game/recipes/26Hamburguesa.png")
    game_Recipe27HuevoTibio = pygame.image.load("res/game/recipes/27HuevoTibio.png")
    game_Recipe28JugoDeMaracuyaYZanahoria = pygame.image.load("res/game/recipes/28JugoDeMaracuyaYZanahoria.png")
    game_Recipe29JugoDePapayaConZanahoria = pygame.image.load("res/game/recipes/29JugoDePapayaConZanahoria.png")
    game_Recipe30LomoDeCerdoEnSalsaDeMango = pygame.image.load("res/game/recipes/30LomoDeCerdoEnSalsaDeMango.png")
    game_Recipe31LomoDeCerdoEnchilado = pygame.image.load("res/game/recipes/31LomoDeCerdoEnchilado.png")
    game_Recipe32MacarronesConAtun = pygame.image.load("res/game/recipes/32MacarronesConAtun.png")
    game_Recipe33PastaConVegetales = pygame.image.load("res/game/recipes/33PastaConVegetales.png")
    game_Recipe34PataconesConCarneDesmechada = pygame.image.load("res/game/recipes/34PataconesConCarneDesmechada.png")
    game_Recipe35PepinosRellenos = pygame.image.load("res/game/recipes/35PepinosRellenos.png")
    game_Recipe36PerroCaliente = pygame.image.load("res/game/recipes/36PerroCaliente.png")
    game_Recipe37PescadoALaPrimavera = pygame.image.load("res/game/recipes/37PescadoALaPrimavera.png")
    game_Recipe38PescadoOriental = pygame.image.load("res/game/recipes/38PescadoOriental.png")
    game_Recipe39PolloALaJardinera = pygame.image.load("res/game/recipes/39PolloALaJardinera.png")
    game_Recipe40QuesoDePina = pygame.image.load("res/game/recipes/40QuesoDePina.png")
    game_Recipe41RefrescoDeManzana = pygame.image.load("res/game/recipes/41RefrescoDeManzana.png")
    game_Recipe42Salchipapas = pygame.image.load("res/game/recipes/42Salchipapas.png")
    game_Recipe43SandwichDeJamonYQueso = pygame.image.load("res/game/recipes/43SandwichDeJamonYQueso.png")
    game_Recipe44SopaDeGarbanzo = pygame.image.load("res/game/recipes/44SopaDeGarbanzo.png")
    game_Recipe45SopaDeLentejas = pygame.image.load("res/game/recipes/45SopaDeLentejas.png")
    game_Recipe46SopaDeVerduras = pygame.image.load("res/game/recipes/46SopaDeVerduras.png")
    game_Recipe47TeDeMango = pygame.image.load("res/game/recipes/47TeDeMango.png")
    game_Recipe48TerneraALaMarinera = pygame.image.load("res/game/recipes/48TerneraALaMarinera.png")
    game_Recipe49TomatesRellenos = pygame.image.load("res/game/recipes/49TomatesRellenos.png")
    game_Recipe50TortaDeAhuyama = pygame.image.load("res/game/recipes/50TortaDeAhuyama.png")
    game_Recipe51TortaDeBanano = pygame.image.load("res/game/recipes/51TortaDeBanano.png")
    game_Recipe52TortaDeZanahoria = pygame.image.load("res/game/recipes/52TortaDeZanahoria.png")
    game_Recipe53TortillaDeAcelga = pygame.image.load("res/game/recipes/53TortillaDeAcelga.png")
    game_Recipe54TortillaDeEspinaca = pygame.image.load("res/game/recipes/54TortillaDeEspinaca.png")
    game_Recipe55Zafresco = pygame.image.load("res/game/recipes/55Zafresco.png")
    
    game_Recipe56TortillaDeMazorca = pygame.image.load("res/game/recipes/56TortillaDeMazorca.png")
    game_Recipe57BatidoDeGuayabaYAvena = pygame.image.load("res/game/recipes/57BatidoDeGuayabaYAvena.png")
    game_Recipe58BatidoDeYogurtFresasYAvena = pygame.image.load("res/game/recipes/58BatidoDeYogurtFresasYAvena.png")
    game_Recipe59PanquequesDeAvena = pygame.image.load("res/game/recipes/59PanquequesDeAvena.png")
    game_Recipe60TortillaDeVerdurasYQueso = pygame.image.load("res/game/recipes/60TortillaDeVerdurasYQueso.png")
    game_Recipe61PanquequesDeFruta = pygame.image.load("res/game/recipes/61PanquequesDeFruta.png")
    game_Recipe62ArepasDeMazorca = pygame.image.load("res/game/recipes/62ArepasDeMazorca.png")
    
    

    # -> Recipes (Disabled)
    game_Recipe01AlbondigasDisabled = pygame.image.load("res/game/recipesDisabled/01Albondigas.png")
    game_Recipe02ArepaRellenaConQuesoDisabled = pygame.image.load("res/game/recipesDisabled/02ArepaRellenaConQueso.png")
    game_Recipe03ArrozALaSuegraDisabled = pygame.image.load("res/game/recipesDisabled/03ArrozALaSuegra.png")
    game_Recipe04ArrozCampesinoDisabled = pygame.image.load("res/game/recipesDisabled/04ArrozCampesino.png")
    game_Recipe05ArrozConMenudenciasDisabled = pygame.image.load("res/game/recipesDisabled/05ArrozConMenudencias.png")
    game_Recipe06ArrozVegetarianoDisabled = pygame.image.load("res/game/recipesDisabled/06ArrozVegetariano.png")
    game_Recipe07ArrozVerdeDisabled = pygame.image.load("res/game/recipesDisabled/07ArrozVerde.png")
    game_Recipe08AvenaEnHojuelasDisabled = pygame.image.load("res/game/recipesDisabled/08AvenaEnHojuelas.png")
    game_Recipe09BrochetaDeFrutasDisabled = pygame.image.load("res/game/recipesDisabled/09BrochetaDeFrutas.png")
    game_Recipe10CaldoDePapaConCostillaDisabled = pygame.image.load("res/game/recipesDisabled/10CaldoDePapaConCostilla.png")
    game_Recipe11ChanguaDeLecheConHuevoDisabled = pygame.image.load("res/game/recipesDisabled/11ChanguaDeLecheConHuevo.png")
    game_Recipe12CremaDeCebollaCabezonaDisabled = pygame.image.load("res/game/recipesDisabled/12CremaDeCebollaCabezona.png")
    game_Recipe13CroquetasDeEspinacaDisabled = pygame.image.load("res/game/recipesDisabled/13CroquetasDeEspinaca.png")
    game_Recipe14EnsaladaAlbaHitDisabled = pygame.image.load("res/game/recipesDisabled/14EnsaladaAlbaHit.png")
    game_Recipe15EnsaladaCarlosDisabled = pygame.image.load("res/game/recipesDisabled/15EnsaladaCarlos.png")
    game_Recipe16EnsaladaCriollaDisabled = pygame.image.load("res/game/recipesDisabled/16EnsaladaCriolla.png")
    game_Recipe17EnsaladaDeColoresDisabled = pygame.image.load("res/game/recipesDisabled/17EnsaladaDeColores.png")
    game_Recipe18EnsaladaDeFrutasConYogurtDisabled = pygame.image.load("res/game/recipesDisabled/18EnsaladaDeFrutasConYogurt.png")
    game_Recipe19EnsaladaDeLaCasaDisabled = pygame.image.load("res/game/recipesDisabled/19EnsaladaDeLaCasa.png")
    game_Recipe20EnsaladaDelHuertoDisabled = pygame.image.load("res/game/recipesDisabled/20EnsaladaDelHuerto.png")
    game_Recipe21EnsaladaFriaDePapaConPolloDisabled = pygame.image.load("res/game/recipesDisabled/21EnsaladaFriaDePapaConPollo.png")
    game_Recipe22EnsaladaRancheraDisabled = pygame.image.load("res/game/recipesDisabled/22EnsaladaRanchera.png")
    game_Recipe23GuarapoDePinaDisabled = pygame.image.load("res/game/recipesDisabled/23GuarapoDePina.png")
    game_Recipe24GuisoDeCarneYVerduraDisabled = pygame.image.load("res/game/recipesDisabled/24GuisoDeCarneYVerdura.png")
    game_Recipe25GuisoDeHabichuelaConCarneDisabled = pygame.image.load("res/game/recipesDisabled/25GuisoDeHabichuelaConCarne.png")
    game_Recipe26HamburguesaDisabled = pygame.image.load("res/game/recipesDisabled/26Hamburguesa.png")
    game_Recipe27HuevoTibioDisabled = pygame.image.load("res/game/recipesDisabled/27HuevoTibio.png")
    game_Recipe28JugoDeMaracuyaYZanahoriaDisabled = pygame.image.load("res/game/recipesDisabled/28JugoDeMaracuyaYZanahoria.png")
    game_Recipe29JugoDePapayaConZanahoriaDisabled = pygame.image.load("res/game/recipesDisabled/29JugoDePapayaConZanahoria.png")
    game_Recipe30LomoDeCerdoEnSalsaDeMangoDisabled = pygame.image.load("res/game/recipesDisabled/30LomoDeCerdoEnSalsaDeMango.png")
    game_Recipe31LomoDeCerdoEnchiladoDisabled = pygame.image.load("res/game/recipesDisabled/31LomoDeCerdoEnchilado.png")
    game_Recipe32MacarronesConAtunDisabled = pygame.image.load("res/game/recipesDisabled/32MacarronesConAtun.png")
    game_Recipe33PastaConVegetalesDisabled = pygame.image.load("res/game/recipesDisabled/33PastaConVegetales.png")
    game_Recipe34PataconesConCarneDesmechadaDisabled = pygame.image.load("res/game/recipesDisabled/34PataconesConCarneDesmechada.png")
    game_Recipe35PepinosRellenosDisabled = pygame.image.load("res/game/recipesDisabled/35PepinosRellenos.png")
    game_Recipe36PerroCalienteDisabled = pygame.image.load("res/game/recipesDisabled/36PerroCaliente.png")
    game_Recipe37PescadoALaPrimaveraDisabled = pygame.image.load("res/game/recipesDisabled/37PescadoALaPrimavera.png")
    game_Recipe38PescadoOrientalDisabled = pygame.image.load("res/game/recipesDisabled/38PescadoOriental.png")
    game_Recipe39PolloALaJardineraDisabled = pygame.image.load("res/game/recipesDisabled/39PolloALaJardinera.png")
    game_Recipe40QuesoDePinaDisabled = pygame.image.load("res/game/recipesDisabled/40QuesoDePina.png")
    game_Recipe41RefrescoDeManzanaDisabled = pygame.image.load("res/game/recipesDisabled/41RefrescoDeManzana.png")
    game_Recipe42SalchipapasDisabled = pygame.image.load("res/game/recipesDisabled/42Salchipapas.png")
    game_Recipe43SandwichDeJamonYQuesoDisabled = pygame.image.load("res/game/recipesDisabled/43SandwichDeJamonYQueso.png")
    game_Recipe44SopaDeGarbanzoDisabled = pygame.image.load("res/game/recipesDisabled/44SopaDeGarbanzo.png")
    game_Recipe45SopaDeLentejasDisabled = pygame.image.load("res/game/recipesDisabled/45SopaDeLentejas.png")
    game_Recipe46SopaDeVerdurasDisabled = pygame.image.load("res/game/recipesDisabled/46SopaDeVerduras.png")
    game_Recipe47TeDeMangoDisabled = pygame.image.load("res/game/recipesDisabled/47TeDeMango.png")
    game_Recipe48TerneraALaMarineraDisabled = pygame.image.load("res/game/recipesDisabled/48TerneraALaMarinera.png")
    game_Recipe49TomatesRellenosDisabled = pygame.image.load("res/game/recipesDisabled/49TomatesRellenos.png")
    game_Recipe50TortaDeAhuyamaDisabled = pygame.image.load("res/game/recipesDisabled/50TortaDeAhuyama.png")
    game_Recipe51TortaDeBananoDisabled = pygame.image.load("res/game/recipesDisabled/51TortaDeBanano.png")
    game_Recipe52TortaDeZanahoriaDisabled = pygame.image.load("res/game/recipesDisabled/52TortaDeZanahoria.png")
    game_Recipe53TortillaDeAcelgaDisabled = pygame.image.load("res/game/recipesDisabled/53TortillaDeAcelga.png")
    game_Recipe54TortillaDeEspinacaDisabled = pygame.image.load("res/game/recipesDisabled/54TortillaDeEspinaca.png")
    game_Recipe55ZafrescoDisabled = pygame.image.load("res/game/recipesDisabled/55Zafresco.png")

    game_Recipe56TortillaDeMazorcaDisabled = pygame.image.load("res/game/recipesDisabled/56TortillaDeMazorca.png")
    game_Recipe57BatidoDeGuayabaYAvenaDisabled = pygame.image.load("res/game/recipesDisabled/57BatidoDeGuayabaYAvena.png")
    game_Recipe58BatidoDeYogurtFresasYAvenaDisabled = pygame.image.load("res/game/recipesDisabled/58BatidoDeYogurtFresasYAvena.png")
    game_Recipe59PanquequesDeAvenaDisabled = pygame.image.load("res/game/recipesDisabled/59PanquequesDeAvena.png")
    game_Recipe60TortillaDeVerdurasYQuesoDisabled = pygame.image.load("res/game/recipesDisabled/60TortillaDeVerdurasYQueso.png")
    game_Recipe61PanquequesDeFrutaDisabled = pygame.image.load("res/game/recipesDisabled/61PanquequesDeFruta.png")
    game_Recipe62ArepasDeMazorcaDisabled = pygame.image.load("res/game/recipesDisabled/62ArepasDeMazorca.png")

class FontController:

    font5 = None
    font10 = None
    font15 = None
    font16 = None
    font17 = None
    font18 = None
    font19 = None
    font20 = None
    font21 = None
    font22 = None
    font23 = None
    font24 = None
    font25 = None
    font26 = None
    font27 = None
    font28 = None
    font29 = None
    font30 = None
    font35 = None
    font40 = None
    font60 = None
    font100 = None
    
    @staticmethod
    def doInit():
        FontController.font5 = pygame.font.Font(ResourceController.font_BorisBlackBloxx, 5)
        FontController.font10 = pygame.font.Font(ResourceController.font_BorisBlackBloxx, 10)
        FontController.font15 = pygame.font.Font(ResourceController.font_BorisBlackBloxx, 15)
        FontController.font16 = pygame.font.Font(ResourceController.font_BorisBlackBloxx, 16)
        FontController.font17 = pygame.font.Font(ResourceController.font_BorisBlackBloxx, 17)
        FontController.font18 = pygame.font.Font(ResourceController.font_BorisBlackBloxx, 18)
        FontController.font19 = pygame.font.Font(ResourceController.font_BorisBlackBloxx, 19)
        FontController.font20 = pygame.font.Font(ResourceController.font_BorisBlackBloxx, 20)
        FontController.font21 = pygame.font.Font(ResourceController.font_BorisBlackBloxx, 21)
        FontController.font22 = pygame.font.Font(ResourceController.font_BorisBlackBloxx, 22)
        FontController.font23 = pygame.font.Font(ResourceController.font_BorisBlackBloxx, 23)
        FontController.font24 = pygame.font.Font(ResourceController.font_BorisBlackBloxx, 24)
        FontController.font25 = pygame.font.Font(ResourceController.font_BorisBlackBloxx, 25)
        FontController.font26 = pygame.font.Font(ResourceController.font_BorisBlackBloxx, 26)
        FontController.font27 = pygame.font.Font(ResourceController.font_BorisBlackBloxx, 27)
        FontController.font28 = pygame.font.Font(ResourceController.font_BorisBlackBloxx, 28)
        FontController.font29 = pygame.font.Font(ResourceController.font_BorisBlackBloxx, 29)
        FontController.font30 = pygame.font.Font(ResourceController.font_BorisBlackBloxx, 30)
        FontController.font35 = pygame.font.Font(ResourceController.font_BorisBlackBloxx, 35)
        FontController.font40 = pygame.font.Font(ResourceController.font_BorisBlackBloxx, 40)
        FontController.font60 = pygame.font.Font(ResourceController.font_BorisBlackBloxx, 60)
        FontController.font100 = pygame.font.Font(ResourceController.font_BorisBlackBloxx, 100)
   
        
class ConnectionController(threading.Thread):
    
    def __init__(self, method, url, parameters):
        threading.Thread.__init__(self)
        self.__method = method
        self.__url = url
        self.__parameters = parameters
        self.__state = None
        self.__result = None
  
    def run(self):
        
        # Comienza el proceso de conexion
        self.__state = eConnectionState.CONNECTING
        
        # Hacemos la solicitud por POST
        if self.__method == eConnectionMethod.POST:
            
            try:
                
                ''' self.__result = urllib.request.urlopen(self.__url, self.__parameters).read() '''
                self.__result = urllib.urlopen(self.__url, self.__parameters).read()
                
                self.__state = eConnectionState.SUCCESS
            except: 
                self.__state = eConnectionState.FAILURE
                
            
            
    def getResult(self):
        return self.__result
        
    def getState(self):        
        return self.__state
    

class GlobalsController:
    
    # Game
    GAME_ID = 0  # 0 = Super Chef
    GAME_FPS = 40
    
    # Info for persistence (Datos iniciales para detectar errores)
    INFO_USERNAME = "None"
    INFO_PASSWORD = "None"
    INFO_ROOT_USER_ID = -1
    INFO_LEAF_USER_ID = -1
    INFO_START_TIME = "None"
    INFO_FINISH_TIME = "None"
    INFO_STARS = 0
    
    # Audio
    AUDIO_FREQ = 44100  # same as audio CD
    AUDIO_BITSIZE = -16  # unsigned 16 bit
    AUDIO_CHANNELS = 2  # 1 == mono, 2 == stereo
    AUDIO_BUFFER = 1024  # audio buffer size in no. of samples
    AUDIO_FRAMERATE = 30  # how often to check if playback has finished
    
    # Chef
    CHEF_MOTION_UNIT = 60  # 46
    CHEF_GENDER = eCharacterGender.MALE
    
    # Tutorial
    SHOW_TUTORIAL = False
    
    # Display (xo display size)
    DISPLAY_WIDTH = 1200
    DISPLAY_HEIGHT = 900 - 75


class MusicThread(threading.Thread):
    
    def __init__(self, musicId):
        
        threading.Thread.__init__(self)
        
        if musicId == eMusic.MIX:
            self.__musicFile = ResourceController.music_Mix
            pygame.mixer.music.set_volume(0.15)
        elif musicId == eMusic.PICKING:
            self.__musicFile = ResourceController.music_Picking
            pygame.mixer.music.set_volume(0.15)
        elif musicId == eMusic.QUIET:
            self.__musicFile = ResourceController.music_Quiet
            pygame.mixer.music.set_volume(0.9)
        elif musicId == eMusic.RESTAURANT:
            self.__musicFile = ResourceController.music_Restaurant
            pygame.mixer.music.set_volume(0.15)
        
        self.__noRepetitions = -1  # (-1 : Reproduccion continua)
        self.__isPlaying = False
  
    def run(self):
        # Stream music with mixer.music module in blocking manner.
        # This will stream the sound from disk while playing.
        pygame.mixer.music.load(self.__musicFile)
        pygame.mixer.music.play(self.__noRepetitions)
        self.__isPlaying = False
        
        clock = pygame.time.Clock()
        while (self.__isPlaying == True) and (pygame.mixer.music.get_busy()):
            clock.tick(GlobalsController.AUDIO_FRAMERATE)
        
    def stop(self):
        pygame.mixer.music.stop()
        self.__isPlaying = False
          
          
class SoundThread(threading.Thread):
    
    def __init__(self, soundFile, noRepetitions):
        
        threading.Thread.__init__(self)
        self.__soundFile = soundFile
        self.__isPlaying = False
        
        if noRepetitions > 0:
            self.__noRepetitions = noRepetitions - 1
        else:
            self.__noRepetitions = 0
    
    def run(self):
        
        # Play sound through default mixer channel in blocking manner.
        # This will load the whole sound into memory before playback
        self.__soundFile.play(self.__noRepetitions)
        self.__isPlaying = True
        
        clock = pygame.time.Clock()
        while pygame.mixer.get_busy():
            clock.tick(GlobalsController.AUDIO_FRAMERATE)
            
        self.__isPlaying = False

    def stop(self):
        pygame.mixer.stop()
        self.__isPlaying = False
        
    def isPlaying(self):
        return self.__isPlaying


class AudioController:

    __musicThread = None
    
    __soundThreadBell = None
    __soundThreadClickIngredientSelection = None
    __soundThreadCookingHot = None
    __soundThreadCookingCold = None
    __soundThreadFoodServed = None
    __soundThreadFoodTimeChange = None
    __soundThreadFridge = None
    __soundThreadIngredientDelete = None
    __soundThreadIngredientSelect = None
    __soundThreadIngredientsMakeRecipe = None
    __soundThreadLevelPassed = None
    __soundThreadOrder = None
    __soundThreadPickDirtyDish = None
    __soundThreadWashing = None
    __soundThreadWashingDishes = None
    
    __soundThreadHelloBoy = None
    __soundThreadHelloGirl = None
    __soundThreadLevelWin = None
    __soundThreadYujuBoy = None
    __soundThreadYujuGirl = None
    
    @staticmethod
    def playSound(soundId, noRepetitions):
        
        # Detenemos los hilos que ya no estan reproduciendo un sonido
        AudioController.__cleanNonActiveThreads()
        
        # Detenemos el hilo que esta utilizando el sonido que se quiere reproducir
        AudioController.stopSound(soundId)
        
        # Reproduciomos el sonido solicitado
        if soundId == eSound.BELL:
            AudioController.__soundThreadBell = SoundThread(ResourceController.soundBell, noRepetitions)
            AudioController.__soundThreadBell.start()
            
        elif soundId == eSound.CLICK_INGREDIENT_SELECTION:
            AudioController.__soundThreadClickIngredientSelection = SoundThread(ResourceController.soundClickIngredientSelection, noRepetitions)
            AudioController.__soundThreadClickIngredientSelection.start()
            
        elif soundId == eSound.COOKING_HOT:
            AudioController.__soundThreadCookingHot = SoundThread(ResourceController.soundCookingHot, noRepetitions)
            AudioController.__soundThreadCookingHot.start()
            
        elif soundId == eSound.COOKING_COLD:
            AudioController.__soundThreadCookingCold = SoundThread(ResourceController.soundCookingCold, noRepetitions)
            AudioController.__soundThreadCookingCold.start()
            
        elif soundId == eSound.FOOD_SERVED:
            AudioController.__soundThreadFoodServed = SoundThread(ResourceController.soundFoodServed, noRepetitions)
            AudioController.__soundThreadFoodServed.start()
            
        elif soundId == eSound.FOOD_TIME_CHANGE:
            AudioController.__soundThreadFoodTimeChange = SoundThread(ResourceController.soundFoodTimeChange, noRepetitions)
            AudioController.__soundThreadFoodTimeChange.start()
            
        elif soundId == eSound.FRIDGE:
            AudioController.__soundThreadFridge = SoundThread(ResourceController.soundFridge, noRepetitions)
            AudioController.__soundThreadFridge.start()
            
        elif soundId == eSound.INGREDIENT_DELETE:
            AudioController.__soundThreadIngredientDelete = SoundThread(ResourceController.soundIngredientDelete, noRepetitions)
            AudioController.__soundThreadIngredientDelete.start()
            
        elif soundId == eSound.INGREDIENT_SELECT:
            AudioController.__soundThreadIngredientSelect = SoundThread(ResourceController.soundIngredientSelect, noRepetitions)
            AudioController.__soundThreadIngredientSelect.start()
            
        elif soundId == eSound.INGREDIENTS_MAKE_RECIPE:
            AudioController.__soundThreadIngredientsMakeRecipe = SoundThread(ResourceController.soundIngredientsMakeRecipe, noRepetitions)
            AudioController.__soundThreadIngredientsMakeRecipe.start()
            
        elif soundId == eSound.LEVEL_PASSED:
            AudioController.__soundThreadLevelPassed = SoundThread(ResourceController.soundLevelPassed, noRepetitions)
            AudioController.__soundThreadLevelPassed.start()
            
        elif soundId == eSound.ORDER:
            AudioController.__soundThreadOrder = SoundThread(ResourceController.soundOrder, noRepetitions)
            AudioController.__soundThreadOrder.start()
            
        elif soundId == eSound.PICK_DIRTY_DISH:
            AudioController.__soundThreadPickDirtyDish = SoundThread(ResourceController.soundPickDirtyDish, noRepetitions)
            AudioController.__soundThreadPickDirtyDish.start()
            
        elif soundId == eSound.WASHING:
            AudioController.__soundThreadWashing = SoundThread(ResourceController.soundWashing, noRepetitions)
            AudioController.__soundThreadWashing.start()
            
        elif soundId == eSound.WASHING_DISHES:
            AudioController.__soundThreadWashingDishes = SoundThread(ResourceController.soundWashingDishes, noRepetitions)
            AudioController.__soundThreadWashingDishes.start()            
            
            
        elif soundId == eSound.HELLO_BOY:
            AudioController.__soundThreadHelloBoy = SoundThread(ResourceController.soundHelloBoy, noRepetitions)
            AudioController.__soundThreadHelloBoy.start()
                                    
        elif soundId == eSound.HELLO_GIRL:
            AudioController.__soundThreadHelloGirl = SoundThread(ResourceController.soundHelloGirl, noRepetitions)
            AudioController.__soundThreadHelloGirl.start()
                                    
        elif soundId == eSound.LEVEL_WIN:
            AudioController.__soundThreadLevelWin = SoundThread(ResourceController.soundLevelWin, noRepetitions)
            AudioController.__soundThreadLevelWin.start()
                                    
        elif soundId == eSound.YUJU_BOY:
            AudioController.__soundThreadYujuBoy = SoundThread(ResourceController.soundYujuBoy, noRepetitions)
            AudioController.__soundThreadYujuBoy.start()
                                    
        elif soundId == eSound.YUJU_GIRL:
            AudioController.__soundThreadYujuGirl = SoundThread(ResourceController.soundYujuGirl, noRepetitions)
            AudioController.__soundThreadYujuGirl.start()

    @staticmethod
    def __cleanNonActiveThreads():
        if (AudioController.__soundThreadBell != None) and (AudioController.__soundThreadBell.isPlaying() == False):
            AudioController.stopSound(eSound.BELL)
        if (AudioController.__soundThreadClickIngredientSelection != None) and (AudioController.__soundThreadClickIngredientSelection.isPlaying() == False):
            AudioController.stopSound(eSound.CLICK_INGREDIENT_SELECTION)
        if (AudioController.__soundThreadCookingHot != None) and (AudioController.__soundThreadCookingHot.isPlaying() == False):
            AudioController.stopSound(eSound.COOKING_HOT)
        if (AudioController.__soundThreadCookingCold != None) and (AudioController.__soundThreadCookingCold.isPlaying() == False):
            AudioController.stopSound(eSound.COOKING_COLD)
        if (AudioController.__soundThreadFoodServed != None) and (AudioController.__soundThreadFoodServed.isPlaying() == False):
            AudioController.stopSound(eSound.FOOD_SERVED)
        if (AudioController.__soundThreadFoodTimeChange != None) and (AudioController.__soundThreadFoodTimeChange.isPlaying() == False):
            AudioController.stopSound(eSound.FOOD_TIME_CHANGE)
        if (AudioController.__soundThreadFridge != None) and (AudioController.__soundThreadFridge.isPlaying() == False):
            AudioController.stopSound(eSound.FRIDGE)
        if (AudioController.__soundThreadIngredientDelete != None) and (AudioController.__soundThreadIngredientDelete.isPlaying() == False):
            AudioController.stopSound(eSound.INGREDIENT_DELETE)
        if (AudioController.__soundThreadIngredientSelect != None) and (AudioController.__soundThreadIngredientSelect.isPlaying() == False):
            AudioController.stopSound(eSound.INGREDIENT_SELECT)
        if (AudioController.__soundThreadIngredientsMakeRecipe != None) and (AudioController.__soundThreadIngredientsMakeRecipe.isPlaying() == False):
            AudioController.stopSound(eSound.INGREDIENTS_MAKE_RECIPE)
        if (AudioController.__soundThreadLevelPassed != None) and (AudioController.__soundThreadLevelPassed.isPlaying() == False):
            AudioController.stopSound(eSound.LEVEL_PASSED)
        if (AudioController.__soundThreadOrder != None) and (AudioController.__soundThreadOrder.isPlaying() == False):
            AudioController.stopSound(eSound.ORDER)
        if (AudioController.__soundThreadPickDirtyDish != None) and (AudioController.__soundThreadPickDirtyDish.isPlaying() == False):
            AudioController.stopSound(eSound.PICK_DIRTY_DISH)
        if (AudioController.__soundThreadWashing != None) and (AudioController.__soundThreadWashing.isPlaying() == False):
            AudioController.stopSound(eSound.WASHING)
        if (AudioController.__soundThreadWashingDishes != None) and (AudioController.__soundThreadWashingDishes.isPlaying() == False):
            AudioController.stopSound(eSound.WASHING_DISHES)
            
        if (AudioController.__soundThreadHelloBoy != None) and (AudioController.__soundThreadHelloBoy.isPlaying() == False):
            AudioController.stopSound(eSound.HELLO_BOY)
        if (AudioController.__soundThreadHelloGirl != None) and (AudioController.__soundThreadHelloGirl.isPlaying() == False):
            AudioController.stopSound(eSound.HELLO_GIRL)
        if (AudioController.__soundThreadLevelWin != None) and (AudioController.__soundThreadLevelWin.isPlaying() == False):
            AudioController.stopSound(eSound.LEVEL_WIN)
        if (AudioController.__soundThreadYujuBoy != None) and (AudioController.__soundThreadYujuBoy.isPlaying() == False):
            AudioController.stopSound(eSound.YUJU_BOY)
        if (AudioController.__soundThreadYujuGirl != None) and (AudioController.__soundThreadYujuGirl.isPlaying() == False):
            AudioController.stopSound(eSound.YUJU_GIRL)

    @staticmethod
    def stopSound(soundId):
        
        if soundId == eSound.BELL:
            if AudioController.__soundThreadBell != None:
                AudioController.__soundThreadBell.stop()
                AudioController.__soundThreadBell = None
        
        elif soundId == eSound.CLICK_INGREDIENT_SELECTION:
            if AudioController.__soundThreadClickIngredientSelection != None:
                AudioController.__soundThreadClickIngredientSelection.stop()
                AudioController.__soundThreadClickIngredientSelection = None
                
        elif soundId == eSound.COOKING_HOT:
            if AudioController.__soundThreadCookingHot != None:
                AudioController.__soundThreadCookingHot.stop()
                AudioController.__soundThreadCookingHot = None
                
        elif soundId == eSound.COOKING_COLD:
            if AudioController.__soundThreadCookingCold != None:
                AudioController.__soundThreadCookingCold.stop()
                AudioController.__soundThreadCookingCold = None
                
        elif soundId == eSound.FOOD_SERVED:
            if AudioController.__soundThreadFoodServed != None:
                AudioController.__soundThreadFoodServed.stop()
                AudioController.__soundThreadFoodServed = None
                
        elif soundId == eSound.FOOD_TIME_CHANGE:
            if AudioController.__soundThreadFoodTimeChange != None:
                AudioController.__soundThreadFoodTimeChange.stop()
                AudioController.__soundThreadFoodTimeChange = None
                
        elif soundId == eSound.FRIDGE:
            if AudioController.__soundThreadFridge != None:
                AudioController.__soundThreadFridge.stop()
                AudioController.__soundThreadFridge = None
                
        elif soundId == eSound.INGREDIENT_DELETE:
            if AudioController.__soundThreadIngredientDelete != None:
                AudioController.__soundThreadIngredientDelete.stop()
                AudioController.__soundThreadIngredientDelete = None
                
        elif soundId == eSound.INGREDIENT_SELECT:
            if AudioController.__soundThreadIngredientSelect != None:
                AudioController.__soundThreadIngredientSelect.stop()
                AudioController.__soundThreadIngredientSelect = None
                
        elif soundId == eSound.INGREDIENTS_MAKE_RECIPE:
            if AudioController.__soundThreadIngredientsMakeRecipe != None:
                AudioController.__soundThreadIngredientsMakeRecipe.stop()
                AudioController.__soundThreadIngredientsMakeRecipe = None
                
        elif soundId == eSound.LEVEL_PASSED:
            if AudioController.__soundThreadLevelPassed != None:
                AudioController.__soundThreadLevelPassed.stop()
                AudioController.__soundThreadLevelPassed = None
                
        elif soundId == eSound.ORDER:
            if AudioController.__soundThreadOrder != None:
                AudioController.__soundThreadOrder.stop()
                AudioController.__soundThreadOrder = None
                
        elif soundId == eSound.PICK_DIRTY_DISH:
            if AudioController.__soundThreadPickDirtyDish != None:
                AudioController.__soundThreadPickDirtyDish.stop()
                AudioController.__soundThreadPickDirtyDish = None
                
        elif soundId == eSound.WASHING:
            if AudioController.__soundThreadWashing != None:
                AudioController.__soundThreadWashing.stop()
                AudioController.__soundThreadWashing = None
                
        elif soundId == eSound.WASHING_DISHES:
            if AudioController.__soundThreadWashingDishes != None:
                AudioController.__soundThreadWashingDishes.stop()
                AudioController.__soundThreadWashingDishes = None
                
                                
        elif soundId == eSound.HELLO_BOY:
            if AudioController.__soundThreadHelloBoy != None:
                AudioController.__soundThreadHelloBoy.stop()
                AudioController.__soundThreadHelloBoy = None
                                
        elif soundId == eSound.HELLO_GIRL:
            if AudioController.__soundThreadHelloGirl != None:
                AudioController.__soundThreadHelloGirl.stop()
                AudioController.__soundThreadHelloGirl = None
                                
        elif soundId == eSound.LEVEL_WIN:
            if AudioController.__soundThreadLevelWin != None:
                AudioController.__soundThreadLevelWin.stop()
                AudioController.__soundThreadLevelWin = None
                                
        elif soundId == eSound.YUJU_BOY:
            if AudioController.__soundThreadYujuBoy != None:
                AudioController.__soundThreadYujuBoy.stop()
                AudioController.__soundThreadYujuBoy = None
                                
        elif soundId == eSound.YUJU_GIRL:
            if AudioController.__soundThreadYujuGirl != None:
                AudioController.__soundThreadYujuGirl.stop()
                AudioController.__soundThreadYujuGirl = None
            
    @staticmethod
    def stopSounds():
        AudioController.stopSound(eSound.BELL)
        AudioController.stopSound(eSound.CLICK_INGREDIENT_SELECTION)
        AudioController.stopSound(eSound.COOKING_HOT)
        AudioController.stopSound(eSound.COOKING_COLD)
        AudioController.stopSound(eSound.FOOD_SERVED)
        AudioController.stopSound(eSound.FOOD_TIME_CHANGE)
        AudioController.stopSound(eSound.FRIDGE)
        AudioController.stopSound(eSound.INGREDIENT_DELETE)
        AudioController.stopSound(eSound.INGREDIENT_SELECT)
        AudioController.stopSound(eSound.INGREDIENTS_MAKE_RECIPE)
        AudioController.stopSound(eSound.LEVEL_PASSED)
        AudioController.stopSound(eSound.ORDER)
        AudioController.stopSound(eSound.PICK_DIRTY_DISH)
        AudioController.stopSound(eSound.WASHING)
        AudioController.stopSound(eSound.WASHING_DISHES)
        
        AudioController.stopSound(eSound.HELLO_BOY)
        AudioController.stopSound(eSound.HELLO_GIRL)
        AudioController.stopSound(eSound.LEVEL_WIN)
        AudioController.stopSound(eSound.YUJU_BOY)
        AudioController.stopSound(eSound.YUJU_GIRL)
    
    @staticmethod
    def playMusic(musicId):
        
        # Detenemos cualquier musica de fondo que se este reproduciendo
        AudioController.stopMusic()
        
        # Iniciamos la reproduccion en un Thread
        AudioController.__musicThread = MusicThread(musicId)
        AudioController.__musicThread.start()
        
    @staticmethod
    def stopMusic():
        if AudioController.__musicThread != None:
            AudioController.__musicThread.stop()
            AudioController.__musicThread = None
