# MyLinkedInLegend

MyLinkedInLegend is a LinkedIn SEO optimization and content automation tool designed to help users stay consistent, grow their presence, and save time.
It streamlines the entire posting process by offering AI-assisted content creation, reusable templates, and automatic scheduling.
Whether you're sharing career updates, building your personal brand, or posting regularly for work, MyLinkedInLegend helps you create better content and stay active on LinkedIn with less effort.

---

## Project Overview

MyLinkedInLegend enables users to:

- Connect their LinkedIn accounts securely using OAuth 2.0
- Create and manage reusable post templates
- Generate high-quality post content with AI assistance
- Schedule posts to be published automatically
- Maintain optimal posting frequency and SEO-friendly structure

The goal is to simplify LinkedIn content strategy through automation, personalization, and intelligent optimization tools.

---

## Features

### Automated LinkedIn Posting

Allows users to schedule posts that will automatically publish through the LinkedIn UGC API.

### AI-Assisted Post Creation

Generates LinkedIn-ready content based on templates, tone settings, and user prompts.

### Template Management

Supports creation, editing, and storage of reusable post templates with customizable parameters.

### LinkedIn OAuth Integration

Provides secure account connection and automatic token refresh handling.

### Serverless Architecture

Built entirely on AWS using Lambdas, DynamoDB, API Gateway, and Cognito for scalable and low-maintenance operation.

---

## Tech Stack

### Frontend

- Next.js (TypeScript)
- Designed for S3 + CloudFront hosting
- Includes the dashboard, template editor, scheduler, and AI generation UI

### Backend

- Python 3.11 AWS Lambda functions
- AWS CDK for infrastructure-as-code
- Handles LinkedIn authentication, AI generation, template CRUD, and scheduled publishing logic

### Authentication

- Amazon Cognito User Pool
- Email and password login
- JWT-secured API access

### Database (DynamoDB)

Tables include:

- Users
- LinkedInTokens
- Templates
- ScheduledPosts

### Secrets Management

Sensitive values stored securely in AWS SSM Parameter Store:

- LinkedIn credentials
- AI provider API keys
