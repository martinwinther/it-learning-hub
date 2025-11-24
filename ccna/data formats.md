# Data Formats

## Overview

Data formats define how application data is encoded so different systems can exchange and interpret it. For CCNA, focus on recognizing JSON, XML, and YAML, and understanding basic structure and data types.

## Data serialization basics

### Purpose of serialization

- Applications store data in language-specific structures
- Directly sharing those internal structures is not practical across systems
- Standard data formats provide:
  - A common way to represent data
  - A byte stream that can be stored or sent over the network
  - A way for another application to reconstruct the original data

### Definition

- Data serialization: convert in-memory data structures into a standard, portable format
- Deserialization: reconstruct data structures from that format on the receiving side
- Common text-based formats in networking:
  - JSON
  - XML
  - YAML

## JavaScript Object Notation (JSON)

### JSON overview

- JavaScript Object Notation (JSON) is a text-based data serialization format
- Origin in JavaScript, but language independent
- Widely used in REST APIs and network automation
- Human readable and easy for machines to parse

### JSON example

```json
{
  "interface_name": "GigabitEthernet1/1",
  "is_up": true,
  "ip_address": "192.168.1.1",
  "netmask": "255.255.255.0",
  "speed": 1000,
  "description": null
}
```

Key points:

- Curly braces enclose an object
- Data is stored as key-value pairs
- Keys are strings in double quotes
- Values can be different data types

### JSON primitive types

Primitive value types:

- String
  - Text in double quotes
  - Examples: `"Hello"`, `"5"`, `"true"`, `"null"`
- Number
  - Numeric value
  - Examples: `5`, `101.25`
- Boolean
  - `true` or `false` (lowercase)
- Null
  - Intentional absence of a value, written as `null` (lowercase)

Notes:

- Anything in double quotes is a string, even if it looks numeric or Boolean
- Keys in key-value pairs are always strings
- Boolean and null keywords must be lowercase

### JSON structured types

Structured types organize data:

- Object
  - Unordered set of key-value pairs
  - Enclosed in `{ }`
- Array
  - Ordered list of values
  - Enclosed in `[ ]`

Values in objects and arrays can be any valid JSON type (primitive or structured).

### JSON objects and nesting

Object rules:

- Enclosed in curly braces
- Key-value pairs separated by commas
- Key and value separated by a colon
- No trailing comma after the last pair

Nested objects:

- A value in a key-value pair can be another object
- Nested objects allow hierarchy (for example, device → interface → settings)

### JSON arrays

Array rules:

- Enclosed in square brackets
- Values separated by commas
- No trailing comma after the last value
- Values can mix data types

Example with arrays and nesting:

```json
{
  "deviceName": "Switch-01",
  "management": {
    "enabled": true,
    "port": "22"
  },
  "allowedIPs": [
    "192.168.1.100",
    "192.168.1.101",
    "192.168.1.102"
  ],
  "lastUpdated": null
}
```

Key points:

- `allowedIPs` is an array of strings
- `management` is a nested object
- `port` is a string, not a number

### Whitespace and validity

Whitespace:

- Spaces, tabs, and newlines are ignored by JSON parsers
- Used only for readability

Common validity issues:

- Uppercase Boolean or null: `TRUE`, `FALSE`, `NULL`
- Missing comma between pairs or values
- Trailing comma after the last element
- Wrong separator between key and value (must be colon)
- Missing closing brace or bracket

## Extensible Markup Language (XML)

### XML overview

- Extensible Markup Language (XML) is a text-based data format
- Syntax style is similar to HTML
- Used for structured data storage and transport
- Supported by many network and management APIs

Many Cisco IOS show commands can output XML with the `| format` keyword.

### XML syntax

Basic structure:

- Uses opening and closing tags: `<key>value</key>`
- Tags define structure and meaning
- Attributes can appear inside tags
- Whitespace is usually ignored, used mainly for readability

Conceptually similar to JSON objects and arrays but expressed with tags instead of braces and brackets.

## YAML Ain't Markup Language (YAML)

### YAML overview

- YAML Ain't Markup Language (YAML) is a human-friendly data format
- Text-based and commonly used for configuration files and automation tools
- Often preferred for playbooks, templates, and configuration definitions

### YAML syntax

Key characteristics:

- Whitespace and indentation are significant
- Indentation defines structure and hierarchy
- No braces, quotes, or commas required in many cases
- Lists are usually written with dashes
- The same data that needs more punctuation in JSON can be shorter in YAML

YAML is easy to read, but strict indentation rules mean that spacing errors break the structure.

## Quick review

- Data serialization converts in-memory data into a standard format that can be stored or transmitted and later reconstructed.
- JSON, XML, and YAML are common text-based formats used in networking and automation.
- JSON:
  - Uses key-value pairs with objects `{ }` and arrays `[ ]`
  - Supports string, number, Boolean, null, object, and array
  - Booleans and null must be lowercase
- XML:
  - Uses nested tags like `<key>value</key>`
  - Often available as an alternate output format for device commands
- YAML:
  - Uses indentation to define structure
  - Designed for readability and often used for configuration files.
