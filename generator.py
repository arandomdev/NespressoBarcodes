"""Used to generate a custom code.

This script is used to generate a custom code that can be passed to
the printer script.

Each ID can be summarized in 4 segments, 3 four character segments and 1 six
character segment. For example "1100 1101 0100 001101"
"""

import argparse
from functools import partial

"""
The four segments are repeated four times with different separators in
between. Though the separators are the same across pods.

For example, Melozio has the following code

01 1100 10 1101 10 0100 10 010110 01
01 1100 10 1101 01 0100 01 010110 10
01 1100 01 1101 10 0100 01 010110 01
01 1100 01 1101 01 0100 01 010110 01
01 1100 01 1101 01 0100 10 010110 10
"""


def _getID() -> tuple[str, str, str, str]:
	"""Get the code from the user
	"""

	parser = argparse.ArgumentParser(description="Generate a code to pass to the printer.")  # noqa
	parser.add_argument(
		"ID",
		nargs="+",
		help="The ID to generate a code with. Formated like this, '1100 1101 0100 001101'"  # noqa
	)

	segments = parser.parse_args().ID

	# verify the segments
	if len(segments) != 4:
		print("Did not get 4 segments!")
		parser.exit()
		pass

	for i, segment in enumerate(segments):
		# check if each segment only contains 1s and 0s
		if any(c not in "10" for c in segment):
			print(f"Segment {i+1} has invalid characters! It can only contain 1s and 0s.")  # noqa
			parser.exit()
			pass

		# check if the length is correct
		if i == 3:
			if len(segment) != 6:
				print("Segment 4 does not have 6 characters!")
				parser.exit()
				pass
			pass
		else:
			if len(segment) != 4:
				print(f"Segment {i+1} does not have 4 characters!")
				parser.exit()
				pass
			pass
		pass

	return segments


def main():
	seg1, seg2, seg3, seg4 = _getID()

	formatter = "01{seg1}{sep1}{seg2}{sep2}{seg3}{sep3}{seg4}{sep4}"
	formatter = partial(
		formatter.format,
		seg1=seg1,
		seg2=seg2,
		seg3=seg3,
		seg4=seg4
	)

	formattedCode = ""
	formattedCode += formatter(
		sep1="10",
		sep2="10",
		sep3="10",
		sep4="01",
	)
	formattedCode += formatter(
		sep1="10",
		sep2="01",
		sep3="01",
		sep4="10",
	)
	formattedCode += formatter(
		sep1="01",
		sep2="10",
		sep3="01",
		sep4="01",
	)
	formattedCode += formatter(
		sep1="01",
		sep2="01",
		sep3="01",
		sep4="01",
	)
	formattedCode += formatter(
		sep1="01",
		sep2="01",
		sep3="10",
		sep4="10",
	)

	print(formattedCode)
	pass


if __name__ == "__main__":
	main()
	pass
