# cs430 Covid Kitchen
This repository was authored by Robert Pelayo (rpelayo@pdx.edu)

## Purpose
The files contained in this repository are used to build a container and be deployed on Amazon's AWS. 

## Usage
AWS credentials are required for this program to run as dynamoDB is used.
To run the program locally (AWS credentials must be imported):
```buildoutcfg
virutal env -p python3 env
source env/bin/activate
pip install -r requirements.txt
export AWS_ACCESS_KEY_ID=ASIA...32F
export AWS_SECRET_ACCESS_KEY=p22Z...COe
export AWS_SESSION_TOKEN=FwoG...A==
export AWS_DEFAULT_REGION=us-east-1
python app.py
```

To run the program locally as a container:
```buildoutcfg
docker build -t covidkitchen .
docker run --env AWS_ACCESS_KEY_ID=ASIA...32F --env AWS_SECRET_ACCESS_KEY=p22Z...COe --env AWS_DEFAULT_REGION=us-east-1 --env AWS_SESSION_TOKEN=FwoG...A== --env PORT=80 -p 8000:80 covidkitchen
```
