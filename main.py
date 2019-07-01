from awsposh.serviceclient import ServiceClient
from awsposh.ec2ops import EC2Ops
import json
import pickle
from collections import defaultdict
from cacheclient import CacheClient
import ec2get

EC2_FILTER_TAG_CLUSTER_APP = [
        {
            'Name': 'tag:Cluster',
            'Values': ['ApiApp', 'WebApp', 'UploadApp']
        },
    ]


def main():
    # creating ec2 clients and then getting client for a region
    ec2_clients = ServiceClient('ec2')
    ec2_client = ec2_clients.get_client('us-west-2')
    ec2_g = ec2get.EC2Get(ec2_client)
    ec2_des_insts = ec2_g.desc_insts()
    print(ec2_g.apply_filter())

if __name__ == "__main__":
    main()
