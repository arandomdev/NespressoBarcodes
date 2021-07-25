# Nespresso Vertuo Barcode Generator
This project aims to decode and generate printable barcodes for the Nespresso's Vertuoline machines. Of course the barcodes aren't guaranteed to work, and i'm not responsible for any broken machines. Though I can't fathom how you could possibly break one.

## Setup
1. Download the latest version of python [here](https://www.python.org/downloads/). Or at least have version 3.7 or greater.
2. Install Pillow through `pip install Pillow`

# Usage
This project has two scripts, the generator and printer.

## The generator
The generator takes a simplified form of a pod's code called the ID to generate a code that can be passed to the printer. The ID has 4 segments of 1s and 0s, for example "1100 1101 0100 001101"

TODO: Example and table

## The printer
The printer takes a code and turns it into a printable image. The code should be 140 characters consisting of only 1s and 0s.

```console
> python printer.py 01110010110110010010001101010111001011010101000100110110011100011101100100010011010101110001110101010001001101010111000111010101001000110110

> python printer.py -o outputPath.png 01110010110110010010001101010111001011010101000100110110011100011101100100010011010101110001110101010001001101010111000111010101001000110110
```


# Helpful links
* https://www.reddit.com/r/nespresso/comments/d9xnv9/breaking_the_nespresso_vertuo_barcodes/
* https://www.reddit.com/r/nespresso/comments/okc1vx/breaking_the_nespresso_vertuo_barcodes_part_2/