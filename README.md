🪩 Playground Final Project · by Betty Jaureguiberry
Curso Python Coderhouse
Comisión 78110
Profesor Alan Prestia

Bienvenidos a mi entrega final del curso — una aplicación web tipo blog construida con Django que compila estética, narrativa técnica y funcionalidades completas.

---

🚀 Funcionalidades principales

- 🏠 Home: Vista inicial con acceso a todas las secciones
- 👤 Perfil de usuario: Edición de bio y avatar con glow técnico
- ✍️ Registro/Login/Logout: Sistema de autenticación completo
- 📖 Blog pages: Crear, leer, editar y borrar entradas desde el módulo principal
- 💬 Mensajería: Comunicación entre usuarias en tiempo real
- 📌 Acerca de mí: Página personal ubicada en /about/
- 📚 Listado de páginas: Navegable desde /pages/ con opción “Leer más”
- 🎨 Estética personalizada: CSS + narrativa visual aplicada en toda la interfaz

---

🛠️ Stack tecnológico

- 🐍 Python 3.12
- ⚙️ Django 5.x
- 🎨 HTML5 / CSS3 / CKEditor / Bootstrap (opcional)
- 💾 SQLite3 para testing local
- ☁️ Deploy local (versión entregada sin DB)

---

📁 Estructura del proyecto

`bash
├── accounts/       # Autenticación y perfil
├── blog/           # Pages: modelo principal
├── messages/       # Mensajería entre usuarias
├── templates/      # HTML extendido con base.html
├── static/         # Estilos CSS e imágenes técnicas
├── media/          # Avatares y contenido subido (ignorado en repo)
├── db.sqlite3      # (no incluido en el repo)
`

---

✨ Requisitos técnicos cumplidos

- Herencia de templates (base.html)
- 2+ CBV + 1 mixin + 1 decorador
- Readme narrativo + video demo 📹
- Archivo .gitignore con db.sqlite3, media/, pycache/
- requirements.txt actualizado

---

👩‍💻 Cómo correr el proyecto localmente

1. Clonar el repo  
   `bash
   git clone https://github.com/BettyJaureguiberry/EntregaFinalPython/tree/master

2. Crear entorno virtual  
   `bash
   python -m venv env
   source env/bin/activate  # o env\Scripts\activate en Windows
   `

3. Instalar dependencias  
   `bash
   pip install -r requirements.txt
   `

4. Migrar la base de datos  
   `bash
   python manage.py migrate
   `

5. Ejecutar el servidor  
   `bash
   python manage.py runserver
   `

---

🧩 Detalles finales

Este proyecto fue creado con actitud técnica, glow narrativo y enfoque visual. Cada vista está pensada para reflejar personalidad y funcionalidad.  
No se incluye la base de datos ni las imágenes en media/.  

> ✉️ Contacto técnico: bettyjaureguiberry@gmail.com  
> 🎥 Demo video entregado por la plataforma 

---

📢 Disclaimer

Este repositorio es parte del proyecto final individual. Todo el código y diseño reflejan mi enfoque personal técnico-creativo. Compila épico o no compila 😉.

