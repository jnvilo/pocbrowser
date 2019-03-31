# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pocbrowser.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!


import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebKit import *
from PyQt5.QtWebKitWidgets import *
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from ui_pocbrowser import Ui_PocBrowser

class PocBrowser(QMainWindow,Ui_PocBrowser):

    def __init__(self):
        super(self, ProcBrowser).__init__()
        self.setupUi()
        
    
    def navigate_home(self):
        self.browser.setUrl( QUrl("http://www.google.com") )
        
    def navigate_to_url(self): # Does not receive the Url
        q = QUrl( self.urlbar.text() )
        if q.scheme() == "":
            q.setScheme("http")
            
        self.browser.setUrl(q)    
        
        
    
    #def update_urlbar(self, q):
        
        #self.urlbar.setText(q.toString())
        #self.urlbar.setCursorPosition(0)
        
    #def setup_connections(self):
        
        #self.browser.urlChanged.connect(self.update_urlbar)
        #self.browser.loadFinished.connect(self.update_title)    
        
    
    