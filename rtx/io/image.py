"""
image.py

handles saving png files
"""

import numpy as np
from typing import Tuple, List

# code taken from https://stackoverflow.com/a/19174800/14277568

import struct
import zlib


def png_pack(png_tag, buf) -> bytes:
    """Pack a small buffer into a chunk"""
    chunk_head = png_tag + buf
    return (struct.pack("!I", len(buf)) + 
                        chunk_head +
                        struct.pack("!I", 0xFFFFFFFF & zlib.crc32(chunk_head))
                )


def write_png(pixelbuffer: bytes, width: int, height: int) -> bytes:
    """Write a pixelbuffer to a png file - RGBA"""
    # reverse the vertical line order and add null bytes at the start
    width_byte_4 = width * 4
    raw_data = b''.join(
        b'\x00' + pixelbuffer[span:span + width_byte_4]
        for span in range((height - 1) * width_byte_4, -1, - width_byte_4)
    )

    return b''.join([
        b'\x89PNG\r\n\x1a\n',
        png_pack(b'IHDR', struct.pack("!2I5B", width, height, 8, 6, 0, 0, 0)),
        png_pack(b'IDAT', zlib.compress(raw_data, 9)),
        png_pack(b'IEND', b'')
        ])


def save_to_file(filename: str, arr: List[List[int]]) -> None:
    """Converts a numpy array to bytes - 1D array please"""
    if any([len(row) != len(arr[0]) for row in arr]):
        raise ValueError("[ERROR][image.py] Elements should have equal size!")
    
    # first row becomes top row of image
    # i hate map, map is bad map(x, y) not work :(
    flat = [pix for row in arr for pix in row]

    # big endian, unsigned 32-byte integer
    # newsflash, I have NO IDEA WHAT THIS LINE OF CODE DOES EXCEPT POSSIBLY CREATE AE MASSIC NUMBER
    buf = b''.join([struct.pack(">I", 
                ((0xffFFff & i32) << 8)|(i32>>24)) for i32 in flat])
    # above also rotates from ARGB to RGBA
    
    data = write_png(buf, len(arr[0]), len(arr))

    # write to a file
    with open(filename, 'wb') as fb:
        fb.write(data)
        fb.close()


def convert_buffer_to_uint32(arr: List[List[Tuple[int, int, int, int]]]) -> List[List[int]]:
    """Converts an (r, g, b, a) array to its single integer counterpart"""
    new: List[List[int]] = []
    # argb
    for i, row in enumerate(arr):
        new.append([])
        for p in row:
            new[i].append((p[3]<<24) + (p[2] << 16) + (p[1] << 8) + p[0])
    return new

