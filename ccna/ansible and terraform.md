# Ansible and Terraform

## Overview

- Topic: CCNA 6.6, configuration management mechanisms (Ansible, Terraform, Puppet, Chef).
- Goal: automate and standardize network device configuration.
- Manual CLI configuration scales poorly in larger networks and leads to configuration drift.

## Configuration management fundamentals

### Configuration management

- Maintain, control, and document network device configurations.
- Critical in larger environments.
- Built on:
  - Common standards
  - Processes to deploy and update configurations
  - Methods to keep devices consistent

### Configuration standards

Shared configuration elements across most devices:

- DNS servers
- NTP servers
- Routing protocols and common settings
- QoS policies
- AAA (RADIUS or TACACS+) servers
- Security policies (ACL patterns, basic firewall rules)
- Logging and monitoring (syslog and SNMP targets)

Device-specific values:

- IP addresses
- Hostnames
- Interface-specific details

Idea: start from a standard baseline, then add only required differences.

### Developing standards

- Based on:
  - Network requirements
  - Security and performance best practices
  - Input from security, server, and network teams, plus vendors
- Usually produced by senior staff.
- Day-to-day work often focuses on implementing and maintaining these standards.

### Configuration drift

- Over time, configurations move away from standards.
- Causes:
  - Manual changes on single devices
  - Human error
  - Different interpretation of standards
  - Emergency fixes that never get cleaned up
- Effects:
  - Inconsistent behavior
  - Security gaps
  - Harder troubleshooting

### Problems with manual management

- Inconsistent configurations across devices
- Higher chance of mistakes
- No realistic way to keep large networks aligned with standards using only per-device CLI work
- Hard to see differences and roll back safely

## Configuration management tools

### Tool model

- Central server stores desired configurations and pushes or pulls them to devices.
- Typical pieces:
  - Template files that describe the desired state
  - Variable files with per-device values
  - Logic that applies changes to the right devices
- Benefits:
  - Less configuration drift
  - Faster and more repeatable changes
  - Easier auditing and rollback

### Templates and variables

- Template:
  - Base configuration with placeholders.
- Variables:
  - Values for each device or group (IP, hostname, site, role).
- Same template can generate configurations for many similar devices.
- Edit template or variable file, then reapply to update all affected devices.

### Configuration enforcement

- Tools compare running device configurations with the desired state.
- Deviations:
  - Reported to admins
  - Optionally corrected automatically
- Checks can run on a schedule or on demand.

## Configuration management tool comparison

### Infrastructure as Code (IaC)

- Ansible, Terraform, Puppet, and Chef all treat infrastructure as code.
- Desired state stored in text files under version control.
- Same configurations reused across environments (lab, test, production).
- Automation covers:
  - Provisioning
  - Ongoing changes
  - Decommissioning

### Common characteristics

When comparing tools, pay attention to:

- Language: implementation language is mostly trivia, but shows ecosystem (Python, Go, Ruby).
- Configuration format: YAML, HCL, or a custom DSL.
- Communication: SSH, APIs, or agents.
- Agent-based vs agentless:
  - Agent-based: software installed on each managed node.
  - Agentless: uses existing services such as SSH.
- Procedural vs declarative:
  - Procedural: list of steps.
  - Declarative: describe end state, tool finds the steps.
- Push vs pull:
  - Push: server initiates changes.
  - Pull: devices regularly fetch desired configuration.

## Ansible

### Ansible basics

- Agentless configuration management tool from Red Hat.
- Written in Python and uses YAML for most files.
- Uses SSH from a control node to managed devices.
- Often used for network device configuration.

### Architecture

- Push model:
  - Control node connects to devices over SSH and sends changes.
- Mainly procedural:
  - Tasks run in the order defined.

Key components:

- Inventory: list of managed hosts, usually grouped and with variables.
- Templates: Jinja2 files with configuration syntax and variables.
- Variable files: YAML files with values that fill templates.
- Playbooks: YAML files that define tasks and workflows.
- Modules: units of work used in playbooks.
- Tasks: single actions in a playbook.

Notes:

- No agent required on network devices.
- Good fit for networks where devices already support SSH.

## Terraform

### Terraform basics

- Infrastructure as code tool from HashiCorp.
- Main focus: provisioning new infrastructure (cloud, on-prem, networks).
- Often combined with Ansible:
  - Terraform provisions resources.
  - Ansible configures them.

### Architecture and workflow

- Agentless push model.
- Workflow:
  1. Write: define desired state in configuration files.
  2. Plan: show what changes will occur.
  3. Apply: make changes to reach desired state.

### Terraform core concepts

- Terraform Core:
  - Reads configuration files.
  - Tracks current state in a state file.
  - Decides what to create, change, or destroy.
- Declarative:
  - Configuration files describe the target state.
  - Core calculates the actions needed.

### Providers

- Providers integrate Terraform with platforms via APIs, for example:
  - AWS, Azure, and GCP
  - VMware vSphere and OpenStack
  - Kubernetes
  - Cisco platforms such as Catalyst Center, ACI, and IOS XE
- Each provider adds resources and data sources Terraform can manage.

### HashiCorp Configuration Language (HCL)

- Terraform configurations use HCL.
- Domain-specific language focused on describing infrastructure.
- Designed for readability and for describing relationships between resources.

## Puppet and Chef

### Puppet

- Configuration management IaC tool written in Ruby.
- Agent-based pull model:
  - Agents on managed devices connect to a Puppet master to get configurations.
- Uses a declarative DSL (Puppet DSL):
  - Desired state described, agents enforce it.
- Less common in networking because many devices do not support the agent.

### Chef

- Ruby-based configuration management tool.
- Agent-based pull model:
  - Chef client on each device pulls from a Chef server.
- Procedural approach:
  - Recipes define steps.
  - Cookbooks group related recipes, templates, and files.
- Limited use for network devices, similar to Puppet.
- Important characteristics to remember:
  - Pull model and agent requirements.
  - Procedural vs declarative styles.

## Choosing a configuration management tool

Key decision points:

- Device support:
  - No agent support on network devices makes agentless tools more attractive.
- Push vs pull:
  - Push: better for centralized control and urgent changes.
  - Pull: spreads load but updates wait for the next check-in.
- Use case:
  - Day-to-day network configuration: often Ansible.
  - Large scale provisioning across clouds and data centers: often Terraform.
- Team skills:
  - YAML, Jinja2, and Python ecosystem for Ansible.
  - HCL and provider ecosystem for Terraform.
  - Ruby and each tool's DSL for Puppet and Chef.

## Quick summary

- Manual CLI configuration does not scale and causes configuration drift.
- Configuration management tools centralize templates and variables and automate changes.
- IaC tools to know for CCNA topic 6.6:
  - Ansible: agentless, SSH, push, procedural, strong for network configurations.
  - Terraform: agentless, SSH or API driven, push, declarative, strong for provisioning, uses HCL and providers.
  - Puppet: agent-based, pull, declarative DSL.
  - Chef: agent-based, pull, procedural recipes and cookbooks.
- Important axes for comparison:
  - Push vs pull
  - Agentless vs agent-based
  - Procedural vs declarative
  - Configuration management vs provisioning focus.
