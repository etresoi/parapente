from ui.Main_ui import Ui_MainWindow
from ui.Ajouter_vol_ui import Ui_Ajouter_vol
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from Ajouter_vol import Ajouter_vol
from Mongo import ConnMongo


class Vols(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Vols, self).__init__()
        self.setupUi(self)
        self.pb_afficher.clicked.connect(self.afficher_vols)
        self.pb_ajouter_vol.clicked.connect(self.lance_affiche_ajouter_vol)

    def afficher_vols(self):
        connection = ConnMongo()
        vols = connection.recherche_vols()
        for vol in vols:
            self.lv_les_vols.addItem(str(f'{vol["Date"]} {vol["Decollage"]} {vol["Temps_vol"]}'))
        tempsvol = connection.total_distance()
        self.lb_resultat_km.setText(str(tempsvol))
        km_total =connection.total_temps()
        self.lb_resultat_temps_vol.setText(str(km_total))

    def lance_affiche_ajouter_vol(self):
        aj_vol = Ajouter_vol()
        aj_vol.affiche_ajouter_vol()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Vols()
    window.show()

    sys.exit(app.exec())
