import argparse
import os
import pathlib
from dataclasses import dataclass

from PIL import Image, ImageDraw

IMAGE_SIZE = 2400
POD_OUTER_DIA = 2.26
POD_INNER_DIA = 2.02

DPI = IMAGE_SIZE / POD_OUTER_DIA
CODON_HEIGHT = int(DPI * (POD_OUTER_DIA - POD_INNER_DIA) * 0.6)
CODON_WIDTH_TOLERANCE = 0.5


class _PrinterArgs(argparse.Namespace):
	code: str = ""
	output: pathlib.Path = None
	pass


@dataclass
class _Codon(object):
	color: str
	startAngle: int
	endAngle: int
	pass


def _getArgs() -> _PrinterArgs:
	parser = argparse.ArgumentParser(description="Create a printable barcode.")
	parser.add_argument(
		"code",
		help="A 140 character code to make a barcode with."
	)

	parser.add_argument(
		"-o", "--output",
		type=pathlib.Path,
		help="The path of the output image. By default it outputs to 'output/customBarcode.png'"  # noqa
	)

	args = parser.parse_args(namespace=_PrinterArgs())

	# verify the input code
	if len(args.code) != 140:
		print("The code is not 140 character!")
		parser.exit()
		pass

	if any(c not in "10" for c in args.code):
		print("The code has invalid characters! It can only have 1s and 0s.")
		parser.exit()
		pass

	return args


def main():
	args = _getArgs()

	# Create the output directory if necessary
	outputPath = args.output
	if outputPath is None:
		outputPath = pathlib.Path("output/customBarcode.png")
		os.makedirs(outputPath.parent, exist_ok=True)
		pass
	else:
		os.makedirs(outputPath.parent, exist_ok=True)
		pass

	# generate a list of codons
	inputData = args.code
	angleSize = 360 / len(inputData)

	code: list[_Codon] = []
	currentAngle = 0

	i = 0
	while i < len(inputData):
		value = inputData[i]

		# check for how many of the same color are in a row
		changeValue = "0" if value == "1" else "1"
		changeIndex = inputData.find(changeValue, i)
		if changeIndex == -1:
			changeIndex = i + 1

		codonWidth = changeIndex - i

		startAngle = currentAngle + CODON_WIDTH_TOLERANCE
		endAngle = startAngle + (codonWidth * angleSize) - CODON_WIDTH_TOLERANCE

		code.append(
			_Codon(
				"white" if value == "0" else "black",
				startAngle,
				endAngle
			)
		)

		currentAngle += codonWidth * angleSize
		i += codonWidth
		pass

	# create the image
	with Image.new("1", (IMAGE_SIZE, IMAGE_SIZE), color=1) as im:
		draw = ImageDraw.Draw(im)

		for codon in code:
			if codon.color == "white":
				continue

			draw.arc(
				((0, 0), (IMAGE_SIZE, IMAGE_SIZE)),
				codon.startAngle,
				codon.endAngle,
				fill=codon.color,
				width=CODON_HEIGHT
			)
			pass

		im.save(outputPath)
		pass
	pass


if __name__ == "__main__":
	main()
	pass
