# THIS IS IN PROD ENVIRONMENT
from flask import Flask, request
import boto3
import os
import time
import redis



#ACCESS_KEY = os.environ['AWS_ACCESS_KEY_ID'] # We used this in the DEV and not for PROD
#SECRET_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
REDIS_HOST= os.environ['REDIS_HOST']
REDIS_PORT= os.environ['REDIS_PORT']

def client_method(service,region):
    #client = boto3.client(service,'''aws_access_key_id=ACCESS_KEY,aws_secret_access_key=SECRET_KEY,''' region_name=region)
    return "received the values outside "+ str(service)+" " + str(region)

client = boto3.client('s3',region_name='us-east-1')#,'''aws_access_key_id=ACCESS_KEY,aws_secret_access_key=SECRET_KEY,''' region_name='us-east-1')
client_ec2 = boto3.client('ec2',region_name='us-east-1')#,'''aws_access_key_id=ACCESS_KEY,aws_secret_access_key=SECRET_KEY,''' region_name='us-east-1')
#print(client)
app = Flask(__name__)

cache =  redis.Redis(host=REDIS_HOST,port=REDIS_PORT)
print(time.time())
cache.set('users:test','lang: python, born:1990')
#print(cache.get('WS39d962103'))
def get_hit_count():
    tries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exec:
            if tries == 0:
                raise exec
            tries -= 1
            time.sleep(0.5)
def set_chache_data(ws_no,service,region):
    cache.set(ws_no,'service: '+service+', region:' + region)

def get_cached_data(ws_no):
    return cache.get(ws_no)

@app.route("/requests", methods=['GET', 'POST'])
def ws_requests():
    ws_no = str(request.args.get('ws_no'))
    service = str(request.args.get('service'))
    region = str(request.args.get('region'))
    data = get_cached_data(ws_no)
    if request.method == 'POST':
        if data == None:
            set_chache_data(ws_no,service,region)
            return "POST Method RECEIVED for "+ws_no
        else:
            return "Data exists for {} with details {}".format(ws_no,data)
    else:
        return "The else statement is for GET, which can be removed"

@app.route("/", methods=['GET', 'POST'])
def hello():
    count = get_hit_count()
    if request.method == 'POST':
        return "POST METHOD RECEIVED"
    else:
        return "MY FIRST Flask API inside docker, and I have seen {} times".format(count)

@app.route("/admin")
def admin():
    service = request.args.get('service')
    region = request.args.get('region')
    print("type service  ",type(service))
    my = client_method(service,region)
    return 'Values returned '+ str(service) +" "  + str(region)+" " +str(my)

@app.route("/list-buckets")
def buckets():
    print("Inside List buckets")
    response = client.list_buckets()
    print("#####################")
    return str(response)

@app.route("/compute-details")
def ec2():
    response = client_ec2.describe_instances()
    return str(response)

#print(str(buckets()))
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
