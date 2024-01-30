import pygame
from ball import *
import physics
import math

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
VELOCITY = 15
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Vector2(x,y), weight, radius, screen, color
ball1 = Ball((300, 50), 30,0,0, 30, window, pygame.Color(255,0,0 ))
ball2 = Ball((200, 50), 30,0,0, 30, window, pygame.Color(0,35,255))

ball_list = []
ball_list.append(ball1)
ball_list.append(ball2)

pygame.init()


def main():

    counter = 0
    start_timer = False
    running = True
    no_click = True

    dt = 0.016
    clock = pygame.time.Clock()

    while running:
        ev = pygame.event.get()

        window.fill((50, 255, 25))
        physics.static_friction(ball_list)
        physics.collision(ball1, ball2)

        physics.calc_acc(ball_list, dt)
        physics.calc_velocity(ball_list, dt)
        physics.calc_position(ball_list, dt)

        ball1.pos[0], ball1.vx = physics.move(ball1.pos[0], ball1.vx, ball1.radius, SCREEN_WIDTH)
        ball1.pos[1], ball1.vy = physics.move(ball1.pos[1], ball1.vy, ball1.radius, SCREEN_HEIGHT)
        ball2.pos[0], ball2.vx = physics.move(ball2.pos[0], ball2.vx, ball2.radius, SCREEN_WIDTH)
        ball2.pos[1], ball2.vy = physics.move(ball2.pos[1], ball2.vy, ball2.radius, SCREEN_HEIGHT)








        if start_timer:
            no_click = False
            counter += 1
        if counter > 1:
            no_click = True
            start_timer =0
            counter =0
        # proceed events
        for event in ev:

            # finds mouse x,y coord to fire the ball in direction
            if event.type == pygame.MOUSEBUTTONUP and no_click:
                start_timer = True

                mouse_pos = pygame.mouse.get_pos()
                dx = mouse_pos[0] - ball1.pos[0]
                dy = mouse_pos[1] - ball1.pos[1]

                distance = math.sqrt(dx * dx + dy * dy)
                dx /= distance
                dy /= distance

                dx *= VELOCITY
                dy *= VELOCITY
                ball1.vx += dx
                ball1.vy += dy
            if event.type ==pygame.KEYDOWN:
                running = False


        physics.apply_kinetic_friction(ball_list)

        for ball in ball_list:
            ball.draw()
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

main()
