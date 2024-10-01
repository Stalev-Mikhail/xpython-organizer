# Conversion Tool 🇺🇦

Welcome to the Conversion Tool, a simple yet powerful converter that translates between different units like yards, inches, and miles! 

## 🌟 Features
- **Unit Conversion**: Convert units from inches to yards and miles effortlessly.
- **User-Friendly Interface**: Easy to read results displayed prominently on the screen.
- **Endless Loop**: The program runs continually until manually exited.

## 🎨 Color Theme
This project honors the beautiful colors of the Ukrainian flag with a vibrant display:
- **Blue** for tranquility and peace.
- **Yellow** for prosperity and warmth.

## 🚀 Getting Started

### Prerequisites
Make sure you have Python and Pygame installed on your system.
```bash
pip install pygame
Usage
To run the converter, simply execute the main.py script:

 
python main.py
After that, you can enter values to convert from inches to yards or miles.

📁 Project Structure
 
├── main.py
└── display.py
main.py
This is the main script which handles all the conversion logic.

 
from display import Display
import pygame
import sys

disp = Display()

def organizer(how_much, to_what):
    if not isinstance(to_what, str) or not isinstance(how_much, (int, float)):
        raise TypeError("Argument 'to_what' must be a string, and 'how_much' must be an integer or float.")

    data = {
        "ярди": 0.333333333,
        "дюйми": 12,
        "милі": 0.000189393939,
    }

    try:
        ret = how_much * data[to_what]
    except KeyError:
        raise ValueError("Unsupported convert: " + to_what)

    return round(ret, 5)

disp.print_display(str(organizer(12, "ярди")))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
display.py
This file handles displaying the conversion results using Pygame.

 
import pygame
import sys

class Display():
    def __init__(self):
        pygame.init()
        self.font = pygame.font.SysFont('couriernew', 40)
        self.screen = pygame.display.set_mode((700, 700))
        pygame.display.set_caption("Конвертер футів")
        self.screen.fill((255, 255, 255))

    def print_display(self, text):
        text = self.font.render("Результат: " + text, True, (0, 255, 0))
        self.screen.blit(text, (50, 50))
        pygame.display.update()
💡 Note
This converter is designed to be easily expandable. Feel free to add more units and conversion logic as needed!

🙌 Contributions
Contributions are welcome! If you have suggestions or improvements, please feel free to submit a pull request.

📜 License
This project is licensed under the MIT License - see the
LICENSE
file for details.

Thank you for checking out the Conversion Tool! Enjoy converting your measurements! 🇺🇦

 