#Q.1 Create a log creator

import logging
from os import path

# Taking the path of the current working directory
cur_dir = path.dirname(__file__)

# Join the log file with the path
filename = path.join(cur_dir,"User_Input_Logger.log")

# Change the Log Format to (Time message Type)
LOGGING_FORMAT = "%(asctime)s  Message:%(message)s  Type:%(levelname)s"

# Assign DEBUG level to the logging preference
logging.basicConfig(filename = filename,level = logging.DEBUG,

# Log creation in append mode
filemode = "a",format = LOGGING_FORMAT,)

logger = logging.getLogger()

print ("\nLog Message Type:\n1.CRITICAL\n2.ERROR\n3.WARNING\n4.DEBUG\n5.INFO")

repeat = "Y"
while(repeat == "Y" or repeat == "y"):
	mssg_type = int(input("Enter your choice - "))
	if (mssg_type >= 1 and mssg_type <=5):
		message = str(input("Enter the message: "))
		if (mssg_type == 1):
			logger.critical(message)
		elif (mssg_type == 2):
			logger.error(message)
		elif (mssg_type == 3):
			logger.warning(message)
		elif (mssg_type == 4):
			logger.debug(message)
		elif (mssg_type == 5):
			logger.info(message)
		print ("Message successfully Logged")
	else:
		print ("INVALID CHOICE")
	rep = str(input("\nLog another entry?\nPress Y for Yes or N for No: "))
	if (rep == "N" or rep == "n"):
		break