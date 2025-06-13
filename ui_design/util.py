import os
import sys
from PyQt5 import QtGui, QtCore

def get_base_path():
    """Returns the correct base directory depending on script vs PyInstaller EXE."""
    if getattr(sys, 'frozen', False):
        return sys._MEIPASS
    return os.path.dirname(os.path.abspath(__file__))

def get_resource_path(relative_path):
    """Builds the full path to the resource, relative to base dir."""
    basedir = get_base_path()
    return os.path.join(basedir, *relative_path.split("/"))

def load_pixmap(relative_path, scale=None):
    """
    Loads and returns a QPixmap, optionally scaled.
    """
    image_path = get_resource_path(relative_path)
    pixmap = QtGui.QPixmap(image_path)
    if scale:
        pixmap = pixmap.scaled(scale[0], scale[1],
                               QtCore.Qt.KeepAspectRatio,
                               QtCore.Qt.SmoothTransformation)
    return pixmap
