from abc import ABC , abstractmethod
class ObjetPostal(ABC):
    def __init__(self,n,a,c,v,re):
        self.name = n
        self.adresse = a
        self.code = c
        self.ville = v
        self.recommande = re
    @abstractmethod
    def prix(self):
        pass
class Lettre(ObjetPostal):
    def __init__(self, n, a, c, v, re,ur):
        super().__init__(n, a, c, v, re)
        self.urgence = ur
    def prix(self):
        x = 0.53
        if (self.recommande == True):
            x +=1.5
        if (self.urgence == True):
            x +=0.6
        return x
class Colis(ObjetPostal):
    def __init__(self, n, a, c, v, re,ex):
        super().__init__(n, a, c, v, re)
        self.exprime = ex
    def prix(self):
        t = self.exprime * 0.8 /100
        if (self.recommande == True):
            return t+3

def afficher_menu():
    print("1. Envoyer une lettre")
    print("2. Envoyer un colis")
    print("0. Quitter")


while True:
    afficher_menu()
    choix = input("Choisissez une option (1, 2, ou 0 pour quitter): ")

    if choix == "1":
        nom_destinataire = input("Nom du destinataire : ")
        adresse_destinataire = input("Adresse du destinataire : ")
        code_postal = int(input("Code postal : "))
        ville_destination = input("Ville destination : ")
        recommande = input("Envoyer en recommandé ? (Oui/Non) : ").lower() == "oui"
        urgence = input("Envoyer en urgence ? (Oui/Non) : ").lower() == "oui"

        lettre = Lettre(nom_destinataire, adresse_destinataire, code_postal, ville_destination, recommande, urgence)
        print("Prix à payer :", lettre.prix())

    elif choix == "2":
        nom_destinataire = input("Nom du destinataire : ")
        adresse_destinataire = input("Adresse du destinataire : ")
        code_postal = int(input("Code postal : "))
        ville_destination = input("Ville destination : ")
        recommande = input("Envoyer en recommandé ? (Oui/Non) : ").lower() == "oui"
        poids_colis = float(input("Poids du colis en grammes : "))

        colis = Colis(nom_destinataire, adresse_destinataire, code_postal, ville_destination, recommande, poids_colis)
        print("Prix à payer :", Colis.prix())

    elif choix == "0":
        break

    else:
        print("Option invalide. Veuillez choisir une option valide.")