from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from tasks.models import Task

class Command(BaseCommand):
    help = 'Carga datos de prueba'

    def handle(self, *args, **kwargs):

        if User.objects.exists():
            self.stdout.write(self.style.WARNING("Ya existen datos, no se cargó nada"))
            return

        # Usuario admin
        admin = User.objects.create_superuser(
            username='admin',
            email='admin@test.com',
            password='admin123'
        )

        # Usuario normal
        user = User.objects.create_user(
            username='user',
            email='user@test.com',
            password='user123'
        )

        # Tareas
        Task.objects.create(title='Aprender Docker', owner=user)
        Task.objects.create(title='Aprender Django REST', owner=user)
        Task.objects.create(title='Preparar CV', owner=user)

        self.stdout.write(self.style.SUCCESS("Datos de prueba creados correctamente"))
