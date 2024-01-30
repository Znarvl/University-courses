import math
from pygame.math import Vector2



#Friction source https://billiards.colostate.edu/faq/physics/physical-properties/
STATIC_FRICTION = 0.5
KINETIC_FRICTION = 0.985  # ball to cloth friction
BALL_TO_BALL_FRICTION = 0.995
BALL_TO_RAIL_RESTITUTION = 0.93


def calc_velocity(ball_list, dt):
    for ball in ball_list:
        vel = ball.vel = (ball.acc * dt)
        ball.vel = vel
        return ball.vel


def calc_position(ball_list, dt):
    for ball in ball_list:
        ball.pos = ball.pos + (ball.acc * dt)
    return ball.pos


def calc_acc(ball_list, dt):
    for ball in ball_list:
        ball.acc = (ball.vel - ball.prev_vel) / dt
        ball.prev_vel = ball.vel

    return ball.acc


def collision(ball1, ball2):
    """
    Checks if two balls collide, and if so it calculates
    new velocity for the balls with the use of impuls formula.
    It also calculate the new direction for the balls.
    """
    dx = ball2.pos[0] - ball1.pos[0]
    dy = ball2.pos[1] - ball1.pos[1]
    distance = math.sqrt(dx * dx + dy * dy)

    if (distance < ball1.radius + ball2.radius):
        angle = math.atan2(dy, dx)
        sin = math.sin(angle)
        cos = math.cos(angle)

        x1 = 0
        y1 = 0
        x2 = dx * cos + dy * sin
        y2 = dy * cos - dx * sin

        # rotate velocity
        vx1 = ball1.vx * cos + ball1.vy * sin
        vy1 = ball1.vy * cos - ball1.vx * sin
        vx2 = ball2.vx * cos + ball2.vy * sin
        vy2 = ball2.vy * cos - ball2.vx * sin

        # Impuls formula:
        # m1_before * v1_before + m2_before * v2_before = m1_after * v1_after + m2_after * v2_after
        vx1final = ((ball1.mass - ball2.mass) * vx1 + 2 * ball2.mass * vx2) / (ball1.mass + ball2.mass)
        vx2final = ((ball2.mass - ball1.mass) * vx2 + 2 * ball1.mass * vx1) / (ball1.mass + ball2.mass)

        vx1 = vx1final * BALL_TO_BALL_FRICTION
        vx2 = vx2final * BALL_TO_BALL_FRICTION

        # solution to overlap glitch
        # If ball overlap push out the ball of the other via knowing the overlap by radius and make both the balls reduce the overlap by half
        absVelocity = abs(vx1) + abs(vx2)
        overlap = (ball1.radius + ball2.radius) - distance
        x1 += (vx1 / absVelocity) * overlap
        x2 += (vx2 / absVelocity) * overlap

        # rotate relative position back
        x1final = x1 * cos - y1 * sin
        y1final = y1 * cos + x1 * sin
        x2final = x2 * cos - y2 * sin
        y2final = y2 * cos + x2 * sin

        ball2.pos[0] = ball1.pos[0] + x2final
        ball2.pos[1] = ball1.pos[1] + y2final

        ball1.pos[0] = ball1.pos[0] + x1final
        ball1.pos[1] = ball1.pos[1] + y1final

        # rotate velocity back
        ball1.vx = vx1 * cos - vy1 * sin
        ball1.vy = vy1 * cos + vx1 * sin
        ball2.vx = vy2 * cos - vx2 * sin
        ball2.vy = vy2 * cos + vx2 * sin

def static_friction(ball_list):
    for ball in ball_list:
        #Fmax = mu static * FN
        fmax = STATIC_FRICTION * (ball.mass * 0.00981)
        force = abs(math.sqrt((ball.vx * ball.vx) + (ball.vy * ball.vy)))
        if  force  <= fmax:
            ball.dx = 0
            ball.dy = 0
'''
Taken from https://stackoverflow.com/questions/63145493/pygame-how-to-let-balls-collide
To get the bounce between walls and movement
'''

def move(c, v, r, m):
    c += v
    if c < r:
        c, v = r, -v * BALL_TO_RAIL_RESTITUTION
    if c > m-r:
        c, v = m-r, -v * BALL_TO_RAIL_RESTITUTION
    return c, v


def apply_kinetic_friction(ball_list):
    for ball in ball_list:
        ball.vx *= KINETIC_FRICTION
        ball.vy *= KINETIC_FRICTION
