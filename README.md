# Container Accelerator

AWS CDK Example of Docker container deploy in AWS Infrastructure as Fargate Service.

## Pre-requirements

1. Have Docker service  installed and running.

2. Configure AWS credentials.

3. Create Public HostedZone in AWS Ruote53.

4. Create `.env` file in `deploy` directory based on `.env.sample` file and configure variables.

5. Install AWS CDK.

    https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html

    ```bash
    npm install -g aws-cdk
    ```

6. Bootstrap CDK if it is not bootstrapped.

    ```bash
    cdk bootstrap
    ```

## Application

Application is a simple Python Streamlit application that runs on 80 port.

Can be run locally with Docker.

```bash
docker compose build
docker compose up
```

## Deploy

1. Clone repository.

2. Install dependencies.

    ```bash
    pip install -r requirements.txt
    ```

3. Run deployment in `deploy` directory.

    ```bash
    cdk deploy
    ```

## Deploy Example

```bash
deploy> cdk deploy --require-approval never
✨  Synthesis time: 9.03s
ContainerAcceleratorStack: building assets...
...
ContainerAcceleratorStack: deploying... [1/1]
✨  Deployment time: 60.28s

Outputs:
ContainerAcceleratorStack.AppServiceAlbUrl = Conta-AppSe-19HEDVTH7E208-717646561.us-east-1.elb.amazonaws.com
ContainerAcceleratorStack.AppServiceUrl = sample-container-app.neurons-lab-demo.com

Stack ARN:
arn:aws:cloudformation:us-east-1:111111111111:stack/ContainerAcceleratorStack/cfb54bd0-ce64-11ed-8dcb-121b44e79a29
✨  Total time: 70.31s
```
