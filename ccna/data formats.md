# Data Formats

## Overview

In the previous chapter, we established that communication between software applications on different devices is essential for network automation. We also covered one essential part of making that possible: application programming interfaces (APIs). APIs open up an application's data to allow external applications to access it in an efficient and uniform manner. In this chapter, we'll cover the second half of the puzzle. For successful communication between applications, it's not enough for App A to be able to access App B's data; the data itself must be in a format that App A understands. That's the role of data serialization formats—standardized data formats that allow applications to communicate data in an agreed-upon format that both parties understand.

## Data Serialization Fundamentals

### Why Data Serialization is Needed

- Applications, which can be developed in many different programming languages, store and interpret data in different ways
- Without using a data serialization format, different applications cannot interpret each other's internal data structures
- Just as standardized protocols enable communications between devices over a network, standardized data formats enable applications to communicate data effectively

### What is Data Serialization?

- **Data serialization** is the process of converting data into a standardized format suitable for storage or transmission
- The data serialization process takes an application's data structures from a computer's memory and converts them into a series of bytes (hence the term serialization) that can be stored in a file or transmitted over a network
- This process enables the data to be later reconstructed (i.e., by a different application)
- Data formats used for this purpose are called **data serialization formats**
- In this chapter, we'll cover three:
  - JavaScript Object Notation (JSON)
  - Extensible Markup Language (XML)
  - YAML Ain't Markup Language (YAML)

### How Data Serialization Works

- Data serialization enables an application to communicate its data to another application in a format both parties understand
- App C's API converts its data structures into JSON-formatted data, allowing Apps A and B to interpret and reconstruct the data in their own languages
- The term data serialization might sound complex, but it just means converting data into a format that's easy to store or transfer
- JSON, XML, and YAML are all standard data formats that many applications can understand, making them common choices for sharing data among different applications

## JavaScript Object Notation (JSON)

### JSON Overview

- **JavaScript Object Notation (JSON)** is an open-standard data serialization format
- It was originally derived from JavaScript, but is language independent
- Applications in many programming languages can generate and interpret JSON-formatted data
- REST APIs often support JSON, which is likely why Cisco chose to include JSON as a CCNA exam topic
- One of JSON's main characteristics is its human readability
- Although it is designed for communication between computer applications, properly formatted JSON data is easy for us to read, too

### JSON Example

- Example of JSON-formatted data:

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

- Even if you don't know anything about JSON yet, you can read and understand that data
- It's composed of a series of **variables**—logical containers for values—and the values they hold
- For example, the variable "interface_name" holds the value "GigabitEthernet1/1"
- You can deduce that the data pertains to an interface with specific characteristics:
  - Its name is GigabitEthernet1/1
  - Its status is up
  - Its IP address is 192.168.1.1
  - Its netmask is 255.255.255.0
  - Its speed is 1000 (Mbps)
  - It currently has no description

### JSON Primitive Data Types

- JSON is explicitly mentioned in exam topic 6.7: Recognize components of JSON-encoded data
- Make sure that you can differentiate between the different data types we cover and interpret simple JSON-formatted data
- JSON data is represented using four fundamental forms called **primitive data types**:
  - **String**: An alphanumeric text value. JSON strings are always enclosed in double quotes
    - Examples: "Hello.", "5", "true", "null"
  - **Number**: A numeric value
    - Examples: 5, 101.25
  - **Boolean**: A data type with only two possible values: true and false
  - **Null**: A data type that represents the intentional absence of a value and is always represented as null

### Important Notes on Primitive Types

- Take a close look at the examples for strings: "5" is a string, not a number; "true" is a string, not a Boolean; "null" is a string, not null
- Any value enclosed in double quotes is a string (a text value), even if it would be a different data type without double quotes
- The key of each key-value pair is a string
- Each of the four primitive data types is present in the values
- The JSON Boolean and null data types must be lowercase: true, false, and null

### JSON Structured Data Types

- While primitive data types in JSON represent singular values, **structured data types**, as the name implies, are used to organize information into more complex structures
- JSON has two structured data types:
  - **Object**: An unordered set of key-value pairs
  - **Array**: An ordered set of values

### JSON Objects

- A JSON **object** is an unordered set of key-value pairs
- **Unordered** means that the order of the key-value pairs in the object is insignificant; they can be reordered without affecting the meaning of the object
- Important points about objects:
  - Objects are enclosed in curly braces
  - The key of each key-value pair must be a string
  - The value of each key-value pair can be any valid JSON data type: string, number, Boolean, null, or even another object (or array)
  - The key and value of each key-value pair are separated by a colon
  - If there are multiple key-value pairs, each pair is separated by a comma
  - There must not be a trailing comma after the final key-value pair

### Nested Objects

- In all of the previous examples' key-value pairs, the value is a primitive data type: string, number, Boolean, or null
- However, structured data types are also valid values for an object's key-value pairs
- These "objects within objects" are called **nested objects**
- Example showing an object that contains two key-value pairs, where the value of each key is a nested object with its own set of key-value pairs

### Whitespace in JSON

- **Whitespace**—including spaces, line breaks, and tabs—is insignificant in terms of data interpretation
- All of the examples shown so far have used whitespace to enhance their readability, but that whitespace has no actual meaning in JSON
- The same JSON data can be written with all whitespace removed and it will have the same meaning

### JSON Arrays

- A JSON **array** is an ordered set of values
- The following example is a JSON object with two key-value pairs; the value of each is an array containing multiple values
- The "interfaces" array contains three strings, and the "random_values" array contains four values of different data types: a string, a number, a Boolean, and null
- Important points about arrays:
  - Arrays are enclosed in square brackets
  - The values can be of any valid JSON data type
  - The values don't have to be of the same data type
  - The values are separated by commas
  - There must not be a trailing comma after the final value

### Invalid JSON Examples

- A single error like a misplaced comma will render JSON data invalid, so precision is essential
- Common errors in invalid JSON:
  - Booleans must be lowercase: true, not TRUE
  - Null must be lowercase: null, not NULL
  - Missing comma after a key-value pair
  - Invalid character separating key from value (must use colon, not dash)
  - Trailing comma after final key-value pair or final array value
  - Missing closing curly brace or square bracket
- If you want to validate JSON data, you can use a website like <https://jsonlint.com/>
- Paste the data and click Validate JSON; it will indicate whether the data is valid or not

### JSON Practice Example

- Example JSON data for practice:

```json
{
  "deviceName": "Switch-01",
  "location": "Office Building B",
  "deviceType": "Switch",
  "firmwareVersion": "4.5.7",
  "uptimeHours": 1023,
  "managementAccess": {
    "enabled": true,
    "port": "22"
  },
  "allowedIPs": ["192.168.1.100", "192.168.1.101", "192.168.1.102"],
  "lastUpdated": null
}
```

- Key points to identify:
  - The value of "allowedIPs" is an array, not an object
  - The value of "port" is a string (enclosed in double quotes), not a number
  - There is one nested object (the value of "managementAccess")
  - This is valid JSON data

## Extensible Markup Language (XML)

### XML Overview

- **Extensible Markup Language (XML)** is a data serialization format with syntax similar to HyperText Markup Language (HTML), which is the standard markup language for web pages
- A **markup language** is used for annotating documents (i.e., web pages), specifying structure, and formatting
- XML has become a popular choice to format data for storage and transmission, although it is less common than JSON or YAML
- Like JSON, XML is commonly supported by REST APIs

### XML Syntax

- XML uses HTML-like tags for its key-value pairs, with an opening and closing tag: `<key>value</key>`
- Interestingly, many Cisco IOS **show** commands can be displayed in XML format by adding **| format** to the end of the command
- Example: **show ip interface brief | format** displays the output in XML format
- XML is generally considered less human readable than JSON, but you can probably decipher the meaning of the output
- Like JSON, whitespace in XML is insignificant, but it's usually formatted to make it more readable
- The same output with whitespace removed is easy for a computer to read, but not so readable for a human!

## YAML Ain't Markup Language (YAML)

### YAML Overview

- **YAML Ain't Markup Language (YAML)**—it rhymes with "camel"—is another popular data serialization format
- YAML originally stood for "Yet Another Markup Language," but it was officially renamed to the recursive acronym "YAML Ain't Markup Language" to emphasize its purpose as a data serialization format rather than a document markup language
- YAML is quite readable; of the three formats we have covered, it is perhaps the most human friendly

### YAML Syntax

- One of the notable differences between YAML and JSON/XML is that **whitespace is significant in YAML**
- Proper indentation in YAML is not just about readability; it defines the structure and hierarchy of the data
- Compared to JSON and XML, YAML-formatted data looks quite minimalistic, contributing to its readability
- In YAML, the structure of the data is defined through indentation levels without the need for many additional markers like those found in JSON (like commas and curly braces) or the tag structure of XML
- The same data represented in JSON requires more syntax (curly braces, commas, square brackets, etc.)

## Summary

- Data serialization is the process of converting data into a standardized format suitable for storage or transmission. This process enables the data to be later reconstructed (i.e., by a different application)
- Data serialization formats like JSON, XML, and YAML enable an application to communicate its data to another application in a format that both parties understand
- JavaScript Object Notation (JSON) is a human-readable data serialization format. Applications in many programming languages can generate and interpret JSON-formatted data, and REST APIs often support JSON
- A variable is a logical container for values. A variable and its value are often called a key-value pair
- JSON data is represented using four fundamental forms called primitive data types
- A JSON string is a text value that is enclosed in double quotes, such as "Hello.", "5", "true", and "null"
- A JSON number is a numeric value, such as 5 or 101.25
- The JSON Boolean data type has only two possible values: true and false
- The JSON null data type represents the intentional absence of a value and is always represented as null
- Any value enclosed in double quotes is a string (a text value), even if it would be a different data type without double quotes (i.e., "5")
- The JSON Boolean and null data types must be lowercase: true, false, and null
- JSON structured data types (object and array) are used to organize information into more complex structures
- A JSON object is an unordered set of key-value pairs. Unordered means that the order of the key-value pairs in an object is insignificant
- Important points about objects:
  - Objects are enclosed in curly braces
  - The key of each key-value pair must be a string
  - The value of each key-value pair can be any valid JSON data type
  - The key and value of each key-value pair are separated by a colon
  - If there are multiple key-value pairs, each pair is separated by a comma
  - There must not be a trailing comma after the final key-value pair
- Structured data types (object/array) are valid values for an object's key-value pairs
- An object within an object is called a nested object
- Whitespace—spaces, line breaks, and tabs—is insignificant in JSON. Whitespace is often used to enhance readability, but it doesn't affect the data's meaning
- A JSON array is an ordered set of values. Important points about arrays:
  - Arrays are enclosed in square brackets
  - The values can be of any valid JSON data type
  - The values don't have to be of the same data type
  - The values are separated by commas
  - There must not be a trailing comma after the final value
- A single error like a misplaced comma will render JSON data invalid, so precision is essential
- Extensible Markup Language (XML) is a data serialization format with syntax similar to HyperText Markup Language (HTML), which is the standard markup language for web pages
- XML is a popular choice as a data serialization format used to format data for storage and transmission. Like JSON, it is commonly supported by REST APIs
- XML uses HTML-like tags for its key-value pairs, with an opening and closing tag: `<key>value</key>`
- Many Cisco IOS commands can be displayed in XML by adding **| format** to the end of the command, such as **show ip interface brief | format**
- Whitespace in XML is insignificant
- YAML Ain't Markup Language (YAML)—formerly "Yet Another Markup Language"—is a popular data serialization format known for being human friendly
- Whitespace is significant in YAML. Proper indentation is not just important for readability; it defines the structure and hierarchy of the data
