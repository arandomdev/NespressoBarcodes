from dataclasses import dataclass
from PIL import Image, ImageDraw

TEST_CODE = "01110010110110010010001101010111001011010101000100110110011100011101100100010011010101110001110101010001001101010111000111010101001000110110"  # noqa

IMAGE_SIZE = 2400
POD_OUTER_DIA = 2.26
POD_INNER_DIA = 2.02

DPI = IMAGE_SIZE / POD_OUTER_DIA
CODON_HEIGHT = int(DPI * (POD_OUTER_DIA - POD_INNER_DIA) * 0.6)
CODON_WIDTH_TOLERANCE = 0.5


@dataclass
class _Codon(object):
	color: str
	startAngle: int
	endAngle: int


def main():
	inputData = TEST_CODE

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

		with open("output\\testImage.png", mode="wb") as outFile:
			im.save(outFile, dpi=(DPI, DPI))
			pass
		pass
	pass


if __name__ == "__main__":
	main()
	pass
