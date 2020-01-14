# Monitor-Internet-Connection
A Python program to monitor Internet connectivity and record the time and duration of any downtime.

Name: 		monitor-internet-connection.py

Version: 	1.1

Date: 		13-January-2020

Author: 	Martin F. O'Connor

YouTube Channel:  [Martin O'Connor](https://www.youtube.com/channel/UCSmYfqnVlhB418ugEZxudQw)


What is monitor-internet-connection.py?
---------------------------------------
It is a simple Python program to monitor Internet connectivity - that is to say to monitor that an external IP address is always reachable.

Why should you use monitor-internet-connection.py?
-------------------------------------------------
If you have any automated long-running process/program/activity on your computer that requires Internet connectivity, there is nothing worse that coming back the next hour/day/week/whenever to review the logs/progress and find out that the program failed or data is missing because of lost Internet connectivity.  What is worse - you may not know exactly when internet connectivity was lost.  Thus, will you need to rerun the entire program or just a part of it and so on.

The program monitor-internet-connection.py is a solution to that problem in that it gives you precise and specific knowledge concerning the uptime and downtime of Internet Connectivity.  You may simply run this program in a console/terminal and leave it running for days/weeks on end.


What does monitor-internet-connection.py do?
--------------------------------------------
This program monitors every 5 seconds whether the Internet connection is alive and an external IP address is reachable.

If the Internet is unreachable:

1) The first observed time of failure is logged. 

2) Every 1-minute interval of subsequent unavailability is logged. The one-minute logs can be useful as a proxy indicator of whether the computer lost power or just the internet connection was unreachable.

3) When Internet connectivity is restored, the first observed time of restoration is logged. 
    
4) Finally, the total duration of the Internet unavailability is logged.

The log file internet_monitor.log is always appended to, never overwritten.  The information written to the log file is also displayed on the console/terminal.

Prerequisites
-------------
1) You must have Python 3 installed.  To determine what version of Python you have installed (if any), you may visit [check-python-version](https://phoenixnap.com/kb/check-python-version) and follow the instructions therein.


How do I run the program monitor-internet-connection.py
-------------------------------------------------------
1) Download the monitor-internet-connection.py program to your chosen current working folder.  
   NOTE: This program requires write-access to the current working folder in order to create and store the log file internet_monitor.log.
   Nothing else is written to your folder.

2) Open up a command line console/terminal and ensure the folder is set to your chosen current working folder

3) Run the following command in the terminal/console:
    `python monitor-internet-connection.py`


How do I exit the program monitor-internet-connection.py
-------------------------------------------------------
To exit the program, simply press `Ctrl-C` inside the console/terminal.  This will cause the program to exit gracefully.


Acknowledgments
---------------
The `is_internet-alive` method was inspired by 7h3rAm's answer on [Stackoverflow](https://stackoverflow.com/questions/3764291/checking-network-connection)
