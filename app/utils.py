import boto3

def get_openai_api_key(ssm_client, parameter_path):
    '''Get the OpenAI API key from the SSM Parameter Store'''
    try:
        response = ssm_client.get_parameter(
            Name=parameter_path,
            WithDecryption=True
        )
        return response['Parameter']['Value']
    except ssm_client.exceptions.ParameterNotFound:
        raise Exception(f'Parameter {parameter_path} not found in SSM Parameter Store')