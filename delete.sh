#!/bin/bash

OUTPUT="$(date)"
echo "Content-type: text/html"
echo ""

echo "<html><head><title>Files deleted</title></head><body>"
echo "Today is $OUTPUT <br />"
rm result.pdf result.aux result.log
echo "Thank you for cleaning up.<br />"
echo "<a href="form.html">Create another document</a>"
