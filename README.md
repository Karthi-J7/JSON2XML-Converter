# JSON2XML-Converter
Welcome to the JSON to XML Converter! This project is a command-line tool designed to convert JSON files into a specific XML format. It takes a JSON input file and converts it into an XML file, preserving the structure and data types of the JSON content.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Files](#files)
- [Contributing](#contributing)
- [License](#license)

## Introduction
The JSON to XML Converter is a Python-based tool that reads a JSON file and converts its contents into an XML format. The tool handles various data types such as objects, arrays, strings, numbers, booleans, and null values, ensuring the XML output accurately reflects the original JSON structure.

## Features
- Converts JSON files to XML format.
- Supports nested objects and arrays.
- Preserves data types in the XML output.
- Command-line interface for easy use.
- Error handling for invalid JSON files and missing input files.

## Installation
To use the JSON to XML Converter, you need to have Python installed on your system. Follow these steps to set up the project:

1. Clone the repository:
```shell
git clone https://github.com/yourusername/json-to-xml-converter.git
```
2. Navigate to the project directory:
```shell
cd json-to-xml-converter
```

## Usage
The JSON to XML Converter can be used via the command line. It requires two arguments: the input JSON file and the output XML file location.
```commandline
python json_to_xml.py input.json output.xml
```
### Arguments
- input.json: Path to the input JSON file.
- output.xml: Path where the output XML file will be saved.

## Example
Here is an example demonstrating how to use the JSON to XML Converter:
1. Create a JSON file named demo.json with the following content:
```json
{
    "organization": {
        "name": "Securin",
        "type": "Inc",
        "building_number": 4,
        "floating": -17.4,
        "null_test": null
    },
    "security_related": true,
    "array_example0": ["red", "green", "blue", "black"],
    "array_example1": [1, "red", [{"nested": true}], {"obj": false}]
}
```
2. Run the JSON to XML Converter:
```commandline
python json_to_xml.py demo.json demo.xml
```
3. The output XML file demo.xml will contain:
```xml
<object>
<object name="organization">
<string name="name">
Securin
</string>
<string name="type">
Inc
</string>
<number name="building_number">
4
</number>
<number name="floating">
-17.4
</number>
<null name="null_test"/>
</object>
<boolean name="security_related">
True
</boolean>
<array name="array_example0">
<string>
red
</string>
<string>
green
</string>
<string>
blue
</string>
<string>
black
</string>
</array>
<array name="array_example1">
<number>
1
</number>
<string>
red
</string>
<array>
<object>
<boolean name="nested">
True
</boolean>
</object>
</array>
<object>
<boolean name="obj">
False
</boolean>
</object>
</array>
</object>
```

## Files
- `json_to_xml.py`: Main script for converting JSON to XML.
- `banner.txt`: ASCII art banner displayed when running the script.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request on GitHub.

## License
This project is licensed under the MIT License. See the LICENSE file for details.