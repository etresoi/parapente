from PySide6.QtCore import QEvent
from Mongo import ConnMongo
from ui.Ajouter_vol_ui import Ui_Ajouter_vol
from datetime import datetime
from PySide6.QtWidgets import QWidget
from bson import Decimal128

class AjouterVol(QWidget, Ui_Ajouter_vol):
    def __init__(self):
        super().__init__()
        self.form = QWidget()
        self.fenetre = Ui_Ajouter_vol()
        self.fenetre.setupUi(self.form)  # Créer une instance unique de Ui_Ajouter_vol
        #Ajoute un listener pour supprimer le label "vol ajouté"
        self.fenetre.le_date.installEventFilter(self)

    def affiche_ajouter_vol(self):
        self.alimente_list_voile()
        conn = ConnMongo()
        self.form.show()
        self.fenetre.lb_Vol_enregistre.hide()
        self.fenetre.pb_fermer_ajouter_vol.clicked.connect(self.form.close)

        def ajouter_vol():
            date_str = self.fenetre.le_date.text()
            date_obj = datetime.strptime(date_str, "%d.%m.%Y")
            vol = {
                "Date": date_obj,
                "Decollage": self.fenetre.le_decollage.text(),
                "Aterrissage": self.fenetre.le_atterissage.text(),
                "Distance": Decimal128(self.fenetre.le_distance.text()),
                "Voile": self.fenetre.comboBox.currentText(),
                "Distance_cumulee": Decimal128(self.fenetre.le_distance_cumulee.text()),
                "Vitesse_max": Decimal128(self.fenetre.le_vitesse_max.text()),
                "Vitesse_moyenne": Decimal128(self.fenetre.le_vitesse_moyenne.text()),
                "Plafond": Decimal128(self.fenetre.le_plafond.text()),
                "Gain": Decimal128(self.fenetre.le_gain.text()),
                "Temps_vol": Decimal128(self.fenetre.le_temps_vol.text()),
                "Vario_max": Decimal128(self.fenetre.le_vario_max.text()),
                "G-max": Decimal128(self.fenetre.le_g_max.text())
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

    def eventFilter(self, obj, event):
        if obj == self.fenetre.le_date and event.type() == QEvent.FocusIn:
            self.hidelabel()
        return super().eventFilter(obj, event)

    def hidelabel(self):
        self.fenetre.lb_Vol_enregistre.hide()
