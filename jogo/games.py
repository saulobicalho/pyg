import forca
import guess

print("*********************************")
print("*******Escolha o seu jogo!*******")
print("*********************************")

print("(1) Forca (2) guess")

jogo = int(input("Qual jogo? "))

if (jogo == 1):
    print("Jogando forca")
elif (jogo == 2):
    print("Jogando guess")