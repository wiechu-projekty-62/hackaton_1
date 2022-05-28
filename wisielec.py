from random import choice
def wisielec():
    slownik = wczytaj("miasta.txt")
    password = choice(slownik)
    guessed = "*" * len(password)
    trials = 10

    while guessed != password and trials > 0:
        print("Zgadnij hasło", guessed)
        zapyt = "t"
        while zapyt == "t" and trials > 0:
            zapyt = input("Chcesz podać całe hasło ? [t/n] ")
            if zapyt == "t":
                allguessed = input("Podaj całe hasło: ")
                if allguessed == password:
                    trials = 0
                    zapyt = "n"
                    break

                else:
                    print("nieprawidłowe hasło :-(")
                    trials -= 1
                    print("Pozostało prób: ", trials)
            else:
                allguessed = ""
                break

        if trials > 0:
            print("Pozostało prób: ", trials)
            response = input("Podaj literę ")
            if  response in password:
                for i in range(len(password)):
                    if response == password[i]:
                        guessed = guessed[:i] + response + guessed[i + 1:]
            else:
                trials -= 1
    if guessed == password or allguessed == password:
        print("Odgadłeś - hasło to", password)
    else:
        print("nieprawidłowe hasło :-(")
def wczytaj(nazwa):
    ident = open(nazwa)
    lista = []
    for x in ident:
        lista.append(x.strip())
    ident.close()
    return lista
wisielec()





