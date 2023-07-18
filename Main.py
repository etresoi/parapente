from ui.Main_ui import Ui_MainWindow
from ui.Ajouter_vol_ui import Ui_Ajouter_vol
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from Mongo import ConnMongo


class Vols(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Vols, self).__init__()
        self.setupUi(self)
        self.form = QWidget()
        self.fenetre = Ui_Ajouter_vol()
        self.fenetre.setupUi(self.form)  # Créer une instance unique de Ui_Ajouter_vol
        self.pb_afficher.clicked.connect(self.afficher_vols)
        self.pb_ajouter_vol.clicked.connect(self.affiche_ajouter_vol)

    # Alimente le combobox "voile" pour choix de voile dans ajouter un vol
    def alimente_list_voile(self):
        conn = ConnMongo()
        liste = conn.recherche_voile()
        for elem in liste:
            self.fenetre.comboBox.addItem(elem)

    def afficher_vols(self):
        connection = ConnMongo()
        vols = connection.recherche_vols()
        for vol in vols:
            self.lv_les_vols.addItem(str(f'{vol["Date"]} {vol["Decollage"]} {vol["Temps_vol"]}'))
        tempsvol = connection.total_distance()
        self.lb_resultat_km.setText(str(tempsvol))
        km_total =connection.total_temps()
        self.lb_resultat_temps_vol.setText(str(km_total))



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


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Vols()
    window.show()

    sys.exit(app.exec())
