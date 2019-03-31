# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pocbrowser.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PocBrowser(object):
    def setupUi(self, PocBrowser):
        PocBrowser.setObjectName("PocBrowser")
        PocBrowser.resize(1053, 841)
        self.centralwidget = QtWidgets.QWidget(PocBrowser)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.webEngine = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.webEngine.setUrl(QtCore.QUrl("about:blank"))
        self.webEngine.setObjectName("webEngine")
        self.gridLayout.addWidget(self.webEngine, 3, 0, 1, 2)
        self.urlLineEditWidget = QtWidgets.QLineEdit(self.centralwidget)
        self.urlLineEditWidget.setObjectName("urlLineEditWidget")
        self.gridLayout.addWidget(self.urlLineEditWidget, 2, 0, 1, 2)
        PocBrowser.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PocBrowser)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1053, 22))
        self.menubar.setObjectName("menubar")
        PocBrowser.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PocBrowser)
        self.statusbar.setObjectName("statusbar")
        PocBrowser.setStatusBar(self.statusbar)

        self.retranslateUi(PocBrowser)
        QtCore.QMetaObject.connectSlotsByName(PocBrowser)

    def retranslateUi(self, PocBrowser):
        _translate = QtCore.QCoreApplication.translate
        PocBrowser.setWindowTitle(_translate("PocBrowser", "MainWindow"))

from PyQt5 import QtWebEngineWidgets
