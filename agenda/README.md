# Agenda gratuita para profesionales · v0.3.0

Una agenda web gratuita, multipropósito y mobile-first. Se abre vacía y permite empezar sin cuenta ni configuración.

## Ediciones y plataformas
- Una sola agenda gratuita para profesionales de distintos rubros.
- Web app: disponible para escritorio, Android e iOS mediante navegador.
- Android ZIP y Windows ZIP: enlaces preparados, ocultos hasta que los paquetes nativos/portables estén construidos, probados y publicados.
- Apple: no se publica paquete nativo en esta etapa; iPhone/iPad usan la web app.

## Privacidad y datos de demostración
- La agenda inicia vacía. Los datos de ejemplo no se solicitan automáticamente.
- La lista ficticia `mock-requestors.json` solo se obtiene cuando el usuario activa expresamente la casilla de demostración.
- `services.json` es un catálogo público de solo lectura.
- Las citas reales se guardan en el almacenamiento local del navegador.
- No hay inicio de sesión, backend, sincronización ni almacenamiento remoto de citas.
- No introduzcas datos sensibles o clínicos en esta demo pública.

## Migración de datos v0.2.0 → v0.3.0
- Se conserva la clave antigua `agenda-demo-v0.1.0` como origen de migración.
- En la primera apertura de v0.3.0, los registros existentes se copian a `agenda-demo-v0.3.0`.
- El campo histórico `person` se transforma en `requestorName`; se conserva el registro original en la clave antigua como respaldo.
- Exportaciones nuevas usan `agenda-local-backup-v2`; importación acepta tanto `requestorName` como el campo histórico `person`.
- No borres los datos del navegador hasta verificar una exportación de respaldo.

## Descargas
Los enlaces de Android y Windows están incluidos como elementos ocultos en la interfaz. No deben mostrarse ni habilitarse hasta que los ZIP reales hayan sido generados, revisados y publicados en `agenda/downloads/`.

## Alcance
El ZIP web generado desde el navegador contiene el HTML de la aplicación. No incluye backend, SQL Server ni servicios locales. La conexión pública solo obtiene el catálogo de servicios y, opcionalmente, los datos ficticios solicitados por el usuario.
