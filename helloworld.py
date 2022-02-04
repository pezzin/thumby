# HelloWorld
# Written by Christian Pezzin
# Last edited 04 feb 2022

'''
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

import time
import thumby
import math

# BITMAP: width: 32, height: 32
bitmap0 = [255,255,255,255,255,255,255,255,255,255,63,135,243,251,9,173,141,29,249,155,27,91,91,243,231,159,63,255,255,255,255,255,
           255,255,255,255,255,255,255,255,255,255,248,11,227,251,250,154,146,247,150,150,246,246,246,7,231,239,224,255,255,255,255,255,
           255,255,255,255,255,255,255,255,255,247,231,238,220,211,7,228,245,245,245,229,19,187,188,222,239,247,255,255,255,255,255,255,
           255,255,255,255,255,255,255,255,255,255,255,207,231,243,251,252,252,252,252,248,242,231,207,159,255,255,255,255,255,255,255,255]
           
# Make a sprite object using bytearray (a path to binary file from 'IMPORT SPRITE' is also valid)
thumbySprite = thumby.Sprite(32, 32, bitmap0)

# Set the FPS (without this call, the default fps is 30)
thumby.display.setFPS(60)

while(1):
    t0 = time.ticks_ms()   # Get the current time in milliseconds
    thumby.display.fill(0) # Fill canvas to black to make it 'blank'
    bobRate = 250 # How fast the animation is (higher is slower, arbitrary)
    bobRange = 5  # The range in pixels of the bob (how far it moves up/down, -5px to 5px)

    # Calculate number of pixels to offset sprite for bob animation
    bobOffset = math.sin(t0 / bobRate) * bobRange

    # Center the sprite using screen and bitmap dimensions and apply bob offset
    thumbySprite.x = int((thumby.display.width/2) - (32/2))
    thumbySprite.y = int(round((thumby.display.height/2) - (32/2) + bobOffset))

    # Display the bitmap using bitmap data, position, and bitmap dimensions
    thumby.display.drawSprite(thumbySprite)
    thumby.display.update()
