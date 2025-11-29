from aws_cdk import (
    Stack,
    aws_lambda as lambda_,
    aws_apigateway as apigw,
)
from constructs import Construct

class InfrastructureStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        hello_fn = lambda_.Function(
            self,
            "HelloFunction",
            runtime=lambda_.Runtime.PYTHON_3_11,
            handler="hello.handler",
            code=lambda_.Code.from_asset("lambdas"),
        )

        api = apigw.LambdaRestApi(
            self,
            "MyLinkedInLegendAPI",
            handler=hello_fn,
            proxy=True,
        )
