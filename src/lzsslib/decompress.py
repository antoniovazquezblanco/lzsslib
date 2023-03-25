#!/usr/bin/env python

from bitstring import BitStream

from .windowed_buffer import _WindowedBuffer


class LzssDecompressor:
    def __init__(self, offset_width=12, size_width=5, size_min=3) -> None:
        self._offset_width = offset_width
        self._size_width = size_width
        self._ref_width = offset_width + size_width + 1
        self._size_min = size_min
        self._window_buf = _WindowedBuffer(window_size=(1 << offset_width))
        self._bitstream = BitStream()

    def decompress(self, data, max_out_len=-1):
        out = b''
        self._bitstream += data

        while len(out) < max_out_len and \
            len(self._bitstream) > 9:
            if self._bitstream.read('bool:1'):
                byte = self._bitstream.read('bytes:1')
                del self._bitstream[:9]
                self._bitstream.pos = 0
                out += byte
                self._window_buf += byte
            else:
                if len(self._bitstream) < self._ref_width:
                    self._bitstream.pos = 0
                    break
                offset = self._bitstream.read(f'uint:{self._offset_width}')
                size = self._bitstream.read(f'uint:{self._size_width}')+self._size_min
                del self._bitstream[:self._ref_width]
                self._bitstream.pos = 0
                elems = self._window_buf[offset:offset+size]
                out += elems
                self._window_buf += elems

        return out
