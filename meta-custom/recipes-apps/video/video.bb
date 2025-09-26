SUMMARY = "Add video1.mp4"
LICENSE = "CLOSED"

SRC_URI = "file://video1.mp4"

S = "${UNPACKDIR}"

do_install() {
    install -d ${D}${datadir}
    install -m 0644 ${S}/video1.mp4 ${D}${datadir}/video1.mp4
}



FILES:${PN} += "${datadir} ${datadir}/video1.mp4"

