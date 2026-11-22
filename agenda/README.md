# Agenda gratuita para profesionales · v0.5.0

Agenda web multipropósito, gratuita y optimizada para móvil. La demo carga solicitantes ficticios automáticamente para que se pueda probar de inmediato. La casilla permite retirarlos y volver a una lista vacía.

## Interfaz
- Tipografía principal: Century Gothic, con alternativas compatibles cuando no está instalada.
- Selector de idioma: Español e English.
- Preferencia de idioma guardada localmente en el navegador.

## Funcionalidades
- Administración independiente de solicitantes: añadir y eliminar personas o contactos.
- Crear citas seleccionando un solicitante existente.
- Añadir un solicitante desde el formulario de cita.
- Descargar una plantilla JSON vacía, sin datos ficticios.
- Importar y exportar respaldos JSON.
- Catálogo público de servicios con alternativa básica si no está disponible.
- Datos ficticios cargados automáticamente al abrir la demo; la casilla permite retirarlos.

## Datos y privacidad
- Citas y solicitantes se almacenan en localStorage del navegador.
- Los registros ficticios se identifican con `source: "mock"`; al desactivar la casilla se eliminan de la colección local.
- La plantilla vacía siempre se descarga sin citas ni solicitantes.
- No hay login, backend, sincronización ni almacenamiento remoto.
- No usar esta demo para información clínica o sensible.

## Migración y compatibilidad
- Se conserva la clave de citas `agenda-demo-v0.3.0` y los registros históricos de `agenda-demo-v0.1.0`.
- Los nombres históricos de citas se migran a la colección local de solicitantes cuando esta aún no existe.
- Solicitantes se guardan en `agenda-requestors-v1`.
- No se eliminan automáticamente claves antiguas.

## Plataformas
- Web app: escritorio, Android e iOS mediante navegador.
- Android y Windows ZIP permanecen ocultos hasta disponer de paquetes probados.
- No se publica paquete Apple en esta etapa.
