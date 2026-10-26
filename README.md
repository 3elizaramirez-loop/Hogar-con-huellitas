# Hogar con Huellitas V3 — Aventura acogedora 🐾

Flask + Turso + Cloudinary + Google Colab + ngrok. **Registro, login, publicación con foto subida desde dispositivo, catálogo, ficha, solicitud, panel y decisión del dueño.** Diseño con ilustraciones de animales y naturaleza pixel art.

## Pasos en Colab
1. Crear una **base Turso nueva y vacía de pruebas**, sin reutilizar la base original.
2. Crear una cuenta Cloudinary y obtener Cloud name, API key y API secret (mantener privados).
3. Abrir `Huellitas_V3_Colab.ipynb` en Colab; ejecutar las celdas en orden y subir `hogar-con-huellitas-v3.zip` cuando se solicite.
4. Proporcionar en Colab las variables de Turso y Cloudinary; luego ejecutar la creación de las tablas.
5. Ejecutar Flask, comprobar HTTP 200 y crear el túnel de ngrok.
6. Regístrate en la web; usa **Dar en adopción** y selecciona tu foto JPG/PNG/WebP (máximo 2 MB).

**¡No pegues claves en GitHub ni en este chat!** `Cloudinary API secret`, Turso token y ngrok token son privados. Si Colab se reinicia se perderá el entorno y deberán reponerse en memoria. Una secret key regenerada invalida las sesiones; no borra usuarios.

**Limitaciones:** ngrok/Colab son temporales, faltan moderación, privacidad y verificación para lanzarlo públicamente; la aprobación de una solicitud es una decisión dentro de la app y no prueba la entrega física. Los gráficos pixel art son decorativos; las fotografías publicadas son las que suben los usuarios. Esta versión admite perros y gatos. Las tablas se crean sin insertar mascotas ficticias.
