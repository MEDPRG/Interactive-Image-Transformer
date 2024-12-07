import cv2
import numpy as np
import math

# Global variables for transformation parameters
# These will be adjusted interactively with the keyboard
angle = 0.81
tx, ty = 200, 150
sx, sy = 0.5, 0.5
skew_factor = 0.2
persp1, persp2 = 0.0001, 0.002


def create_transformation(angle, tx, ty, sx, sy, skew_factor, persp1, persp2):
    # Rotation matrix
    R = np.eye(3, dtype=np.float32)
    R[0, 0] = math.cos(angle)
    R[0, 1] = -math.sin(angle)
    R[1, 0] = math.sin(angle)
    R[1, 1] = math.cos(angle)

    # Translation matrix
    t = np.eye(3, dtype=np.float32)
    t[0, 2] = tx
    t[1, 2] = ty

    # Scaling matrix
    Scale = np.eye(3, dtype=np.float32)
    Scale[0, 0] = sx
    Scale[1, 1] = sy

    # Skewing matrix
    Skew = np.eye(3, dtype=np.float32)
    Skew[0, 1] = skew_factor

    # Multiply matrices to combine all transformations
    T = t @ R @ Skew @ Scale

    # Perspective transformation
    T[2, 0] = persp1
    T[2, 1] = persp2

    return T


def apply_transformation(img, T, is_perspective):
    HEIGHT, WIDTH = img.shape[:2]
    new_img = np.zeros_like(img)  # Create a blank image of the same size as the input

    # Compute the inverse of the transformation matrix
    T_inv = np.linalg.inv(T)

    for i in range(HEIGHT):
        for j in range(WIDTH):
            # Create a pixel (homogeneous coordinates) in the output image
            p = np.array([[j], [i], [1]], dtype=np.float32)

            # Apply the inverse transformation to find the corresponding point in the original image
            original_p = T_inv @ p
            original_z = original_p[2, 0]

            # perspective transformations and applying homogeneous division
            if is_perspective:
                original_x = int(original_p[0, 0] / original_z)
                original_y = int(original_p[1, 0] / original_z)
            else:
                original_x = int(original_p[0, 0])
                original_y = int(original_p[1, 0])

            # Only copy the pixel if the original position is within image bounds
            if 0 <= original_x < WIDTH and 0 <= original_y < HEIGHT:
                new_img[i, j] = img[original_y, original_x]

    return new_img


def update_image(img):
    # Create the transformation matrix
    T = create_transformation(angle, tx, ty, sx, sy, skew_factor, persp1, persp2)

    # Apply the transformation and update the display
    new_img = apply_transformation(img, T, True)
    cv2.imshow("Transformations", new_img)


def main():
    global angle, tx, ty, sx, sy, skew_factor, persp1, persp2

    # Load the image from disk
    img = cv2.imread("istockphoto.jpg")  # change the path if something goes wrong in the reading of the image.

    # Handle case if image is not found
    if img is None:
        print("Couldn't read image!")
        return

    # Resize the image for faster performance
    img = cv2.resize(img, (300, 300))

    # Initial transformation and display
    update_image(img)

    update_needed = False  # indicate whether an update is needed

    while True:
        key = cv2.waitKey(0)

        # Adjust transformation
        if key == ord('r'):  # Negative rotation angle
            angle += 0.05
            update_needed = True
        elif key == ord('R'):  # Positive rotation angle
            angle -= 0.05
            update_needed = True

        # Adjust translation
        elif key == ord('w'):  # Move up
            ty -= 10
            update_needed = True
        elif key == ord('s'):  # Move down
            ty += 10
            update_needed = True
        elif key == ord('a'):  # Move left
            tx -= 10
            update_needed = True
        elif key == ord('d'):  # Move right
            tx += 10
            update_needed = True

        # Adjust scaling
        elif key == ord('z'):  # Increase scale zoom in
            sx += 0.1
            sy += 0.1
            update_needed = True
        elif key == ord('x'):  # Decrease scale zoom out
            sx = max(0.1, sx - 0.1)
            sy = max(0.1, sy - 0.1)
            update_needed = True

        # Adjust skew factor
        elif key == ord('k'):  # Increase skew factor
            skew_factor += 0.1
            update_needed = True
        elif key == ord('l'):  # Decrease skew factor
            skew_factor -= 0.1
            update_needed = True

        # Update and redraw the transformed image only if a change was made
        if update_needed:
            update_image(img)
            update_needed = False

        if key == ord('q'):
            break

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
