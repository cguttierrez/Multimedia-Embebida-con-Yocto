SUMMARY = "Rostros"
LICENSE = "CLOSED"

SRC_URI += "file://reconoceRostros.py"

S = "${UNPACKDIR}"

do_install() {
    install -d ${D}${bindir}
    install -m 0755 ${S}/reconoceRostros.py ${D}${bindir}/reconoceRostros
}


