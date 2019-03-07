# Carlos Calderon, 15219
# SR2 Lines
# Program that create a lines with bresenham algorithm

from SR1 import SoftwareRender

x = SoftwareRender('out.bmp')

x.glCreateWindow(600, 600)
x.glViewPort(0, 0, 599, 599)
x.glClear()
x.glColor(1, 0, 0)
x.glVertex(0, 0)
x.line_brese(0, -1, 1, 1)
x.glFinish()
