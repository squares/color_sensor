import analogio
import board
import neopixel
import displayio
import terminalio
import time
from adafruit_display_text import label
from adafruit_gizmo import tft_gizmo
from adafruit_display_shapes.rect import Rect

# Create the TFT Gizmo display
display = tft_gizmo.TFT_Gizmo()

# Make the display context
splash = displayio.Group(max_size=10)
display.show(splash)

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=1.0)
light = analogio.AnalogIn(board.LIGHT)

rect = Rect(80, 20, 41, 41, fill=0xff0000)
splash.append(rect)


# Draw a label
# Set text, font, and color
text = "HELLO WORLD"
font = terminalio.FONT
color = 0x0000FF

# Create the text label
text_area = label.Label(font, text=text, color=color)

# Set the location
text_area.x = 100
text_area.y = 80
splash.append(text_area)

while True:

    #grab 5 values and then update display?

    pixels.fill((0, 0, 0))
    
    pixels[1] = (255, 0, 0)
    raw_red = light.value
    red = int(raw_red * (255 / 65535))
    
    pixels[1] = (0, 255, 0)
    raw_green = light.value
    green = int(raw_green * (255 / 65535))
    
    pixels[1] = (0, 0, 255)
    raw_blue = light.value
    blue = int(raw_blue * (255 / 65535))
    
    pixels.fill((0, 0, 0))
    
    print(red)
    
    # text_area.text = str(red)+ ":" + str(green) + ":" + str(blue)
    
    # rect.fill = hexColorString
 
