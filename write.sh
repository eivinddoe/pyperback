#!/bin/bash

OUTPUT="$(date)"
echo "Content-type: text/html"
echo ""

echo "<html><head><title>PDF conversion complete</title></head><body>"
echo "Today is $OUTPUT <br />"
pdflatex -interaction nonstopmode temp/result.tex > /dev/null 2>&1
echo "Download your PDF:"
echo ""
echo "<a href="result.pdf">Download</a><br />"
echo "<a href="delete.sh">Delete files</a>"
