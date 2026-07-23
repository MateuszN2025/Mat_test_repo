# QA Endpoint Security Basics for Complete Beginners (Pareto 80/20)

## Goal
Learn the small set of topics that covers most real API security testing.

## 1) Five Things To Learn First
1. Authentication: who is calling the API
2. Authorization: what that user is allowed to do
3. JWT: common token format used for login sessions
4. TLS and certificates: secure HTTPS connection
5. File signature checks: detect changed or fake files

## 2) Simple Dictionary
- API: application programming interface (endpoint URLs)
- Authentication: prove identity
- Authorization: check permissions
- JWT: JSON Web Token (a signed text token)
- TLS: Transport Layer Security (encryption for HTTPS)
- Certificate: digital identity of a server
- File hash: fingerprint of a file
- Digital signature: proof who signed a file and that it was not changed

## 3) The Most Important Test Rule
For protected endpoints, always test these 4 cases:
1. No token -> 401
2. Bad or expired token -> 401
3. Valid token but wrong role -> 403
4. Valid token and correct role -> 200

If this works everywhere, you already cover a big part of security basics.

## 4) JWT for Beginners
JWT means JSON Web Token.

Think of JWT like a "signed pass" with information inside:
- who you are
- when token expires
- what you can do

Basic checks:
1. Expired JWT must fail
2. Edited JWT must fail
3. JWT with missing role/scope must fail

## 5) Certificates and HTTPS
When API uses HTTPS, certificate must be trusted and valid.

Basic checks:
1. Expired certificate should fail
2. Wrong host name in certificate should fail
3. HTTP (no TLS) should redirect to HTTPS or be blocked

## 6) File Signature Basics
Two similar terms:
1. Hash: checks file changed or not
2. Digital signature: checks file changed or not, and who signed it

Basic checks for upload endpoints:
1. Changed file is rejected
2. Wrong signature is rejected
3. Fake file type (wrong extension) is rejected

## 7) Minimal Python QA Stack
- pytest
- requests or httpx
- simple fixtures for user roles and tokens

## 8) Beginner Priority Order
If you have little time, do this order:
1. Authentication and authorization tests
2. JWT expiration and tamper tests
3. HTTPS and certificate checks
4. File integrity/signature checks

This is the Pareto path: small effort, big coverage.
