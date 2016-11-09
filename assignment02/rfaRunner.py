'''
Created on Oct 19, 2016
Continued on Nov 4, 2016

@author: sashaalexander, yulia_z
@author: team X, team 3

'''
from rfaUtils import getAppName, getLog, qaPrint, getLocalEnv, getTestCases
import sys
import re

# exit if there are not two command-line arguments 
if len(sys.argv) != 2:
    sys.exit("Testrun must be set as an argument. Proper usage: rfaRunner.py --testrun=42")

# if we want to see command-line argument
print "The second command-line argument is: %s" % sys.argv[1]

# exit if format of accepted command-line argument does't match to required one
# using regular expressions 
matchObj = re.match (r'--testrun=(\d+)', sys.argv[1], re.I)
if matchObj:
    # assigning value of command-line argument as integer to testrun id 
    trid = int(matchObj.group(1))
    # exit if testrun id is not in range (1, 10001)
    if trid not in range(1,10001):
        sys.exit("Testrun value is not in range")
else:
    sys.exit("invalid format of argument: " + sys.argv[1])

# assigning testrun file name where test case parameters are stored
trid_file = str(trid) + ".txt"

# assigning file name where testrun properties are stored
properties_file = "local.properties"
# call getLocalEnv to get dictionary of testrun properties
testrun_properties = getLocalEnv(properties_file)
# exit if dictionary of testrun properties failed
if testrun_properties == -1:
    sys.exit("Unable to open " + properties_file + " file or invalid format of the file content, the required format is key=value.")

# exit if key or value in dictionary does't exist
def usage(key):
    try:
        if testrun_properties[key]:
            return testrun_properties[key]
        else: 
            return sys.exit("Value of " + key + " is not found. Check parameters in " + properties_file + " file." )
    except KeyError:
        return sys.exit("Key " + key + " is not found. Check parameters in " + properties_file + " file." )

# getting the log file handle
log = getLog(usage('log_dir'), getAppName())
# exit if log creation failed
if log == -1:
    sys.exit("Unable to create log file")

# creating list of parameter names
tc_parameter_names = ["rest_URL", "HTTP_method", "HTTP_RC_desired", "param_list"]

message = "It is working, right?"
# call qaPrint to print a message with time stamp and write it to the log file
qaPrint(log, message)
qaPrint(log, "Me like what me see")
# if we want to check how getLocalEnv works
qaPrint(log, "Dictionary of parameters from " + properties_file + " is: %s" % testrun_properties)
# if we want to check how getTestCases works
qaPrint(log, "Dictionary of test cases from " + trid_file + " is: %s" % getTestCases(trid_file, tc_parameter_names))

# close the log file if it's open
if not log.closed:
    log.close()
