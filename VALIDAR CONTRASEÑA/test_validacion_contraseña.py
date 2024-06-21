import unittest
from tkinter import messagebox
from unittest.mock import patch
from validacion_contrasena_tkinter import validar_contrasena

class TestValidarContrasena(unittest.TestCase):

    def test_contrasena_valida(self):
        with patch.object(messagebox, 'showinfo') as mock_info:
            resultado = validar_contrasena("Password123@")
            self.assertTrue(resultado)
            mock_info.assert_called_with("Éxito", "Contraseña válida.")

    def test_contrasena_demasiado_corta(self):
        with patch.object(messagebox, 'showerror') as mock_error:
            resultado = validar_contrasena("abc")
            self.assertFalse(resultado)
            mock_error.assert_called_with("Error de validación", "La contraseña es demasiado corta.")

    def test_contrasena_sin_letras(self):
        with patch.object(messagebox, 'showerror') as mock_error:
            resultado = validar_contrasena("12345678")
            self.assertFalse(resultado)
            mock_error.assert_called_with("Error de validación", "La contraseña debe contener al menos una letra.")

    def test_contrasena_sin_numeros(self):
        with patch.object(messagebox, 'showerror') as mock_error:
            resultado = validar_contrasena("Password@")
            self.assertFalse(resultado)
            mock_error.assert_called_with("Error de validación", "La contraseña debe contener al menos un número.")

    def test_contrasena_sin_caracteres_especiales(self):
        with patch.object(messagebox, 'showerror') as mock_error:
            resultado = validar_contrasena("Password123")
            self.assertFalse(resultado)
            mock_error.assert_called_with("Error de validación", "La contraseña debe contener al menos un carácter especial.")

if __name__ == "__main__":
    unittest.main()