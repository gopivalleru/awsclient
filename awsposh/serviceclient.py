import os
from boto3 import client
from collections import defaultdict


class ServiceClient:
    '''creates clients for aws services in multiple regions'''
    def __init__(self, service):
        self.clts = {}
        regions = ["us-east-1", "us-east-2", "us-west-1", "us-west-2"]
        aws_acs_key_id = os.environ['aws_access_key_id']
        aws_sec_acs_key = os.environ['aws_secret_access_key']
        aws_sess_token = os.environ['aws_session_token']
        print(aws_acs_key_id, aws_sec_acs_key, aws_sess_token)

        for region in regions:
            self.clts[region] = client(service,
                                       region,
                                       aws_access_key_id=aws_acs_key_id,
                                       aws_secret_access_key=aws_sec_acs_key,
                                       aws_session_token=aws_sess_token
                                       )

    def get_client(self, region):
        '''Returns client for a particular region'''
        return self.clts[region]
