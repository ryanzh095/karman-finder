import sys
from display import *


PANEL_WIDTH = SCREEN_WIDTH - 2 * PADDING
PANEL_TOTAL_HEIGHT = SCREEN_HEIGHT - 2 * PADDING
TEXT_PANEL_HEIGHT = int(PANEL_TOTAL_HEIGHT * 0.25)
TRAJECTORY_PANEL_HEIGHT = PANEL_TOTAL_HEIGHT - TEXT_PANEL_HEIGHT - PADDING


# pg Setup
pg.init()
screen = pg.display.set_mode(SCREEN_SIZE)
pg.display.set_caption("Rocket Control Panel (Sketch Layout)")
clock = pg.time.Clock()



# --- Game Variables ---
altitude = 0.0
speed = 0.0
rocket_angle = 0
fuel_percentage = 1.0
rocket_sim_pos = (0.0, 0.0)
trajectory_points_sim = []


text_panel = DashboardDisplay((PADDING, PADDING), (PANEL_WIDTH, TEXT_PANEL_HEIGHT))
trajectory_panel = TrajectoryDisplay((PADDING, text_panel.panel.bottom + PADDING), (PANEL_WIDTH, TRAJECTORY_PANEL_HEIGHT))


# --- Main Game Loop ---
running = True
while running:
    # --- Event Handling ---
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # --- Game Logic / State Updates (TOY INPUT) ---
    altitude += 0.1
    speed += 0.5

    dx = 0.5
    dy = 0.2
    rocket_sim_pos = (rocket_sim_pos[0] + dx, rocket_sim_pos[1] + dy)

    trajectory_points_sim.append(rocket_sim_pos)
    # --- Drawing ---
    screen.fill(BLACK)
    text_panel.update(screen, altitude, speed)
    trajectory_panel.update(screen, trajectory_points_sim)

    pg.display.flip()

    # --- Frame Rate Control ---
    clock.tick(FPS)

# --- Quit pg ---
print("Exiting simulator...")
pg.quit()
sys.exit() 