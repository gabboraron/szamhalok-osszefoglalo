#!/usr/bin/python
#beadando 1
import json
import subprocess
import sys


def print_command_output(output):
	tmp = output.splitlines()
	#print("tmp"+ str(tmp))					#print the full array
	#print("size of tmp: " + str(len(tmp)))	#print the size of array
	for line in tmp:
		print(str(line).strip())


########
# PING #
########

p = subprocess.Popen(["ping","-c",  "5", "google.com"], stdout= subprocess.PIPE)
ping_output = p.communicate()[0]
#print(output)
print_command_output(ping_output)


###########
# TRACERT #
###########

pp = subprocess.Popen(["traceroute","-m",  "30", "google.com"], stdout= subprocess.PIPE)
tracert_otput = pp.communicate()[0]
print("tracert")
print_command_output(tracert_otput)
