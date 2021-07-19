

SEG1 = "1100"
SEG2 = "1101"
SEG3 = "1011"
SEG4 = "010110"


def main():
	code = ""

	formatter = "01{seg1}{sep1}{seg2}{sep2}{seg3}{sep3}{seg4}{sep4}"
	code += formatter.format(
		seg1=SEG1,
		seg2=SEG2,
		seg3=SEG3,
		seg4=SEG4,
		sep1="10",
		sep2="10",
		sep3="10",
		sep4="01",
	)
	code += formatter.format(
		seg1=SEG1,
		seg2=SEG2,
		seg3=SEG3,
		seg4=SEG4,
		sep1="10",
		sep2="01",
		sep3="01",
		sep4="10",
	)
	code += formatter.format(
		seg1=SEG1,
		seg2=SEG2,
		seg3=SEG3,
		seg4=SEG4,
		sep1="01",
		sep2="10",
		sep3="01",
		sep4="01",
	)
	code += formatter.format(
		seg1=SEG1,
		seg2=SEG2,
		seg3=SEG3,
		seg4=SEG4,
		sep1="01",
		sep2="01",
		sep3="01",
		sep4="01",
	)
	code += formatter.format(
		seg1=SEG1,
		seg2=SEG2,
		seg3=SEG3,
		seg4=SEG4,
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
