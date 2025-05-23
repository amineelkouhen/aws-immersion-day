import boto3
import json
from botocore.exceptions import ClientError

# Set the AWS Region
region = "us-east-1"

# Initialize the Bedrock Runtime client
client = boto3.client("bedrock-runtime", region_name=region)

# Define the model ID for Amazon Titan Text Premier
model_id = "amazon.titan-text-express-v1"

# Define the input prompt
prompt = """
Command: Compose an email from Amine, A Partner Solution Architect at Cockroach Labs, to the Partner team at "AWS" about setting up a GenAI workshop called 'immersion days' """

# Configure inference parameters
inference_parameters = {
    "inputText": prompt,
    "textGenerationConfig": {
        "maxTokenCount": 512,  # Limit the response length
        "temperature": 0.5,    # Control the randomness of the output
    },
}

# Convert the request payload to JSON
request_payload = json.dumps(inference_parameters)

try:
    # Invoke the model
    response = client.invoke_model(
        modelId=model_id,
        body=request_payload,
        contentType="application/json",
        accept="application/json"
    )

    # Decode the response body
    response_body = json.loads(response["body"].read())

    # Extract and print the generated text
    generated_text = response_body["results"][0]["outputText"]
    print("Generated Text:\n", generated_text)

except ClientError as e:
    print(f"ClientError: {e.response['Error']['Message']}")
except Exception as e:
    print(f"An error occurred: {e}")