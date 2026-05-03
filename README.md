# Zero Trust IAM & GRC Program

## Overview
This project demonstrates a Zero Trust Identity and Access Management (IAM) system combined with Governance, Risk, and Compliance (GRC) practices. It simulates real-world access control, logging, and audit processes.

## Key Features
- Role-Based Access Control (RBAC)
- Multi-Factor Authentication (MFA)
- Access Control Matrix
- Audit Logging and Monitoring
- Risk Register and Compliance Checklist

## Architecture
![Architecture Diagram](implementation/screenshots/architecture_diagram.png)  
*Figure 1: Zero Trust IAM & GRC Architecture Overview*

## Implementation
- Python scripts generate user access logs
- Audit script summarizes access activity
- Logs stored and analyzed for compliance monitoring
- Audit summary output example:  
![Audit Summary](implementation/screenshots/audit_summary_output.png)  
*Figure 2: Sample Audit Summary Output*

## GRC Components
- HIPAA Compliance Checklist
- Risk Register
- Security Policies

## Project Structure
- zero-trust-iam-grc-program
  - [README.md](./README.md)
  - implementation
    - scripts (Python scripts for audit & logging)
    - screenshots (Screenshots for documentation)
    - audit
      - [Audit Summary](./implementation/audit/audit_summary.md)
  - architecture
    - [Access Control Matrix](./architecture/access-control-matrix.md)
  - compliance
    - [HIPAA Compliance Checklist](./compliance/sample-hipaa-checklist.md)
  - policies
    - [Password Policy](./policies/password-policy.md)
  - risk-register
    - [Risk Register](./risk-register/sample-risk-register.md)
  - logs
    - [user_access.log](./logs/user_access.log) (Raw access logs for audit analysis)


 
## Tools Used
- Python
- Git & GitHub
- VS Code
- draw.io (for diagrams)

**Note:** The audit summary output is generated dynamically and may vary with each run of the scripts.

## Author
Miguel Carrillo
