#!/usr/bin/env python3

import argparse
from PIL import Image, ImageOps
import os

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
    Parse color string in format 'r,g,b' to RGB tuple.
    
    Args:
        color_str (str): Color string in format 'r,g,b'
        
    Returns:
        tuple: RGB color tuple
    """
    try:
        r, g, b = map(int, color_str.split(','))
        # Validate RGB values
        if not all(0 <= c <= 255 for c in (r, g, b)):
            raise ValueError("RGB values must be between 0 and 255")
        return (r, g, b)
    except ValueError as e:
        raise argparse.ArgumentTypeError(f"Invalid color format. Use 'r,g,b' with values 0-255: {e}")

def main():
    parser = argparse.ArgumentParser(description='Add border to an image')
    parser.add_argument('input_image', help='Path to the input image')
    parser.add_argument('-o', '--output', help='Path to save the output image. If not specified, adds "_border" suffix to the input filename')
    parser.add_argument('-t', '--thickness', type=int, default=10, help='Border thickness in pixels (default: 10)')
    parser.add_argument('-c', '--color', type=parse_color, default=(0, 0, 0), help='Border color in RGB format "r,g,b" (default: "0,0,0" - black)')
    
    args = parser.parse_args()
    
    # If output path is not specified, create one based on the input path
    if not args.output:
        input_name, input_ext = os.path.splitext(args.input_image)
        args.output = f"{input_name}_border{input_ext}"
    
    add_border(args.input_image, args.output, args.thickness, args.color)

if __name__ == "__main__":
    main() 