import boto3
import json


def lambda_handler(event, context):
    # Ambil detail event dari CloudWatch Event
    detail = event['detail']

    # Cek event type
    event_type = detail['eventName']

    # Identifikasi instance EC2
    instance_id = detail['resources'][0].split('/')[-1]

    # Inisialisasi client EC2
    ec2_client = boto3.client('ec2', region_name='your_region')

    sns_topic_arn = 'arn:aws:sns:your_region:your_account_id:your_sns_topic'

    if event_type == 'StopInstances':
        # Matikan EC2
        ec2_client.stop_instances(InstanceIds=[instance_id])
        send_sns_notification(
            sns_topic_arn, f"EC2 instance {instance_id} has been stopped.")

    elif event_type == 'CreateImage':
        # Lakukan replikasi
        ami_id = detail['responseElements']['instancesSet']['items'][0]['imageId']
        new_instance_id = replicate_instance(ami_id)
        send_sns_notification(
            sns_topic_arn, f"Replicated instance {instance_id} with new instance {new_instance_id}.")

    elif event_type == 'ModifyInstanceAttribute':
        # Ubah tipe mesin
        new_instance_type = 'your_new_instance_type'
        modify_instance_type(instance_id, new_instance_type, new_volume_size="You size")
        send_sns_notification(
            sns_topic_arn, f"Modified instance type for instance {instance_id}.")

    elif event_type == 'StartInstances':
        # Nyalakan EC2
        ec2_client.start_instances(InstanceIds=[instance_id])
        send_sns_notification(
            sns_topic_arn, f"EC2 instance {instance_id} has been started.")

    elif event_type == 'ModifyTraffic':
        # Pindah traffic
        modify_traffic(instance_id, new_security_group_id="yourSecurtyGroupId")
        send_sns_notification(
            sns_topic_arn, f"Modified traffic for instance {instance_id}.")

    # Log atau lakukan tindakan lain sesuai kebutuhan
    print(f"Event type: {event_type} for instance {instance_id}")
    return {
        'statusCode': 200,
        'body': 'Script executed successfully'
    }


def send_sns_notification(topic_arn, message):
    sns_client = boto3.client('sns', region_name='your_region')
    sns_client.publish(TopicArn=topic_arn, Message=message)


def replicate_instance(ami_id, instance_type="t2.micro"):
    ec2_client = boto3.client('ec2', region_name="region name")
    response = ec2_client.run_instances(
        ImageId=ami_id,
        InstanceType=instance_type,
        MinCount=2,
        MaxCount=2
    )

    # Buat dua instance baru (replicas)
    replication_instances = ec2_client.create_instances(**response)

    # Dapatkan instance IDs dari instance baru yang telah dibuat
    new_instance_ids = [instance.id for instance in replication_instances]
    return new_instance_ids


def modify_instance_type(instance_id, new_instance_type, new_volume_size):
    # Ubah tipe mesin instance
    ec2_client = boto3.client('ec2', region_name='your_region')
    ec2_client.modify_instance_attribute(InstanceId=instance_id, InstanceType={
                                         'Value': new_instance_type})

    response = ec2_client.describe_instances(InstanceIds=[instance_id])
    volume_id = response['Reservations'][0]['Instances'][0]['BlockDeviceMappings'][0]['Ebs']['VolumeId']

    # Modifikasi ukuran volume
    ec2_client.modify_volume(
        VolumeId=volume_id,
        Size=new_volume_size
    )
def modify_traffic(instance_id, new_security_group_id):
    # Inisialisasi client EC2
    ec2_client = boto3.client('ec2', region_name='your_region')

    # Dapatkan informasi grup keamanan yang terkait dengan instance
    response = ec2_client.describe_instances(InstanceIds=[instance_id])
    security_group_id = response['Reservations'][0]['Instances'][0]['SecurityGroups'][0]['GroupId']

    # Ubah grup keamanan untuk instance
    ec2_client.modify_instance_attribute(
        InstanceId=instance_id,
        Groups=[new_security_group_id]
    )
