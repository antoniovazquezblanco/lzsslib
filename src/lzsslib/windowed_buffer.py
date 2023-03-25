#!/usr/bin/env python


class _WindowedBuffer(bytearray):
    def __init__(self, window_size, **kwargs) -> None:
        self._window_size = window_size
        super().__init__(**kwargs)

    def _check_len(self) -> None:
        excess = len(self) - self._window_size
        if excess > 0:
            del self[:excess]

    def append(self, i) -> None:
        super().append(i)
        self._check_len()

    def __iadd__(self, i):
        super().__iadd__(i)
        self._check_len()
        return self
