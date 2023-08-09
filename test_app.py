import unittest
from app import app, transacciones, tasas_de_cambio

class TestAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_obtener_todas_las_tasas(self):
        # Esta prueba verifica que el endpoint /tasas devuelva un estado HTTP 200
        respuesta = self.app.get('/tasas')
        self.assertEqual(respuesta.status_code, 200)

    def test_obtener_tasa_por_codigo(self):
        # Esta prueba verifica que el endpoint /tasa/EUR devuelva un estado HTTP 200 y contenga el código "EUR"
        respuesta = self.app.get('/tasa/EUR')
        data = respuesta.get_json()
        self.assertEqual(respuesta.status_code, 200)
        self.assertTrue(any(tasa["from"] == "EUR" or tasa["to"] == "EUR" for tasa in data))

    def test_obtener_transacciones_por_moneda(self):
        # Esta prueba verifica que al solicitar transacciones de una moneda, se obtengan solo las transacciones de esa moneda
        respuesta = self.app.get('/transacciones/USD')
        data = respuesta.get_json()
        self.assertEqual(respuesta.status_code, 200)
        self.assertTrue(all(transaccion["currency"] == "USD" for transaccion in data))

    def test_obtener_transacciones_por_sku_y_moneda(self):
        # Esta prueba verifica que al solicitar transacciones por SKU y moneda, se obtengan las transacciones correctas
        respuesta = self.app.get('/transacciones/T2006/USD')
        data = respuesta.get_json()
        self.assertEqual(respuesta.status_code, 200)
        self.assertTrue(all(transaccion["sku"] == "T2006" and transaccion["currency"] == "USD" for transaccion in data))

    def test_obtener_tasa_inexistente(self):
        # Esta prueba verifica que si se pide una tasa que no existe, se devuelve un estado HTTP 404 (No encontrado)
        respuesta = self.app.get('/tasa/ABC')
        self.assertEqual(respuesta.status_code, 404)

    def test_obtener_transacciones_moneda_inexistente(self):
        # Esta prueba verifica que si se piden transacciones de una moneda inexistente, se devuelve un estado HTTP 404
        respuesta = self.app.get('/transacciones/ABC')
        self.assertEqual(respuesta.status_code, 404)

if __name__ == "__main__":
    unittest.main()
