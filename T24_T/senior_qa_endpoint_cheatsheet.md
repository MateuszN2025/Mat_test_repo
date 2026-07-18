# Senior QA & Automation Engineer — Endpoint / Autonomous IT
## Interview & Study Cheat Sheet

---

## 1. Operating Systems

### Linux Essentials

#### OS Installation & Configuration
- **Package managers:** `apt` (Debian/Ubuntu), `dnf`/`yum` (RHEL/Fedora), `rpm` (low-level)
- **Common install tasks:**
  ```bash
  apt update && apt install -y curl wget git
  rpm -qa | grep agent          # list installed RPM packages
  dpkg -l | grep tanium         # list installed DEB packages
  ```

#### Process & Service Management
```bash
# systemd — modern init system
systemctl start|stop|restart|enable|disable|status <service>
systemctl list-units --type=service --state=running
journalctl -u <service> -f          # follow logs for a specific service
journalctl --since "1 hour ago"

# Process inspection
ps aux                              # all processes with CPU/mem
ps aux | grep agent
top / htop                          # interactive process monitor
kill -9 <PID>                       # SIGKILL — force kill
kill -15 <PID>                      # SIGTERM — graceful stop

# Open files and network sockets of a process
lsof -p <PID>
lsof -i :443                        # which process owns port 443
ss -tlnp                            # listening TCP sockets (faster than netstat)
netstat -tlnp
```

#### Filesystem Layout (critical paths)
| Path | Purpose |
|---|---|
| `/etc` | Configuration files |
| `/var/log` | System and application logs |
| `/proc` | Virtual FS — kernel/process runtime info |
| `/sys` | Virtual FS — hardware/driver info |
| `/tmp` | Temporary files (cleared on reboot) |
| `/opt` | Third-party software installs |
| `/usr/bin`, `/usr/sbin` | User and system binaries |

#### Permissions Model
```bash
# Format: [type][owner][group][others]  e.g. -rwxr-xr--
chmod 755 script.sh                 # rwxr-xr-x
chmod +x script.sh                  # add execute for all
chown user:group file.txt
umask 022                           # default: new files get 644, dirs get 755

# ACLs (extended permissions)
getfacl file.txt
setfacl -m u:bob:rw file.txt

# SUID/SGID/Sticky bit
chmod u+s /usr/bin/passwd           # runs as file owner (root)
chmod +t /tmp                       # sticky: only owner can delete
```

#### User & Group Management
```bash
useradd -m -s /bin/bash alice
passwd alice
usermod -aG sudo alice              # add to sudo group
cat /etc/passwd                     # user accounts
cat /etc/shadow                     # hashed passwords (root only)
cat /etc/sudoers                    # who can sudo what
visudo                              # safe way to edit sudoers
```

#### Log Analysis
```bash
grep "Failed password" /var/log/auth.log | tail -20
grep -i "error" /var/log/syslog | awk '{print $1,$2,$3,$5,$NF}'
journalctl -xe                      # recent errors with context
# Count occurrences
grep "ERROR" app.log | wc -l
# Extract unique IPs from log
awk '{print $1}' /var/log/nginx/access.log | sort | uniq -c | sort -rn
```

---

## 2. Authentication

### Concept Map
```
Authentication  → WHO are you?       (verify identity)
Authorization   → WHAT can you do?   (verify permissions)
```

### Authentication Methods

#### Password-based
- Stored as salted hashes: `bcrypt`, `argon2`, `sha512crypt`
- `/etc/shadow` contains: `username:$6$salt$hash:...`

#### SSH Key-based Auth
```bash
# Generate a key pair
ssh-keygen -t ed25519 -C "qa-bot@ci"

# Copy public key to remote server
ssh-copy-id -i ~/.ssh/id_ed25519.pub user@host

# Manual: append to authorized_keys
cat ~/.ssh/id_ed25519.pub >> ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys

# Connect
ssh -i ~/.ssh/id_ed25519 user@host
```

#### Token-based (JWT)
- Structure: `header.payload.signature` (Base64URL encoded)
- Signed with server's private key; client sends in `Authorization: Bearer <token>`
- **Verify:** decode at [jwt.io](https://jwt.io) or `python -m base64 -d <<< "<payload>"`

#### Certificate-based (mTLS)
- Both client **and** server present certificates
- Used in endpoint agents to authenticate device identity to management server

#### Kerberos (enterprise)
- Ticket-based; KDC issues TGT after password auth; TGT used to get service tickets
- Common in Windows AD environments; `kinit`, `klist`, `kdestroy` on Linux

#### LDAP / Active Directory
- Central directory for user accounts
- Tools: `ldapsearch`, `sssd`, `realm join`

---

## 3. Certificates & PKI (X.509)

### Certificate Anatomy
```
Subject:        CN=agent.company.com, O=Company, C=US
Issuer:         CN=Company Intermediate CA
Serial Number:  0x1A2B3C
Validity:       Not Before: 2025-01-01  Not After: 2026-01-01
Public Key:     RSA 2048-bit / EC P-256
SAN:            DNS:agent.company.com, IP:10.0.0.5
Signature Alg:  sha256WithRSAEncryption
```

### Certificate Chain
```
Root CA  (self-signed, trusted by OS/browser)
  └── Intermediate CA  (signed by Root CA)
        └── Leaf/End-entity cert  (signed by Intermediate CA)
```
- Browsers/OS trust **Root CAs** stored in trust stores
- Endpoint agents often ship with a **pinned** certificate or custom CA

### Key openssl Commands
```bash
# View a certificate
openssl x509 -in cert.pem -text -noout

# View a certificate from a live server
openssl s_client -connect host:443 -showcerts </dev/null 2>/dev/null \
  | openssl x509 -text -noout

# Check certificate expiry
openssl x509 -in cert.pem -noout -enddate

# Verify cert against a CA bundle
openssl verify -CAfile ca-bundle.pem cert.pem

# Generate a self-signed cert (for testing)
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem \
  -days 365 -nodes -subj "/CN=localhost"

# Generate CSR (Certificate Signing Request)
openssl req -new -key key.pem -out request.csr -subj "/CN=agent.company.com"

# Decode a CSR
openssl req -in request.csr -text -noout

# Convert formats
openssl pkcs12 -export -out bundle.pfx -inkey key.pem -in cert.pem  # PEM → PFX
openssl pkcs12 -in bundle.pfx -out cert.pem -nodes                  # PFX → PEM
```

### TLS Handshake (step by step)
```
Client                              Server
  |--- ClientHello ----------------->|   (supported TLS version, cipher suites, random)
  |<-- ServerHello ------------------|   (chosen cipher, server random)
  |<-- Certificate ------------------|   (server's X.509 cert)
  |<-- ServerHelloDone --------------|
  |--- ClientKeyExchange ----------->|   (pre-master secret, encrypted with server pubkey)
  |--- ChangeCipherSpec ------------>|
  |--- Finished (encrypted) -------->|
  |<-- ChangeCipherSpec -------------|
  |<-- Finished (encrypted) ---------|
  |=== Application Data (encrypted) =|
```
- TLS 1.3 is simpler: 1-RTT handshake, forward secrecy by default

---

## 4. File Signatures & Integrity

### Cryptographic Hashing
```bash
# Generate hash
sha256sum agent_installer.pkg          # most common for integrity
sha512sum file.bin
md5sum file.bin                        # WEAK — do not use for security

# Verify a downloaded file
echo "expected_hash  file.bin" | sha256sum --check

# Hash a string
echo -n "hello" | sha256sum
```

### Digital Signatures
```
Signing:    hash(file) → encrypt with PRIVATE key  → signature
Verifying:  decrypt signature with PUBLIC key → compare with hash(file)
```

#### GPG Signatures
```bash
# Verify a signed file
gpg --verify file.pkg.sig file.pkg

# Import a public key
gpg --import pubkey.asc
gpg --keyserver keyserver.ubuntu.com --recv-keys <KEY_ID>

# Sign a file
gpg --armor --detach-sign file.pkg
```

#### openssl Signatures
```bash
# Sign
openssl dgst -sha256 -sign private.key -out file.sig file.bin

# Verify
openssl dgst -sha256 -verify public.key -signature file.sig file.bin
```

### Code Signing (Endpoint Agents)
- Windows: Authenticode signing with a code-signing certificate (`signtool.exe`)
- macOS: `codesign`, notarization with Apple
- Linux: RPM/DEB packages signed with GPG key
- **QA test:** verify binary signature before install; test with tampered binary (should fail)

---

## 5. Network Security & Packet Capture

### tcpdump

```bash
# Basic capture on interface
tcpdump -i eth0 -n

# Filter by host and port
tcpdump -i eth0 -n host 10.0.0.1 and port 443

# Save to file
tcpdump -i eth0 -w capture.pcap

# Read saved capture
tcpdump -r capture.pcap

# Show TLS Client Hello packets
tcpdump -r capture.pcap 'tcp port 443'

# Verbose output with hex+ASCII
tcpdump -i eth0 -XX -v port 8080

# Capture only N packets
tcpdump -i eth0 -c 100 -w out.pcap

# Common flags
# -n     don't resolve hostnames (faster, clearer)
# -nn    don't resolve hostnames OR ports
# -v     verbose
# -X     show hex + ASCII payload
# -s 0   capture full packet (default in modern tcpdump)
```

### Wireshark Key Skills

**Display filters:**
```
http                          # HTTP traffic
tls                           # TLS (HTTPS, etc.)
tcp.port == 443               # by port
ip.addr == 10.0.0.5           # by IP
ip.src == 10.0.0.5            # source only
tcp.flags.syn == 1            # TCP SYN packets
!(arp or dns)                 # exclude noise
tls.handshake.type == 1       # TLS Client Hello
```

**Key workflows:**
- **Follow stream:** Right-click packet → Follow → TCP/TLS Stream
- **TLS cert inspection:** Filter `tls.handshake.type == 11` → expand Certificate layer
- **Export objects:** File → Export Objects → HTTP (save files from capture)
- **Statistics:** Statistics → Conversations / Protocol Hierarchy / IO Graph

### Common Network Security Concepts

| Term | Meaning |
|---|---|
| **Port scanning** | Discover open services (QA: verify only expected ports open) |
| **TLS certificate pinning** | App trusts only specific cert/CA; rejects others |
| **MITM (Man-in-the-Middle)** | Attacker intercepts traffic; TLS + cert pinning prevents this |
| **Firewall rules** | Control which traffic is allowed (iptables, nftables, firewalld) |
| **VPN** | Encrypted tunnel; endpoint agents often require VPN connectivity |
| **mTLS** | Mutual TLS — both sides authenticate with certificates |

```bash
# Check iptables rules
iptables -L -n -v
nft list ruleset

# Test port connectivity
nc -zv host 443
curl -v https://host:443/healthz
```

---

## 6. QA Automation Test Design for Endpoint Agents

### Test Pyramid Applied to Endpoint Products

```
         /\
        /E2E\        ← Full install on real OS VM, agent communicates with server
       /------\
      /Integr. \     ← Agent API, registration flow, certificate exchange
     /----------\
    /  Unit/Mock  \  ← Config parsing, hash verification logic, retry logic
   /--------------\
```

### Key Test Scenarios

#### Install / Uninstall
```
✓ Install succeeds on supported OS versions
✓ Service starts and is enabled after install
✓ Correct binary signature before install
✗ Install with tampered binary → should fail / warn
✗ Install without root/admin → should fail with clear error
✓ Uninstall removes service, config, and data cleanly
```

#### Communication / Connectivity
```
✓ Agent connects to management server on expected port (443/8443)
✓ TLS version ≥ 1.2 used (capture with tcpdump, verify in Wireshark)
✓ Server certificate validated (test with expired/self-signed → should fail)
✓ mTLS: agent presents valid client cert
✗ Network interruption mid-registration → agent retries correctly
✗ Proxy environment → agent respects proxy settings
```

#### Authentication & Authorization
```
✓ Agent authenticates with valid token/cert
✗ Expired token → agent re-authenticates or fails gracefully
✗ Revoked certificate → connection rejected
✗ Wrong tenant credentials → 401/403, not 500
```

#### Resilience
```
✓ Agent survives OS reboot (service auto-starts)
✓ Agent survives network outage (queues data, sends on reconnect)
✗ Management server down → agent queues, does not crash
✓ Agent resource usage within limits (CPU/memory under load)
```

### Automation Approach (Python + pytest)
```python
import subprocess
import pytest

@pytest.fixture(scope="module")
def agent_installed():
    """Install agent and yield; uninstall after tests."""
    subprocess.run(["installer.sh", "--install"], check=True)
    yield
    subprocess.run(["installer.sh", "--uninstall"], check=True)

def test_service_is_running(agent_installed):
    result = subprocess.run(
        ["systemctl", "is-active", "my-agent"],
        capture_output=True, text=True
    )
    assert result.stdout.strip() == "active"

def test_agent_binary_hash(agent_installed):
    import hashlib
    expected = "abc123..."
    with open("/opt/agent/bin/agent", "rb") as f:
        actual = hashlib.sha256(f.read()).hexdigest()
    assert actual == expected, "Binary hash mismatch — possible tampering"
```

---

## 7. Quick Reference — Key Terms

| Term | Definition |
|---|---|
| **Authentication** | Verifying identity — proving you are who you claim to be |
| **Authorization** | What an authenticated identity is permitted to do |
| **File signature** | Cryptographic proof that a file was produced by a known entity and has not been modified |
| **Certificate (X.509)** | Document binding a public key to an identity, signed by a Certificate Authority |
| **CA (Certificate Authority)** | Trusted entity that issues and signs certificates |
| **PKI** | Infrastructure for managing certificates: issuance, renewal, revocation |
| **TLS** | Protocol that encrypts network traffic; uses certificates for authentication |
| **mTLS** | Mutual TLS — both client and server authenticate with certificates |
| **CRL** | Certificate Revocation List — list of revoked certificates |
| **OCSP** | Online Certificate Status Protocol — real-time cert revocation check |
| **Hash** | One-way function mapping data to fixed-size digest; used for integrity |
| **Digital signature** | Hash of data encrypted with private key; verified with public key |
| **Endpoint agent** | Software running on a device (laptop/server) reporting telemetry to a central platform |
| **Certificate pinning** | Application only trusts a specific cert or CA, ignoring system trust store |
| **SUID** | Linux: file executes with owner's privileges (e.g., `passwd`) |

---

## 8. Study Order (2 Weeks)

| Days | Focus | Hands-on Task |
|---|---|---|
| 1–3 | Linux deep dive | Manage services, read logs, set permissions |
| 4–5 | Certificates + TLS | `openssl` cert chain, inspect with `s_client` |
| 6–7 | Authentication mechanisms | SSH key auth, JWT decode, mTLS concept |
| 8–9 | tcpdump + Wireshark | Capture TLS handshake, inspect cert in capture |
| 10–11 | File signatures + code signing | `sha256sum`, `gpg --verify`, tamper test |
| 12–14 | Mock interview | Design test plan for endpoint agent install + communication |

---

## 9. Capstone Exercise

**Goal:** Touch all three required areas in one exercise.

```bash
# 1. Generate self-signed cert
openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem \
  -days 1 -nodes -subj "/CN=localhost"

# 2. Start a local HTTPS server (Python)
python3 -c "
import ssl, http.server
ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ctx.load_cert_chain('cert.pem', 'key.pem')
server = http.server.HTTPServer(('localhost', 4443), http.server.SimpleHTTPRequestHandler)
server.socket = ctx.wrap_socket(server.socket, server_side=True)
print('HTTPS server on :4443')
server.serve_forever()
"

# 3. Capture the TLS handshake
sudo tcpdump -i lo -w tls_test.pcap port 4443 &
curl -k https://localhost:4443/     # -k skips cert validation (self-signed)
kill %1

# 4. Inspect in tcpdump
tcpdump -r tls_test.pcap -n 'tcp port 4443'

# 5. Hash and sign the cert file
sha256sum cert.pem > cert.pem.sha256
gpg --armor --detach-sign cert.pem      # requires GPG key setup
gpg --verify cert.pem.asc cert.pem

# 6. Open tls_test.pcap in Wireshark
# Filter: tls.handshake.type == 11  (Certificate message)
# Expand: Transport Layer Security → Handshake Protocol → Certificate
```
