import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

def delete_default_vpc(region_name):
    try:
        ec2 = boto3.client('ec2', region_name=region_name)

        # Find the default VPC
        response = ec2.describe_vpcs(Filters=[{'Name': 'isDefault', 'Values': ['true']}])
        if not response['Vpcs']:
            print(f"No default VPC found in region {region_name}.")
            return

        vpc_id = response['Vpcs'][0]['VpcId']
        print(f"Default VPC found: {vpc_id}")

        # Delete the VPC
        # First, delete all subnets
        subnets = ec2.describe_subnets(Filters=[{'Name': 'vpc-id', 'Values': [vpc_id]}])['Subnets']
        for subnet in subnets:
            ec2.delete_subnet(SubnetId=subnet['SubnetId'])
            print(f"Deleted subnet: {subnet['SubnetId']}")

        # Delete internet gateways
        igws = ec2.describe_internet_gateways(Filters=[{'Name': 'attachment.vpc-id', 'Values': [vpc_id]}])['InternetGateways']
        for igw in igws:
            ec2.detach_internet_gateway(InternetGatewayId=igw['InternetGatewayId'], VpcId=vpc_id)
            ec2.delete_internet_gateway(InternetGatewayId=igw['InternetGatewayId'])
            print(f"Deleted internet gateway: {igw['InternetGatewayId']}")

        # Delete route tables
        rtbs = ec2.describe_route_tables(Filters=[{'Name': 'vpc-id', 'Values': [vpc_id]}])['RouteTables']
        for rtb in rtbs:
            if not any([assoc['Main'] for assoc in rtb['Associations']]):
                ec2.delete_route_table(RouteTableId=rtb['RouteTableId'])
                print(f"Deleted route table: {rtb['RouteTableId']}")

        # Delete security groups
        sgs = ec2.describe_security_groups(Filters=[{'Name': 'vpc-id', 'Values': [vpc_id]}])['SecurityGroups']
        for sg in sgs:
            if sg['GroupName'] != 'default':
                ec2.delete_security_group(GroupId=sg['GroupId'])
                print(f"Deleted security group: {sg['GroupId']}")

        # Finally, delete the VPC
        ec2.delete_vpc(VpcId=vpc_id)
        print(f"Deleted VPC: {vpc_id}")

    except NoCredentialsError:
        print("Error: No AWS credentials found. Please configure your AWS credentials.")
    except PartialCredentialsError:
        print("Error: Incomplete AWS credentials found. Please check your AWS credentials.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    region_name = 'us-east-1'  # Specify the region where your default VPC is located
    delete_default_vpc(region_name)

