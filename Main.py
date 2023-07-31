from ui.Main_ui import Ui_MainWindow
from ui.Ajouter_vol_ui import Ui_Ajouter_vol
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from AjouterVol import AjouterVol
from Mongo import ConnMongo
from ModifierVol import ModifierVol


class Vols(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Vols, self).__init__()
        self.setupUi(self)
        self.pb_afficher.clicked.connect(self.afficher_vols)
        self.pb_ajouter_vol.clicked.connect(self.lance_affiche_ajouter_vol)
        self.pb_afficher_detail.clicked.connect(self.detail_vol)
        self.pb_quitter.clicked.connect(QApplication.quit)

    def afficher_vols(self):
        connection = ConnMongo()
        vols = connection.recherche_vols()
        for vol in vols:
            date_obj = vol["Date"]
            date_str = date_obj.strftime("%d.%m.%Y")
            self.lv_les_vols.addItem(str(f'{date_str} {"|"} {vol["Decollage"]} {"|"} {vol["Temps_vol"]}'))
        tempsvol = connection.total_distance()
        self.lb_resultat_km.setText(str(tempsvol))
        km_total = connection.total_temps()
        self.lb_resultat_temps_vol.setText(str(km_total))

    def lance_affiche_ajouter_vol(self):
        aj_vol = AjouterVol()
        aj_vol.affiche_ajouter_vol()

    def detail_vol(self):
        det_vol = ModifierVol()
        det_vol.affiche_modifier_vol()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Vols()
    window.show()

    sys.exit(app.exec())
