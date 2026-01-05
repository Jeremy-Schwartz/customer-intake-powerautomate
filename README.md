# Customer Intake → Approval → CRM Sync (Power Automate)

Automates customer requests from intake (Forms/SharePoint) through approvals and creates/updates records in CRM (Dataverse or HTTP API), with auditing, SLAs, and retry handling.

## Problem
Teams receive customer requests via email/Slack and lose track of approvals, status, and follow-ups.

## Solution
A Power Automate workflow that:
- Captures requests in a system of record
- Routes approvals based on business rules
- Syncs approved requests to CRM
- Handles failures with retries and alerts

## Architecture
**Trigger:** Form submission / SharePoint item  
**System of record:** SharePoint List (CustomerRequests)  
**Approvals:** Power Automate Approvals (Teams/Outlook)  
**Sync:** Dataverse upsert or HTTP API  
**Notifications:** Teams + email  
**Reliability:** TRY/CATCH scopes + retry flow

(Insert diagram image)

## Flows
1. **Customer Intake - Create Request**
2. **Customer Intake - Approvals**
3. **Customer Intake - Sync to CRM**
4. **Customer Intake - Retry Failed Sync**

## Setup
See [docs/setup.md](docs/setup.md)

## Runbook
See [docs/runbook.md](docs/runbook.md)

## Failure Scenarios
See [docs/failure-scenarios.md](docs/failure-scenarios.md)

## Roadmap
- Add business-hours SLA calc
- Add Power BI dashboard for request status + cycle time
- Add environment variables + solution packaging
