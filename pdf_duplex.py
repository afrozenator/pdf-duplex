import argparse
import os

import pypdf

_DESCRIPTION = r"""
Splits a pdf into two, one with odd and the other with even pages.

This is to print duplex on non duplex printers.
"""

def split_into_even_odd(original_file,
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


def fix_filenames(filename, filename_odd, filename_even):
    if not filename:
        raise ValueError("Base filename needs to be given with -f.")

    # Both are present, return early.
    if filename_odd and filename_even:
        return filename, filename_odd, filename_even

    base_dir = os.path.dirname(filename)

    # Either or both are absent.
    if not filename_odd:
        filename_odd = f'{base_dir}/odd.pdf'
    if not filename_even:
        filename_even = f'{base_dir}/even.pdf'

    return filename, filename_odd, filename_even


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
            prog='pdf_duplex',
            description=_DESCRIPTION,
            epilog='@afrozenator')
    parser.add_argument('-f', '--filename')
    parser.add_argument('-o', '--filename_odd')
    parser.add_argument('-e', '--filename_even')
    args = parser.parse_args()
    filename, filename_odd, filename_even = fix_filenames(
            args.filename, args.filename_odd, args.filename_even)
    split_into_even_odd(filename, filename_odd, filename_even)
