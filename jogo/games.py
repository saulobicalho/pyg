import hang
import guess

print("*********************************")
print("*******Escolha o seu jogo!*******")
print("*********************************")

print("(1) hang (2) guess")

jogo = int(input("Qual jogo? "))

if (jogo == 1):
    print("Jogando hang")
    hang.play()
elif (jogo == 2):
    print("Jogando guess")
    guess.play()
