import pygame as pg
# from state import *
from utils import *
import numpy as np

class Panel:
    def __init__(self, pos, size):
        x, y = pos
        width, height = size
        self.panel = pg.Rect(x, y, width, height)

    def update(self, screen):
        # Draw outline
        pg.draw.rect(screen, WHITE, self.panel, 1)
        


class DashboardDisplay(Panel):
    def __init__(self, pos, size):
        super().__init__(pos, size)
        try:
    # Increased font size slightly for the text panel
            font = pg.font.SysFont(None, 32)
        except Exception as e:
            print(f"Could not load system font: {e}. Using default pg font.")
            font = pg.font.Font(None, 32)
        self.font = font

    def update(self, screen, alt, spd):
        super().update(screen)
        alt_text = f"Altitude: {alt:.4f}"
        spd_text = f"Speed: {spd:.4f}"
        alt_surf = self.font.render(alt_text, True, WHITE)
        spd_surf = self.font.render(spd_text, True, WHITE)
        # Position text inside the text panel
        screen.blit(alt_surf, (self.panel.left + PADDING, self.panel.top + PADDING))
        screen.blit(spd_surf, (self.panel.left + PADDING, self.panel.top + PADDING + 35))



class TrajectoryDisplay(Panel):
    def __init__(self, pos, size):
        margin=25
        super().__init__(pos, size)
        self.usable_area = pg.Rect(pos[0] + margin, pos[1] + margin, size[0]-2*margin, size[1]-2*margin)


    def __draw_axis(self, screen):
        pg.draw.line(screen, WHITE, self.usable_area.topleft, self.usable_area.bottomleft, 2)
        pg.draw.line(screen, WHITE, self.usable_area.bottomleft, self.usable_area.bottomright, 2)


    def __world2screen(self, coord):
        # transform
        # check in screen

        screen_pos = []
        for sim_point in coord:
            sim_x, sim_y = sim_point
            screen_x = self.usable_area.left + sim_x * 0.4
            screen_y = self.usable_area.bottom - sim_y * 0.4

            screen_pos.append((screen_x, screen_y))
        return screen_pos

    def update(self, screen, coord_hist):
        super().update(screen)
        # Draw Axes
        self.__draw_axis(screen)
        

        # Draw trajectory
        screen_traj_hist = self.__world2screen(coord_hist)
        # the line should be one continuous segment
        if len(screen_traj_hist) >= 2:
            pg.draw.lines(screen, WHITE, False, screen_traj_hist, 2)



    