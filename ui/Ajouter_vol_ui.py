# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ajouter_vol.ui'
##
## Created by: Qt User Interface Compiler version 6.0.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_Ajouter_vol(object):
    def setupUi(self, Ajouter_vol):
        if not Ajouter_vol.objectName():
            Ajouter_vol.setObjectName(u"Ajouter_vol")
        Ajouter_vol.resize(574, 615)
        self.lb_date = QLabel(Ajouter_vol)
        self.lb_date.setObjectName(u"lb_date")
        self.lb_date.setGeometry(QRect(50, 100, 100, 30))
        font = QFont()
        font.setPointSize(12)
        self.lb_date.setFont(font)
        self.lb_voile = QLabel(Ajouter_vol)
        self.lb_voile.setObjectName(u"lb_voile")
        self.lb_voile.setGeometry(QRect(50, 190, 100, 30))
        self.lb_voile.setFont(font)
        self.lb_decollage = QLabel(Ajouter_vol)
        self.lb_decollage.setObjectName(u"lb_decollage")
        self.lb_decollage.setGeometry(QRect(50, 130, 100, 30))
        self.lb_decollage.setFont(font)
        self.lb_distance_cumulee = QLabel(Ajouter_vol)
        self.lb_distance_cumulee.setObjectName(u"lb_distance_cumulee")
        self.lb_distance_cumulee.setGeometry(QRect(50, 250, 171, 30))
        self.lb_distance_cumulee.setFont(font)
        self.lb_distance = QLabel(Ajouter_vol)
        self.lb_distance.setObjectName(u"lb_distance")
        self.lb_distance.setGeometry(QRect(50, 220, 100, 30))
        self.lb_distance.setFont(font)
        self.lb_plafond = QLabel(Ajouter_vol)
        self.lb_plafond.setObjectName(u"lb_plafond")
        self.lb_plafond.setGeometry(QRect(50, 340, 100, 30))
        self.lb_plafond.setFont(font)
        self.lb_vitesse_moyenne = QLabel(Ajouter_vol)
        self.lb_vitesse_moyenne.setObjectName(u"lb_vitesse_moyenne")
        self.lb_vitesse_moyenne.setGeometry(QRect(50, 310, 141, 30))
        self.lb_vitesse_moyenne.setFont(font)
        self.lb_vitesse_max = QLabel(Ajouter_vol)
        self.lb_vitesse_max.setObjectName(u"lb_vitesse_max")
        self.lb_vitesse_max.setGeometry(QRect(50, 280, 100, 30))
        self.lb_vitesse_max.setFont(font)
        self.lb_vario_max = QLabel(Ajouter_vol)
        self.lb_vario_max.setObjectName(u"lb_vario_max")
        self.lb_vario_max.setGeometry(QRect(50, 430, 100, 30))
        self.lb_vario_max.setFont(font)
        self.lb_temps_vol = QLabel(Ajouter_vol)
        self.lb_temps_vol.setObjectName(u"lb_temps_vol")
        self.lb_temps_vol.setGeometry(QRect(50, 400, 121, 30))
        self.lb_temps_vol.setFont(font)
        self.lb_gain = QLabel(Ajouter_vol)
        self.lb_gain.setObjectName(u"lb_gain")
        self.lb_gain.setGeometry(QRect(50, 370, 100, 30))
        self.lb_gain.setFont(font)
        self.lb_atterissage = QLabel(Ajouter_vol)
        self.lb_atterissage.setObjectName(u"lb_atterissage")
        self.lb_atterissage.setGeometry(QRect(50, 160, 100, 30))
        self.lb_atterissage.setFont(font)
        self.lb_g_max = QLabel(Ajouter_vol)
        self.lb_g_max.setObjectName(u"lb_g_max")
        self.lb_g_max.setGeometry(QRect(50, 460, 100, 30))
        self.lb_g_max.setFont(font)
        self.le_date = QLineEdit(Ajouter_vol)
        self.le_date.setObjectName(u"le_date")
        self.le_date.setGeometry(QRect(220, 100, 271, 21))
        self.le_decollage = QLineEdit(Ajouter_vol)
        self.le_decollage.setObjectName(u"le_decollage")
        self.le_decollage.setGeometry(QRect(220, 130, 271, 21))
        self.le_atterissage = QLineEdit(Ajouter_vol)
        self.le_atterissage.setObjectName(u"le_atterissage")
        self.le_atterissage.setGeometry(QRect(220, 160, 271, 21))
        self.le_distance = QLineEdit(Ajouter_vol)
        self.le_distance.setObjectName(u"le_distance")
        self.le_distance.setGeometry(QRect(220, 220, 271, 21))
        self.le_distance_cumulee = QLineEdit(Ajouter_vol)
        self.le_distance_cumulee.setObjectName(u"le_distance_cumulee")
        self.le_distance_cumulee.setGeometry(QRect(220, 250, 271, 21))
        self.le_vitesse_max = QLineEdit(Ajouter_vol)
        self.le_vitesse_max.setObjectName(u"le_vitesse_max")
        self.le_vitesse_max.setGeometry(QRect(220, 280, 271, 21))
        self.le_vitesse_moyenne = QLineEdit(Ajouter_vol)
        self.le_vitesse_moyenne.setObjectName(u"le_vitesse_moyenne")
        self.le_vitesse_moyenne.setGeometry(QRect(220, 310, 271, 21))
        self.le_plafond = QLineEdit(Ajouter_vol)
        self.le_plafond.setObjectName(u"le_plafond")
        self.le_plafond.setGeometry(QRect(220, 340, 271, 21))
        self.le_gain = QLineEdit(Ajouter_vol)
        self.le_gain.setObjectName(u"le_gain")
        self.le_gain.setGeometry(QRect(220, 370, 271, 21))
        self.le_temps_vol = QLineEdit(Ajouter_vol)
        self.le_temps_vol.setObjectName(u"le_temps_vol")
        self.le_temps_vol.setGeometry(QRect(220, 400, 271, 21))
        self.le_vario_max = QLineEdit(Ajouter_vol)
        self.le_vario_max.setObjectName(u"le_vario_max")
        self.le_vario_max.setGeometry(QRect(220, 430, 271, 21))
        self.le_g_max = QLineEdit(Ajouter_vol)
        self.le_g_max.setObjectName(u"le_g_max")
        self.le_g_max.setGeometry(QRect(220, 460, 271, 21))
        self.lb_ajouter_vol = QLabel(Ajouter_vol)
        self.lb_ajouter_vol.setObjectName(u"lb_ajouter_vol")
        self.lb_ajouter_vol.setGeometry(QRect(180, 20, 231, 61))
        font1 = QFont()
        font1.setPointSize(18)
        self.lb_ajouter_vol.setFont(font1)
        self.pb_ajouter_vol = QPushButton(Ajouter_vol)
        self.pb_ajouter_vol.setObjectName(u"pb_ajouter_vol")
        self.pb_ajouter_vol.setGeometry(QRect(370, 500, 111, 50))
        self.pb_ajouter_vol.setFont(font)
        self.pb_fermer_ajouter_vol = QPushButton(Ajouter_vol)
        self.pb_fermer_ajouter_vol.setObjectName(u"pb_fermer_ajouter_vol")
        self.pb_fermer_ajouter_vol.setGeometry(QRect(190, 500, 171, 50))
        self.pb_fermer_ajouter_vol.setFont(font)
        self.lb_Vol_enregistre = QLabel(Ajouter_vol)
        self.lb_Vol_enregistre.setObjectName(u"lb_Vol_enregistre")
        self.lb_Vol_enregistre.setGeometry(QRect(220, 570, 191, 31))
        font2 = QFont()
        font2.setPointSize(13)
        self.lb_Vol_enregistre.setFont(font2)
        self.comboBox = QComboBox(Ajouter_vol)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(220, 190, 271, 22))

        self.retranslateUi(Ajouter_vol)

        QMetaObject.connectSlotsByName(Ajouter_vol)
    # setupUi

    def retranslateUi(self, Ajouter_vol):
        Ajouter_vol.setWindowTitle(QCoreApplication.translate("Ajouter_vol", u"Ajouter un vol", None))
        self.lb_date.setText(QCoreApplication.translate("Ajouter_vol", u"Date du vol :", None))
        self.lb_voile.setText(QCoreApplication.translate("Ajouter_vol", u"Voile :", None))
        self.lb_decollage.setText(QCoreApplication.translate("Ajouter_vol", u"D\u00e9collage :", None))
        self.lb_distance_cumulee.setText(QCoreApplication.translate("Ajouter_vol", u"Distance cumul\u00e9e :", None))
        self.lb_distance.setText(QCoreApplication.translate("Ajouter_vol", u"Distance :", None))
        self.lb_plafond.setText(QCoreApplication.translate("Ajouter_vol", u"Plafond :", None))
        self.lb_vitesse_moyenne.setText(QCoreApplication.translate("Ajouter_vol", u"Vitesse moyenne :", None))
        self.lb_vitesse_max.setText(QCoreApplication.translate("Ajouter_vol", u"Vitesse max :", None))
        self.lb_vario_max.setText(QCoreApplication.translate("Ajouter_vol", u"Vario Max :", None))
        self.lb_temps_vol.setText(QCoreApplication.translate("Ajouter_vol", u"Temps de vol :", None))
        self.lb_gain.setText(QCoreApplication.translate("Ajouter_vol", u"Gain :", None))
        self.lb_atterissage.setText(QCoreApplication.translate("Ajouter_vol", u"Atterissage :", None))
        self.lb_g_max.setText(QCoreApplication.translate("Ajouter_vol", u"G max :", None))
        self.lb_ajouter_vol.setText(QCoreApplication.translate("Ajouter_vol", u"Ajouter un vol :", None))
        self.pb_ajouter_vol.setText(QCoreApplication.translate("Ajouter_vol", u"Ajouter le vol", None))
        self.pb_fermer_ajouter_vol.setText(QCoreApplication.translate("Ajouter_vol", u"Fermer la fen\u00eatre", None))
        self.lb_Vol_enregistre.setText(QCoreApplication.translate("Ajouter_vol", u"Vol enregistr\u00e9", None))
    # retranslateUi

