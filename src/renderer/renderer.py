# src/renderer/renderer.py
import glfw
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader

class Renderer:
    def __init__(self, width=800, height=600):
        if not glfw.init():
            raise Exception("GLFW can not be initialized!")
        
        self.window = glfw.create_window(width, height, "3D Game Engine", None, None)
        if not self.window:
            glfw.terminate()
            raise Exception("GLFW window can not be created!")
        
        glfw.make_context_current(self.window)

    def start(self):
        while not glfw.window_should_close(self.window):
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            self.render()
            glfw.swap_buffers(self.window)
            glfw.poll_events()

    def render(self):
        # Example: draw something simple
        glBegin(GL_TRIANGLES)
        glVertex2f(-0.6, -0.4)
        glVertex2f(0.6, -0.4)
        glVertex2f(0.0, 0.6)
        glEnd()
