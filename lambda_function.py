import boto3
from datetime import datetime

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')

    instance_id = event.get('detail', {}).get('instance-id')

    if instance_id:
        print(f"Triggered by EC2 instance: {instance_id}")
    else:
        print("No instance-id found in event. Running in manual mode.")
        
        # Optional: fallback instance ID for testing
        #instance_id = 'i-xxxxxxxxxxxxxxxxx'
        #print(f"Using test instance: {instance_id}")

    current_date = datetime.utcnow().strftime('%Y-%m-%d')

    # Apply tags
    ec2.create_tags(
        Resources=[instance_id],
        Tags=[
            {'Key': 'CreatedOn', 'Value': current_date},
            {'Key': 'Environment', 'Value': 'Dev'}
        ]
    )

    print(f"✅ Tagged instance {instance_id}")

    return {
        'statusCode': 200,
        'body': f"Tagged {instance_id}"
    }
