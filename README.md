# AWS Serverless URL Shortener

## Overview
A fully serverless URL shortener built using AWS services.  
The project generates short URLs and redirects users to original URLs without managing any servers.

## Architecture
- AWS Lambda (Backend logic)
- DynamoDB (URL storage)
- Lambda Function URLs (API replacement)
- S3 (Frontend hosting)
- CloudWatch (Logging)

## Features
- Generate short URLs
- Redirect to original URLs
- Serverless & auto-scalable
- Works in restricted AWS lab environments

## Tech Stack
- AWS Lambda (Python)
- Amazon DynamoDB
- AWS CloudWatch
- HTML / JavaScript

## How It Works
1. User submits a long URL
2. Lambda generates a short code
3. Mapping is stored in DynamoDB
4. Redirect Lambda forwards user to original URL

## Resume Bullet
Built a serverless URL shortener using AWS Lambda and DynamoDB, implementing scalable backend logic with zero server management.
