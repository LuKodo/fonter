<p align="center">
  <img src="./fonter.svg" alt="Fonter logo" width="120" height="120">
</p>

<h1 align="center">Fonter</h1>

<p align="center">
  Instalador de fuentes para Linux con drag & drop, interfaz moderna (PySide6/Qt) y empaquetado nativo para Arch.
</p>

---

## Características

- **Arrastra y suelta** archivos `.ttf`, `.otf` o `.ttc` directamente sobre la ventana.
- Alternativa con selector de archivos si prefieres no arrastrar.
- Interfaz oscura, con zona de drop que reacciona al pasar el archivo por encima.
- Instala en `~/.local/share/fonts` (nivel usuario, sin necesidad de `sudo`).
- Refresca automáticamente el caché de fuentes (`fc-cache`) tras cada instalación.
- Empaquetado como paquete nativo de Arch (`PKGBUILD`), con ícono y entrada de menú.

## Requisitos

- Python ≥ 3.9
- [PySide6](https://pypi.org/project/PySide6/)
- `fontconfig` (para `fc-cache`, viene preinstalado en casi cualquier distro)

## Instalación

### Arch Linux / CachyOS (recomendado)

```bash
git clone https://github.com/tu-usuario/fonter.git
cd fonter
makepkg -si
```

Esto compila el paquete, instala `pyside6` como dependencia si falta, y lo registra en el sistema:

```bash
fonter
```

También aparecerá en tu menú de aplicaciones como **Instalador de Fuentes**.

### Manual (cualquier distro con Python)

```bash
git clone https://github.com/tu-usuario/fonter.git
cd fonter
python3 -m venv venv
source venv/bin/activate
pip install PySide6
python3 fonter.py
```

## Uso

1. Abre Fonter.
2. Arrastra tus archivos de fuente sobre la zona punteada, o usa el botón **Seleccionar archivo(s)**.
3. Las fuentes válidas se copian a `~/.local/share/fonts` y el caché se actualiza automáticamente.
4. Revisa el panel inferior para confirmar qué se instaló y qué se ignoró.

## Desinstalar

```bash
sudo pacman -R fonter
```

Esto no borra las fuentes ya instaladas en `~/.local/share/fonts` — solo elimina el programa.

## Estructura del repositorio

```
fonter/
├── PKGBUILD
├── fonter.py
├── fonter.desktop
├── fonter.svg
└── README.md
```

## Licencia

[Adivinando] Sin licencia definida todavía — agrega un `LICENSE` (MIT es lo más simple para un proyecto personal de este tamaño) si planeas que otros lo clonen o modifiquen.
