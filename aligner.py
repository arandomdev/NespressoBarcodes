"""
Start code has this format
01 ---- 10 ---- 10 ---- 10 ------ 01
"""

TEST_CODE = "01011001011100010001010010010101100101110001000101001010010110100111001000011000101001011001011100100001010010010101101001110001000110001001"  # noqa


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
			print(currentCode)
			break

		currentCode = shift(currentCode)
		pass
	pass


if __name__ == "__main__":
	main()
