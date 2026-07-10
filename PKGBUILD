pkgname=fonter
pkgver=0.1
pkgrel=1
pkgdesc="Instalador de fuentes simple, con drag & drop"
arch=('any')
depends=('python' 'pyside6' 'qt6-svg' 'hicolor-icon-theme')
source=('fonter.py' 'fonter.desktop' 'fonter.svg')
sha256sums=('SKIP' 'SKIP' 'SKIP')

package() {
    install -Dm755 "$srcdir/fonter.py" \
        "$pkgdir/usr/lib/fonter/fonter.py"

    install -Dm755 /dev/stdin "$pkgdir/usr/bin/fonter" <<EOF
#!/bin/sh
exec python3 /usr/lib/fonter/fonter.py
EOF

    install -Dm644 "$srcdir/fonter.desktop" \
        "$pkgdir/usr/share/applications/fonter.desktop"

    install -Dm644 "$srcdir/fonter.svg" \
        "$pkgdir/usr/share/icons/hicolor/scalable/apps/fonter.svg" 
}