def validar_temperatura(temperatura):
   
    if -20 <= temperatura <= 50:
        return True
    else:
        return False

def pruebas_validar_temperatura():
    casos_de_prueba = [
        (-20, True),  
        (50, True),  
        (49, True),  
        (-19, True), 
        (-21, False),
        (51, False),  
    ]

    for temperatura, resultado_esperado in casos_de_prueba:
        resultado = validar_temperatura(temperatura)
        assert resultado == resultado_esperado, f"Error: para temperatura {temperatura}, se esperaba {resultado_esperado} pero se obtuvo {resultado}"
        print(f"Prueba con temperatura {temperatura} pasada exitosamente")

pruebas_validar_temperatura()