from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):

    def test_crear_usuario_con_email(self):
        """test para crear usuarios con correo exitosamente"""
        email = 'prueba@prueba.com'
        password = '123456'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_usuario_email_normalizado(self):
        """prueba que el email de nuevo usuasrio este normalizado"""
        email = 'prueba@EJEMPLO.COM'
        user = get_user_model().objects.create_user(email, '123456')

        self.assertEqual(user.email, email.lower())

    def test_nuevo_usuario_email_invalido(self):
        """prueba para validar un usuario con email no valido"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, '123456')

    def test_crear_superusuario(self):
        """prueba para validar al crear superUsuario"""
        user = get_user_model().objects.create_superuser(
            'admin@admin.com',
            '123456'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
