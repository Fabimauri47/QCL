import unittest
import Matriz_Complejos

class TestMyModule(unittest.TestCase):

    def test_Suma_Vectores(self):
        self.assertEqual(Matriz_Complejos.Sumar_vectores([(5,8),(4,9)],[(3,7),(6,7)]),[(8,15),(10,16)])
    def test_Inversa_Vectores(self):
        self.assertEqual(Matriz_Complejos.Inversa_vectores([(5,8),(4,9)]),[(-5,-8),(-4,-9)])
    def test_Producto_escalar_vectores(self):
        self.assertEqual(Matriz_Complejos.MultiplicacionEsc_vectores((5,8),[(3,7),(1,-5)]),[(-41,59),(45,-17)])
    def test_Suma_Matriz(self):
        self.assertEqual(Matriz_Complejos.Suma_matrices_complejas([[(3,5),(2,1)],[(14,-1),(16,0)]],[[(7,9),(6,-2)],[(1,-4),(5,3)]]),[[(10,14),(8,-1)],[(15,-5),(21,3)]])
    def test_Inversa_Matriz(self):
        self.assertEqual(Matriz_Complejos.inversa_matrices_complejas([[(3,5),(2,1)],[(14,-1),(16,0)]]),[[(-3,-5),(-2,-1)],[(-14,1),(-16,0)]])
    def test_Producto_escalar_matriz(self):
        self.assertEqual(Matriz_Complejos.multiplicacionEsc_matrices_complejas((6,0),[[(3,5),(2,1)],[(14,-1),(16,0)]]),[[(18,30),(12,6)],[(84,-6),(96,0)]])
    def test_Matriz_Transpuesta(self):
        self.assertEqual(Matriz_Complejos.Transpusta_matrices([[(4,7),(3,8),(45,87)],[(12,3),(56,69),(0,1)],[(1,2),(45,13),(900,657)]]),[[(4,7),(12,3),(1,2)],[(3,8),(56,69),(45,13)],[(45,87),(0,1),(900,657)]])
    def test_Matriz_Conjugado(self):
        self.assertEqual(Matriz_Complejos.matriz_conjugada([[(1,2),(3,4),(5,-6)],[(7,-8),(2,-4),(9,3)],[(6,8),(7,-5),(2,6)]]),[[(1,-2),(3,-4),(5,6)],[(7,8),(2,4),(9,-3)],[(6,-8),(7,5),(2,-6)]])
    def test_Matriz_Adjunta(self):
        self.assertEqual(Matriz_Complejos.matriz_adjunta([[(1,2),(2,-3),(3,4)],[(4,-5),(5,6),(6,-7)],[(7,8),(8,-9),(9,10)]]),[[(1,-2),(4,5),(7,-8)],[(2,3),(5,-6),(8,9)],[(3,-4),(6,7),(9,-10)]])
    def test_Norma_Matriz(self):
        self.assertEqual(Matriz_Complejos.norma_matrices([[(1,2),(2,-3),(3,4)],[(4,-5),(5,6),(6,-7)],[(7,8),(8,-9),(9,10)]]),25.865034312755125)
    def test_Distancia_Matriz(self):
        self.assertEqual(Matriz_Complejos.matriz_distancia([[(3,0),(7,0)],[(5,0),(8,0)]],[[(2,0),(9,0)],[(4,0),(-5,0)]]),13.228756555322953)
    def test_Revisar_matriz_unitaria(self):
        self.assertEqual(Matriz_Complejos.matriz_unitaria([[(3,0),(7,0)],[(5,0),(8,0)]],[[(2,0),(9,0)],[(4,0),(-5,0)]]),13.228756555322953)
    def test_Revisar_Matriz_Hermitan(self):
        self.assertEqual(Matriz_Complejos.matriz_hermitian([[(3,0),(7,0)],[(5,0),(8,0)]],[[(2,0),(9,0)],[(4,0),(-5,0)]]),13.228756555322953)
    def test_Producto_Tensor_Matriz(self):
        self.assertEqual(Matriz_Complejos.matriz_producto_tensor([[(1,0),(2,0)],[(0,0),(1,0)]],[[(3,0),(2,0)],[(-1,0),(0,0)]]),[[(3,0),(2,0),(6,0),(4,0)],[(-1,0),(0,0),(-2,0),(0,0)],[(0,0),(0,0),(3,0),(2,0)],[(0,0),(0,0),(-1,0),(0,0)]])

if __name__ == "__main__":
    unittest.main()
