## Building docker image
echo "Building the docker image..." 
docker build --platform linux/amd64 -t flash-agent:new .

## Authenticating to AWS
aws ecr get-login-password --region us-west-2 --profile flash| docker login --username AWS --password-stdin 799492718470.dkr.ecr.us-west-2.amazonaws.com

# Tag it as the right ECR reppo
docker tag flash-agent:new 799492718470.dkr.ecr.us-west-2.amazonaws.com/flash-agent:latest

# Push it to AWS
docker push 799492718470.dkr.ecr.us-west-2.amazonaws.com/flash-agent:latest

# Update the lambda code
aws lambda update-function-code --function-name flash --profile flash --image-uri 799492718470.dkr.ecr.us-west-2.amazonaws.com/flash-agent:latest