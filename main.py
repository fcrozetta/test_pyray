from pyray import *
from raylib import (
    FLAG_BORDERLESS_WINDOWED_MODE,
    FLAG_FULLSCREEN_MODE,
    FLAG_WINDOW_MAXIMIZED,
    FLAG_WINDOW_RESIZABLE,
    FLAG_WINDOW_TRANSPARENT,
    KEY_F,
    KEY_SPACE,
)

MAX_COLORS_COUNT = 21

original_screen_width = 800
original_screen_height = 600
screen_width = 800
screen_height = 600
set_config_flags(FLAG_WINDOW_RESIZABLE)
init_window(screen_width, screen_height, "raylib [shapes] example - colors palette")
colors = [
    DARKGRAY,
    MAROON,
    ORANGE,
    DARKGREEN,
    DARKBLUE,
    DARKPURPLE,
    DARKBROWN,
    GRAY,
    RED,
    GOLD,
    LIME,
    BLUE,
    VIOLET,
    BROWN,
    LIGHTGRAY,
    PINK,
    YELLOW,
    GREEN,
    SKYBLUE,
    PURPLE,
    BEIGE,
]

color_names = [
    "DARKGRAY",
    "MAROON",
    "ORANGE",
    "DARKGREEN",
    "DARKBLUE",
    "DARKPURPLE",
    "DARKBROWN",
    "GRAY",
    "RED",
    "GOLD",
    "LIME",
    "BLUE",
    "VIOLET",
    "BROWN",
    "LIGHTGRAY",
    "PINK",
    "YELLOW",
    "GREEN",
    "SKYBLUE",
    "PURPLE",
    "BEIGE",
]


# create  empty rectsangles
color_rects: list[Rectangle] = [Rectangle(0, 0, 0, 0) for _ in range(MAX_COLORS_COUNT)]
# if not is_window_fullscreen():
#     toggle_fullscreen()
# Fills colorsRecs data (for every rectangle)
for i, rect in enumerate(color_rects):
    rect.width = 100
    rect.height = 100
    rect.x = 20.0 + 100.0 * (i % 7) + 10.0 * (i % 7)
    rect.y = 80.0 + 100.0 * (i // 7) + 10.0 * (i // 7)

color_state: list[int] = [
    0 for _ in range(MAX_COLORS_COUNT)
]  # Color state: 0-DEFAULT, 1-MOUSE_HOVER
mousePoint: Vector2 = Vector2(0.0, 0.0)

set_target_fps(60)  # Set our game to run at 60 frames-per-second

while not window_should_close():  # Detect window close button or ESC key
    if is_key_pressed(KEY_F):
        print(f"{is_window_fullscreen()=}\n{screen_height=}\n{screen_width=}")
        if is_window_fullscreen():
            screen_width = original_screen_width
            screen_height = original_screen_height
        else:
            screen_height = get_screen_height()
            screen_width = get_screen_width()
        toggle_fullscreen()
    mousePoint = get_mouse_position()
    for i in range(MAX_COLORS_COUNT):
        if check_collision_point_rec(mousePoint, color_rects[i]):
            color_state[i] = 1
        else:
            color_state[i] = 0
    begin_drawing()
    clear_background(RAYWHITE)
    draw_text("raylib colors palette", 28, 42, 20, BLACK)
    draw_text(
        "press SPACE to see all colors",
        get_screen_width() - 180,
        get_screen_height() - 40,
        10,
        GRAY,
    )

    for i in range(MAX_COLORS_COUNT):
        draw_rectangle_rec(
            color_rects[i], fade(colors[i], 0.6 if color_state[i] else 1.0)
        )

        if is_key_down(KEY_SPACE) or color_state[i]:
            draw_rectangle(
                int(color_rects[i].x),
                int(color_rects[i].y + color_rects[i].height - 26),
                int(color_rects[i].width),
                20,
                BLACK,
            )
            draw_rectangle_lines_ex(color_rects[i], 6, fade(BLACK, 0.3))
            draw_text(
                color_names[i],
                int(
                    color_rects[i].x
                    + color_rects[i].width
                    - measure_text(color_names[i], 10)
                    - 12
                ),
                int(color_rects[i].y + color_rects[i].height - 20),
                10,
                colors[i],
            )
    end_drawing()
