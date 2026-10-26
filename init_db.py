from app.db import database,save
schema = [
    "CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY AUTOINCREMENT,nombre TEXT NOT NULL,email TEXT NOT NULL UNIQUE,password_hash TEXT NOT NULL,creado_en TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP)",
    "CREATE TABLE IF NOT EXISTS mascotas (id INTEGER PRIMARY KEY AUTOINCREMENT,usuario_id INTEGER NOT NULL REFERENCES usuarios(id),nombre TEXT NOT NULL,especie TEXT NOT NULL CHECK(especie IN ('perro','gato')),edad TEXT NOT NULL,tamano TEXT NOT NULL CHECK(tamano IN ('pequeño','mediano','grande')),ubicacion TEXT NOT NULL,descripcion TEXT NOT NULL,foto_url TEXT,estado TEXT NOT NULL DEFAULT 'disponible' CHECK(estado IN ('disponible','adoptado')),creado_en TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP)",
    "CREATE TABLE IF NOT EXISTS solicitudes (id INTEGER PRIMARY KEY AUTOINCREMENT,mascota_id INTEGER NOT NULL REFERENCES mascotas(id),solicitante_id INTEGER NOT NULL REFERENCES usuarios(id),mensaje TEXT NOT NULL,estado TEXT NOT NULL DEFAULT 'pendiente' CHECK(estado IN ('pendiente','aprobada','rechazada')),creado_en TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP)",
    "CREATE UNIQUE INDEX IF NOT EXISTS uq_solicitud_pendiente ON solicitudes(mascota_id,solicitante_id) WHERE estado='pendiente'"
]
with database() as db:
    for sql in schema:
        db.execute(sql)
    save(db)
print('✅ Turso listo: usuarios, mascotas y solicitudes')
