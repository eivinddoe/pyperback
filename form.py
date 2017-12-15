#!/usr/bin/python

# This script takes the form input and generates PDF
import subprocess
import cgi
import cgitb

cgitb.enable()

print('Content-Type: text/html')
print()
print()

form = cgi.FieldStorage()

# Load files
file = open('template.tex', 'r')
template = file.read()

# Tags
title = form.getvalue('thetitle')
author = form.getvalue('theauthor')
section1 = form.getvalue('section1')
content1 = form.getvalue('content1')

page = template % {'title' : title,
    	'author' : author,
	'section1' : section1,
	'content1' : content1}

# Write to tex
output = open('temp/result.tex', 'w+')
output.write(page)

# Run subprocess
#subprocess.call(['pdflatex', '-quiet', 'temp/result.tex'])
#subprocess.call(['pdflatex', 'temp/result.tex'])

print()
print('<h1>TeX-file generated</h1>')
print('<p><a href="temp/result.tex">Download .tex</a>')
print('<p><a href="write.sh">Convert to .pdf</a>')
