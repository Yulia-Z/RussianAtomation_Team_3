'''
Created on Oct 19, 2016
Continued on Nov 4, 2016

@author: sashaalexander, yulia_z
@author: team X, team 3

'''
from datetime import datetime
import os
import sys


def getAppName(): 
    app_name = os.path.basename(sys.argv[0]) 
    if app_name.endswith('.py'): 
        app_name = app_name[:-3]
    return app_name
    
    
def getLog(location, filename):
    """
    Creates 'logs' directory, if it doesn't exist,
    creates or opens a log file in 'logs' directory.
    """
    try:
        # if logs directory doesn't exist, create it
        if not os.path.isdir(location):
            os.makedirs(location)
        # open log file with passed filename and timestamp (platform independent) in Append mode
        log = open(os.path.join(location, filename + " " + getCurTime("%Y%m%d_%H-%M") + ".log"), "a")
        return log
    except (OSError, IOError):
        # return -1 in case of exception
        return -1


def qaPrint(log, message):
    """
    Prints 'timestamp + message' to console and writes it to the log file
    """
    # current date and time as string + message. example: [Oct 25 01:52:33.000001] TC1 - Passed
    log_message = getCurTime("[%b %d %H:%M:%S.%f]") + " " + message
    # prints log_message
    print log_message
    # writes message to a log file
    log.write(log_message + "\n")


def getCurTime(date_time_format):
    """
    Returns current date_time as a string formatted according to date_time_format
    """
    date_time = datetime.now().strftime(date_time_format)
    return date_time
    
    
def getLocalEnv(properties_file):
    """ 
    Returns dictionary of parameters from passed file. 
    """
    dict_of_parameters = {}
    try:
        prop_f = open(properties_file, 'r')
        for line in prop_f:
            # removing spaces from beginning and end of the line
            line = line.strip()
            # creating a dictionary if line is not empty
            if line:
                # transforming string to list
                line = line.split('=')
                key = line[0].strip()
                val = line[1].strip()
                dict_of_parameters[key] = val
            # pass empty lines in the file
            else:
                continue
        prop_f.close() 
        return dict_of_parameters
    except (IOError, IndexError):
        return -1 


def getTestCases(trid_file, name_list):
    """
    Returns dictionary from passed file 
    where values are dictionaries where keys are from passed list 
    and values are from passed file
    """
    tc_dict = {}
    try:
        tc_file = open(trid_file, 'r')
        for line in tc_file:
            # removing spaces from beginning and end of the line
            line = line.strip()
            # creating a dictionary if line is not empty
            if line:
                line = line.split('|')
                # getting key which is test case id from line of passed file
                tc_key = int(line[0].strip())
                # getting list of values from the line of the file
                tc_val_list = line[1:]
                # transforming string to list for last item of previous list (line 92)
                tc_val_list[-1] = tc_val_list[-1].strip().split(',')
            # assigning value to key where value is a dictionary received from two lists
            tc_dict[tc_key] = dict(zip(name_list, tc_val_list))
        tc_file.close()
        return tc_dict
    except (IOError, ValueError):
        print "Cannot open " + trid_file + " for reading or invalid format of test case id"
        return -1 
    

