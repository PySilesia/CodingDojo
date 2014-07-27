#!/bin/sh

monfile="src.py" #source file with solution
monfile2="test_src.py" #source file with tests
moddate=$(stat -f "%m" $monfile)
moddate2=$(stat -f "%m" $monfile2)


while true
do
	sleep 1
	if [ $(stat -f "%m" $monfile) != $moddate ] || \
	   [ $(stat -f "%m" $monfile2) != $moddate2 ]
	then
			moddate=$(stat -f "%m" $monfile)
			moddate2=$(stat -f "%m" $monfile2)
			
			clear
			nosetests-2.7
	fi	
done
