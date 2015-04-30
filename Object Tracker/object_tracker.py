import pygame
import pygame.camera
from pygame.locals import *
import time

__author__ = 'Kyle'


class Capture(object):
    def __init__(self):
        pygame.init()
        pygame.camera.init()
        self.size = (640, 480)
        self.display = pygame.display.set_mode(self.size, 0)
        self.clist = pygame.camera.list_cameras()
        if not self.clist:
            raise ValueError("Sorry, no cameras detected.")
        self.cam = pygame.camera.Camera(self.clist[0], self.size, "HSV")
        self.cam.start()
        self.snapshot = pygame.surface.Surface(self.size, 0, self.display)

    def get_and_flip(self):
        if self.cam.query_image():
            self.snapshot = self.cam.get_image(self.snapshot)
        mask = pygame.mask.from_threshold(self.snapshot, self.ccolor, (30, 30, 30))
        self.display.blit(self.snapshot, (0, 0))
        connected = mask.connected_component()
        if mask.count() > 100:
            coord = mask.centroid()
            pygame.draw.circle(self.display, (255, 0, 0), coord, max(min(50, mask.count() / 400), 5))
        pygame.display.flip()

    def main(self):
        going = True
        self.calibrate()
        while going:
            events = pygame.event.get()
            print events
            for e in events:
                if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
                    self.cam.stop()
                    going = False
                    pygame.quit()
            if (going):
                self.get_and_flip()
            time.sleep(0.01)

    def calibrate(self):
        self.snapshot = self.cam.get_image(self.snapshot)
        self.display.blit(self.snapshot, (0, 0))
        crect = pygame.draw.rect(self.display, (255, 0, 0), (640 / 2, 480 / 2, 30, 30), 4)
        self.ccolor = pygame.transform.average_color(self.snapshot, crect)
        self.display.fill(self.ccolor, (0, 0, 50, 50))
        pygame.display.flip()
        self.thresholded = pygame.surface.Surface(self.size, 0, self.display)
        pygame.transform.threshold(self.thresholded, self.snapshot, self.ccolor, (30, 30, 30), (0, 0, 0), 2)


cap = Capture()
cap.main()
