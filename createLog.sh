#!/bin/bash
# file="portLogs.txt"

# if [ -f $file ] ; then
#     rm $file
# fi


echo "Creating logs for control ports"
#echo "Control Ports\n\n" >> portLogs.txt
sudo netstat -tulpn | grep $1 >> portLogs.txt

echo "Creating logs for Access ports" 
#echo "Acess Ports\n\n" >> portLogs.txt
sudo netstat -tulpn | grep $2 >> portLogs.txt


