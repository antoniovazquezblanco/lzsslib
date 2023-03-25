#!/usr/bin/env python

import unittest
from lzsslib.windowed_buffer import _WindowedBuffer

class TestWindowedBuffer(unittest.TestCase):
    def setUp(self):
        self.buf = _WindowedBuffer(100)

    def tearDown(self):
        del self.buf

    def test_initial_size(self):
        self.assertEqual(len(self.buf), 0, 'incorrect initial len')

    def test_append(self):
        for i in range(0, 50):
            self.buf.append(i)
        self.assertEqual(len(self.buf), 50, 'incorrect length')
        self.assertEqual(self.buf[0], 0, 'incorrect first element')
        self.assertEqual(self.buf[49], 49, 'incorrect last element')
        for i in range(50, 100):
            self.buf.append(i)
        self.assertEqual(len(self.buf), 100, 'incorrect length')
        self.assertEqual(self.buf[0], 0, 'incorrect first element')
        self.assertEqual(self.buf[49], 49, 'incorrect intermediate element')
        self.assertEqual(self.buf[99], 99, 'incorrect last element')
        for i in range(100, 150):
            self.buf.append(i)
        self.assertEqual(len(self.buf), 100, 'incorrect length')
        self.assertEqual(self.buf[0], 50, 'incorrect first element')
        self.assertEqual(self.buf[99], 149, 'incorrect last element')

    def test_iadd(self):
        for i in range(0, 50):
            self.buf += int.to_bytes(i, 1)
        self.assertEqual(len(self.buf), 50, 'incorrect length')
        self.assertEqual(self.buf[0], 0, 'incorrect first element')
        self.assertEqual(self.buf[49], 49, 'incorrect last element')
        for i in range(50, 100):
            self.buf += int.to_bytes(i, 1)
        self.assertEqual(len(self.buf), 100, 'incorrect length')
        self.assertEqual(self.buf[0], 0, 'incorrect first element')
        self.assertEqual(self.buf[49], 49, 'incorrect intermediate element')
        self.assertEqual(self.buf[99], 99, 'incorrect last element')
        for i in range(100, 150):
            self.buf += int.to_bytes(i, 1)
        self.assertEqual(len(self.buf), 100, 'incorrect length')
        self.assertEqual(self.buf[0], 50, 'incorrect first element')
        self.assertEqual(self.buf[99], 149, 'incorrect last element')

if __name__ == '__main__':
    unittest.main()
