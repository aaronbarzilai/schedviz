#######################################################################
#	A01_Test_S3_With_Lambda.py
#
#	Testing can interact with AWS programmatically
########################################################################

from __future__ import print_function
import time, datetime
import traceback

import boto3 # For Amazon
import json



def main():
	try:
		print("Running main")
		print("Now",curr_est_time_as_string(),"EST (UTC-5)\n")
		
		start_time=time.time()

		################################################ Main code starts here ################################################
		
		# Let's use Amazon S3
		s3 = boto3.resource('s3')

		# Print out bucket names
		for bucket in s3.buckets.all():
		    print(bucket.name)

		# Let's make a made up file and put it on the bucket
		filecontent = "<!DOCTYPE html>\n<html>\n<body>\n"
		filecontent = filecontent + "Generated this content at " + curr_est_time_as_string() + " EST (UTC-5) programmatically with AWS lambda."
		filecontent = filecontent + "</body></html>"

		s3.Bucket('schedviz.com').put_object(Key='testfilelambda.html', Body=filecontent,ContentType='text/html')

		################################################ Main code ends here ################################################
		
	except:
		print(traceback.format_exc())
		print("There was an error at",curr_est_time_as_string(),"EST (UTC-5)\n")
	finally:
		end_time = time.time()
		print("\nEnd at",curr_est_time_as_string(),"EST (UTC-5)\n")
		print("{0:.3f} secs elapsed, or {1:.3f} mins or {2:.3f} hours\n" \
			.format(end_time-start_time,(end_time-start_time)/60.0,(end_time-start_time)/(60.0*60.0)))

def first_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    main()
    return True
    #return event['key1']  # Echo back the first key value
    #raise Exception('Something went wrong')

def curr_est_time_as_string():
	dt = datetime.datetime.utcnow() - datetime.timedelta(hours=5)
	dt_string = dt.strftime('%Y-%m-%d %H:%M:%S')
	#print(dt_string)
	return dt_string

if __name__ == "__main__":
	main()
	