#!/usr/bin/python

from pisi.actionsapi import get, pisitools, shelltools
import shutil

WorkDir = "."


def install():
    shutil.rmtree("idea-IU-163.11103.6/jre")
    pisitools.insinto("/opt/idea", "idea-IU-163.11103.6/*")
    pisitools.dosym("/opt/idea/bin/idea.sh", "/usr/bin/idea")
