requisitos ={
    "titulo": "requerido",
    "notas": "requerido",
    "foto": "opcional"
}
# # Accediendo a la propiedad
# print(f' las notas son de tipo: {requisitos["notas"]}')

# print(f' las foto son de tipo: {requisitos["foto"]}')

# #Modificando una propiedad
# requisitos["notas"] = "opcional"
# requisitos["foto"] = "requerido"

# print(f'las notas ahora son de tipo: {requisitos["notas"]}')
# print(f'las fotos ahora son de tipo: {requisitos["foto"]}')

# Construir un diccionario de datos para guardar
# la informacion de un avion, coloque al menos 6 propiedades
# imprima 3 de ellas y cambie el valor de dos
# al menos debe existir una propiedad bool, una int,
# una float, un arreglo, un diccionario

Avion = {
    "modelo": "A320",
    "tipo": "avion espacial",
    "capacidad": 5,
    "encendido_motor": False,
    "precio" : 10000000.00,
    "datos_pilotos" : {
        "nombre": "Jack",
        "Apellido": "Lens"  
    },
    "azafatas": {
        "nombre": "Lauren",
        "Apellido": "Sanchez"
    },
    
    "tripulacion" : "[datos_pilotos,azafatas]"
    

}

# print(Avion)

# construya un programa que solicite el peso en kg de una persona y si el peso
# esta entre 60 - 70 recomiende una dieta de 5 comidas altas en carbohidratos
# si el peso esta entre 70 - 80 recomiende una dieta en 4 comidas alta en proteinas
# si el peso esta entre 80 - 90 recomiende una dieta en 3 comidas alta en fibras
# utilice solo diccionarios para agrupar los respectivos menus.?


# info_peso = float(input("Ingrese su peso: "))

# menu_carbohidratos = {
#     "desayuno": ["avena", "plátano", "leche"],
#     "almuerzo": ["arroz", "frijoles", "pollo"],
#     "merienda": ["manzana", "nueces"],
#     "cena": ["pasta", "salsa de tomate", "queso"],
#     "snack": ["yogur", "granola"]
# }

# menu_proteinas = {
#     'desayuno': {
#         'comida': 'Huevos revueltos con espinacas y queso',
#         'proteina': 25,
#         'carbohidrato': 5,
#         'grasa': 10
#     },
#     'almuerzo': {
#         'comida': 'Ensalada de pollo con aguacate',
#         'proteina': 30,
#         'carbohidrato': 10,
#         'grasa': 15
#     },
#     'snack': {
#         'comida': 'Yogur griego con nueces',
#         'proteina': 15,
#         'carbohidrato': 10,
#         'grasa': 12
#     },
#     'cena': {
#         'comida': 'Salmón a la parrilla con espárragos',
#         'proteina': 35,
#         'carbohidrato': 8,
#         'grasa': 20
#     }
# }

# menu_fibras = {

#     "desayuno": ["avena", "frutas", "nueces"],
#     "almuerzo": ["ensalada", "pollo", "arroz_integral"],
#     "cena": ["salmon", "vegetales al vapor", "cus-cus"]

# }

# if info_peso >= 60 and info_peso <= 70:
#     print(f'Le recomiendo este menu para el desayuno: {menu_carbohidratos["desayuno"]}')
#     print(f'Le recomiendo este menu para la merienda: {menu_carbohidratos["merienda"]}')
#     print(f'Le recomiendo este menu para el almuerzo: {menu_carbohidratos["almuerzo"]}')
#     print(f'Le recomiendo este menu para el snack: {menu_carbohidratos["snack"]}')
#     print(f'Le recomiendo este menu para la cena: {menu_carbohidratos["cena"]}')
# if info_peso > 70 and info_peso <= 80:
#     print(f'Le recomiendo este menu para el desayuno: {menu_proteinas["desayuno"]}')
#     print(f'Le recomiendo este menu para el almuerzo: {menu_proteinas["almuerzo"]}')
#     print(f'Le recomiendo este menu para el snack: {menu_proteinas["snack"]}')
#     print(f'Le recomiendo este menu para la cena: {menu_proteinas["cena"]}')
# if info_peso > 80 and info_peso <= 90:
#     print(f' Le recomiendo este menu: {menu_fibras}')






name = 'jack', 'lens'
print(name, sep='-')
