from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    gluOrtho2D(-10.0, 10.0, -10.0, 10.0)

def draw_house():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(-3, -5)
    glVertex2f(4, -5)
    glVertex2f(5, 3)
    glVertex2f(-4, 3)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glVertex2f(-4.5, 3)
    glVertex2f(0.5, 7)
    glVertex2f(5.5, 3)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glVertex2f(-1.5, -5)
    glVertex2f(1, -5)
    glVertex2f(1, -1)
    glVertex2f(-1.5, -1)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glVertex2f(2.5, 0)
    glVertex2f(4, 0)
    glVertex2f(4, 1.5)
    glVertex2f(2.5, 1.5)
    glEnd()

    glFlush()
def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Casa com OpenGL")
    init()
    glutDisplayFunc(draw_house)
    glutMainLoop()

if __name__ == "__main__":
    main()
