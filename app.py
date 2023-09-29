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
def reset():
    conn = sqlite3.connect('bddclient.db')
    cur = conn.cursor()
    sql = "DELETE FROM commande"
    sql2 = "DELETE FROM client"
    cur.execute(sql)
    cur.execute(sql2)
    conn.commit()
    print("Enregistrement supprimé avec succès")
    cur.close()
    conn.close()

def commandes_bd(donnees_commandes):
    con = sqlite3.connect("bddclient.db")
    cur = con.cursor()
    for L in donnees_commandes:
       s=Template("""INSERT INTO commande(idclient, idmeuble, quantite, date) VALUES ("$idclient", "$idmeuble", "$quantite", "$date")""")
       requete = s.substitute(idclient=L[0],idmeuble = L[1], quantite=L[2], date=L[3])
       cur.execute(requete)
       con.commit()

def client_bd(donnees_client):
    con = sqlite3.connect("bddclient.db")
    cur = con.cursor()
    for L in donnees_client:
        s=Template("""INSERT INTO client(nom, prenom, adresse, ville, email, mdp) VALUES ("$nom","$prenom", "$adresse", "$ville", "$email", "$mdp")""")
        requete = s.substitute(nom=L[0],prenom = L[1], adresse =L[2], ville=L[3], email = L[4], mdp = L[5])
        cur.execute(requete)
        con.commit()

if __name__ == "__main__":
    donnees_commandes = ouvrir_le_csv("commandes.csv", "commandes")
    donnees_client = ouvrir_le_csv("clients.csv", "client")
    con = sqlite3.connect("bddclient.db")
    reset()
    commandes_bd(donnees_commandes)
    client_bd(donnees_client)