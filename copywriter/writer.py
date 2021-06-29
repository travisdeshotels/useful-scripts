import re as regex
from lib.colors import yellow

"""
Replace the copyright header in a sourcecode file with a new one using a template
A file named 'template' must be defined in the same directory as this file
Usage: python copywriter.py <file>
"""


def fill_template(template_data, file_name):
    # add more template variables as needed
    filename_parts = regex.split('/', file_name)
    short_filename = regex.sub('.[a-zA-Z]+', '', filename_parts[-1])
    return regex.sub('{FILENAME}', short_filename, template_data)


def load_copyright_template(file_name):
    with open('copywriter/template', 'r') as infile:
        template_data = infile.read()
    return fill_template(template_data, file_name)


def load_file_data(file_name):
    with open(file_name, 'r') as infile:
        file_data = infile.read()
    return file_data


def strip_copyright_block(file_data, file_name, verbose):
    # search for "Copyright" and "all rights reserved"
    # ignores case
    updated_file_data = file_data
    if regex.search('/\*[\S\s]*[Cc]opyright[\S\s]*[Aa]ll\s[Rr]ights\s[Rr]eserved[\S\s]*\*/', file_data):
        if verbose:
            print('Found copyright block for file {}'.format(file_name))
        updated_file_data = regex.sub('/\*[\S\s]*[Cc]opyright[\S\s]*[Aa]ll\s[Rr]ights\s[Rr]eserved[\S\s]*\*/', '',
                                      file_data)
    elif regex.search('[Cc]opyright\s[0-9]{4}', file_data):
        print(yellow(f'Warning: could not match copyright block in file {file_name}'))
    elif verbose:
        print(f'No strip for file {file_name}')
    return updated_file_data


def write_output(output_data, output_file):
    with open(output_file, 'w') as outfile:
        outfile.write(output_data)


def main(args):
    file_name = args.filename
    template_data = load_copyright_template(file_name)
    file_data = load_file_data(file_name)
    if not args.nostrip:
        file_data = strip_copyright_block(file_data, file_name, args.verbose)
    write_output(template_data + file_data, file_name)
