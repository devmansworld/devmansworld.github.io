# Agenda Demo v0.2.0

Public static local-first HTML demo.

## Data boundaries
- `services.json` and `mock-requestors.json` are public, read-only GitHub Pages resources.
- Mock requestor names are invented synthetic demo data.
- Select **Plantilla vacía** to work without the mock requestor list.
- Real names and appointments entered by a visitor remain in that visitor's browser localStorage.
- No real appointment/requestor information is sent to the public catalogue.
- Import/export is local; never place real patient data in public repository files or issue reports.

## Portable ZIP
The browser-generated ZIP contains the standalone HTML. It retrieves public mock catalogues from GitHub Pages while online. It does not contain a backend or local SQL Server.

## Scope
No login, backend, remote appointment storage, or real patient records.
