from cons import *
import pygame
import random


class Ptak:
    def __init__(self):
        self.ROZMIAR = 40
        self.KOLOR = (255, 255, 0)

        # ustawiamy flappiego na środku ekranu
        self.Y = WYSOKOSC // 2 - self.ROZMIAR // 2
        self.X = SZEROKOSC // 2 - self.ROZMIAR // 2

        # początkowa prędkość i stałe związane z prędkością
        self.predkosc = 1
        self.SILA_SKOKU = 60
        self.PRZYSPIESZENIE = 0.1

    def skacz(self):
        # przesuń flappiego do góry o siłę skoku
        self.Y = self.Y - self.SILA_SKOKU
        self.predkosc = 0

    def spadaj(self):
        # Sprawdź czy flappy dotyka dolnej krawędzi ekranu
        if self.Y >= WYSOKOSC - self.ROZMIAR:
            self.Y = WYSOKOSC - self.ROZMIAR
            self.predkosc = 0
        elif self.Y <= 0:
            self.Y = 0
            self.predkosc = 0
        # poruszanie flappim
        self.predkosc = self.predkosc + self.PRZYSPIESZENIE
        self.Y = self.Y + self.predkosc

    def rysuj(self, ekran):
        pygame.draw.rect(ekran, self.KOLOR, (self.X, self.Y, self.ROZMIAR, self.ROZMIAR))

class Rura:
    def __init__(self, x):
        self.y = 0
        self.start = x
        self.x = self.start
        self.SZEROKOSC = 50
        self.WYSOKOSC = WYSOKOSC
        self.PREDKOSC = 5
        self.KOLOR = (0, 255, 0)
        self.przerwa_wysokosc = random.randint(150, 450)
        self.odstęp = 200
    
    def poruszanie(self):
        self.x = self.x - self.PREDKOSC
        if self.x <= 0:
            self.x = self.start
            self.przerwa_wysokosc = random.randint(150, 450)
    
    def rysuj(self, ekran):
        pygame.draw.rect(ekran, self.KOLOR, (self.x, 0, self.SZEROKOSC, self.przerwa_wysokosc))
        pygame.draw.rect(ekran, self.KOLOR, (self.x, self.przerwa_wysokosc + self.odstęp, self.SZEROKOSC, self.WYSOKOSC))

    def sprawdz_kolizje(self, ptak):
        # Sprawdzenie, czy ptak uderza w rurę
        if ptak.X + ptak.ROZMIAR > self.x and ptak.X < self.x + self.SZEROKOSC:
            if ptak.Y < self.przerwa_wysokosc or ptak.Y + ptak.ROZMIAR > self.przerwa_wysokosc + self.odstęp:
                return True
        return False
