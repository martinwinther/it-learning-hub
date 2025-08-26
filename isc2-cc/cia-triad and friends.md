# CIA Triad and Cybersecurity Fundamentals

## Overview

The CIA triad is the foundation of information security, consisting of three core
principles:

- **Confidentiality**: Ensuring only authorized individuals have access to
  information
- **Integrity**: Maintaining data accuracy and consistency
- **Availability**: Ensuring information is accessible when needed

## Confidentiality

Confidentiality ensures that sensitive information is accessible only to authorized
individuals and systems.

### Key Concepts

- **Access Control**: Implementing mechanisms to restrict unauthorized access
- **Encryption**: Protecting data in transit and at rest
- **Authentication**: Verifying user identity before granting access
- **Authorization**: Determining what resources users can access

### Common Threats and Protections

#### 1. Snooping

- **Threat**: Unauthorized individuals physically accessing sensitive information
- **Example**: Someone wandering around an office looking at documents
- **Protection**:
  - Clean desk policies
  - Screen locks and timeouts
  - Physical access controls
  - Privacy screens

#### 2. Dumpster Diving

- **Threat**: Attackers searching through discarded materials for sensitive
  information
- **Example**: Looking for documents in trash outside buildings
- **Protection**:
  - Paper shredders for sensitive documents
  - Secure disposal procedures
  - Digital document management
  - Regular security audits

#### 3. Eavesdropping

- **Physical Eavesdropping**: Attackers trying to overhear conversations
- **Electronic Eavesdropping**: Unauthorized network access to intercept
  communications
- **Protection**:
  - Limit sensitive conversations in public areas
  - Use encryption for all communications
  - Implement secure communication channels
  - Regular security awareness training

#### 4. Social Engineering

- **Threat**: Attackers manipulating people to gain unauthorized access
- **Example**: Pretending to be a manager to request sensitive data
- **Protection**:
  - User education and awareness training
  - Verification procedures for sensitive requests
  - Multi-factor authentication
  - Incident reporting procedures

## Integrity

Integrity ensures that data remains accurate, complete, and unaltered throughout its
lifecycle.

### Integrity Key Concepts

- **Data Validation**: Checking data accuracy and completeness
- **Checksums**: Verifying data hasn't been modified
- **Version Control**: Tracking changes to data
- **Backup and Recovery**: Maintaining data consistency

### Integrity Common Threats

- **Data Tampering**: Unauthorized modification of data
- **Malware**: Viruses and other malicious software
- **System Failures**: Hardware or software malfunctions

### Integrity Protection Measures

- **Access Controls**: Limiting who can modify data
- **Audit Logs**: Tracking all data modifications
- **Encryption**: Protecting data from unauthorized changes
- **Regular Backups**: Ensuring data can be restored

## Availability

Availability ensures that information and systems are accessible when needed by
authorized users.

### Availability Key Concepts

- **Redundancy**: Having backup systems and components
- **Fault Tolerance**: Systems that continue operating despite failures
- **Disaster Recovery**: Plans for restoring services after major incidents
- **Load Balancing**: Distributing workload across multiple systems

### Availability Common Threats

- **Denial of Service (DoS)**: Attacks that prevent legitimate access
- **Hardware Failures**: Equipment malfunctions
- **Natural Disasters**: Events that damage infrastructure
- **Human Error**: Accidental system disruptions

### Availability Protection Measures

- **Backup Systems**: Redundant infrastructure
- **Monitoring**: Real-time system health checks
- **Incident Response**: Quick recovery procedures
- **Business Continuity**: Plans for maintaining operations

## Additional Security Concepts

### Non-Repudiation

- **Definition**: Ensuring that parties cannot deny their actions
- **Methods**: Digital signatures, audit logs, timestamps
- **Applications**: Legal compliance, transaction verification

### Authentication vs. Authorization

- **Authentication**: Verifying identity ("Who are you?")
- **Authorization**: Determining permissions ("What can you do?")
- **Examples**:
  - Authentication: Username/password, biometrics
  - Authorization: Role-based access, permissions

## Real-World Applications

### Banking Systems

- **Confidentiality**: Encrypted transactions, secure login
- **Integrity**: Transaction verification, audit trails
- **Availability**: 24/7 system access, backup servers

### Healthcare

- **Confidentiality**: HIPAA compliance, patient privacy
- **Integrity**: Accurate medical records, drug interaction checks
- **Availability**: Emergency system access, backup power

### E-commerce

- **Confidentiality**: Secure payment processing, customer data protection
- **Integrity**: Order accuracy, inventory management
- **Availability**: Website uptime, order processing systems

## Summary

The CIA triad provides a comprehensive framework for information security:

- **Confidentiality** protects sensitive information from unauthorized access
- **Integrity** ensures data accuracy and prevents unauthorized modifications
- **Availability** guarantees that authorized users can access information when needed

Understanding these principles is fundamental to cybersecurity and helps organizations
develop effective security strategies that protect their information assets while
maintaining business operations.
