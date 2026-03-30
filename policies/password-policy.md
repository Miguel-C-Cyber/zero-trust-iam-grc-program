# Password Policy
Author: Miguel Carrillo
Date: 2026-03-30

## Purpose
Define standards for secure password creation, storage, and usage.

## Policy
- Minimum 12 characters, mix of upper/lowercase, numbers, symbols
- Mandatory MFA for all accounts
- Passwords stored using secure hashing (bcrypt, Argon2)
- Passwords changed every 90 days

## Enforcement
- IAM system automatically checks password complexity
- Audit logs reviewed monthly by SOC