from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

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

def draw_circle_bresenham(radius):

    x = 0
    y = radius
    d = 3 - 2 * radius

    while x <= y:
        plot_point(x, y)
        if d <= 0:
            d = d + 4 * x + 6
        else:
            d = d + 4 * (x - y) + 10
            y -= 1
        x += 1
    glFlush()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.0, 0.0)
    draw_circle_bresenham(50)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Circunferencia de Bresenham")
    init()
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()