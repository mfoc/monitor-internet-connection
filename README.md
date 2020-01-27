# monitor internet connection
A Python module to monitor the uptime of the Internet connection in real-time and record the time and duration of any downtime.


Sample output
-----------------------------

```
--------------------------------------------------------------
--------------------------------------------------------------
Monitoring Internet Connection commencing : 2020-01-10 10:34:45 polling every 1 second(s)
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
Name: 		monitor_internet_connection

Version: 	1.2.1

Date: 		27th January 2020

Author: 	Martin F. O'Connor

YouTube Channel:  [Martin O'Connor](https://www.youtube.com/channel/UCSmYfqnVlhB418ugEZxudQw)


What is monitor_internet_connection?
---------------------------------------
It is a Python module to monitor the uptime of the Internet connection - that is to say to monitor that an external IP address is always reachable.


Why should I use monitor_internet_connection?
-------------------------------------------------
If you have automated long-running processes/programs/activities on your computer that requires Internet connectivity, there is nothing worse than coming back the next hour/day/week/whenever to review the logs/progress and find out that the program(s) failed or data is missing because of lost Internet connectivity.  What is worse - you may not know exactly when Internet connectivity was lost.  Thus, will you need to rerun the entire program/process? Or just a part of it? and so on.

The Python module `monitor_internet_connection` is a solution to this problem in that it monitors Internet connectivity in real-time, displaying on the console/terminal and recording to a log file: the start time, the end time and the duration of any Internet connectivity downtime. You may simply run this module in a console/terminal and leave it running for days/weeks on end.


What does monitor_internet_connection do?
--------------------------------------------
Every X seconds (default polling frequency is 1 second), the program monitors whether the Internet connection is alive and an external IP address is reachable.

If the Internet is unreachable:

1) The first observed time of failure is logged.

2) Every one-minute interval of subsequent unavailability is logged. The one-minute logs can be useful as a proxy indicator of whether the computer lost power or just the Internet connection was unavailable.

3) When Internet connectivity is restored, the first observed time of restoration is logged.

4) Finally, the total time duration of the Internet unavailability is logged.



Log File
--------------------------------------------

-  The log file is called `internet_monitor.log`.
-  The log file is written to the current working folder.
-  The log file is always appended to, never overwritten.
-  The information written to the log file is also displayed on the console/terminal.

-  The log file may be disabled via a command line parameter.  See Usage below.

Prerequisites
-------------
You must have Python 3.6 or higher installed.


Installation
-------------------------------------------------------------------


```console
pip install monitor_internet_connection
```


QuickStart
-------------------------------------------------------

```console
python -m monitor_internet_connection
```


How do I exit the program
-------------------------------------------------------
To exit the program, simply press `Ctrl-C` inside the console/terminal.  This will cause the program to exit gracefully.

Usage
-------------------------------------------------------

```console
usage: python -m monitor_internet_connection [-h] [-n] [-f N]

Monitor the uptime of the Internet connection and record any downtime

optional arguments:
  -h, --help        show this help message and exit
  -n, --no-logfile  do not create a log file (default: False)
  -f N, --freq N    specify polling frequency in seconds (default: 1)

```

Acknowledgments
---------------
The `is_internet-alive` method was inspired by 7h3rAm's answer on [Stackoverflow](https://stackoverflow.com/questions/3764291/checking-network-connection)


Licence
---------------
This project is licensed under the MIT License - see the LICENSE.md file for details
