MyLinkedInLegend — Project Overview (Updated)
Project Summary

MyLinkedInLegend is a cloud native, serverless LinkedIn Auto-Poster and SEO Optimization platform.
Users can connect their LinkedIn accounts, generate posts using AI, create custom templates, and schedule posts to publish automatically.
Everything is deployed entirely on AWS using a scalable, secure serverless architecture.

Architecture Overview
Frontend

Next.js (React) with TypeScript

Hosted on S3 + CloudFront

Provides:

Login/signup page

LinkedIn connect flow

Dashboard

Template creation UI

AI post generator

Schedule editor/list

Backend

Python 3.11 AWS Lambda functions

Deployed using AWS CDK

Contains logic for:

Token handling

LinkedIn OAuth 2.0

AI post generation

Template management

Post scheduling

DynamoDB CRUD

Publishing to LinkedIn UGC API

Authentication

Cognito User Pool (email + password)

JWT auth for API Gateway

OAuth redirect flow for LinkedIn access tokens

Database (DynamoDB)

Three core tables:

1. Users

Stores user profile + Cognito linkage.

2. LinkedInTokens

Stores:

LinkedIn access token

Refresh token

Token expiration

User ID reference

3. ScheduledPosts

Includes:

User ID

Scheduled datetime

Template ID or raw content

Whether AI is required

Status (pending, completed, failed)

4. Templates (New)

Template ID

User ID

Template text

Tags / category

AI-generation parameters (tone, style, etc)

Secrets

SSM Parameter Store:

LinkedIn Client Secret

AI Provider API Keys (OpenAI or Anthropic)

Infrastructure

AWS CDK (Python)

Resources:

Lambda functions (backend logic)

API Gateway REST API

Cognito User Pool

DynamoDB tables

S3 + CloudFront frontend hosting

IAM roles / permissions

CloudWatch EventBridge scheduled jobs

Development Phases
Phase 1 — Backend Skeleton

Build CDK project

Create a test Lambda + API Gateway endpoint

Deploy and confirm environment works

Phase 2 — Cognito Authentication

User Pool + App Client

Hosted UI for testing

JWT-protected API routes

Phase 3 — DynamoDB Core Tables

Users table

LinkedInTokens

Templates

ScheduledPosts

Phase 4 — LinkedIn OAuth Integration

Redirect handler Lambda

Exchange authorization code for tokens

Store tokens in DynamoDB

Implement token refresh workflow

Frontend “Connect LinkedIn” button and screen

Phase 5 — Posting System (LinkedIn UGC API)

Lambda to publish posts

CRUD for scheduled posts

AWS EventBridge Scheduler for delayed posting

Post status tracking in DynamoDB

Frontend UI for creating and editing schedules

Phase 6 — AI Integration (Major Feature)
Includes:

AI post generator (OpenAI or Anthropic Lambda)

Template storage + editing

Prompt engineering for styles (professional, casual, storytelling, SEO, etc)

Automatic post creation using:

user’s template

user’s custom instructions

AI model personalization

Scheduled posting with AI:

At the schedule time, EventBridge triggers Lambda

Lambda:

Loads the selected template

Calls AI API to generate final post

Publishes the post to LinkedIn

Logs status back to DynamoDB

Phase 7 — Frontend Application (Full UI)

Dashboard

Template editor

AI generator screen

Scheduled posts calendar

LinkedIn connection status

Profile settings

Phase 8 — SEO/Analytics

AI rewriting tool

Keyword/advice engine

Engagement estimator

Post performance tracking

Purpose of This Document

This file is the long-term architectural and functional blueprint for MyLinkedInLegend.
Every future feature must match the phases and design principles here.

Next Steps

Finish WSL development environment

Install Node.js, npm, Python 3.11, pip, AWS CLI, and CDK

Begin Phase 1: Initialize CDK Python project

Deploy test Lambda + API Gateway
