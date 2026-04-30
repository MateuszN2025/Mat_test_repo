#!/usr/bin/env python3
"""Create a simple football icon for the application."""

from PIL import Image, ImageDraw

def create_football_icon():
    """Create a simple football icon and save as ICO."""
    # Create a new image with white background
    img = Image.new('RGB', (256, 256), color='white')
    draw = ImageDraw.Draw(img)
    
    # Draw a simple football (oval shape)
    # Football body - brown oval
    ball_color = (139, 69, 19)  # Brown
    draw.ellipse([40, 60, 216, 196], fill=ball_color, outline='black', width=2)
    
    # Football laces - white line in the middle
    laces_color = (255, 255, 255)  # White
    draw.line([60, 128, 196, 128], fill=laces_color, width=3)
    
    # Add small dashes on the laces
    for x in range(80, 190, 15):
        draw.line([x, 118, x, 138], fill=laces_color, width=2)
    
    # Add a small circle in the center (valve)
    draw.ellipse([120, 118, 136, 134], fill='black', outline='white', width=1)
    
    # Save as ICO
    img.save('football_icon.ico')
    print("Icon created: football_icon.ico")

if __name__ == "__main__":
    create_football_icon()
