#!/usr/bin/env python3
"""
Instalador de fuentes para Linux - GUI moderna con PySide6 + drag & drop nativo.

Instalación (CachyOS / Arch):
    yay -S python-pyside6
    # o
    python3 -m venv venv && source venv/bin/activate
    pip install PySide6

Ejecutar:
    python3 instalador_fuentes_qt.py
"""

import os
import shutil
import subprocess
import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QDragEnterEvent, QDropEvent
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QPushButton,
    QTextEdit, QFileDialog, QFrame
)

FONT_DIR = os.path.expanduser("~/.local/share/fonts")
VALID_EXT = (".ttf", ".otf", ".ttc")

QSS = """
QWidget {
    background-color: #1e1f26;
    color: #e6e6e6;
    font-family: "Sans";
    font-size: 13px;
}

#DropZone {
    border: 2px dashed #5c5f77;
    border-radius: 14px;
    background-color: #262832;
    padding: 30px;
}

#DropZone[dragging="true"] {
    border: 2px dashed #8ab4f8;
    background-color: #2c2f3d;
}

QPushButton {
    background-color: #3b82f6;
    color: white;
    border: none;
    border-radius: 8px;
    padding: 10px 16px;
    font-weight: 600;
}

QPushButton:hover {
    background-color: #2563eb;
}

QPushButton:pressed {
    background-color: #1d4ed8;
}

QTextEdit {
    background-color: #16171c;
    border: 1px solid #33343d;
    border-radius: 8px;
    padding: 8px;
}
"""


def instalar_fuente(path: str):
    if not path.lower().endswith(VALID_EXT):
        return False, f"Ignorado (no es fuente válida): {os.path.basename(path)}"

    os.makedirs(FONT_DIR, exist_ok=True)
    destino = os.path.join(FONT_DIR, os.path.basename(path))

    try:
        shutil.copy2(path, destino)
        return True, f"✓ Instalada: {os.path.basename(path)}"
    except Exception as e:
        return False, f"✗ Error con {os.path.basename(path)}: {e}"


def refrescar_cache():
    try:
        subprocess.run(["fc-cache", "-f"], check=True,
                        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except Exception:
        return False


class DropZone(QFrame):
    def __init__(self, on_files_dropped):
        super().__init__()
        self.setObjectName("DropZone")
        self.setAcceptDrops(True)
        self.on_files_dropped = on_files_dropped

        layout = QVBoxLayout(self)
        self.label = QLabel("Arrastra aquí tus archivos .ttf / .otf")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)
        layout.addWidget(self.label)

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            self.setProperty("dragging", "true")
            self.style().unpolish(self)
            self.style().polish(self)
            event.acceptProposedAction()

    def dragLeaveEvent(self, event):
        self.setProperty("dragging", "false")
        self.style().unpolish(self)
        self.style().polish(self)

    def dropEvent(self, event: QDropEvent):
        self.setProperty("dragging", "false")
        self.style().unpolish(self)
        self.style().polish(self)

        rutas = [url.toLocalFile() for url in event.mimeData().urls()]
        self.on_files_dropped(rutas)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Instalador de Fuentes")
        self.resize(440, 380)

        layout = QVBoxLayout(self)
        layout.setSpacing(14)
        layout.setContentsMargins(20, 20, 20, 20)

        self.dropzone = DropZone(self.procesar)
        layout.addWidget(self.dropzone)

        btn = QPushButton("Seleccionar archivo(s)")
        btn.clicked.connect(self.seleccionar)
        layout.addWidget(btn)

        self.log = QTextEdit()
        self.log.setReadOnly(True)
        layout.addWidget(self.log)

    def escribir_log(self, mensaje):
        self.log.append(mensaje)

    def procesar(self, rutas):
        instaladas = 0
        for path in rutas:
            ok, msg = instalar_fuente(path)
            self.escribir_log(msg)
            if ok:
                instaladas += 1

        if instaladas > 0:
            if refrescar_cache():
                self.escribir_log(f"\nCaché actualizado ({instaladas} fuente(s) instalada(s)).")
            else:
                self.escribir_log("\nCopiadas, pero fc-cache falló. Ejecuta 'fc-cache -f' manualmente.")

    def seleccionar(self):
        rutas, _ = QFileDialog.getOpenFileNames(
            self, "Selecciona fuentes", "", "Fuentes (*.ttf *.otf *.ttc)"
        )
        if rutas:
            self.procesar(rutas)


def main():
    app = QApplication(sys.argv)
    app.setStyleSheet(QSS)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()