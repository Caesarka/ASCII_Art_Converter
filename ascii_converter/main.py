import argparse
from ascii_converter.converter import covert_image_to_ASCII


def main():

    descStr = "This program converts an image into ASCII art."
    parser = argparse.ArgumentParser(description=descStr)

    parser.add_argument('--file', dest='img_file', required=True)
    parser.add_argument('--scale', dest='scale', required=False)
    parser.add_argument('--out', dest='out_file', required=False)
    parser.add_argument('--cols', dest='cols', required=False)
    parser.add_argument('--more_levels', dest='more_levels',
                        action='store_true')

    args = parser.parse_args()

    img_file = args.img_file
    name = args.img_file[args.img_file.rindex('/') + 1: args.img_file.rindex('.')]
    out_file = f'output/{name}.txt'

    if args.out_file:
        out_file = args.out_file

    scale = 0.45

    if args.scale:
        scale = float(args.scale)

    cols = 80

    if args.cols:
        cols = int(args.cols)

    #if args.more_levels:
    #    more_levels = args.more_levels
    #print(args.more_levels)
    aimg = covert_image_to_ASCII(img_file, cols, scale, args.more_levels)

    f = open(out_file, 'w')

    for row in aimg:
        f.write(row + '\n')

    f.close()
    print(f"ASCII art written to {out_file}")
