from aws_cdk import (
    aws_cloudfront as cloudfront,
    aws_lambda as _lambda,
    aws_iam as iam,
    core,
)

class LambdaEdgeStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Define Lambda function
        lambda_fn = _lambda.Function(
            self,
            "MyLambdaEdgeFunction",
            runtime=_lambda.Runtime.PYTHON_3_8,
            code=_lambda.Code.asset("lambda_edge_function"),
            handler="index.handler",
        )

        # Add permission to Lambda function to be invoked by CloudFront
        lambda_fn.add_to_role_policy(
            iam.PolicyStatement(
                actions=["lambda:InvokeFunction"],
                resources=[lambda_fn.function_arn],
                principals=[
                    iam.ServicePrincipal("edgelambda.amazonaws.com"),
                    iam.ServicePrincipal("cloudfront.amazonaws.com"),
                ],
            )
        )

        # Create CloudFront distribution with Lambda@Edge function
        cloudfront.Distribution(
            self,
            "MyDistribution",
            default_behavior=cloudfront.BehaviorOptions(
                origin=cloudfront.S3Origin("my-s3-bucket.s3.amazonaws.com"),
                viewer_protocol_policy=cloudfront.ViewerProtocolPolicy.REDIRECT_TO_HTTPS,
                edge_lambdas=[cloudfront.EdgeLambda(lambda_version=lambda_fn.current_version)]
            )
        )
