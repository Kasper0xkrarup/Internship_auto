#!/bin/bash

while true; do
    # Download the Excel file using cURL
    curl -o test.xlsx "https://pms.laerepladsen.dk/api/export/soeg-opslag/Data-%20og%20kommunikationsuddannelsen/-1/s%C3%B8geresultat.xlsx?fritekst=&aftaleFilter=alle&medarbejdereFilter=alle&latitude=&longitude=&afstand="

    # Convert the downloaded Excel file to CSV using xlsx2csv
    xlsx2csv -a 'test.xlsx' > output.csv

    # Read the contents to find the keyword, if found execute python script
    cat output.csv |  grep 'DANSK MIL' > ja.csv
    if grep -wq 'Ja' ja.csv; then
        python3 /home/pi/cv/sendcv.py
        echo 'Så er der nyt'
    fi

    # output to test.log with text and time of execute
    echo -n 'running sleeping 8 houres --  ' | tee -a test.log && date | tee -a test.log
    # Sleep for 8 hours (28800 seconds) before repeating the loop
    sleep 28800
done
