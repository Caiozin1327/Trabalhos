from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    gluOrtho2D(-100, 100, -100, 100)

def plot_point(x, y):

    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glVertex2f(-x, y)
    glVertex2f(x, -y)
    glVertex2f(-x, -y)
    glVertex2f(y, x)
    glVertex2f(-y, x)
    glVertex2f(y, -x)
    glVertex2f(-y, -x)
    glEnd()

def draw_circle_dda(radius):

    step = 1 / radius
    angle = 0

    while angle <= 2 * math.pi:
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        plot_point(round(x), round(y))
        angle += step
    glFlush()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.0, 0.0)
    draw_circle_dda(50)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Circunferencia com DDA")
    init()
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()
