#!/usr/bin/env python3

import argparse
from PIL import Image, ImageOps, ImageColor
import os
import re

def add_border(input_image_path, output_image_path, border_thickness, border_color):
    """
    Add a border to an image.
    
    Args:
        input_image_path (str): Path to the input image
        output_image_path (str): Path to save the output image
        border_thickness (int): Border thickness in pixels
        border_color (tuple): RGB color tuple for the border
    """
    try:
        # Open the image
        img = Image.open(input_image_path)
        
        # Add border
        img_with_border = ImageOps.expand(img, border=border_thickness, fill=border_color)
        
        # Save the result
        img_with_border.save(output_image_path)
        
        print(f"Border added successfully. Image saved to {output_image_path}")
        
    except Exception as e:
        print(f"Error: {e}")

def parse_color(color_str):
    """
    Parse color string in multiple formats to RGB tuple.
    
    Supported formats:
    - RGB format: 'r,g,b' (e.g., '255,0,0')
    - Hex format: '#RRGGBB' or 'RRGGBB' (e.g., '#FF0000' or 'FF0000')
    - Color name: 'red', 'blue', etc. (standard HTML color names)
    
    Args:
        color_str (str): Color string in one of the supported formats
        
    Returns:
        tuple: RGB color tuple
    """
    # Check if it's RGB format (r,g,b)
    rgb_pattern = re.compile(r'^(\d+),(\d+),(\d+)$')
    rgb_match = rgb_pattern.match(color_str)
    
    if rgb_match:
        try:
            r, g, b = map(int, rgb_match.groups())
            # Validate RGB values
            if not all(0 <= c <= 255 for c in (r, g, b)):
                raise ValueError("RGB values must be between 0 and 255")
            return (r, g, b)
        except ValueError as e:
            raise argparse.ArgumentTypeError(f"Invalid RGB format. Use 'r,g,b' with values 0-255: {e}")
    
    # Check if it's a hex color code
    hex_pattern = re.compile(r'^#?([0-9A-Fa-f]{6})$')
    hex_match = hex_pattern.match(color_str)
    
    if hex_match:
        try:
            hex_value = hex_match.group(1)
            r = int(hex_value[0:2], 16)
            g = int(hex_value[2:4], 16)
            b = int(hex_value[4:6], 16)
            return (r, g, b)
        except ValueError as e:
            raise argparse.ArgumentTypeError(f"Invalid hex color format: {e}")
    
    # Check if it's a color name
    try:
        # ImageColor.getrgb handles standard color names like 'red', 'blue', etc.
        rgb = ImageColor.getrgb(color_str)
        return rgb
    except ValueError:
        pass
    
    # If we get here, the color format is invalid
    raise argparse.ArgumentTypeError(
        "Invalid color format. Use one of the following formats:\n"
        "- RGB: '255,0,0' for red\n"
        "- Hex: '#FF0000' or 'FF0000' for red\n"
        "- Name: 'red', 'blue', etc. (standard HTML color names)"
    )

def main():
    parser = argparse.ArgumentParser(description='Add border to an image')
    parser.add_argument('input_image', help='Path to the input image')
    parser.add_argument('-o', '--output', help='Path to save the output image. If not specified, adds "_border" suffix to the input filename')
    parser.add_argument('-t', '--thickness', type=int, default=10, help='Border thickness in pixels (default: 10)')
    parser.add_argument('-c', '--color', type=parse_color, default=(0, 0, 0), 
                        help='Border color in one of these formats: RGB "255,0,0", Hex "#FF0000", or name "red" (default: black)')
    
    args = parser.parse_args()
    
    # If output path is not specified, create one based on the input path
    if not args.output:
        input_name, input_ext = os.path.splitext(args.input_image)
        args.output = f"{input_name}_border{input_ext}"
    
    add_border(args.input_image, args.output, args.thickness, args.color)

if __name__ == "__main__":
    main() 