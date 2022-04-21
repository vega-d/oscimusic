import sys
import threading
import pygame
import os
from OpenGL.GL import *
from OpenGL.GLU import *
from scipy.io import wavfile

# selecting the file
try:
    filename = ""
    files = os.listdir(os.curdir)
    files = list(filter(lambda x: x[-4:] == ".wav", files))
    if len(files) == 1:
        filename = files[0]
        print("found", filename, "as the only .wav. Selecting that automatically.")
    else:
        print("Multiple .wav files were found, here's the list:")
        for i in range(len(files)):
            print(i, "=>", files[i])
        selected_number = int(input("Which one would you like to play? (enter the number): "))
        filename = files[selected_number]
    print("Playing", filename)
except Exception as e:
    print("Looks like file reading failed, please make sure you have a playable .wav file and you selected it correctly.")
    print("Possible reason why it might've failed:", e)
    exit(0)

# reading basic metadata of the file
samplerate, data = wavfile.read(filename)
print("number of channels =", data.shape[1])
print("type:", type(data))
print("samplerate is:", samplerate)

# configuration variables.
windowSize = width, height = 1300, 720
center = cw, ch = width // 2, height // 2
framebuffer_len = 5500
max_flow_x, max_flow_y = 10, 10
sim = 10
fps_ms = 10
skip = 2

# utility variables
counter = 0
points_to_draw = []
frames = 0
framebuffer = []
iskill = False


# utility functions
def draw_origin():
    line_length = 1
    # Draw x-axis line.
    glColor3f(1, 1, 1)

    glBegin(GL_LINES)
    glVertex3f(0, 0, 0)
    glVertex3f(line_length, 0, 0)
    glEnd()

    # Draw y-axis line.
    glColor3f(0, 1, 0)

    glBegin(GL_LINES)
    glVertex3f(0, 0, 0)
    glVertex3f(0, line_length, 0)
    glEnd()

    # Draw z-axis line.
    glColor3f(0, 0, 1)

    glBegin(GL_LINES)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 0, line_length)
    glEnd()


def coord_from_freq(data):
    left, right = data
    maxamp = 32768
    x = (left / maxamp * max_flow_x)
    y = (right / maxamp * max_flow_y)
    return [x, y]


def init_surface():
    pygame.init()
    screen = pygame.display.set_mode(windowSize, pygame.HWSURFACE | pygame.OPENGL | pygame.DOUBLEBUF)
    glViewport(0, 0, width, height)
    glShadeModel(GL_SMOOTH)
    glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)
    viewport = glGetIntegerv(GL_VIEWPORT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60.0, float(viewport[2]) / float(viewport[3]), 0.1, 1000.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glClearColor(0.1, 0.1, 0.1, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(15, 0, 0, 0, 0, 0, 0, 0, 1)
    print("opengl surface initialized")
    return screen


# rendering thread
class Renderer(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.data = data
        self.counter = 0

    def run(self):
        print("running thread", self.name)
        init_surface()
        while True:
            global iskill
            if iskill:
                exit(0)
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glColor3f(1, 1, 1)
            glBegin(GL_LINES)
            for point in framebuffer:
                glVertex3f(0, point[0], point[1])
            glEnd()
            pygame.display.flip()
            pygame.time.wait(fps_ms)


# starting the rendering thread
thread_renderer = Renderer(1, "renderer")
thread_renderer.start()

# main thread
while True:
    try:
        framebuffer = []
        for i in range(0, framebuffer_len, skip):
            coord = coord_from_freq(data[frames + i])
            framebuffer.append(coord)
        frames += framebuffer_len
        if frames > len(data):
            frames = 0
        pygame.time.wait(sim)
    except KeyboardInterrupt:
        print("Exiting...")
        iskill = True
        thread_renderer.join()
        sys.exit()