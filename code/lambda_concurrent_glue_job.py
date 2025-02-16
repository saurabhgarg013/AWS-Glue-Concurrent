import boto3

def lambda_handler(event, context):
    glue_client = boto3.client('glue')

    # Get S3 paths from EventBridge event
    input_s3 = event.get("s3_location", "s3://techno-data-bucket/emp/")
    output_s3 = event.get("s3_output_location", "s3://techno-data-bucket/output/emp/")


    response = glue_client.start_job_run(
        JobName="Mygluejob-16",
        Arguments={
            "--s3_location": input_s3,
            "--s3_output_location": output_s3
        }
    )

    return {
        "JobRunId": response["JobRunId"],
        "Message": "Glue job started successfully"
    }
