import struct

from collections import namedtuple
from array import array

LabelMeta = namedtuple("LabelMeta", ["magic", "size"], defaults=[None, None])
ImageMeta = namedtuple(
    "ImageMeta",
    ["magic", "size", "rows", "cols"],
    defaults=[None, None, None, None],
)


class MNIST(object):
    def __init__(self, path_images, path_labels):
        self.path_images = path_images
        self.path_labels = path_labels
        self.label_meta = None
        self.image_meta = None

    def load_labels(self):

        with open(self.path_labels, "rb") as file:
            # magic, number of items
            magic, size = struct.unpack(">II", file.read(8))
            if magic != 2049:
                raise ValueError(
                    "Magic number mismatch, expected 2049,"
                    "got {}".format(magic)
                )

            return array("B", file.read())

    def load_images(self):
        with open(self.path_images, "rb") as file:
            # Pixels are organized row-wise. Pixel values are 0 to 255. 0 means background (white), 255 means foreground (black).
            magic, size, rows, cols = struct.unpack(">IIII", file.read(16))
            if magic != 2051:
                raise ValueError(
                    "Magic number mismatch, expected 2051,"
                    "got {}".format(magic)
                )

            return array("B", file.read())

    def get_label_meta(self):
        if not self.label_meta:
            with open(self.path_labels, "rb") as file:
                maigc, size = struct.unpack(">II", file.read(8))
                self.image_meta = LabelMeta(magic, size)

        return self.label_meta

    def get_image_meta(self):
        if not self.image_meta:
            with open(self.path_images, "rb") as file:
                magic, size, rows, cols = struct.unpack(">IIII", file.read(16))
                self.image_meta = ImageMeta(magic, size, rows, cols)
        return self.image_meta
