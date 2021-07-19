"""
Start code has this format
01 ---- 10 ---- 10 ---- 10 ------ 01
"""

TEST_CODE = "10101101000101001110100111000110111000010100111001011100011011010001010011100101110001101101000110001110100111001010111000011000111001011100"  # noqa


def shift(number: str) -> str:
	return number[1:] + number[0]


def main():
	currentCode = TEST_CODE
	for i in range(140):
		# Test format
		if (
			currentCode[0:2] == "01"
			and currentCode[6:8] == "10"
			and currentCode[12:14] == "10"
			and currentCode[18:20] == "10"
			and currentCode[26:28] == "01"
		):
			print(f"Aligned: {currentCode}")
			print(f"Inverted: {''.join(['1' if x == '0' else '0' for x in currentCode])}")  # noqa
			break

		currentCode = shift(currentCode)
		pass
	pass


if __name__ == "__main__":
	main()
