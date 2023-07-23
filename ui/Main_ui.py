# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(726, 563)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lb_les_vols = QLabel(self.centralwidget)
        self.lb_les_vols.setObjectName(u"lb_les_vols")
        self.lb_les_vols.setGeometry(QRect(190, 10, 171, 31))
        font = QFont()
        font.setPointSize(23)
        self.lb_les_vols.setFont(font)
        self.pb_afficher = QPushButton(self.centralwidget)
        self.pb_afficher.setObjectName(u"pb_afficher")
        self.pb_afficher.setGeometry(QRect(330, 70, 121, 51))
        font1 = QFont()
        font1.setPointSize(11)
        self.pb_afficher.setFont(font1)
        self.pb_ajouter_vol = QPushButton(self.centralwidget)
        self.pb_ajouter_vol.setObjectName(u"pb_ajouter_vol")
        self.pb_ajouter_vol.setGeometry(QRect(330, 130, 121, 51))
        self.pb_ajouter_vol.setFont(font1)
        self.pb_supprimer_vol = QPushButton(self.centralwidget)
        self.pb_supprimer_vol.setObjectName(u"pb_supprimer_vol")
        self.pb_supprimer_vol.setGeometry(QRect(330, 190, 121, 51))
        self.pb_supprimer_vol.setFont(font1)
        self.lv_les_vols = QListWidget(self.centralwidget)
        self.lv_les_vols.setObjectName(u"lv_les_vols")
        self.lv_les_vols.setGeometry(QRect(40, 80, 256, 411))
        self.pb_afficher_detail = QPushButton(self.centralwidget)
        self.pb_afficher_detail.setObjectName(u"pb_afficher_detail")
        self.pb_afficher_detail.setGeometry(QRect(330, 250, 121, 51))
        self.pb_afficher_detail.setFont(font1)
        self.pb_quitter = QPushButton(self.centralwidget)
        self.pb_quitter.setObjectName(u"pb_quitter")
        self.pb_quitter.setGeometry(QRect(330, 310, 121, 51))
        self.pb_quitter.setFont(font1)
        self.lb_Main_deco = QLabel(self.centralwidget)
        self.lb_Main_deco.setObjectName(u"lb_Main_deco")
        self.lb_Main_deco.setGeometry(QRect(50, 60, 49, 16))
        self.lb_Main_deco_2 = QLabel(self.centralwidget)
        self.lb_Main_deco_2.setObjectName(u"lb_Main_deco_2")
        self.lb_Main_deco_2.setGeometry(QRect(110, 60, 61, 16))
        self.lb_Main_duree = QLabel(self.centralwidget)
        self.lb_Main_duree.setObjectName(u"lb_Main_duree")
        self.lb_Main_duree.setGeometry(QRect(180, 60, 61, 16))
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(470, 140, 241, 121))
        font2 = QFont()
        font2.setBold(True)
        self.groupBox.setFont(font2)
        self.groupBox.setFlat(False)
        self.lb_temps_vol = QLabel(self.groupBox)
        self.lb_temps_vol.setObjectName(u"lb_temps_vol")
        self.lb_temps_vol.setGeometry(QRect(10, 40, 111, 21))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        self.lb_temps_vol.setFont(font3)
        self.lb_resultat_km = QLabel(self.groupBox)
        self.lb_resultat_km.setObjectName(u"lb_resultat_km")
        self.lb_resultat_km.setGeometry(QRect(130, 70, 91, 21))
        self.lb_resultat_km.setFont(font3)
        self.lb_resultat_temps_vol = QLabel(self.groupBox)
        self.lb_resultat_temps_vol.setObjectName(u"lb_resultat_temps_vol")
        self.lb_resultat_temps_vol.setGeometry(QRect(130, 40, 91, 21))
        self.lb_resultat_temps_vol.setFont(font3)
        self.lb_km = QLabel(self.groupBox)
        self.lb_km.setObjectName(u"lb_km")
        self.lb_km.setGeometry(QRect(10, 70, 111, 21))
        self.lb_km.setFont(font3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 726, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Parapente", None))
        self.lb_les_vols.setText(QCoreApplication.translate("MainWindow", u"Les vols :", None))
        self.pb_afficher.setText(QCoreApplication.translate("MainWindow", u"Afficher les vols", None))
        self.pb_ajouter_vol.setText(QCoreApplication.translate("MainWindow", u"Ajouter un vol", None))
        self.pb_supprimer_vol.setText(QCoreApplication.translate("MainWindow", u"Supprimer un vol", None))
        self.pb_afficher_detail.setText(QCoreApplication.translate("MainWindow", u"Afficher d\u00e9tail", None))
        self.pb_quitter.setText(QCoreApplication.translate("MainWindow", u"Quitter", None))
        self.lb_Main_deco.setText(QCoreApplication.translate("MainWindow", u"Date |", None))
        self.lb_Main_deco_2.setText(QCoreApplication.translate("MainWindow", u"D\u00e9collage |", None))
        self.lb_Main_duree.setText(QCoreApplication.translate("MainWindow", u"Dur\u00e9e", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"R\u00e9sum\u00e9", None))
        self.lb_temps_vol.setText(QCoreApplication.translate("MainWindow", u"Temps de vol :", None))
        self.lb_resultat_km.setText("")
        self.lb_resultat_temps_vol.setText("")
        self.lb_km.setText(QCoreApplication.translate("MainWindow", u"KM parcouru :", None))
    # retranslateUi

