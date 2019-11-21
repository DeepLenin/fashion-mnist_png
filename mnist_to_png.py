#!/usr/bin/python3
import os
import png
import struct


ORIG_DIR = "./original_data"
OUT_DIR = "./data"
TRAIN_FILES = ["train-images-idx3-ubyte", "train-labels-idx1-ubyte"]
TRAIN_NUM = 60000
TEST_FILES = ["t10k-images-idx3-ubyte", "t10k-labels-idx1-ubyte"]
TEST_NUM = 10000


def gunzip(orig_dir, filename):
    """
    Gunzip of gzipped files if they exist.
    It will check if unzipped files exist.
    """
    filename = os.path.join(orig_dir, filename)
    fname_gz = filename + ".gz"
    if os.path.exists(fname_gz):
        cmd = f"gunzip {fname_gz}"
        print(cmd)
        os.system(cmd)
    assert os.path.exists(filename), \
        f"{filename} does not exist. Try to run last command yourself"


def parse_images(filename):
    """
    Reading images information and converting from bytearray to list of ints
    with help of python's struct module.
    """
    images = []
    imgs_file = open(filename, 'rb')
    # Get only the size of following data
    size = struct.unpack(">IIII", imgs_file.read(16))[1]
    for _ in range(size):
        # Read whole image pixel and unpack it from unsigned bytes to integers
        barray = imgs_file.read(784)
        img = list(struct.unpack("<" + "B"*784, barray))
        images.append(img)

    return images


def parse_labels(filename):
    """
    Reading labels file and convert every byte of it to label for specific
    image
    """
    labels = []
    lbls_file = open(filename, 'rb')
    # Get only size of following data
    size = struct.unpack(">II", lbls_file.read(8))[1]
    for _ in range(size):
        # Byte per label
        barray = lbls_file.read(1)
        lbl = struct.unpack("<B", barray)[0]
        labels.append(lbl)
    return labels


def write_files(out_folder, images, labels, inc=True):
    """
    This function will write lists of pixel ([int])

    inc=True meaning that every image will have it's own incremental id
    inc=False meaning that every image of specific label will have incremental
    id
    """
    imgs = {}
    for i in range(10):
        os.makedirs(os.path.join(out_folder, str(i)), exist_ok=True)
        imgs[i] = 0

    for idx, (img, lbl) in enumerate(zip(images, labels)):
        # e.g. train/0/15.png
        if inc:
            fpath = os.path.join(out_folder, str(lbl), str(idx) + ".png")
        else:
            fpath = os.path.join(out_folder, str(lbl), str(imgs[lbl]) + ".png")
        img_file = open(fpath, "wb")
        writer = png.Writer(28, 28, greyscale=True)
        # Reshape img from 784 to 28x28
        img = [img[n*28:(n+1)*28] for n in range(28)]
        writer.write(img_file, img)
        img_file.close()
        imgs[lbl] += 1


def convert(orig_dir, out_dir, img_file, lbl_file):
    """
    Function which converts pair of files into images
    """
    fpath = os.path.join(orig_dir, img_file)
    images = parse_images(fpath)
    print(f"Parsed {len(images)} images: {fpath}")

    fpath = os.path.join(orig_dir, lbl_file)
    labels = parse_labels(fpath)
    print(f"Parsed {len(labels)} labels: {fname}")

    write_files(out_dir, images, labels)
    print(f"Images created in {out_dir}")


if __name__ == "__main__":
    print("Unziping all files")
    for fname in TRAIN_FILES + TEST_FILES:
        gunzip(ORIG_DIR, fname)

    convert(ORIG_DIR, OUT_DIR + "/train",
            img_file=TRAIN_FILES[0],
            lbl_file=TRAIN_FILES[1])

    convert(ORIG_DIR, OUT_DIR + "/test",
            img_file=TEST_FILES[0],
            lbl_file=TEST_FILES[1])
