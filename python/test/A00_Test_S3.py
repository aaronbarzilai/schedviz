#######################################################################
#	A00_Test_S3.py
#
#	Testing can interact with AWS programmatically
########################################################################

from __future__ import print_function
import time, datetime

import boto3 # For Amazon



if __name__ == "__main__":
	try:
		print("Running main")
		print("Now",datetime.datetime.now(),"\n")
		start_time=time.time()

		################################################ Main code starts here ################################################
		
		# Let's use Amazon S3
		s3 = boto3.resource('s3')

		# Print out bucket names
		for bucket in s3.buckets.all():
		    print(bucket.name)

		################################################ Main code ends here ################################################
		
	except:
		print(traceback.format_exc())
		print("There was an error at",datetime.datetime.now())
	finally:
		end_time = time.time()
		print("\nEnd at",datetime.datetime.now(),"\n")
		print("{0:.3f} secs elapsed, or {1:.3f} mins or {2:.3f} hours\n" \
			.format(end_time-start_time,(end_time-start_time)/60.0,(end_time-start_time)/(60.0*60.0)))