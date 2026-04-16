#!/usr/bin/python3
"""This module handles conversion between dictionaries and XML files."""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Save dictionary data into an XML file."""
    root = ET.Element("data")

    for key in dictionary:
        value = dictionary[key]

        element = ET.Element("item")
        element.attrib["key"] = str(key)
        element.attrib["type"] = type(value).__name__
        element.text = str(value)

        root.append(element)

    ET.ElementTree(root).write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """Load XML data and rebuild it into a dictionary."""
    root = ET.parse(filename).getroot()

    result = {}

    converters = {
        "int": int,
        "float": float,
        "bool": lambda x: x == "True",
        "NoneType": lambda x: None
    }

    for element in root:
        key = element.attrib.get("key")
        raw_value = element.text
        value_type = element.attrib.get("type")

        if value_type in converters:
            value = converters[value_type](raw_value)
        else:
            value = raw_value

        result[key] = value

    return result
