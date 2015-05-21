import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *

def render():
    glClear(GL_COLOR_BUFFER_BIT); 
    glutSwapBuffers(); 
    return None

def mouse_event(button, state, x, y):
    return None

def close_event():
    return true

glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(1024, 1024)
glutInitWindowPosition(100, 100) 
glutCreateWindow("Styx3D Demo")
glutDisplayFunc(render)
glutMouseFunc(mouse_event)
#glutCloseFunc(close_event)


glClearColor(1.0, 0.0, 0.0, 1.0)


glutMainLoop();