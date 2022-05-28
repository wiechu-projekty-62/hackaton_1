from random import choice
from turtle import *
def wisielec():
    slownik = wczytaj("miasta.txt")
    password = choice(slownik)
    guessed = "*" * len(password)
    trials = 10
    rysunek(trials)

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
                    rysunek(trials)
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
                rysunek(trials)

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

def rysunek(nr):

    #czyszczenie
    seth(0); setpos(0, 0); clear()
    if nr == 10: return

    #podstawa
    bk(80); fd(40); lt(90)
    if nr == 9: return
    #pion
    fd(200); rt(90)
    if nr == 8: return

    #poziom
    fd(100); rt(90)
    if nr == 7: return

    #haczyk
    fd(30)
    if nr == 6: return

    #głowa
    lt(90)
    for i in range(36):
        fd(3); rt(10)
    rt(90)
    if nr == 5: return

    #tułów
    pu(); fd(36); pd()
    fd(60)
    if nr == 4: return

    #prawa ręka
    bk(50); rt(45); fd(30); bk(30)
    if nr ==3: return

    #lewa ręka
    lt(90); fd(30); bk(30); rt(45)
    if nr == 2: return

    #prawa noga
    fd(50); rt(30); fd(50); bk(50)
    if nr == 1: return

    #lewa noga
    lt(60); fd(50); bk(50); rt(45)

    pu()
    ht()
    x = input("Zakończ wyswietlanie grafiki [enter]")

wisielec()





