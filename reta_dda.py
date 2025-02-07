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

def draw_line_dda(x1, y1, x2, y2):

    dx = x2 - x1
    dy = y2 - y1
    steps = int(max(abs(dx), abs(dy)))
    x_increment = dx / steps
    y_increment = dy / steps

    x = x1
    y = y1
    for _ in range(steps + 1):
        plot_point(round(x), round(y))
        x += x_increment
        y += y_increment
    glFlush()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.0, 0.0)
    draw_line_dda(-50, -50, 50, 50)  

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Reta DDA")
    init()
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()
