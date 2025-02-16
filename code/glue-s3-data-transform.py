import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsgluedq.transforms import EvaluateDataQuality

args = getResolvedOptions(sys.argv, ['JOB_NAME','s3_location','s3_output_location'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

s3_location = args['s3_location']
s3_output_location = args['s3_output_location']

# Default ruleset used by all target nodes with data quality enabled
DEFAULT_DATA_QUALITY_RULESET = """
    Rules = [
        ColumnCount > 0
    ]
"""

# Script generated for node Amazon S3
AmazonS3_node1739709471894 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": [s3_location], "recurse": True}, transformation_ctx="AmazonS3_node1739709471894")

# Script generated for node Amazon S3
EvaluateDataQuality().process_rows(frame=AmazonS3_node1739709471894, ruleset=DEFAULT_DATA_QUALITY_RULESET, publishing_options={"dataQualityEvaluationContext": "EvaluateDataQuality_node1739709437759", "enableDataQualityResultsPublishing": True}, additional_options={"dataQualityResultsPublishing.strategy": "BEST_EFFORT", "observations.scope": "ALL"})
AmazonS3_node1739709527373 = glueContext.write_dynamic_frame.from_options(frame=AmazonS3_node1739709471894, connection_type="s3", format="glueparquet", connection_options={"path": s3_output_location, "partitionKeys": []}, format_options={"compression": "snappy"}, transformation_ctx="AmazonS3_node1739709527373")

job.commit()