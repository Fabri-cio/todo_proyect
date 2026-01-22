# 📝 Task Manager API

API REST para gestión de tareas con **autenticación JWT**.  
Cada usuario puede crear, ver, actualizar y eliminar **solo sus propias tareas**.

---

## 🚀 Tecnologías

- Python 3.11
- Django 4.2.11
- Django REST Framework
- JWT (SimpleJWT)
- SQLite (para desarrollo)
- Interfaz web de Django REST Framework para probar endpoints

---

## ⚙️ Instalación y ejecución

1. **Clonar el repositorio**

```bash
git clone https://github.com/tu_usuario/tu_repo.git
cd tu_repo
```

2. **Crear y activar entorno virtual**

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux / Mac
source venv/bin/activate
```

3. **Instalar dependencias**

```bash
pip install -r requirements.txt
```

4. **Migrar base de datos**

```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Crear superusuario**

```bash
python manage.py createsuperuser
```

6. **Ejecutar servidor**

```bash
python manage.py runserver
```

La API estará disponible en http://127.0.0.1:8000/

## Ejecucion con Docker

1. **Construir y levantar los contenedores**
   Este comando crea las imágenes (si no existen), aplica migraciones, carga datos de prueba y deja los servicios corriendo en **segundo plano**:

```bash
docker-compose up -d --build
```
2. **Verigficar que la API esté funcionando**
LA API estará disponible en http://127.0.0.1:8000/

3. **Credenciales de prueba**
   Administrador:

- user: admin
- password: admin123
  Usuario normal:
- user: user
- password: user123

## Autenticación

- Para obtener un token JWT: `POST /api/token/` con `{ "username": "admin", "password": "admin123" }`
- Para refrescar el token: `POST /api/token/refresh/` con el token actual
- Para verificar el token: `GET /api/token/verify/` con el token

8. **Endpoints**
   usuarios

- `POST /api/users/` - Crear un nuevo usuario
- `POST /api/token/` - Obtener token JWT
- `POST /api/token/refresh/` - Refrescar token
- `POST /api/token/verify/` - Verificar token

tareas

- `GET /api/tasks/` - Listar todas las tareas del usuario autenticado
- `POST /api/tasks/` - Crear una nueva tarea
- `GET /api/tasks/<id>/` - Ver una tarea específica
- `PUT /api/tasks/<id>/` - Actualizar una tarea
- `DELETE /api/tasks/<id>/` - Eliminar una tarea

---
