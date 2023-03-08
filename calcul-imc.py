def calculIMC(taille,masse):
    return masse/(taille**2)

masse = float(input("Veuillez entrez votre poids en kg :"))
taille = float(input("Veuillez entrez votre taille en mètres :"))

imc = calculIMC(taille,masse)

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

