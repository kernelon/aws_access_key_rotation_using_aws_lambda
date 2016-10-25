#import boto3
import boto3

#import boto3 session
import boto3.session

#import threading
import threading

class Aws_Iam(threading.Thread):
    def list_Iam_Users_With_Access_Key(self):
	session = boto3.session.Session()
	iam = session.resource('iam')
	for user in iam.users.all():   
           for key in user.access_keys.all():
		AccessId = key.access_key_id
		Status = key.status
		if (Status == "Active"):
		    print ("User: ", user.user_name, "Key: ",  AccessId,  "Active")
                else:
		    print ("User: ",  user.user_name, "Key: ",  AccessId,  "InActive")

#	   access_key = iam.AccessKey(users.user_name, users.user_id)
#	   print(access_key.status)
# 	   if access_key.status == Active :
#	       print(users.user_name)
		

a = Aws_Iam()
a.list_Iam_Users_With_Access_Key()

#List all users with access key.
#Create a second access key in addition to the one in use.
#Email all users with new access key and the expiry day of the previous access key.
#Update all your applications to use the new access key and validate that the applications are working.
#Change the state of the previous access key to inactive.
#Validate that your applications are still working as expected.
#Delete the inactive access key.
