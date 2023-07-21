from Mongo import ConnMongo
from ui.Ajouter_vol_ui import Ui_Ajouter_vol
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget



class Ajouter_vol(QWidget,Ui_Ajouter_vol):
    def __init__(self):
        self.form = QWidget()
        self.fenetre = Ui_Ajouter_vol()
        self.fenetre.setupUi(self.form)  # Créer une instance unique de Ui_Ajouter_vol

    def affiche_ajouter_vol(self):
        self.alimente_list_voile()
        conn = ConnMongo()
        self.form.show()
        self.fenetre.lb_Vol_enregistre.hide()

        def ajouter_vol():
            vol = {
                "Date": self.fenetre.le_date.text(),
                "Decollage": self.fenetre.le_decollage.text(),
                "Aterrissage": self.fenetre.le_atterissage.text(),
                "Distance": self.fenetre.le_distance.text(),
                "Voile": self.fenetre.comboBox.currentText(),
                "Distance_cumulee": self.fenetre.le_distance_cumulee.text(),
                "Vitesse_max": self.fenetre.le_vitesse_max.text(),
                "Vitesse_moyenne": self.fenetre.le_vitesse_moyenne.text(),
                "Plafond": self.fenetre.le_plafond.text(),
                "Gain": self.fenetre.le_gain.text(),
                "Temps_vol": self.fenetre.le_temps_vol.text(),
                "Vario_max": self.fenetre.le_vario_max.text(),
                "G-max": self.fenetre.le_g_max.text()
            }
            conn.ajouter_un_vol(vol)
            self.fenetre.lb_Vol_enregistre.show()
            self.fenetre.le_date.clear()
            self.fenetre.le_gain.clear()
            self.fenetre.le_temps_vol.clear()
            self.fenetre.le_vario_max.clear()
            self.fenetre.le_atterissage.clear()
            self.fenetre.le_decollage.clear()
            self.fenetre.le_distance.clear()
            self.fenetre.le_distance_cumulee.clear()
            self.fenetre.le_g_max.clear()
            self.fenetre.le_plafond.clear()
            self.fenetre.le_vario_max.clear()
            self.fenetre.le_temps_vol.clear()
            self.fenetre.le_vitesse_max.clear()
            self.fenetre.le_vitesse_moyenne.clear()

        self.fenetre.pb_ajouter_vol.clicked.connect(ajouter_vol)



    # Alimente le combobox "voile" pour choix de voile dans ajouter un vol
    def alimente_list_voile(self):
        conn = ConnMongo()
        liste = conn.recherche_voile()
        for elem in liste:
            self.fenetre.comboBox.addItem(elem)