# Monitor-Internet-Connection
A Python program to monitor Internet connectivity and record the time and duration of any downtime.


Logfile/Console Sample output
-----------------------------

```
--------------------------------------------------------------
--------------------------------------------------------------
Monitoring Internet Connection commencing : 2020-01-10 10:34:45
-------Internet Connection unavailable at : 2020-01-11 07:35:01
-------Internet Connection restored at    : 2020-01-11 07:35:10
-------The duration of the downtime was   :             0:00:09
-------Internet Connection unavailable at : 2020-01-12 08:35:20
-------Internet Connection restored at    : 2020-01-12 08:36:27
-------The duration of the downtime was   :             0:01:07
Monitoring Internet Connection stopped at : 2020-01-13 12:42:38
```

Overview
--------
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
If you have an automated long-running process/program/activity on your computer that requires Internet connectivity, there is nothing worse than coming back the next hour/day/week/whenever to review the logs/progress and find out that the program failed or data is missing because of lost Internet connectivity.  What is worse - you may not know exactly when Internet connectivity was lost.  Thus, will you need to rerun the entire program? Or just a part of it? and so on.

The program `monitor-internet-connection.py` is a solution to that problem in that it both displays on the console/terminal and logs to a logfile, precise and specific details concerning the availability and unavailability of Internet Connectivity.  You may simply run this program in a console/terminal and leave it running for days/weeks on end.


What does monitor-internet-connection.py do?
--------------------------------------------
Every 5 seconds, the program monitors whether the Internet connection is alive and an external IP address is reachable.

If the Internet is unreachable:

1) The first observed time of failure is logged. 

2) Every one-minute interval of subsequent unavailability is logged. The one-minute logs can be useful as a proxy indicator of whether the computer lost power or just the Internet connection was unavailable.

3) When Internet connectivity is restored, the first observed time of restoration is logged. 
    
4) Finally, the total time duration of the Internet unavailability is logged.

Note:

-  The log file `internet_monitor.log` is always appended to, never overwritten.  
-  The information written to the log file is also displayed on the console/terminal.

Prerequisites
-------------
1) You must have Python 3 already installed.  To determine what version of Python you have installed (if any), you may visit [check-python-version](https://phoenixnap.com/kb/check-python-version) and follow the instructions therein.


How do I download/install the program monitor-internet-connection.py
-------------------------------------------------------------------

1)  Download using Git from the console/terminal to your current working folder (to which you have write access).
```console
git clone https://github.com/mfoc/Monitor-Internet-Connection
```

2)  From the current working folder in the console/terminal, change to the `Monitor-Internet-Connection` folder.
```console
cd Monitor-Internet-Connection
```

OR

1) Download via your Internet Browser by selecting the `Clone or Download` button on the [Monitor-Internet-Connection github repository page](https://github.com/mfoc/Monitor-Internet-Connection) and then selecting `Download zip`.  Save the zip file to your current working folder and extract it there.

2)  From the current working folder in the console/terminal, change to the `Monitor-Internet-Connection-master` folder.
```console
cd Monitor-Internet-Connection-master
```


How do I run the program monitor-internet-connection.py
-------------------------------------------------------
Run the following command in the console/terminal.

```console
python monitor-internet-connection.py
```

How do I exit the program monitor-internet-connection.py
-------------------------------------------------------
To exit the program, simply press `Ctrl-C` inside the console/terminal.  This will cause the program to exit gracefully.


Acknowledgments
---------------
The `is_internet-alive` method was inspired by 7h3rAm's answer on [Stackoverflow](https://stackoverflow.com/questions/3764291/checking-network-connection)


Licence
---------------
This project is licensed under the MIT License - see the LICENSE.md file for details
