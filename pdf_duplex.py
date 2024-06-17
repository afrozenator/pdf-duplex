import argparse

import pypdf

_DESCRIPTION = r"""
Splits a pdf into two, one with odd and the other with even pages.

This is to print duplex on non duplex printers.
"""

def split_into_two(original_file,
                   odd_file,
                   even_file):
    orig_pdf = pypdf.PdfReader(original_file)
    num_pages = len(orig_pdf.pages)
    odd_writer = pypdf.PdfWriter()
    odd_writer.append(fileobj=orig_pdf, pages=(0, num_pages, 2))
    odd_writer.write(odd_file)
    even_writer = pypdf.PdfWriter()
    even_writer.append(fileobj=orig_pdf, pages=(1, num_pages, 2))
    even_writer.write(even_file)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
            prog='pdf_duplex',
            description=_DESCRIPTION,
            epilog='@afrozenator')
    parser.add_argument('-f', '--filename')
    parser.add_argument('-o', '--filename_odd')
    parser.add_argument('-e', '--filename_even')
    args = parser.parse_args()
    print(args.filename)
    print(args.filename_odd)
    print(args.filename_even)
    split_into_two(args.filename, args.filename_odd, args.filename_even)
