#! /bin/bash

curl --location --request POST 'https://conformity.us-1.cloudone.trendmicro.com/api/compliance-standards/custom' \
--header 'Authorization: ApiKey <yourKeyHere>' \
--header 'Content-Type: application/vnd.api+json' \
--data-raw '{
    "data": {
        "name": "Internal Cloud Controls Framework",
        "version": "v0.2a",
        "description": "A demo of creating a custom compliance framework using the Cloud One Conformity Custom Compliance API.",
        "isEnabled": true,
        "type": "DRAFT",
        "controls": [
            {
                "aid": "CCM.IAM.1",
                "awsRules": [
                    "IAM-016",
                    "IAM-034"
                ],
                "azureRules": [
                    "ActiveDirectory-003"
                ],
                "gcpRules": [
                    "CloudIAM-007"
                ],
                "headings": {
                    "level1": "Access Control",
                    "level2": "Account Management"
                },
                "title": "Cloud user accounts must be managed using the CSP-provided IAM System."
            }
        ]
    }
}'