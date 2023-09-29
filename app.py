import csv
import sqlite3
from string import Template

def ouvrir_le_csv(nom_du_fichier, f):
    with open(nom_du_fichier, newline='') as f:
        dialect = csv.Sniffer().sniff(f.read(1024))
        f.seek(0)
        reader = csv.reader(f, dialect)
        donnees = list(reader)
        return donnees[1:]

def commandes_bd(donnees_commandes):
    con =
    for L in donnees_commandes:
       s=Template("""INSERT INTO commandes VALUES ($idclient, $idmeuble, $quantite, $date)""")
       print(len(L))
       requete = s.substitute(idclient=L[0],idmeuble = L[1], quantite=L[2], date=L[3])
       print(requete)



if __name__ == "__main__":
    donnees_commandes = ouvrir_le_csv("commandes.csv", "commandes")
    donnees2 = ouvrir_le_csv("clients.csv", "client")
    con = sqlite3.connect("bddclient.db")
    commandes_bd(donnees_commandes)