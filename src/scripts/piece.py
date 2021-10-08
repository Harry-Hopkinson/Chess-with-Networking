import pygame
import os

b_bishop = pygame.image.load(os.path.join("media", "black_bishop.png"))
b_king = pygame.image.load(os.path.join("media", "black_king.png"))
b_knight = pygame.image.load(os.path.join("media", "black_knight.png"))
b_pawn = pygame.image.load(os.path.join("media", "black_pawn.png"))
b_queen = pygame.image.load(os.path.join("media", "black_queen.png"))
b_rook = pygame.image.load(os.path.join("media", "black_rook.png"))

w_bishop = pygame.image.load(os.path.join("media", "white_bishop.png"))
w_king = pygame.image.load(os.path.join("media", "white_king.png"))
w_knight = pygame.image.load(os.path.join("media", "white_knight.png"))
w_pawn = pygame.image.load(os.path.join("media", "white_pawn.png"))
w_queen = pygame.image.load(os.path.join("img", "white_queen.png"))
w_rook = pygame.image.load(os.path.join("media", "white_rook.png"))

b = [b_bishop, b_king, b_knight, b_pawn, b_queen, b_rook]
w = [w_bishop, w_king, w_knight, w_pawn, w_queen, w_rook]

B = []
W = []

for img in b:
    B.append(pygame.transform.scale(img, (55, 55)))

for img in w:
    W.append(pygame.transform.scale(img, (55, 55)))


class Piece:
    img = -1
    rect = (113, 113, 525, 525)
    startX = rect[0]
    startY = rect[1]

    def __init__(self) -> None:
        pass