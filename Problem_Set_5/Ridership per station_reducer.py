import sys
import logging

from util import reducer_logfile
logging.basicConfig(filename=reducer_logfile, format='%(message)s',
                    level=logging.INFO, filemode='w')

def reducer():
    '''
    Given the output of the mapper for this exercise, the reducer should PRINT 
    (not return) one line per UNIT along with the total number of ENTRIESn_hourly 
    over the course of May (which is the duration of our data), separated by a tab.
    An example output row from the reducer might look like this: 'R001\t500625.0'

    You can assume that the input to the reducer is sorted such that all rows
    corresponding to a particular UNIT are grouped together.

    Since you are printing the output of your program, printing a debug 
    statement will interfere with the operation of the grader. Instead, 
    use the logging module, which we've configured to log to a file printed 
    when you click "Test Run". For example:
    logging.ninfo("My debugging message")
    '''
    old_key=None
    entries=0
    
    for line in sys.stdin:
        # your code here
        data=line.strip().split("\t")
        
        this_key = data[0]
        count = float(data[1])

        if old_key and old_key != this_key:
            print "{0}\t{1}".format(old_key, entries)
            entries = 0.0
            old_key = None

        old_key = this_key
        entries = entries + count

        if old_key != None:
            print "{0}\t{1}".format(old_key, entries)

        
reducer()
