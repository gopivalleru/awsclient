from awsposh.ec2ops import EC2Ops
import cacheclient
import pickle
from collections import defaultdict


def _get_desc_insts(ec2client):
        ec2_read = EC2Ops(ec2client)
        # creating cache client
        cache_cli = cacheclient.CacheClient(host='localhost', port=6379)
        ec2_des_insts = cache_cli.get('ec2_des_insts')
        # if not found it cache then get instances data from aws and dump the
        # data into cache in binary format.
        if ec2_des_insts is None:
            print("in if loop")
            ec2_des_insts = ec2_read.des_insts()
            cache_cli.set("ec2_des_insts", pickle.dumps(ec2_des_insts))
        else:
            ec2_des_insts = pickle.loads(ec2_des_insts)
        return ec2_des_insts


class EC2Get:
    def __init__(self, ec2client):
        self.ec2client = ec2client
        self.ec2_des_insts = _get_desc_insts(self.ec2client)

    def desc_insts(self):
        return self.ec2_des_insts

    def apply_filter(self, filter=None):
        '''Yet to create'''
        ec2_tags_instances = defaultdict(list)
        for reservation in self.ec2_des_insts["Reservations"]:
            for instance in reservation["Instances"]:
                if "Tags" in instance:
                    tag_Cluster = 'none'
                    tag_Name = 'none'
                    for tag in instance["Tags"]:
                        if tag["Key"] == "Cluster":
                            tag_Cluster = tag["Value"]
                        elif tag["Key"] == "Name":
                            tag_Name = tag["Value"]
                    ins = {instance["InstanceId"]: tag_Name}
                    ec2_tags_instances[tag_Cluster].append(ins)
        print(ec2_tags_instances['none'])

