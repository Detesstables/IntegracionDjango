from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class UserAuthenticationTests(TestCase):
    def setUp(self):
        # Configurar un usuario para pruebas de inicio de sesión
        self.test_user = User.objects.create_user(username='testuser', password='testpassword')

    def test_registro_view_get(self):
        # Prueba para asegurar que la vista de registro se carga correctamente
        response = self.client.get(reverse('registro'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registro.html')

    def test_registro_view_post(self):
        # Prueba para asegurar que un nuevo usuario puede registrarse
        response = self.client.post(reverse('registro'), {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'newpassword',
            'password2': 'newpassword'
        })
        self.assertEqual(response.status_code, 302)  # Redirección después del registro
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_login_view_get(self):
        # Prueba para asegurar que la vista de inicio de sesión se carga correctamente
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_login_view_post(self):
        # Prueba para asegurar que un usuario puede iniciar sesión
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 302)  # Redirección después del inicio de sesión
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_logout_view(self):
        # Prueba para asegurar que un usuario puede cerrar sesión
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)  # Redirección después del cierre de sesión
        self.assertFalse(response.wsgi_request.user.is_authenticated)