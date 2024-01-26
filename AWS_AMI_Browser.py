def get_latest_ami_id(aws_product, key_id, secret, region, filters):
    """Fetch the latest AMI ID from AWS Marketplace."""
    ec2_client = boto3.client(aws_product, aws_access_key_id=key_id,
                              aws_secret_access_key=secret, region_name=region)
    
    # Filter AMIs
    # Adust as needed
    filters = [{'Name': 'name', 'Values': [filters]}]
    response = ec2_client.describe_images(Filters=filters)
    images = response['Images']
    
    # Sort images by creation date and get the latest one
    if not images:
        raise ValueError("No AMIs found matching the filters")
    latest_image = max(images, key=lambda x: x['CreationDate'])
    return latest_image['ImageId']
