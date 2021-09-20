#!/bin/bash
putty -load dot &
cd /home/pi/Desktop
python3 run_main1_v913.py dot.txt
