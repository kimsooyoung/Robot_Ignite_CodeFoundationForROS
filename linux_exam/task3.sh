#!/bin/bash

cd ~/catkin_ws/src/linux_exam/this/is/my/linux/exam
rm -rf *
touch exam1.py exam2.py exam3.py

chmod 754 exam1.py
chmod 501 exam2.py
chmod 241 exam3.py
