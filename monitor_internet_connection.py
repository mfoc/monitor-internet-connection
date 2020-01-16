"""
Name:           monitor_internet_connection.py
Author:         Martin F. O'Connor (C)
Description:    Monitor Internet connectivity and record time and duration 
                of any downtime.

How to run:		To run this program from the Console/Terminal, type:
					python monitor_internet_connection.py

Date:           23rd June 2019
Version:        1.0

This program checks every X (5) seconds whether the Internet connection
is alive and an external IP address is reachable.
If the Internet connection is unavailable:
    1. The first observed time of failure is logged. 
    2. Every 1-minute interval of subsequent downtime is logged.
    3. When Internet connectivity is restored, the first observed time of 
       restoration is logged. 
    4. Finally, the total duration of the downtime is logged.


Date:           13th January 2020
Version:        1.1

Added functionality to capture Ctrl-C (and SIGINT) and exit the program
gracefully.


Date:           15th January 2020
Version:        1.1.3

Updates:
    1.  Made available as a public package called 'monitor internet connection'.
        on the Python Package Index https://pypi.org/

    2.  Greatly simplified the installation instructions.
        To install: pip install monitor_internet_connection
        To run:     python -m monitor_internet_connection


Date:           16th January 2020
Version:        1.2.0

Updates:
    1. Added the argparse library.
    2. Added command line option to display a help message.
    3. Added command line option to disable the logfile.
       With this option, no write-access to disk is required.
    4. Added command line option to specify the polling frequency in seconds.
       There are nine options available [1, 2, 3, 4, 5, 10, 20, 30, 60].
    5. When logfile is enabled, verify logfile can be created
       in current working folder.
"""

import time
import datetime
import socket
import os
import signal
import argparse
import sys

# If enabled, the log file will be created in the current working folder.
log_filename = "internet_monitor.log"
file = os.path.join(os.getcwd(), log_filename)


def parse_args(args=sys.argv[1:]):
    """Parse arguments."""

    parser = argparse.ArgumentParser(
        description="Monitor the uptime of the Internet connection and record any downtime",
        prog='python -m monitor_internet_connection')

    parser.add_argument("-n", "--no-logfile", dest='disable_logfile',
                   help="do not create a logfile",
                   action="store_true")

    parser.add_argument("-f", "--freq", dest="polling_freq", metavar="N",
                   default=1,
                   type=int,
                   choices=[1, 2, 3, 4, 5, 10, 20, 30, 60],
                   help="specify polling frequency in seconds")

    return parser.parse_args(args)



def is_internet_alive(host="8.8.8.8", port=53, timeout=3):
    """Check if Internet Connection is alive and external IP address is reachable.

    Input Parameters:
        host: (string) 8.8.8.8 (google-public-dns-a.google.com)
        port: (integer) (53/tcp DNS Service).
        timeout: (float) timeout in seconds.

    Returns:
        True (Boolean) if external IP address is reachable.
        False (Boolean) if external IP address is unreachable.
    """

    try:
        socket.setdefaulttimeout(timeout)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        return True
    except OSError as error:
        # print(error.strerror)
        return False
    else:
        s.close()
        return True


def calc_time_diff(start, end):
    """ Calculate duration between two times and return as HH:MM:SS

    Input Params:
        start and end times
        both datetime objects created from datetime.datetime.now()

    Returns:
        The duration (string) in the form HH:MM:SS
    """

    time_difference = end - start
    secs = str(time_difference.total_seconds())
    return str(datetime.timedelta(seconds=float(secs))).split(".")[0]


def signal_handler(signal_received, frame):
    """ Capture Ctrl-C (or SIGINT) and exit the program gracefully. 

    Input Params:
        signal_received (integer) is the signal number captured and received.
        frame (frame object) is the current stack frame.

    Returns:
        This method exits the program, thus nothing is returned.
    """

    # Display exit message to console and record in log file.
    exit_time = datetime.datetime.now()
    exit_msg = "Monitoring Internet Connection stopped at : " + exit_time.strftime("%Y-%m-%d %H:%M:%S")
    print(exit_msg)

    if enable_logfile:
        with open(file, 'a') as writer:
            writer.write(exit_msg + "\n")

    sys.exit()


def verify_write_access():
    """ Verify the logfile can be created in the current working folder"""

    if enable_logfile:
        try:
            with open(file, 'a') as writer:
                pass
        except OSError as err:
            print("Unable to create logfile in current working folder. Exiting program.")
            sys.exit()
        finally:
            pass



def monitor_inet_connection(enable_logfile = True, polling_freq = 1):
    """ Monitor internet connection indefinitely."""

    # Capture the Ctrl-C (or SIGINT) signal to permit the program to exit gracefully.
    signal.signal(signal.SIGINT, signal_handler)

    if enable_logfile:
        verify_write_access()

    # Write to log file when Internet monitoring commences.
    now = datetime.datetime.now()
    # msg = "Monitoring Internet Connection commencing: " + now.strftime("%Y-%m-%d %H:%M:%S")
    msg = "Monitoring Internet Connection commencing : " + str(now).split(".")[0] + \
            " polling every " + str(polling_freq) + " second(s)"
    print(msg)

    if enable_logfile:
        with open(file, 'a') as writer:
            writer.write("--------------------------------------------------------------\n")
            writer.write("--------------------------------------------------------------\n")
            writer.write(msg + "\n")

    while True:
        # When run on cmd line, exit program via Ctrl-C.
        if is_internet_alive():
            time.sleep(polling_freq)
        else:
            # Record observed time when internet connectivity fails.
            fail_time = datetime.datetime.now()
            msg = "-------Internet Connection unavailable at : " + str(fail_time).split(".")[0]
            print(msg)
            if enable_logfile:
                with open(file, 'a') as writer:
                    writer.write(msg + "\n")

            # Check every 1 second to see if internet connectivity restored.
            counter = 0
            while not is_internet_alive():
                time.sleep(1)
                counter += 1
                # For each minute of downtime, log it.
                # The one-minute logs can be useful as a proxy to indicate whether the computer lost power,
                # or just the internet connection was unavailable.
                if counter >= 60:
                    counter = 0
                    now = datetime.datetime.now()
                    msg = "-----------Internet Connection still unavailable at : " + str(now).split(".")[0]
                    print(msg)
                    if enable_logfile:
                        with open(file, 'a') as writer:
                            writer.write(msg + "\n")

            # Record observed time when internet connectivity restored.
            restore_time = datetime.datetime.now()
            restore_msg = "-------Internet Connection restored at    : " + str(restore_time).split(".")[0]

            # Calculate the total duration of the downtime
            downtime_duration = calc_time_diff(fail_time, restore_time)
            duration_msg = "-------The duration of the downtime was   :             " + downtime_duration

            # Display restoration message to console and record in log file.
            print(restore_msg)
            print(duration_msg)
            if enable_logfile:
                with open(file, 'a') as writer:
                    writer.write(restore_msg + "\n")
                    writer.write(duration_msg + "\n")



if __name__ == "__main__":
    args = parse_args()

    enable_logfile = not args.disable_logfile
    monitor_inet_connection(enable_logfile, args.polling_freq)


