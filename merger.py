import sys
from pathlib import Path
from pypdf import PdfWriter

user_files = sys.argv[1:]


def merge_files(files):
    print(f"Starting to merge {len(files)} files...")

    merger = PdfWriter()

    for pdf in files:
        pdf_path = "input/" + pdf
        print(f"Merging {pdf_path}")
        merger.append(pdf_path)

    if (not Path("output/").exists()):
        Path.mkdir(Path("output/"))

    merger.write("output/result.pdf")

    merger.close()

    print('Finished! PDF saved in "output/result.pdf"')


merge_files(user_files)
