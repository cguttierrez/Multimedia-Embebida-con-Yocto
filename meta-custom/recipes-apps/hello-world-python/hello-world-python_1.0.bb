SUMMARY = "Simple Hello World script in Python"
LICENSE = "CLOSED"

SRC_URI = "file://hello-world.py"

S = "${UNPACKDIR}"

do_install() {
    install -d ${D}${bindir}
    install -m 0755 ${S}/hello-world.py ${D}${bindir}/hello-world
}

