import analogio
import board
import neopixel
import displayio
import terminalio
import time
from adafruit_display_text import label
from adafruit_gizmo import tft_gizmo

# Create the TFT Gizmo display
display = tft_gizmo.TFT_Gizmo()

# Make the display context
splash = displayio.Group(max_size=10)
display.show(splash)

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=1.0)
light = analogio.AnalogIn(board.LIGHT)

color_bitmap = displayio.Bitmap(240, 240, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0x00FF00  # Bright Green

bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
splash.append(bg_sprite)

# Draw a smaller inner rectangle
inner_bitmap = displayio.Bitmap(200, 200, 1)
inner_palette = displayio.Palette(1)
inner_palette[0] = 0xAA0088  # Purple
inner_sprite = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette, x=20, y=20)
splash.append(inner_sprite)

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
display.show(text_area)



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

    time.sleep(1.5)

    # Printed to match the color lines on the Mu plotter!
    # The orange line represents red.
    # print((green, blue, red))

    colorString = str(red) + ":" + str(green) + ":" + str(blue)
    # text_area = label.Label(font, text=colorString, color=color)
    print(colorString)
    text_area = label.Label(font, text=colorString, color=color)
    # Set the location
    # text_area.x = 100
    # text_area.y = 80
    display.show(text_area)
