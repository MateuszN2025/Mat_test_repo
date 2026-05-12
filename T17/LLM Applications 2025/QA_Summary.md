# OWASP Top 10 for LLM Applications 2025 - QA Testing & Quality Assurance Summary

**Document**: OWASP Top 10 for LLM Applications v2025  
**Release Date**: November 18, 2024  
**Total Pages**: 45  
**License**: Creative Commons CC BY-SA 4.0

---

## Executive Summary

The OWASP Top 10 for LLM Applications 2025 is a comprehensive security guide identifying the most critical vulnerabilities in AI applications. This document outlines 10 major vulnerability categories with specific testing considerations, prevention strategies, and real-world attack scenarios essential for QA professionals.

---

## 10 Critical Vulnerability Categories & QA Testing Requirements

### 1. **LLM01:2025 - Prompt Injection** 🎯
**Risk Level**: CRITICAL  
**Impact**: Unauthorized access, disclosure of sensitive data, content manipulation, arbitrary command execution

#### QA Testing Checklist:
- ✓ Test direct prompt injection attacks where user input alters model behavior
- ✓ Validate indirect prompt injections via external sources (websites, files)
- ✓ Test multimodal attack scenarios (images with hidden malicious instructions)
- ✓ Verify adversarial suffix attacks and multilingual/obfuscated attacks
- ✓ Test payload splitting and code injection scenarios
- ✓ Conduct adversarial testing and breach simulations
- ✓ Verify context adherence and output format validation
- ✓ Test input/output filtering mechanisms

#### Prevention Testing:
- Input validation and semantic filters
- Output format validation using RAG Triad (context relevance, groundedness, Q&A relevance)
- Privilege control enforcement
- Human-in-the-loop approval for high-risk actions
- External content segregation and identification

---

### 2. **LLM02:2025 - Sensitive Information Disclosure** 🔐
**Risk Level**: CRITICAL  
**Impact**: PII leakage, proprietary algorithm exposure, confidential business data disclosure

#### QA Testing Checklist:
- ✓ Test for PII leakage (names, addresses, SSNs, etc.)
- ✓ Verify data sanitization prevents user data from entering training
- ✓ Test model inversion attacks to recover training data
- ✓ Validate restricted data sources and access controls
- ✓ Test federated learning and differential privacy implementations
- ✓ Verify system preamble concealment
- ✓ Test data masking and tokenization techniques

#### Data Protection Scenarios:
- User education on safe LLM interaction
- Terms of Use policies and opt-out mechanisms
- System prompt restrictions on sensitive data types
- Homomorphic encryption testing

---

### 3. **LLM03:2025 - Supply Chain** ⛓️
**Risk Level**: HIGH  
**Impact**: Biased outputs, security breaches, system failures, model tampering

#### QA Testing Checklist:
- ✓ Vulnerability scanning of third-party packages and components
- ✓ Software Bill of Materials (SBOM) validation
- ✓ Vet and audit third-party suppliers and dependencies
- ✓ Test pre-trained model integrity with signing and file hashes
- ✓ Validate LoRA adapter security in model merge environments
- ✓ Red team testing on supplied models and data
- ✓ Test model provenance verification
- ✓ Licensing compliance verification

#### Attack Scenarios to Test:
- Vulnerable Python library exploitation
- Direct model tampering and parameter changes
- Fine-tuning attacks removing safety features
- Compromised LoRA adapter integration
- Model merge service vulnerabilities
- On-device LLM tampering and reverse-engineering

---

### 4. **LLM04: Data and Model Poisoning** ☠️
**Risk Level**: HIGH  
**Impact**: Biased outputs, toxic content, backdoor exploitation, model impairment

#### QA Testing Checklist:
- ✓ Test data poisoning in pre-training, fine-tuning, and embedding stages
- ✓ Verify data origin tracking using ML-BOM and CycloneDX
- ✓ Validate training data legitimacy
- ✓ Test sandboxing to limit exposure to unverified data
- ✓ Anomaly detection for adversarial data filtering
- ✓ Verify data version control (DVC) implementation
- ✓ Monitor training loss and detect poisoning signs
- ✓ Test model robustness with red team campaigns

#### Testing Attack Vectors:
- Split-View Data Poisoning
- Frontrunning Poisoning
- Backdoor trigger insertion
- Malicious data injection during training
- Credential and proprietary information leakage

---

### 5. **LLM05:2025 - Improper Output Handling** 🔄
**Risk Level**: HIGH  
**Impact**: XSS, CSRF, SSRF, privilege escalation, remote code execution

#### QA Testing Checklist:
- ✓ Test output validation and sanitization
- ✓ Verify context-aware output encoding (HTML, JavaScript, SQL)
- ✓ Test parameterized queries for LLM-generated SQL
- ✓ Validate file path sanitization to prevent traversal attacks
- ✓ Test email template content escaping
- ✓ Verify Content Security Policy (CSP) implementation
- ✓ Test rate limiting and anomaly detection
- ✓ Validate output logging and monitoring

#### OWASP Compliance:
- ASVS (Application Security Verification Standard) adherence
- Zero-trust approach to model output
- Input validation on responses to backend functions

---

### 6. **LLM06:2025 - Excessive Agency** 🤖
**Risk Level**: HIGH  
**Impact**: Unintended actions, data exfiltration, privilege escalation, unauthorized operations

#### QA Testing Checklist:
- ✓ Test extension functionality minimization
- ✓ Verify extension permission restrictions
- ✓ Validate privilege escalation prevention
- ✓ Test user authorization context enforcement
- ✓ Verify human-in-the-loop controls for high-risk actions
- ✓ Test complete mediation of authorization
- ✓ Validate input/output sanitization (SAST/DAST)
- ✓ Test rate limiting on sensitive operations
- ✓ Verify logging and monitoring of extension activity

#### Agency Limitations Testing:
- Minimize excessive functionality
- Minimize excessive permissions
- Minimize excessive autonomy
- Complete mediation principle enforcement
- Principle of least privilege validation

---

### 7. **LLM07:2025 - System Prompt Leakage** 💔
**Risk Level**: MEDIUM  
**Impact**: Disclosure of internal rules, filtering criteria, role structures, architectural details

#### QA Testing Checklist:
- ✓ Test system prompt extraction attempts
- ✓ Verify sensitive data is NOT in system prompts
- ✓ Validate API keys and credentials are externalized
- ✓ Test role-based permission information exposure
- ✓ Verify guardrail implementation outside LLM
- ✓ Test security control enforcement independence
- ✓ Validate system prompt content against leakage
- ✓ Test multi-agent systems with least privileges

#### Prevention Testing:
- Separation of sensitive data from prompts
- Avoidance of system prompts for strict behavior control
- Guardrail implementation outside LLM
- Independent security control enforcement

---

### 8. **LLM08:2025 - Vector and Embedding Weaknesses** 🔢
**Risk Level**: MEDIUM  
**Impact**: Data leakage, model output manipulation, unauthorized access to embeddings

#### QA Testing Checklist:
- ✓ Test RAG (Retrieval-Augmented Generation) security
- ✓ Validate fine-grained access controls on vector databases
- ✓ Test multi-tenant isolation in shared environments
- ✓ Verify embedding inversion attack resistance
- ✓ Test data poisoning in vector stores
- ✓ Validate data validation pipelines for knowledge sources
- ✓ Test cross-context information leakage prevention
- ✓ Monitor retrieval activity logging

#### RAG-Specific Testing:
- Data source authentication and validation
- Knowledge base integrity auditing
- Dataset combination and classification
- Immutable logging of retrieval activities
- Hidden code detection in documents

---

### 9. **LLM09:2025 - Misinformation** 📢
**Risk Level**: MEDIUM  
**Impact**: Factual inaccuracies, false legal cases, unsafe code generation, user overreliance

#### QA Testing Checklist:
- ✓ Test hallucination detection and mitigation
- ✓ Validate RAG implementation for factual accuracy
- ✓ Test code generation for security vulnerabilities
- ✓ Verify cross-verification mechanisms
- ✓ Test human oversight processes
- ✓ Validate automatic validation mechanisms
- ✓ Test content labeling and user warnings
- ✓ Verify domain-specific training effectiveness
- ✓ Test secure coding practice enforcement

#### Misinformation Scenarios:
- **Air Canada Case Study**: Chatbot provided misinformation, led to legal liability
- **ChatGPT Case Study**: Fabricated legal cases referenced in court
- **Healthcare Misinformation**: Unsupported health claims misleading users
- **Code Generation**: Hallucinated non-existent libraries leading to malware

#### Mitigation Testing:
- Retrieval-Augmented Generation (RAG)
- Model fine-tuning with parameter-efficient techniques
- Cross-verification with trusted sources
- Automatic output validation
- Risk communication and UI design

---

### 10. **LLM10:2025 - Unbounded Consumption** 💰
**Risk Level**: MEDIUM  
**Impact**: Denial of Service (DoS), "Denial of Wallet" (DoW), model theft, service degradation

#### QA Testing Checklist:
- ✓ Test input size validation and limits
- ✓ Verify rate limiting implementation
- ✓ Test resource allocation management
- ✓ Validate timeout and throttling mechanisms
- ✓ Test sandbox restrictions on resource access
- ✓ Verify comprehensive logging and anomaly detection
- ✓ Test watermarking for unauthorized use detection
- ✓ Validate graceful degradation under load
- ✓ Test access controls and model inventory management
- ✓ Test MLOps deployment automation

#### Attack Scenarios:
- **Variable-Length Input Flood**: Overwhelming system with varying input lengths
- **Denial of Wallet (DoW)**: Exploiting pay-per-use model for financial harm
- **Context Window Overflow**: Continuous inputs exceeding context limits
- **Model Extraction**: API querying to replicate models
- **Functional Model Replication**: Using target model for synthetic training data
- **Side-Channel Attacks**: Exploiting input filtering to harvest model weights

---

## QA Framework & Testing Methodologies

### 1. **Red Team Testing** 🔴
- Comprehensive AI red teaming for third-party models
- Adversarial testing and breach simulations
- Penetration testing with models treated as untrusted users
- Attack simulation with real-world exploit scenarios

### 2. **Compliance Frameworks**

#### MITRE ATLAS (Adversarial Tactics, Techniques, and Common Knowledge)
- **AML.T0051.000** - LLM Prompt Injection: Direct
- **AML.T0051.001** - LLM Prompt Injection: Indirect
- **AML.T0054** - LLM Jailbreak Injection: Direct
- **AML.T0018** - Backdoor ML Model
- **AML.T0024.000** - Infer Training Data Membership
- **AML.T0024.001** - Invert ML Model
- **AML.T0024.002** - Extract ML Model
- **AML.T0048.002** - Societal Harm
- **AML.T0029** - Denial of ML Service
- **AML.T0034** - Cost Harvesting
- **AML.T0025** - Exfiltration via Cyber Means

#### OWASP Standards
- **OWASP Top 10 Web Application** (A06:2021 - Vulnerable and Outdated Components)
- **OWASP API8:2023** - Security Misconfiguration
- **OWASP ASVS** - Application Security Verification Standard
- **OWASP CycloneDX** - Software Bill of Materials (SBOM)
- **OWASP ASEC** - ML Security Top 10 (ML05:2023 Model Theft)

#### NIST Framework
- **NIST AI Risk Management Framework**: AI integrity strategies
- **NIST CWE-400**: Uncontrolled Resource Consumption

### 3. **Testing Tools & Techniques**

#### Data & Model Protection
- **Software Bill of Materials (SBOM)** - Component tracking
- **Data Version Control (DVC)** - Dataset change tracking
- **ML-BOM & AI-BOM** - ML-specific material bills
- **Decoding Trust Benchmark** - Trustworthy AI evaluation
- **HuggingFace SF_Convertbot Scanner** - Automated vulnerability detection

#### Monitoring & Logging
- **Immutable logging** - Audit trail for retrieval activities
- **Anomaly detection** - Unusual pattern identification
- **Resource usage monitoring** - Dynamic allocation tracking
- **Training loss monitoring** - Poisoning sign detection

#### Security Testing
- **Static Application Security Testing (SAST)**
- **Dynamic Application Security Testing (DAST)**
- **Interactive Application Security Testing (IAST)**
- **Adversarial robustness training**
- **Glitch token filtering**

---

## Key QA Metrics & Quality Checkpoints

### Security Metrics
| Metric | Target | Test Method |
|--------|--------|------------|
| Prompt Injection Resistance | >95% block rate | Automated injection tests |
| Data Leakage Prevention | Zero PII exposure | Data extraction tests |
| Output Validation Rate | 100% enforcement | Output sampling |
| Access Control Effectiveness | 100% enforcement | Permission tests |
| Hallucination Detection | >90% accuracy | Fact-checking tests |

### Performance Metrics
| Metric | Threshold | Monitoring |
|--------|-----------|-----------|
| Input Processing Time | <5 seconds | Per-request logging |
| Resource Consumption | <80% capacity | Real-time monitoring |
| Rate Limit Enforcement | 0 violations | API monitoring |
| System Availability | 99.9% uptime | Continuous monitoring |
| Response Accuracy | >95% correctness | Human review sampling |

### Compliance Metrics
| Requirement | Verification | Frequency |
|-------------|--------------|-----------|
| SBOM Accuracy | Component scanning | Per deployment |
| License Compliance | Automated audits | Quarterly |
| Red Team Results | Vulnerability findings | Quarterly |
| Security Training | Team certification | Annual |

---

## Critical Testing Scenarios & Real-World Case Studies

### Case Study 1: Air Canada Chatbot
- **Issue**: Chatbot provided misinformation to travelers
- **Impact**: Legal liability and operational disruptions
- **QA Lesson**: Implement fact-checking and human oversight for customer-facing systems
- **Test**: Cross-verify outputs with trusted data sources

### Case Study 2: ChatGPT Legal Cases
- **Issue**: Model fabricated non-existent court cases
- **Impact**: Cases cited in actual court proceedings
- **QA Lesson**: Domain-specific hallucination testing for critical applications
- **Test**: Legal database validation and citation verification

### Case Study 3: Hugging Face Model Tampering (PoisonGPT)
- **Issue**: Model directly modified to bypass safety features and spread misinformation
- **Impact**: Compromised model distributed to users
- **QA Lesson**: Model integrity verification and provenance validation
- **Test**: Cryptographic signing and file hash verification

### Case Study 4: PyPI Package Poisoning
- **Issue**: Compromised PyTorch dependency with malware in development environment
- **Impact**: Model development infrastructure compromise
- **QA Lesson**: Supply chain vulnerability scanning and dependency management
- **Test**: Automated vulnerability scanning in development pipelines

### Case Study 5: Google Play Reverse-Engineering Attack
- **Issue**: 116 Google Play apps had models replaced with tampered versions
- **Impact**: Malicious redirects affecting security-critical applications
- **QA Lesson**: On-device model integrity and attestation
- **Test**: Firmware attestation and model tamper detection

---

## Testing Priority Matrix

### Priority 1 (CRITICAL) - Test First
1. Prompt Injection Attacks (LLM01)
2. Sensitive Information Disclosure (LLM02)
3. Improper Output Handling (LLM05)
4. Excessive Agency (LLM06)

### Priority 2 (HIGH) - Test Early
1. Supply Chain Vulnerabilities (LLM03)
2. Data and Model Poisoning (LLM04)
3. System Prompt Leakage (LLM07)

### Priority 3 (MEDIUM) - Test Throughout
1. Vector and Embedding Weaknesses (LLM08)
2. Misinformation (LLM09)
3. Unbounded Consumption (LLM10)

---

## Quality Assurance Recommendations

### Pre-Deployment QA Gates
- ✓ Red team assessment completed
- ✓ SBOM validated and reviewed
- ✓ All top 10 vulnerabilities tested
- ✓ Security controls verified
- ✓ Compliance framework validation
- ✓ Human review of critical outputs
- ✓ Load testing and DoS simulation
- ✓ Data sanitization verification

### Continuous QA During Deployment
- ✓ Real-time anomaly detection monitoring
- ✓ Daily log review and analysis
- ✓ Weekly security metrics review
- ✓ Monthly red team updates
- ✓ Quarterly compliance audits
- ✓ Automated vulnerability scanning

### Post-Deployment QA Maintenance
- ✓ Patch management within 48 hours
- ✓ Quarterly security re-assessment
- ✓ Annual third-party penetration testing
- ✓ Continuous model behavior monitoring
- ✓ Regular training data validation

---

## Key Resources & References

### Official Documentation
- OWASP Top 10 for LLM Applications: https://genai.owasp.org
- MITRE ATLAS Framework: https://atlas.mitre.org
- NIST AI Risk Management Framework

### Testing Tools & Frameworks
- OWASP ASVS (Application Security Verification Standard)
- OWASP CycloneDX (SBOM)
- Decoding Trust Benchmark
- HuggingFace Model Card System

### Security Scanners
- Automated ML model vulnerability scanning
- SAST/DAST tools for LLM applications
- Dependency vulnerability scanners (PyPI, NPM)

---

## Conclusion

The OWASP Top 10 for LLM Applications 2025 provides a comprehensive framework for QA professionals to identify, test, and mitigate critical vulnerabilities in AI applications. Success requires:

1. **Comprehensive Testing**: Cover all 10 vulnerability categories
2. **Continuous Monitoring**: Real-time anomaly detection and logging
3. **Red Team Practices**: Regular adversarial testing and simulations
4. **Framework Compliance**: Align with MITRE ATLAS, NIST, and OWASP standards
5. **Human Oversight**: Critical decisions and approvals require human review
6. **Supply Chain Security**: Validate all third-party models and components
7. **Data Protection**: Strict controls on sensitive information handling

By implementing these testing practices and quality metrics, organizations can build more secure and reliable LLM applications.

---

**Document Generated**: May 12, 2026  
**Source PDF**: LLMAll_en-US_FINAL.pdf (45 pages)  
**Classification**: Public (Creative Commons CC BY-SA 4.0)
