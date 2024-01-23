# liblzss

![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/antoniovazquezblanco/lzsslib/test.yml)
![PyPI](https://img.shields.io/pypi/v/lzsslib)

Liblzss is an small library for inflating and deflating LZSS (Lempel, Ziv,
Storer, Szymanski) buffers.

The LZSS format is originally described in a paper titled ["Data Compression via
Textual Substitution" published in Journal of the ACM, 29(4):928-951, 1982 by
J.A. Storer and T.G. Szymanski.](https://doi.org/10.1145/322344.322346)


## Installing

Install and update using `pip`:

```bash
$ pip install -U lzsslib
```


## Usage

The following example shows how to decompress a file using default options.

```python
from pathlib import Path
from lzsslib.decompress import LzssDecompressor

# Create a decompressor object with default options
decomp = LzssDecompressor()

# Open an input and output files
fin = Path('input.lzss').open(mode='rb')
fout = Path('output.bin').open(mode='wb')

# Read the input, decompress and write
while (buffer := fin.read(1024)):
    out = decomp.decompress(buffer, remaining_size)
    fout.write(out)

# Ensure output is written and close
fout.flush()
fin.close()
fout.close()
```

## Links

-   PyPI Releases: https://pypi.org/project/lzsslib/
-   Source Code: https://github.com/antoniovazquezblanco/lzsslib
-   Issue Tracker: https://github.com/antoniovazquezblanco/lzsslib/issues
