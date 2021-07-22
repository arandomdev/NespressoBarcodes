"""Used to generate a custom barcode.

This Script is used to generate a custom code that can be passed to
the printer script.

Each code consist of 4 segments, 3 four characters and 1 six character.
for example "1100 1101 0100 001101"
"""

import argparse
from functools import partial

"""
The four segments are repeated for times with different separators in
between. Though the separators are the same across pods.

for example, Melozio has the following code

01 1100 10 1101 10 0100 10 010110 01
01 1100 10 1101 01 0100 01 010110 10
01 1100 01 1101 10 0100 01 010110 01
01 1100 01 1101 01 0100 01 010110 01
01 1100 01 1101 01 0100 10 010110 10
"""


# 4 segments in order, seperated by a space
SEGMENTS = "1100 1101 0100 001101"


def main():
	code = ""

	seg1, seg2, seg3, seg4 = SEGMENTS.split(" ")

	formatter = "01{seg1}{sep1}{seg2}{sep2}{seg3}{sep3}{seg4}{sep4}"
	formatter = partial(
		formatter.format,
		seg1=seg1,
		seg2=seg2,
		seg3=seg3,
		seg4=seg4
	)

	code += formatter(
		sep1="10",
		sep2="10",
		sep3="10",
		sep4="01",
	)
	code += formatter(
		sep1="10",
		sep2="01",
		sep3="01",
		sep4="10",
	)
	code += formatter(
		sep1="01",
		sep2="10",
		sep3="01",
		sep4="01",
	)
	code += formatter(
		sep1="01",
		sep2="01",
		sep3="01",
		sep4="01",
	)
	code += formatter(
		sep1="01",
		sep2="01",
		sep3="10",
		sep4="10",
	)

	print(code)
	pass


if __name__ == "__main__":
	main()
	pass
