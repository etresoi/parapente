from datetime import timedelta

from pymongo import MongoClient


class ConnMongo:
    liste_vols = []
    client = MongoClient(host='localhost', port=27017)
    db = client.parapente
    collectionClient = db.vols

    def recherche_vols(self):
        vols = self.collectionClient.find()
        self.liste_vols = []

        for vol in vols:
            self.liste_vols.append(vol)
        return self.liste_vols

    def ajouter_un_vol(self, vol):
        self.collectionClient.insert_one(vol)

    def recherche_voile(self):
        res = self.collectionClient.find({}, {"Voile": True})
        liste = set()
        for doc in res:
            voile = doc.get("Voile")
            if voile is not None:
                liste.add(voile)
        liste = list(liste)
        return liste

    def total_distance(self):
        req = [{"$group" : {"_id": "null", "dist_tot": {"$sum":"$Distance_cumulee"}}}]
        res = self.collectionClient.aggregate(req)
        for re in res:
            r = float(str(re["dist_tot"]))
        return (r/1000)

    def total_temps(self):
        req = [{"$group" : {"_id": "null", "temps_tot": {"$sum":"$Temps_vol"}}}]
        res = self.collectionClient.aggregate(req)
        for re in res:
            minutes = float(str(re["temps_tot"]))
        r = timedelta(minutes=minutes)
        return (r)

