#!/bin/bash

processFile="/var/log/systemusage/process.log"
diskFile="/var/log/systemusage/disk.log"
memoryFile="/var/log/systemusage/memory.log"
loadFile="/var/log/systemusage/load.log"


verifyFile(){
	if [ ! -f $1 ]
	then
		touch $1
	fi
} 

verifyFile $processFile
verifyFile $diskFile
verifyFile $memoryFile
verifyFile $loadFile

logValues(){
	for i in $*
	do
		case $i in 
			$processFile) 
				date +"%a %b %d %T %Y:" >> $i
				top -bn1 -o %CPU | head -n12 | tail -n5 | awk '{print "\t-"$12"\t"$1"\t"$9}' | column -t >> $i ;;
			$diskFile) 
				date +"%a %b %d %T %Y:" >> $i
				df -h | awk '{print $1 " " $5 " " $6}' >> $i ;;
			$memoryFile) 
				free |sed -n '2p' | awk '{print $2 " " $3 " " $4 " " $5 " " $6}'| gawk '{print strftime("%a %b %d %T %Y")":",$0}' >> $i ;;
			$loadFile) 
				cat /proc/loadavg | awk '{print $1 " " $2 " " $3}' | gawk '{print strftime("%a %b %d %T %Y")":",$0}' >> $i ;;
		esac
	done
	
}
logValues $processFile $diskFile $memoryFile $loadFile
