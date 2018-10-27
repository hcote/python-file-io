#!/bin/bash
# Practice. My first script

echo $PWD
echo {1..3}
declare -i d=123
echo $d
echo $MACHTYPE

a='hello'
b='world'
c=$a$b
echo $c # returns helloworld
echo ${#a} # returns 5 (length of string)
d=${c:3} 
echo $d # returns sub string of c starting at index 3 (zero indexed)
echo ${c:3:4} # returns substring starting at index three and going 4 indexes over
# can also do ${c: -3} to start at end of string

