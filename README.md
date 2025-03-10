# Image Border Adder

A simple Python script to add borders to images with customizable thickness and color.

## Requirements

- Python 3.6+
- Pillow library

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/add-image-border.git
   cd add-image-border
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

Basic usage:
```
python add_border.py input_image.jpg
```

This will add a default 10-pixel black border to the image and save it as `input_image_border.jpg`.

### Options

- `-o, --output`: Specify the output image path (default: input filename with "_border" suffix)
- `-t, --thickness`: Border thickness in pixels (default: 10)
- `-c, --color`: Border color in RGB format "r,g,b" (default: "0,0,0" - black)

### Examples

Add a 20-pixel red border:
```
python add_border.py input_image.jpg -t 20 -c 255,0,0
```

Add a 15-pixel blue border and save to a specific location:
```
python add_border.py input_image.jpg -t 15 -c 0,0,255 -o output_with_border.jpg
```

## License

MIT 