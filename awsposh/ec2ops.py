import boto3


class EC2Ops:
    '''Read operations on EC2. This class take ec2 client as input
        :
    '''
    def __init__(self, clt):
        self.client = clt

    def des_insts(self, filters=None):
        '''returns ec2 client describe_instances for a provided region'''
        if filters is None:
            return self.client.describe_instances()
        else:
            return self.client.describe_instances(Filters=filters)
