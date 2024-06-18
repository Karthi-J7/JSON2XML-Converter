import sys
import json

def display_banner():
    with open('banner.txt', 'r') as fp:
        print("\033[31m")
        print(fp.read())
        print("\033[32mWelcome, JSON TO XML Converter...")
        print("For Further Help use the Command: `json2xml -h`")
        print("\033[0m")

def read_file(file_name):
    try :
        with open(file_name, 'r', encoding='utf-8') as fp:
            try: 
                content = json.load(fp)
                return content
            except json.JSONDecodeError:
                print("Not a Valid JSON File ...")
                sys.exit(0)
    except FileNotFoundError:
        print("JSON File Not Exists !!!")
        sys.exit(0)

def write_xml_file(xml_file_name, xml_content):
    with open(xml_file_name, 'w') as fp:
        fp.write(xml_content)

def isObject(content):
    return True if checkType(type(content)) == 'object' else False

def checkType(ctype):
    ctype = str(ctype)
    ctype = ctype[8 : -2]       # Extracting the data type only
    match ctype:
        case 'dict' :
            return 'object'

        case 'int':
            return 'number'

        case 'float':
            return 'number'
        
        case 'str' :
            return 'string'

        case 'NoneType' :
            return 'null'
        
        case 'bool':
            return 'boolean'
        
        case 'list':
            return 'array'

def fill_array(array, key = None):
    xml_content = f'<array name="{key}">\n' if key else '<array>\n'
    for value in array:
        ctype = checkType(type(value))
        if ctype == 'array':
            xml_content += fill_array(value)
        
        elif ctype == 'object':
            xml_content += fill_object(value)
            
        else:
            if value:
                xml_content += f'<{ctype}>\n{value}\n</{ctype}>\n'
            else:
                xml_content += f'<{ctype}>\n</{ctype}>\n'
                
    xml_content += '</array>\n'
    return xml_content

def fill_object(object, key = None):
    xml_content = f'<object name="{key}">\n' if key else '<object>\n'
    for key, value in object.items():
        ctype = checkType(type(value))
        
        if ctype == 'array':
            xml_content += fill_array(value, key)
        
        elif ctype == 'object':
            xml_content += fill_object(value, key)

        else:
            if value is not None:
                xml_content += f'<{ctype} name="{key}">\n{value}\n</{ctype}>\n'
            else:
                xml_content += f'<{ctype} name="{key}"/>\n'
                
    xml_content += '</object>\n'
    return xml_content 


display_banner()

if not 2 < len(sys.argv) < 4:
    print(f'Usage: {sys.argv[0]} Json_File XML_File')
    sys.exit(0)

json_file = sys.argv[1]
xml_file = sys.argv[2]

content = read_file(json_file)

xml_content = ''

if isObject(content):
    xml_content = fill_object(content)
    write_xml_file(xml_file_name=xml_file, xml_content=xml_content)

    
else:
    ctype = type(content)
    if content == None:
        xml = f'<{checkType(ctype)}>\n</{checkType(ctype)}>'
    else:
        xml = f'<{checkType(ctype)}>\n{content}\n</{checkType(ctype)}>'
    write_xml_file(xml_file, xml_content=xml)

print("JSON CONVERTED INTO XML")
print("XML File Stored in", sys.argv[2])