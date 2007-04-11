""" Command line interface to difflib.py providing diffs in four formats:

* ndiff:    lists every line and highlights interline changes.
* context:  highlights clusters of changes in a before/after format.
* unified:  highlights clusters of changes in an inline format.
* html:     generates side by side comparison with change highlights.

"""

import sys, os, time, difflib, optparse, codecs

def main():

    usage = "usage: %prog [options] fromfile tofile"
    parser = optparse.OptionParser(usage)
    parser.add_option("-c", action="store_true", default=False, help='Produce a context format diff (default)')
    parser.add_option("-u", action="store_true", default=False, help='Produce a unified format diff')
    parser.add_option("-m", action="store_true", default=False, help='Produce HTML side by side diff (can use -c and -l in conjunction)')
    parser.add_option("-n", action="store_true", default=False, help='Produce a ndiff format diff')
    parser.add_option("-f", action="store_true", default=False, help='Create a file of output text')
    parser.add_option("-l", "--lines", type="int", default=3, help='Set number of context lines (default 3)')
    (options, args) = parser.parse_args()

    if len(args) == 0:
        parser.print_help()
        sys.exit(1)
    if len(args) != 2:
        parser.error("need to specify both a fromfile and tofile")

    n = options.lines
    fromfile, tofile = args

    fromdate = time.ctime(os.stat(fromfile).st_mtime)
    todate = time.ctime(os.stat(tofile).st_mtime)
    fromlines = open(fromfile, 'U').readlines()
    tolines = open(tofile, 'U').readlines()

    if options.u:
        diff = difflib.unified_diff(fromlines, tolines, fromfile, tofile, fromdate, todate, n=n)
        #if options.f:
        #    fs = codecs.open('dif.dat', 'a', 'utf-8')
        #    fs.write('%s'%diff)
        #    fs.close()
    elif options.n:
        diff = difflib.ndiff(fromlines, tolines)
        #if options.f:
        #    fs = codecs.open('dif.dat', 'a', 'utf-8')
        #    fs.write('%s'%diff)
        #    fs.close()
    elif options.m:
        diff = difflib.HtmlDiff().make_file(fromlines,tolines,fromfile,tofile,context=options.c,numlines=n)
        if options.f:
            fs = codecs.open('dif.html', 'a', 'utf-8')
            fs.write(u'%s'%diff)
            fs.close()
    else:
        diff = difflib.context_diff(fromlines, tolines, fromfile, tofile, fromdate, todate, n=n)
        #if options.f:
        #    fs = codecs.open('dif.dat', 'a', 'utf-8')
        #    fs.write('%s'%diff)
        #    fs.close()

    sys.stdout.writelines(diff)

if __name__ == '__main__':
    main()
