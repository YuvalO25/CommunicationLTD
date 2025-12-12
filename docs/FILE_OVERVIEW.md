# Project file overview

This guide summarizes what each major module does so you can quickly explain the secure vs. vulnerable flows during a presentation.

## Top-level layout
- `communication_ltd/` – Django project configuration (settings, root URLs, password policy config).
- `core/` – Django app containing models, security helpers, views, templates, and URL routes for secure and intentionally vulnerable flows.
- `README.md` – quick summary of endpoints, password policy, and security goals.

## Project configuration (`communication_ltd/communication_ltd`)
- `settings.py` – Standard Django settings plus a `TEMPLATES_DIR` that points to `core/templates`, SQLite configuration, and a `PASSWORD_POLICY_PATH` pointing at the JSON policy file used by secure flows.
- `urls.py` – Root URL configuration that mounts the Django admin and includes `core.urls` for the secure/vulnerable routes.
- `config/password_policy.json` – Default password policy (length/complexity rules, history limit, login-attempt limit, blacklist) consumed by the secure views via the security helpers.

## App models and helpers (`communication_ltd/core`)
- `models.py` – Defines domain models: `Sector`, `Package`, `Customer` with relationships, `UserAccount` for stored credentials/reset data, and `PasswordHistory` to enforce password reuse limits.
- `security.py` – Security utilities: load password policy JSON with safe defaults; generate random salts; hash passwords with HMAC-SHA256 using Django's `SECRET_KEY`; verify hashes with constant-time comparison; validate password strength (length/upper/lower/digit/special/blacklist).

## Secure flows (`communication_ltd/core/secure_views.py`)
- `register_secure` – Applies password policy, prevents duplicate usernames, salts/hashes passwords, seeds default sector/package, and records password history atomically.
- `login_secure` – Enforces login-attempt limits from the policy, resets the counter on success, and compares hashes securely.
- `change_password_secure` – Checks optional reset tokens, verifies the old password, validates the new one, blocks reuse of recent hashes per the history limit, trims old history entries, and clears reset data on success.
- `forgot_password_secure` – Generates a random SHA-1 token per request, stores timestamped reset data, and surfaces the token for demo purposes.
- `add_customer_secure` – Inserts customers via ORM with escaped rendering and seeds default sector/package relationships.

## Vulnerable flows (`communication_ltd/core/vulnerable_views.py`)
- `register_vulnerable` – Uses string-interpolated SQL without hashing/salting passwords (SQL injection risk, plaintext storage).
- `login_vulnerable` – Authenticates via raw SQL with interpolated credentials, exposing SQL injection and plaintext comparison.
- `change_password_vulnerable` – Updates passwords with raw SQL and no validation.
- `forgot_password_vulnerable` – Sets a static, predictable reset token via raw SQL.
- `add_customer_vulnerable` – Inserts customers with raw SQL and renders names unescaped to demonstrate stored XSS alongside SQL injection risk.

## Routing (`communication_ltd/core/urls.py`)
Maps the secure and vulnerable view functions under `/secure/...` and `/vulnerable/...` prefixes so you can demo both implementations from the same server.

## Entry points and admin
- `manage.py` – Standard Django management script for running the server, migrations, etc.
- `core/admin.py` – Registers models with the Django admin so you can inspect data through `/admin/` (after creating a superuser).
