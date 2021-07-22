from functools import partial

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
