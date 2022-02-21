import sys
import PyPDF2

files = sys.argv[1:]


def pdf_merger(files):
    merger = PyPDF2.PdfFileMerger()
    for file in files:
        merger.append(file)
    merger.write("merged.pdf")


pdf_merger(files)

# usage: python pdf_merger.py [name_of_file_to_merge] [name_of_file_to_merge_2]
