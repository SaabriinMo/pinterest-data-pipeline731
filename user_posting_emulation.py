import awsdb
import requests
from time import sleep
import random
from multiprocessing import Process
import boto3
import json
from sqlalchemy import text
import datetime

random.seed(100)

new_connector = awsdb.AWSDBConnector()

def send_data_to_s3(request_type, invoke_url, dict_results):

    """
    This functions get sends the data (dict_results) to each kafka topics using the API Invoke URL

    Parameters:
    -----------

        request_type: str
            the type of API request made

        invoke_url: str
            the url to send the data to

        dict_results: dict
            the data

    Returns:
    --------
        None

    Raises:
    -------
        requests.exceptions.RequestException: any errors relating to requests.
    """

    for key, value in dict_results.items():
        if type(value) == datetime.datetime:
            dict_results[key] = dict_results[key].strftime("%Y-%m-%d %H:%M:%S")
        
    payload = json.dumps({
    "records": [
        {
        #Data should be send as pairs of column_name:value, with different columns separated by commas       
        "value": dict_results
        }
    ]
})
    print(payload)
    headers = {'Content-Type': 'application/vnd.kafka.json.v2+json'}
    try:
        response = requests.request(request_type, invoke_url, headers=headers, data=payload)
        print(response.status_code)
    except requests.exceptions.RequestException as errex: 
        print("Exception request") 
    




def run_infinite_post_data_loop():
    while True:
        sleep(random.randrange(0, 2))
        random_row = random.randint(0, 11000)
        engine = new_connector.create_db_connector()

        with engine.connect() as connection:

            pin_string = text(f"SELECT * FROM pinterest_data LIMIT {random_row}, 1")
            pin_selected_row = connection.execute(pin_string)
            
            for row in pin_selected_row:
                pin_result = dict(row._mapping)

            geo_string = text(f"SELECT * FROM geolocation_data LIMIT {random_row}, 1")
            geo_selected_row = connection.execute(geo_string)
            
            for row in geo_selected_row:
                geo_result = dict(row._mapping)

            user_string = text(f"SELECT * FROM user_data LIMIT {random_row}, 1")
            user_selected_row = connection.execute(user_string)
            
            for row in user_selected_row:
                user_result = dict(row._mapping)

            send_data_to_s3("POST", "https://qynzmaevn3.execute-api.us-east-1.amazonaws.com/streaming_test/topics/1232252d77df.pin", pin_result)
            send_data_to_s3("POST", "https://qynzmaevn3.execute-api.us-east-1.amazonaws.com/streaming_test/topics/1232252d77df.geo", geo_result)
            send_data_to_s3("POST", "https://qynzmaevn3.execute-api.us-east-1.amazonaws.com/streaming_test/topics/1232252d77df.user", user_result)



if __name__ == "__main__":
    run_infinite_post_data_loop()
    print('Working')
    
    


