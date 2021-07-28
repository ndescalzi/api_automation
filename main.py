import unittest
import funciones

"""
Impresion del error en caso de exisitir para su visualización en el reporte y tener las claro el error  
"""
def impresion(error):
    print("Los errores son: ")
    for i in error:
        print(i, ". ")

"""
Generacion de la clase para casos de prueba. 
"""
class Api_Estructura(unittest.TestCase):

    def test_para_nasa(self):
        resultado = funciones.llaves("nasa")
        rta = True
        if resultado:
            rta = False
            impresion(resultado)
        self.assertTrue(rta)

    def test_para_covid(self):
        resultado = funciones.llaves("covid")
        rta = True
        if resultado:
            rta = False
            impresion(resultado)
        self.assertTrue(rta)
    
    def test_para_finanzas(self):
        resultado = funciones.llaves("finanzas")
        rta = True
        if resultado:
            rta = False
            impresion(resultado)
        self.assertTrue(rta)


if __name__ == '__main__':
    unittest.main()
