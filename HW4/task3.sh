#!/bin/bash
cat titanic.csv | \
awk -F, '$3 == 2 && $7 == "S" {print $0}' | \
sed 's/male/M/g; s/female/F/g' | \
awk -F, 'BEGIN {sum=0; count=0} {if($6 != "") {sum+=$6; count+=1}} END {if(count>0) print "Average Age: " sum/count}'