import unittest
import Matriz_Complejos

class TestMyModule(unittest.TestCase):

    def test_SumVec(self):
        self.assertEqual(Matriz_Complejos.Sumar_vectores([(5,8),(4,9)],[(3,7),(6,7)]),[(8,15),(10,16)])
    def test_InvVec(self):
        self.assertEqual(Matriz_Complejos.Inversa_vectores([(5,8),(4,9)]),[(-5,-8),(-4,-9)])
    def test_ProdEscVec(self):
        self.assertEqual(Matriz_Complejos.multiplicacionEsc_vector_complejas((5,8),[(3,7),(1,-5)]),[(-41,59),(45,-17)])
    def test_SumMatr(self):
        self.assertEqual(Matriz_Complejos.Suma_matrices_complejas([[(3,5),(2,1)],[(14,-1),(16,0)]],[[(7,9),(6,-2)],[(1,-4),(5,3)]]),[[(10,14),(8,-1)],[(15,-5),(21,3)]])
    def test_InvMatr(self):
        self.assertEqual(Matriz_Complejos.inversa_matrices_complejas([[(3,5),(2,1)],[(14,-1),(16,0)]]),[[(-3,-5),(-2,-1)],[(-14,1),(-16,0)]])
    def test_ProdEscMatr(self):
        self.assertEqual(Matriz_Complejos.MultiplicacionEsc_matrix((6,0),[[(3,5),(2,1)],[(14,-1),(16,0)]]),[[(18,30),(12,6)],[(84,-6),(96,0)]])
    def test_MatrTrans(self):
        self.assertEqual(Matriz_Complejos.Transpusta_matrices([[(4,7),(3,8),(45,87)],[(12,3),(56,69),(0,1)],[(1,2),(45,13),(900,657)]]),[[(4,7),(12,3),(1,2)],[(3,8),(56,69),(45,13)],[(45,87),(0,1),(900,657)]])
    def test_MatrConj(self):
        self.assertEqual(Matriz_Complejos.matriz_conjugada([[(1,2),(3,4),(5,-6)],[(7,-8),(2,-4),(9,3)],[(6,8),(7,-5),(2,6)]]),[[(1,-2),(3,-4),(5,6)],[(7,8),(2,4),(9,-3)],[(6,-8),(7,5),(2,-6)]])
    def test_MatrAdj(self):
        self.assertEqual(Matriz_Complejos.matriz_adjunta([[(1,2),(2,-3),(3,4)],[(4,-5),(5,6),(6,-7)],[(7,8),(8,-9),(9,10)]]),[[(1,-2),(4,5),(7,-8)],[(2,3),(5,-6),(8,9)],[(3,-4),(6,7),(9,-10)]])
    def test_AccMaVe(self):
        self.assertEqual(Matriz_Complejos.Accion_Matriz_Vector([[(-3,0),(5,0),(-6,0)],[(7,0),(10,0),(-1,0)]],[(-6,0),(-2,0),(5,0)]),[(-22,0),(-67,0)])
    def test_NormMatr(self):
        self.assertEqual(Matriz_Complejos.norma_matrices([[(1,2),(2,-3),(3,4)],[(4,-5),(5,6),(6,-7)],[(7,8),(8,-9),(9,10)]]),25.865034312755125)
    def test_DistMatr(self):
        self.assertEqual(Matriz_Complejos.matriz_distancia([[(3,0),(7,0)],[(5,0),(8,0)]],[[(2,0),(9,0)],[(4,0),(-5,0)]]),13.228756555322953)
    def test_ReviMatrU(self):
        self.assertEqual(Matriz_Complejos.RevisarUnitaria([[(0,0),(1,0)],[(-1,0),(0,0)]]),True)
    def test_ReviMatrH(self):
        self.assertEqual(Matriz_Complejos.MatrizHermitania([[(7,0),(6,5)],[(6,-5),(-3,0)]]),True)
    def test_ProdTens(self):
        self.assertEqual(Matriz_Complejos.ProductoTensor([[(1,0),(2,0)],[(0,0),(1,0)]],[[(3,0),(2,0)],[(-1,0),(0,0)]]),[[(3,0),(2,0),(6,0),(4,0)],[(-1,0),(0,0),(-2,0),(0,0)],[(0,0),(0,0),(3,0),(2,0)],[(0,0),(0,0),(-1,0),(0,0)]])

if __name__ == "__main__":
    unittest.main()
