from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    gluOrtho2D(-10.0, 10.0, -10.0, 10.0)

def draw_circle():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.0, 0.0)

    radius = 5
    num_segments = 100

    glBegin(GL_LINE_LOOP)
    for i in range(num_segments):
        theta = 2.0 * math.pi * i / num_segments
        x = radius * math.cos(theta)
        y = radius * math.sin(theta)
        glVertex2f(x, y)
    glEnd()

    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Circunferencia com OpenGL")
    init()
    glutDisplayFunc(draw_circle)
    glutMainLoop()

if __name__ == "__main__":
    main()