SUMMARY = "Add haarcascade_eye"
LICENSE = "CLOSED"

SRC_URI = "file://haarcascade_eye.xml"

S = "${UNPACKDIR}"

do_install() {
    install -d ${D}${datadir}
    install -m 0644 ${S}/haarcascade_eye.xml ${D}${datadir}/haarcascade_eye.xml
}



FILES:${PN} += "${datadir} ${datadir}/haarcascade ${datadir}/haarcascade/*"

