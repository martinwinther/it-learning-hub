# Logical Access Controls

## Overview

Logical access controls are security mechanisms that manage and control access to
information systems, applications, and data. These controls work in conjunction
with physical access controls to provide comprehensive security for organizational
assets.

## Authorization

### Definition and Purpose

Authorization is the final step of the access control process. Once authenticated,
authorization determines the privileges users have to access resources.

### Authorization Process

- **Authentication Verification**: Confirm user identity
- **Permission Check**: Verify user has required permissions
- **Access Grant**: Allow or deny access to requested resource
- **Logging**: Record access attempts and decisions

## Core Access Control Principles

### Principle of Least Privilege

The principle of least privilege says that users should have only the minimum set
of privileges necessary to carry out their job responsibilities.

#### Benefits

- **Damage Limitation**: Minimizes potential damage from an insider attack
- **Attack Surface Reduction**: Limits ability for external attackers to gain
  access when compromising employee accounts
- **Compliance**: Meets regulatory requirements for access control
- **Audit Efficiency**: Simplifies security audits and reviews

#### RBAC Implementation

- **Role Analysis**: Define minimum permissions for each role
- **Regular Reviews**: Periodic review of user permissions
- **Just-in-Time Access**: Grant temporary elevated access when needed
- **Automated Provisioning**: Use automated tools to manage permissions

### Segregation of Duties

The segregation of duties principle says that no single person should possess two
permissions that, in combination, allow them to perform a sensitive operation.

#### Key Distinction

**Important**: Segregation, not separation (important distinction!)

#### Examples

- **Financial Systems**: Creating new vendors in a payment system and
  authorizing payments to vendors
- **IT Development**: Coder cannot put their own code directly into production,
  but must submit their code to testing
- **Banking**: Person who opens accounts cannot approve loans
- **Healthcare**: Person who orders medications cannot dispense them

#### SOD Implementation

- **Permission Analysis**: Identify conflicting permissions
- **Role Design**: Design roles to prevent conflicts
- **Monitoring**: Monitor for violations of segregation
- **Audit Reviews**: Regular audits of permission assignments

## Authorization Models

### Mandatory Access Control (MAC)

Mandatory access control (MAC) systems are the most stringent type of access
control. In MAC systems, the operating system itself restricts the permissions
that may be granted to users and processes on system resources.

#### MAC Characteristics

- **System-Enforced**: The operating system enforces access control
- **Label-Based**: Permissions are granted based on a series of labels
- **Non-Modifiable**: Users and administrators cannot modify permissions
- **Rare Implementation**: Rarely fully implemented on production systems

#### MAC Use Cases

- **Military Systems**: Classified information handling
- **Government Systems**: Sensitive government data
- **High-Security Environments**: Critical infrastructure protection
- **Compliance Requirements**: Systems requiring strict access control

#### MAC Implementation Challenges

- **Complexity**: Difficult to implement and maintain
- **Flexibility**: Limited flexibility for changing requirements
- **Cost**: High implementation and operational costs
- **User Impact**: Can impact user productivity

### Discretionary Access Control (DAC)

Discretionary access control (DAC) systems allow users to assign access
permissions to other users—the owners of files, computers, and other resources
have the discretion to configure permissions as they see fit.

#### DAC Characteristics

- **Owner Control**: Resource owners control access permissions
- **Flexible**: Users can modify permissions on their resources
- **ACL-Based**: Uses access control lists (ACL) for permission management
- **Common Implementation**: Widely used in most operating systems

#### DAC Implementation

- **Access Control Lists**: Users change permissions on ACLs
- **Ownership Model**: Resource owners have full control
- **Inheritance**: Permissions can be inherited from parent objects
- **Granular Control**: Fine-grained permission management

#### DAC Advantages

- **Flexibility**: Easy to modify permissions
- **User Control**: Users control their own resources
- **Simplicity**: Relatively simple to implement
- **Wide Support**: Supported by most systems

#### DAC Disadvantages

- **Security Risk**: Users may grant excessive permissions
- **Inconsistent**: Can lead to inconsistent security policies
- **Difficult Auditing**: Hard to audit and monitor
- **Privilege Escalation**: Risk of privilege escalation

### Role-Based Access Control (RBAC)

In role-based access control (RBAC) systems, administrators assign users to roles
based upon their job responsibilities and assign the permissions necessary to
carry out different jobs to those roles.

#### RBAC Characteristics

- **Role-Based**: Permissions are assigned to roles, not users
- **Job-Focused**: Roles based on job responsibilities
- **Administrative Control**: Administrators manage role assignments
- **Scalable**: Efficient for large organizations

#### RBAC Implementation Process

1. **Role Definition**: Define roles based on job functions
2. **Permission Assignment**: Assign permissions to roles
3. **User Assignment**: Assign users to appropriate roles
4. **Regular Review**: Periodically review role assignments

#### RBAC Models

- **Core RBAC**: Basic role-based access control
- **Hierarchical RBAC**: Roles can inherit from other roles
- **Constrained RBAC**: Additional constraints on role assignments
- **Symmetric RBAC**: Bidirectional role-permission relationships

#### RBAC Advantages

- **Scalability**: Efficient for large user populations
- **Consistency**: Consistent permission management
- **Auditability**: Easy to audit and review
- **Compliance**: Supports regulatory compliance requirements

## Account Types

### User Accounts

- **Purpose**: Typically everyone has a user account, but accounts may have
  different privileges
- **Management**: Should be routinely monitored for compromises
- **Lifecycle**: Should follow a lifecycle management process for creation and
  removal
- **Security**: Regular password changes and access reviews

### Administrator Accounts

- **Purpose**: Have extensive privileges to modify configurations
- **Security**: Should be carefully guarded using privileged account management
  (PAM)
- **Monitoring**: Every action should be logged and monitored
- **Separation**: Administrators typically have user accounts as well for routine
  tasks

### Guest Accounts

- **Purpose**: Grants temporary access to resources
- **Requirements**: Should be tied to a unique individual
- **Expiration**: Should expire after a period of time
- **Limitations**: Limited access to system resources

### Shared/Generic Accounts

- **Definition**: Accounts shared by more than one user
- **Security Risk**: Bad idea from a security perspective
- **Problems**: Difficult to audit, violates accountability
- **Best Practice**: Avoid shared accounts when possible

### Service Accounts

- **Purpose**: Typically used internally by a system to run a process or perform
  other actions
- **Privileges**: Typically have privileged access and should be carefully
  controlled
- **Usage**: Should not be used to log in to the system interactively
- **Management**: Regular review and rotation of credentials

## Non-Repudiation

### Non-Repudiation Definition

Non-repudiation uses technical measures to ensure that a user is not able to
later deny that they took some action.

### Non-Repudiation Concept Explanation

Repudiation means denying something is true. Non-repudiation is a security goal
that prevents someone from falsely denying that something is true.

### Non-Repudiation Technical Measures

- **Digital Signatures**: Cryptographic proof of action
- **Audit Logs**: Comprehensive logging of all actions
- **Timestamping**: Time-stamped records of activities
- **Authentication**: Strong authentication mechanisms
- **Encryption**: Secure communication channels

### Non-Repudiation Implementation

- **Digital Certificates**: Use of PKI for authentication
- **Audit Trails**: Complete record of user actions
- **Secure Logging**: Tamper-proof log systems
- **Legal Compliance**: Support for legal requirements

### Non-Repudiation Use Cases

- **Financial Transactions**: Banking and payment systems
- **Legal Documents**: Contract signing and verification
- **Healthcare**: Medical record access and modifications
- **Government**: Official communications and actions

## Access Control Implementation

### Access Control Lists (ACLs)

- **Definition**: Lists that specify which users or groups have access to
  resources
- **Implementation**: Used in DAC systems
- **Management**: Resource owners control ACLs
- **Granularity**: Can specify different permissions (read, write, execute)

### Access Control Matrix

- **Definition**: Table showing permissions for users and resources
- **Use**: Theoretical model for access control
- **Implementation**: Basis for ACL and capability systems
- **Scalability**: Can become unwieldy in large systems

### Capability-Based Access Control

- **Definition**: Users hold capabilities (tokens) that grant access
- **Characteristics**: Object-oriented approach to access control
- **Security**: Capabilities cannot be forged or modified
- **Implementation**: Used in some high-security systems

## Real-World Applications

### Financial Services

- **RBAC Implementation**: Role-based access for different job functions
- **Segregation of Duties**: Separate roles for transaction initiation and
  approval
- **Non-Repudiation**: Digital signatures for financial transactions
- **Audit Requirements**: Comprehensive logging for compliance

### Healthcare

- **HIPAA Compliance**: Role-based access to patient data
- **Least Privilege**: Minimum access necessary for patient care
- **Audit Trails**: Complete logging of data access
- **Emergency Access**: Break-glass procedures for emergencies

### Technology Companies

- **Development Teams**: Separate roles for development and deployment
- **Service Accounts**: Managed service accounts for applications
- **Privileged Access**: Controlled access to production systems
- **Continuous Monitoring**: Real-time access monitoring

## Best Practices

### For Organizations

- **Regular Reviews**: Periodic review of access permissions
- **Documentation**: Comprehensive documentation of access policies
- **Training**: Regular training on access control principles
- **Monitoring**: Continuous monitoring of access activities
- **Incident Response**: Procedures for access control violations

### For IT Teams

- **Automation**: Use automated tools for access management
- **Standardization**: Standardize access control procedures
- **Testing**: Regular testing of access control mechanisms
- **Backup Procedures**: Backup and recovery procedures for access systems
- **Vendor Management**: Manage third-party access appropriately

## Summary

Effective logical access controls require:

- **Clear Principles**: Understanding least privilege and segregation of duties
- **Appropriate Models**: Choosing the right access control model (MAC, DAC, RBAC)
- **Account Management**: Proper management of different account types
- **Non-Repudiation**: Technical measures to prevent denial of actions
- **Continuous Monitoring**: Ongoing oversight and review

Key success factors:

- **Policy Development**: Clear access control policies
- **User Training**: Training users on access control principles
- **Regular Audits**: Periodic audits of access permissions
- **Technology Integration**: Effective use of access control technologies
- **Incident Response**: Procedures for access control violations

Understanding logical access controls is essential for cybersecurity professionals
and helps organizations protect information assets while maintaining operational
efficiency and regulatory compliance.
