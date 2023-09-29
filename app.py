import csv
import sqlite3
from string import Template

def ouvrir_le_csv(nom_du_fichier, f):
    with open(nom_du_fichier, newline='') as f:
        dialect = csv.Sniffer().sniff(f.read(1024))
        f.seek(0)
        reader = csv.reader(f, dialect)
        donnees = [row for row in reader]
        return donnees[1:]

def commandes_bd(donnees_commandes):
    print(donnees_commandes)
    for L in donnees_commandes:
       s=Template("""INSERT INTO commandes VALUES ($nom, $prenom, $adresse, $ville, $email, $motdepasse)""")
       print(L)
       #requete = s.substitute(nom=L[0],prenom=L[1],adresse = L[2], ville=L[3], email=L[4], motdepasse=L[5])
       #print(requete)
       #print(L)

if __name__ == "__main__":
    donnees_commandes = ouvrir_le_csv("commandes.csv", "commandes")
    donnees2 = ouvrir_le_csv("clients.csv", "client")
    con = sqlite3.connect("bddclient.db")
    commandes_bd(donnees_commandes)