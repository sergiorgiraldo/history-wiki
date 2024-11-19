#!/bin/sh

touch "docs/$1.md"
echo "# $1" >> "docs/$1.md"

lnk="\n<li><a href='$1'>$1</a></li>\n<!--NEXT-->"
awk -v lnk="$lnk" '{gsub(/<!--NEXT-->/, lnk)}1' docs/index.html > docs/index.tmp 
mv docs/index.tmp docs/index.html

code "docs/$1.md"