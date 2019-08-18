from PIL import Image
import random
import hashlib
import argparse
import shutil

if __name__ == '__main__':
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    option = parser.add_mutually_exclusive_group(required=True)
    option.add_argument('-e', nargs=3, dest='encrypt', metavar=('Image_Path,', 'Message_File_Path,', 'Key'))
    option.add_argument('-d', nargs=2, dest='decrypt', metavar=('Image_Path,', 'Key'))
    args = parser.parse_args()

    image_path = args.encrypt[0] if args.encrypt else args.decrypt[0]
    key = args.encrypt[2] if args.encrypt else args.decrypt[1]

    random.seed(int(hashlib.sha512(key.encode('utf-8')).hexdigest(), 16) % (10 ** 64))

    img = Image.open(image_path)
    pixels = [list(color) for color in list(img.getdata())]
    pixel_count = len(pixels) - 1 if len(pixels) & 1 else len(pixels)

    step_map = [_ for _ in range(pixel_count)]
    color_step_map = [random.randint(0, 2) for _ in range(pixel_count)]
    random.shuffle(step_map)

    if args.encrypt:
        with open(args.encrypt[1], 'rb') as file:
            msg = file.read()
        bite_list = ''.join(['{0:08b}'.format(n) for n in msg]) + '00000100'  # EOT

        for idx, bite in enumerate(bite_list):
            data = pixels[step_map[idx]][color_step_map[idx]]
            pixels[step_map[idx]][color_step_map[idx]] = data | 0b00000001 if bite == '1' else data & 0b11111110

        encrypted_img = Image.new(img.mode, img.size)
        encrypted_img.putdata([tuple(color) for color in pixels])
        encrypted_img.save(image_path.replace('jpg', 'png'))
        shutil.move(image_path.replace('jpg', 'png'), image_path)
    else:
        bits = ''
        i = 0
        while not (len(bits) % 8 == 0 and bits[-8:] == '00000100'):  # EOT
            bits += str(1 & pixels[step_map[i]][color_step_map[i]])
            i += 1

        print(''.join(chr(int(''.join(x), 2)) for x in zip(*[iter(bits[:-8])]*8)))
