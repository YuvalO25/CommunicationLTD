# Communication_LTD – Secure Web System (Demo)

This project demonstrates both secure and intentionally vulnerable implementations of common web flows in Django.

## Endpoints

- Secure: `/secure/register/`, `/secure/login/`, `/secure/change-password/`, `/secure/forgot/`, `/secure/add-customer/`
- Vulnerable: `/vulnerable/register/`, `/vulnerable/login/`, `/vulnerable/change-password/`, `/vulnerable/forgot/`, `/vulnerable/add-customer/`
- Admin: `/admin/`

## Password Policy

Configured in `communication_ltd/communication_ltd/config/password_policy.json` (min length 10, upper/lower/digit/special, history 3, login attempts limit 3, blacklist).

## Models

- `UserAccount` + `PasswordHistory` for credential storage and history tracking.
- `Customer`, `Sector`, `Package`.

## Notes

- Secure flows use HMAC(salt+password) and enforce policy/history.
- Vulnerable flows use raw SQL, no hashing, and stored XSS on add-customer to showcase risks.

