"""
Copyright (c) 2012 Shotgun Software, Inc
----------------------------------------------------
"""
import nuke
import os
import sys

from PySide import QtCore, QtGui
from .ui.header import Ui_Header
from .list_base import ListBase

class ListHeader(ListBase):
    
    def __init__(self, app, worker, parent=None):
        ListBase.__init__(self, app, worker, parent)

        # set up the UI
        self.ui = Ui_Header() 
        self.ui.setupUi(self)
        self.ui.label.setText("<big>Shots and Shit</big>")        
        self.ui.background.setStyleSheet("background-color: #6F6F6F;")

    def set_title(self, title):
        self.ui.label.setText("<big>%s</big>" % title)
        
    def get_title(self):
        return self.ui.label.text()