import argparse
import json
import yaml
import xmltodict
import os

def parse_args():
    parser = argparse.ArgumentParser(description="Konwerter plikow JSON, XML i YAML")
    parser.add_argument("input_file", help="Plik wejsciowy do konwersji")
    parser.add_argument("output_file", help="Plik wyjsciowy po konwersji")
    return parser.parse_args()

def read_json(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)

def write_json(file_path, data):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

def read_yaml(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)

def write_yaml(file_path, data):
    with open(file_path, "w", encoding="utf-8") as file:
        yaml.dump(data, file)

def read_xml(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return xmltodict.parse(file.read())

def write_xml(file_path, data):
    # Ensure the data has one root element
    if len(data) == 1:
        xml_data = xmltodict.unparse(data, pretty=True)
    else:
        xml_data = xmltodict.unparse({"root": data}, pretty=True)
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(xml_data)

def get_file_extension(file_path):
    return os.path.splitext(file_path)[1].lower()

def main():
    args = parse_args()

    input_ext = get_file_extension(args.input_file)
    output_ext = get_file_extension(args.output_file)

    if input_ext == ".json":
        data = read_json(args.input_file)
        print("Dane JSON załadowane pomyslnie")
    elif input_ext in [".yaml", ".yml"]:
        data = read_yaml(args.input_file)
        print("Dane YAML załadowane pomyslnie")
    elif input_ext == ".xml":
        data = read_xml(args.input_file)
        print("Dane XML załadowane pomyslnie")
    else:
        raise ValueError("Nieobslugiwany format pliku wejsciowego")

    if output_ext == ".json":
        write_json(args.output_file, data)
        print("Dane zapisane w formacie JSON")
    elif output_ext in [".yaml", ".yml"]:
        write_yaml(args.output_file, data)
        print("Dane zapisane w formacie YAML")
    elif output_ext == ".xml":
        write_xml(args.output_file, data)
        print("Dane zapisane w formacie XML")
    else:
        raise ValueError("Nieobslugiwany format pliku wyjsciowego")

if __name__ == "__main__":
    main()