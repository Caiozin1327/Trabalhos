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
    glEnd()

def draw_line_analytic(x1, y1, x2, y2):


    if x2 - x1 != 0:  # Evitar divisão por zero
        m = (y2 - y1) / (x2 - x1)
        b = y1 - m * x1

        x = x1
        while x <= x2:
            y = m * x + b
            plot_point(round(x), round(y))
            x += 1
    else:

        y = min(y1, y2)
        while y <= max(y1, y2):
            plot_point(x1, y)
            y += 1
    glFlush()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.0, 0.0)
    draw_line_analytic(-50, -50, 50, 50)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Reta Analitica")
    init()
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()
