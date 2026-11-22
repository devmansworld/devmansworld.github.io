# Agenda gratuita para profesionales · v0.4.0

Agenda web multipropósito, gratuita y optimizada para móvil. La aplicación abre vacía y permite administrar solicitantes y citas sin cuenta.

## Funcionalidades
- Administración independiente de solicitantes: añadir y eliminar personas o contactos.
- Crear citas seleccionando un solicitante existente.
- Añadir un nuevo solicitante desde el propio formulario de cita.
- Descargar una plantilla JSON vacía.
- Importar y exportar respaldos JSON.
- Catálogo de servicios público con servicio básico de respaldo.
- Datos ficticios opcionales: solo se solicitan e incorporan al marcar la casilla.

## Datos y privacidad
- Citas y solicitantes se almacenan en localStorage del navegador.
- Los datos ficticios se marcan con `source: "mock"` y se pueden retirar desmarcando la casilla.
- No hay login, backend, sincronización ni almacenamiento remoto.
- No usar esta demo para información clínica o sensible.

## Migración
- Conserva la clave de citas v0.3.0 y los registros anteriores en `agenda-demo-v0.1.0`.
- En el primer inicio, migra nombres históricos de citas a la colección de solicitantes local.
- Los datos migrados se conservan; no se borran las claves anteriores.
- Solicitantes nuevos se guardan separadamente en `agenda-requestors-v1`.

## Plataformas
- Web app: escritorio, Android e iOS mediante navegador.
- Android y Windows ZIP permanecen ocultos hasta disponer de paquetes probados.
- No se publica paquete Apple en esta etapa.
