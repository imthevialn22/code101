
import pygame
import random
from cons import *
from clas import Rura, Ptak

# Włączamy silnik Pygame
pygame.init()
czekaj = True

# Wybieramy kolory
CZERWONY = (255, 0, 0)
SZARY = (169, 169, 169)

# Zegar gry
zegar = pygame.time.Clock()

# Tworzymy okno gry, gdzie wszystko będziemy wyświetlać
ekran = pygame.display.set_mode((SZEROKOSC, WYSOKOSC))
font = pygame.font.Font(None, 74)
font_small = pygame.font.Font(None, 40)  # Mały font do napisu "Życia"
# Ustawiamy tytuł okna
pygame.display.set_caption('Flappy Bird')

# Wybieramy kolory, rozmiar i położenie Flappiego
punkty = 0
zycia = 3  # Dodajemy zmienną do śledzenia żyć

flappy = Ptak()
rura = Rura(x = SZEROKOSC)
rura2 = Rura(x = SZEROKOSC +300)
kolizja = False
niesmiertelnosc  = False
nigger = False
# Główna pętla gry
gra_dziala = True

while gra_dziala:
    # -------- Sprawdzamy wydarzenia (np. kliknięcia) --------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gra_dziala = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not czekaj and not kolizja:
            flappy.skacz()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            czekaj = False

    # Sprawdzamy kolizje
    if czekaj:
        ekran.fill(CZARNY)
        flappy.rysuj(ekran)
    else:
        if (rura.sprawdz_kolizje(flappy) or flappy.Y >= WYSOKOSC - flappy.ROZMIAR) and not niesmiertelnosc:
            # Jeśli Flappy dotknie rury lub podłogi, straci życie
            if zycia <= 0:
                zycia = 0
            else:
                zycia -= 1

            if zycia <= 0:
                text_lose = font.render("Game Over", True, (255, 0, 0))
                ekran.blit(text_lose, (150, 250))
                kolizja = True
                for i in range(zycia, 3):
                    pygame.draw.rect(ekran, SZARY, (350 + font_small.size("Życia")[0] + 10 + i * 40, 40, 30, 30))
            else:
                niesmiertelnosc = True

        else:
            flappy.spadaj()
            rura.poruszanie()

            # Zwiększamy punkty, jeśli Flappy przeleciał przez rurę
            if flappy.X == rura.x + rura.SZEROKOSC:
                punkty += 69
                niesmiertelnosc = False

            # -------- Rysujemy na ekranie --------
            ekran.fill(CZARNY)

            # Rysujemy flappiego
            flappy.rysuj(ekran)

            # Rysujemy rurę
            rura.rysuj(ekran)
            rura2.rysuj(ekran)

            # Rysujemy punkty
            text_lose = font.render("punkty: " + str(punkty), True, (255, 255, 255))
            ekran.blit(text_lose, (0, 0))

            # Rysujemy napisy i życie
            text_lives = font_small.render("Życia:", True, (255, 255, 255))
            ekran.blit(text_lives, (350, 70))  # Napis "Życia" obok kwadratów

            # Rysujemy żyć w postaci czerwonych kwadratów
            for i in range(zycia):
                pygame.draw.rect(ekran, CZERWONY, (350 + font_small.size("Życia")[0] + 10 + i * 40, 40, 30, 30))  # Rysujemy czerwone kwadraty

            # Rysujemy szare kwadraty dla utraconych żyć
            for i in range(zycia, 3):
                pygame.draw.rect(ekran, SZARY, (350 + font_small.size("Życia")[0] + 10 + i * 40, 40, 30, 30))  # Rysujemy szare kwadraty

    # -------- Pokazujemy wszystko na ekranie --------
    pygame.display.update()
    zegar.tick(FPS)
