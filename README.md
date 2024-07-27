
# Pinterest data pipeline

## A description of the project: what it does, the aim of the project, and what you learned
This project aims to simiulate the process of data ingestion and data processing of social media data using AWS data engineering services

## Installation instructions
You would need an aws account to set up this pipeline.

To set up your EC2 enviroment, you would need to generate a key pair (this is stores as a .pem file) and use this to connect with the ec2 **securely**.

Due to security reasons we need to make this file private. To do this, navigate to where the .pem and run the following command in terminal.

```bash
chomd 400 "your_private_key.pem"
```

Then run this:

```bash
ssh -i /path/key-pair-name.pem instance-user-name@instance-public-dns-name
```

You'll have to create your own MSK cluster on AWS.

To download kafka (ensure that the kafka file is the same veirson as the IAM MSK authenticator):

## Usage instructions

## File structure of the project
```
.
├── README.md
├── creds
│   ├── 1232252d77df-key-pair.pem
│   ├── credential.yaml
│   └── important.txt
└── user_posting_emulation.py

2 directories, 5 files
```
## License information