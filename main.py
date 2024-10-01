from display import Display
import pygame
import sys

disp = Display()

def organizer(how_much, to_what):
    if not isinstance(to_what, str) or not isinstance(how_much, (int, float)):
        raise TypeError(
            "Argument 'to_what' must be a string, " +
            "and 'how_much' must be an integer or float."
        )

    data = {
        "ярди": 0.333333333,
        "дюйми": 12,
        "милі": 0.000189393939,
    }
    
    try:
        ret = how_much * data[to_what]
    except:
        raise ValueError("Unsupported convert" + to_what)
    
    return round(ret,5)

disp.print_display(str(organizer(12,"ярди")))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
