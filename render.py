#!/usr/bin/env python3
# Copyright © 2020 Clément Pit-Claudel
# https://github.com/cpitclaudel/academic-poster-template
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""Render a jinja2 template."""

import argparse
from os.path import dirname, realpath, relpath


from jinja2 import *
from pybtex.database.input import bibtex
import bibble


def parse_arguments():
    parser = argparse.ArgumentParser(description='Render a Jinja2 template.')
    parser.add_argument("input", help="Read from INPUT")
    parser.add_argument("output", nargs="?", default="-",
                        help="Write to OUTPUT (default: -)")
    parser.add_argument("--bibtex", help="bibtex file to render references (optional)", default=None)

    return parser.parse_args()

def main():
    args = parse_arguments()
    

    
    srcdir = '.' #dirname(realpath(args.input))
    env = Environment(loader=FileSystemLoader(srcdir),
                      autoescape=select_autoescape(('html', 'xml')),
                      trim_blocks=True,
                      undefined=StrictUndefined)
    
    # handle references
    env.filters['author_fmt'] = bibble._author_fmt
    env.filters['author_list'] = bibble._author_list
    env.filters['title'] = bibble._title
    env.filters['venue_type'] = bibble._venue_type
    env.filters['venue'] = bibble._venue
    env.filters['main_url'] = bibble._main_url
    env.filters['extra_urls'] = bibble._extra_urls
    env.filters['monthname'] = bibble._month_name
    
    if args.bibtex is not None:
        # Parse the BibTeX file.
        db = bibtex.Parser().parse_stream(open(relpath(args.bibtex, srcdir), 'r'))
        
        # Include the bibliography key in each entry.
        for k, v in db.entries.items():
            v.fields['key'] = k
            bib_sorted = sorted(db.entries.values(), key=bibble._sortkey, reverse=True)
    else:
        bib_sorted=[]

        
    with argparse.FileType('w')(args.output) as output:
        output.write(env.get_template(relpath(args.input, srcdir)).render(ref_entries=bib_sorted))

if __name__ == '__main__':
    main()
