import urllib
import xhtml2pdf.pisa as pisa
import xhtml2pdf.pdf as pisa_pdf
import sys

def download_page_contents(url):
    f = urllib.urlopen(url)
    contents = f.read()
    f.close()
    return contents

def get_urls(contents):
    lower_contents = contents.lower()
    needle = 'href="'
    href_list = []
    ndx = lower_contents.find(needle)
    while ndx >= 0:
        token = contents[ndx+len(needle):]
        end_dnx = token.find('"')
        token = token[:end_dnx]
        # Don't attempt to follow links to named anchors or email addresses
        if (token.find("#") == -1) and (token[0:6] != 'mailto'):
            href_list.append(token)
        contents = contents[ndx+len(needle):]
        lower_contents = contents.lower()
        ndx = lower_contents.find(needle)
    return href_list

def convert_index(url, outfile):
    ndx = url.rfind("/")
    base_url = url[:ndx]
    c = download_page_contents(url)
    list = get_urls(c)

    pdf = pisa_pdf.pisaPDF()
    for l in list:
        u = base_url + "/" + l
        c = download_page_contents(u)

        subPdf = pisa.pisaDocument(c)
        pdf.addDocument(subPdf)

    res = pdf.getvalue()
    f = open(outfile, "wb").write(res)


def print_help():
    print """This program will convert an html document with an index into a single pdf.  It first goes to the index page and extracts every link.  It them goes to every link, converts the html doc into a pdf, and then finally joins every pdf into a dingle file"""
    print "%s <url to index> <output file name>"

def main():

    try:
        if "--help" in sys.argv or "-h" in sys.argv:
            print_help()
            return
        if len(sys.argv) != 3:
            print_help()
            return
        url = sys.argv[1]
        outfile = sys.argv[2]
        convert_index(url, outfile)
    except Exception, ex:
        print_help()
        raise

    print "Done"
    return 0


if __name__ == "__main__":
    rc = main()
    sys.exit(rc)
