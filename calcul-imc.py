import argparse

def calculIMC(taille_cm,poids):
    taille_m = taille_cm / 100
    return poids/(taille_m**2)

if __name__=='__main__':
        parser = argparse.ArgumentParser(description='Calcul de l\'IMC')
        parser.add_argument('taille', type=float, help='Taille en centimètres')
        parser.add_argument('poids_actuel', type=float, help='Poids en kilogrammes')
        args = parser.parse_args()

imc = calculIMC(args.taille,args.poids_actuel)

if imc < 16.5:
    print("Votre IMC : ",imc,". Vous souffrez d'insuffisance pondérale sévère.")
if 16.5 <= imc < 18.5 :
    print("Votre IMC : ",imc,". Vous souffrez d'insuffisance pondérale.")
if 18.5 <= imc < 25 :
    print("Votre IMC : ",imc,". Votre poids est normal.")
if 25 <= imc < 30 :
    print("Votre IMC : ",imc,". Votre êtes en surpoids.")
if 30 <= imc < 35 :
    print("Votre IMC : ",imc,". Vous souffrez d'obésité de grade 1.")
if 35 <= imc < 40 :
    print("Votre IMC : ",imc,". Vous souffrez d'obésité de grade 2.")
if imc >= 40 :
    print("Votre IMC : ",imc,". Vous souffrez d'obésité de grade 3.")

