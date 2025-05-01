# archivo: test_my_code.py
import unittest
from codigo1001 import suma

class TestMyCode(unittest.TestCase):
    
    def test_suma(self):
        """Prueba que verifica que la función suma funcione correctamente."""
        self.assertEqual(suma(2, 3), 5)
        self.assertEqual(suma(-1, 1), 0)
        self.assertEqual(suma(0, 0), 0)
        self.assertEqual(suma(100, 50), 150)

if __name__ == '__main__':
    # Iniciar las pruebas
    unittest.main()