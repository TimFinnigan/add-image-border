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
- `-c, --color`: Border color in one of these formats:
  - RGB format: `255,0,0` (red)
  - Hex format: `#FF0000` or `FF0000` (red)
  - Color name: `red`, `blue`, etc. (standard HTML color names)

### Examples

Add a 20-pixel red border using RGB format:
```
python add_border.py input_image.jpg -t 20 -c 255,0,0
```

Add a 15-pixel blue border using hex format:
```
python add_border.py input_image.jpg -t 15 -c "#0000FF"
```

Add a 25-pixel green border using color name:
```
python add_border.py input_image.jpg -t 25 -c green
```

Save to a specific location:
```
python add_border.py input_image.jpg -t 15 -c blue -o output_with_border.jpg
```

## License

MIT 