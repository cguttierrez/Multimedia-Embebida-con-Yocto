SUMMARY = "Add haarcasxades"
LICENSE = "CLOSED"

SRC_URI = "file://haarcascade_frontalface_default.xml"

S = "${UNPACKDIR}"

do_install() {
    install -d ${D}${datadir}
    install -m 0644 ${S}/haarcascade_frontalface_default.xml ${D}${datadir}/haarcascade_frontalface_default.xml
}



FILES:${PN} += "${datadir} ${datadir}/haarcascades ${datadir}/haarcascades/*"

