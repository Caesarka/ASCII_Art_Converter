from PIL import Image
import numpy as np


def covert_image_to_ASCII(file_name, cols, scale, more_levels):

    gscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
    gscale2 = "@%#*+=-:. "

    image = Image.open(file_name).convert('L')
    W, H = image.size
    print(f"Input image dimentions: {W} x {H}")

    w = W / cols
    h = w / scale
    rows = int(H / h)

    print(f"cols: {cols}, rows: {rows}")
    print(f"tile's dimentions: {w} x {h}")

    if cols > W or rows > H:
        print("Image too small for specified cols!")
        exit(0)
    print(f"More levels?: {more_levels}")

    ascii_img = []
    for row in range(rows):
        y1 = int(row * h)
        y2 = int((row + 1) * h)

        if row == rows - 1:
            y2 = H

        ascii_img.append('')

        for col in range(cols):

            x1 = int(col * w)
            x2 = int((col + 1) * w)

            if col == cols - 1:
                x2 = W

            img = image.crop((x1, y1, x2, y2))
            avg = int(get_average_grayscale_value(img))

            if more_levels:
                gsval = gscale1[int((avg * (len(gscale1) - 1)) / 255)]
            else:
                gsval = gscale2[int((avg * (len(gscale2) - 1)) / 255)]
            ascii_img[row] += gsval

    for _ in ascii_img:
        print(_)

    return ascii_img


def get_average_grayscale_value(image):

    im = np.array(image)
    w, h = im.shape

    return np.average(im.reshape(w * h))
