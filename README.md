
# Interactive Image Transformation with Python and OpenCV

This repository contains a Python script for interactively applying various geometric transformations to an image using keyboard controls. The script supports rotation, translation, scaling, skewing, and perspective transformations.

## Features

- **Interactive Transformations**:
  - Rotate, translate, scale, skew, and apply perspective transformations to an image using keyboard inputs.

- **Customizable Parameters**:
  - Adjust transformation parameters such as rotation angle, translation offsets, scaling factors, skew factor, and perspective distortion.

- **Real-Time Visualization**:
  - View the transformed image in real-time as you adjust parameters.

## Requirements

To run the script, ensure you have the following dependencies installed:

- Python 3.x
- OpenCV (`cv2`)
- NumPy

Install the required packages using pip:

```bash
pip install opencv-python numpy
```

## Usage

1. **Prepare Your Image**:
   - Replace `bottle.jpg` in the script with the path to your input image.

2. **Run the Script**:
   - Execute the script to start the interactive transformation process:
     ```bash
     python transformation_script.py
     ```

3. **Control the Transformations**:
   - Use the following keyboard controls to adjust the transformations:

     | Key        | Action                               |
     |------------|--------------------------------------|
     | `r`        | Rotate counterclockwise             |
     | `R`        | Rotate clockwise                    |
     | `w`        | Move up                             |
     | `s`        | Move down                           |
     | `a`        | Move left                           |
     | `d`        | Move right                          |
     | `z`        | Zoom in (increase scale)            |
     | `x`        | Zoom out (decrease scale)           |
     | `k`        | Increase skew factor                |
     | `l`        | Decrease skew factor                |
     | `q`        | Quit the application                |

4. **View Results**:
   - The script displays the transformed image in a window. Adjust parameters interactively and see the changes in real-time.

## Input Data

The script processes a single image, which should be in a supported format (e.g., JPEG or PNG).

## Output

The output is displayed in a window, showing the transformed version of the input image. Transformations are applied in the following order: **Translation → Rotation → Skewing → Scaling → Perspective**.

## Example

Here’s an example of how to use the script:

1. **Original Image**:
   - ![istockphoto](https://github.com/user-attachments/assets/78dda76e-da0c-4a4b-b5e3-6245977025cf)

2. **Transformed Image**:
   - Interact with the keyboard to modify the image in real-time. View transformations like rotation, scaling, or skewing directly.
   - ![image](https://github.com/user-attachments/assets/f6b214a8-b6bf-4687-b154-b7586dc0765d)

---

## Author

**MEDPRG**  
[GitHub Profile](https://github.com/MEDPRG)
