# OWASP Top 10 for LLM Applications 2025 - General Summary

**Document:** OWASP Top 10 for LLM Applications  
**Version:** 2025 (Released November 18, 2024)  
**License:** Creative Commons CC BY-SA 4.0  
**Total Pages:** 45  
**Official Website:** genai.owasp.org

---

## Overview
Community-driven effort highlighting security issues specific to AI/LLM applications. Updated from 2023 version with expanded coverage based on real-world feedback and emerging threats in LLM deployments.

---

## 10 Critical Vulnerabilities

### 1. **LLM01:2025 - Prompt Injection**
Attackers manipulate prompts to alter LLM behavior unintentionally. Includes direct injections (user input) and indirect injections (external sources like websites/files). Can lead to unauthorized access, sensitive data disclosure, or system compromise.

### 2. **LLM02:2025 - Sensitive Information Disclosure**
LLMs expose PII, financial data, health records, business secrets, or security credentials through output. Risks include privacy violations, IP breaches, and unauthorized access via training data extraction.

### 3. **LLM03:2025 - Supply Chain**
Vulnerabilities in third-party models, datasets, and dependencies. Risks from outdated components, licensing violations, vulnerable pre-trained models, and weak model provenance. New risks from open-access LLMs and fine-tuning methods (LoRA, PEFT).

### 4. **LLM04:2025 - Data & Model Poisoning**
Attackers contaminate training data or manipulate models directly to introduce biases, backdoors, or malicious behavior. Can be injected during development, training, or deployment phases.

### 5. **LLM05:2025 - Improper Output Handling**
Inadequate validation/sanitization of LLM outputs before use in downstream systems. Can lead to code execution, content injection, or unintended system behavior when outputs are consumed without proper controls.

### 6. **LLM06:2025 - Excessive Agency**
LLMs with excessive autonomy and uncontrolled permissions cause unintended actions. Critical with agentic architectures and plugin ecosystems where models execute arbitrary functions.

### 7. **LLM07:2025 - System Prompt Leakage**
Attackers extract system prompts revealing internal instructions, operational details, or security mechanisms. Can enable further attacks by exposing system architecture and constraints.

### 8. **LLM08:2025 - Vector & Embedding Weaknesses**
Vulnerabilities in Retrieval-Augmented Generation (RAG) and embedding-based systems. Risks include poisoned embeddings, similarity search exploitation, and unauthorized data access.

### 9. **LLM09:2025 - Misinformation**
Models generate false, misleading, or fabricated information. Sources include hallucinations, outdated knowledge, poisoned data, or adversarial manipulation. Harmful in healthcare, finance, legal, and news sectors.

### 10. **LLM10:2025 - Unbounded Consumption**
Unrestricted resource usage leading to DoS attacks and unexpected costs. Includes token exhaustion, computational overload, and financial impact from uncontrolled API consumption.

---

## What's New in 2025

- **Unbounded Consumption** - Expanded from DoS to cover resource management and cost risks
- **Vector & Embeddings** - New entry for RAG security guidance (now critical practice)
- **System Prompt Leakage** - Added for real-world exploitation patterns
- **Excessive Agency** - Expanded for agentic architectures and autonomous agent risks
- Broader, more diverse contributor base with global real-world feedback

---

## Key Frameworks & Taxonomies Referenced

- **MITRE ATLAS** - LLM-specific attack techniques (AML.T0051, AML.T0054, AML.T0024)
- **OWASP ASVS** - Application security verification standards
- **OWASP CycloneDX** - Software bill of materials
- **NIST AI Risk Management Framework** - Compliance and governance
- **OWASP API Security** - Integration with API security best practices

---

## General Prevention & Mitigation Principles

1. **Input Validation** - Strict validation, filtering, and sanitization of user/external inputs
2. **Output Handling** - Define expected formats, validate adherence, implement filtering
3. **Access Control** - Least privilege principle, restrict API tokens and data sources
4. **Supply Chain Security** - Verify dependencies, maintain SBOMs, audit third-party models
5. **Human-in-the-Loop** - Approval gates for high-risk actions
6. **Monitoring & Logging** - Track model behavior, detect anomalies
7. **Adversarial Testing** - Regular pentesting, breach simulations, threat modeling
8. **User Education** - Guidance on safe LLM usage and data handling
9. **Privacy Techniques** - Federated learning, differential privacy, tokenization
10. **System Hardening** - Secure prompts, isolate sensitive data, manage resource limits

---

## Real-World Case Studies Referenced

- **Air Canada** - Chatbot disclosed hidden fees
- **ChatGPT/Samsung** - Data leakage from training data inclusion
- **PyPI Attacks** - Supply chain poisoning via malicious packages
- **PoisonGPT** - Model poisoning demonstration
- **Google Play** - App reverse-engineering attacks

---

## Critical Takeaways

- LLM security is **layered** - no single solution prevents all risks
- **Ongoing monitoring** required as threats evolve and models change
- **Community-driven** security guidance based on real incidents
- Security must balance **functionality vs. risk tolerance**
- **Threat modeling** essential for LLM architecture design
- Regular updates needed as LLM deployment patterns mature

---

*For detailed attack scenarios, mitigation code examples, and specific MITRE ATLAS mappings, refer to full OWASP Top 10 for LLM Applications 2025 document.*
