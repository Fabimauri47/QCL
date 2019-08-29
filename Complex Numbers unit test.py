import unittest
import Num_Complejos

class Prueba_Modulo(unittest.TestCase):
    
    def test_sum(self):
        self.assertEqual(Num_Complejos.suma([5,8],[3,7]),(8,15))
        self.assertEqual(Num_Complejos.resta([5,8],[3,7]),(2,1))
        self.assertEqual(Num_Complejos.multiplicacion([5,8],[3,7]),(-41,59))
        self.assertEqual(Num_Complejos.division([5,8],[3,7]),(1.2241379310344827,-0.1896551724137931))
        self.assertEqual(Num_Complejos.modulo([5,8]),9.433981132056603)
        self.assertEqual(Num_Complejos.conjugado([5,8]),[5,-8])
        self.assertEqual(Num_Complejos.cartesiono_A_polares([5,8]),(9.433981132056603,57.9946167919165))
        self.assertEqual(Num_Complejos.polar_A_cartesiano([78,69]),(77.48444961833718,-8.953215475088603))
        self.assertEqual(Num_Complejos.fase([5,8]),57.9946167919165)
        
if __name__ == "__main__":
    unittest.main()
