import os
import optparse
from lxml.html import parse

def convert(i_filename, o_filename):
    page = parse(i_filename)
    resources = page.xpath(".//string")

    f = open(o_filename, "w")
    for resource in resources:
        body = resource.text_content()
        f.write(body.encode("utf-8") + os.linesep)

    f.close()


def main():
    parser = optparse.OptionParser(usage="usage: %prog path", version = '%prog version 1.0')
    parser.add_option('-i', '--input', help ='Input xml file with extension')
    parser.add_option('-o', '--output', help ='Output txt file with extension')

    (opts, args) = parser.parse_args()
    i_filename = opts.input
    o_filename = opts.output

    convert(i_filename, o_filename)


if __name__ == '__main__':
    main()