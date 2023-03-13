
# Lambda@Edge CDK Python Project

This code defines a LambdaEdgeStack class that extends the core.Stack class from AWS CDK. It creates a Lambda function, adds permission for the CloudFront service to invoke it, and then creates a CloudFront distribution with the Lambda@Edge function attached to the default behavior.

You'll need to replace "my-s3-bucket.s3.amazonaws.com" with the actual domain name of your S3 bucket, and "lambda_edge_function" with the path to the directory containing your Lambda function code.

Hope this helps! Let me know if you have any questions.