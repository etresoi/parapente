from  Mongo import ConnMongo
from ui.Detail_vol_ui import Ui_Detail_vol
from PySide6.QtWidgets import QWidget


class ModifierVol(QWidget, Ui_Detail_vol):
    def __init__(self):
        super.__init__()
        self.fen = QWidget
        self.fenetre_detail = Ui_Detail_vol()
        # Créer une instance unique
        self.fenetre_detail.setupUi(self.fen)
