SUMMARY = "Minimal image with Python3, OpenCV, and GStreamer"
LICENSE = "MIT"

inherit core-image

IMAGE_INSTALL += "\
    python3 \
    python3-pip \
    opencv \
    gstreamer1.0 \
    gstreamer1.0-plugins-base \
    gstreamer1.0-plugins-good \
    gstreamer1.0-plugins-bad \
    gstreamer1.0-plugins-ugly \
"

