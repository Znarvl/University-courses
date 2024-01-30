import pygame
from pygame.math import Vector2
from physics import KINETIC_FRICTION
class Ball:
    def __init__(self, pos, mass, vx, vy, radius, screen, color):
        self.pos = Vector2(pos)
        self.mass = mass
        self.vx = vx
        self.vy = vy
        self.vel = Vector2(vx, vy)
        self.prev_vel = Vector2(0, 0)
        self.acc = Vector2(0, 0)
        self.screen = screen
        self.radius = radius
        self.color = color

    def draw(self):
        pygame.draw.circle(self.screen, self.color, self.pos, self.radius)


