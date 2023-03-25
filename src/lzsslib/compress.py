#!/usr/bin/env python

from .windowed_buffer import _WindowedBuffer
from bitstring import BitStream


class LzssCompressor:
    def __init__(self, offset_width=12, size_width=5, size_min=3) -> None:
        self._offset_width = offset_width
        self._size_width = size_width
        self._size_min = size_min
        self._size_max = (1 << size_width) - 1 + size_min
        self._window_buf = _WindowedBuffer(window_size=(1 << offset_width))
        self._instream = bytearray()

    def _match_find(self):
        # Calculate maximum match length...
        match_max_len = min(self._size_max, len(self._window_buf), len(self._instream))
        # Be greedy, start with the max length match...
        candidate = self._instream[:match_max_len]
        while len(candidate) >= self._size_min:
            pos = self._window_buf.find(candidate)
            if pos > -1:
                return (True, pos, len(candidate))
            del candidate[-1:]
        return (False, None, None)

    def compress(self, data, remaining_input):
        out = BitStream()
        self._instream += data

        while len(self._instream) > 0:
            if remaining_input:
                if len(self._window_buf) > len(self._instream):
                    break
                if len(self._instream) < self._size_max:
                    break
            found, pos, length = self._match_find()
            if not found:
                out.append('0b1')
                out.append(self._instream[0:1])
                self._window_buf += self._instream[0:1]
                del self._instream[0:1]
            else:
                encoded_len = length - self._size_min
                out.append('0b0')
                out.append(f'uint:{self._offset_width}={pos}')
                out.append(f'uint:{self._size_width}={encoded_len}')
                self._window_buf += self._instream[0:length]
                del self._instream[0:length]

        return out
