# Simple Windows Domain Overview

## Simple setup

A simplest Windows domain can be imagined as one Windows Server acting as the domain controller and one joined client PC used by a user.

## What AD DS does

Active Directory Domain Services (AD DS) stores the domain’s identities and structure, including users, computers, groups, and policies. It allows the domain controller to handle logons and central management instead of every machine being managed separately.

## How DNS works inside the domain

DNS helps the client find important domain services by resolving names such as the domain name and the domain controller’s hostname to the correct internal IP address. That is how the client knows where to send authentication and directory requests.

## How DHCP fits in

DHCP automatically hands out IP configuration to the client, including its IP address, subnet mask, default gateway, and usually the domain DNS server address. This lets the PC get on the network with the correct settings and locate the domain controller without manual setup.