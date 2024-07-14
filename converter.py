import argparse
import json
import xmltodict
import yaml

def read_json(file_path):
    with open(file_path, 'r') as file:
        try:
            data = json.load(file)
            print("Dane JSON załadowane pomyślnie")
            return data
        except json.JSONDecodeError as e:
            print(f"Błąd podczas odczytu pliku JSON: {e}")
            return None

def write_json(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
        print("Dane zapisane do pliku JSON pomyślnie")

def read_xml(file_path):
    with open(file_path, 'r') as file:
        data = xmltodict.parse(file.read())
        print("Dane XML załadowane pomyślnie")
        return data

def write_xml(file_path, data):
    with open(file_path, 'w') as file:
        xml_data = xmltodict.unparse(data, pretty=True)
        file.write(xml_data)
        print("Dane zapisane do pliku XML pomyślnie")

def read_yaml(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
        print("Dane YAML załadowane pomyślnie")
        return data

def write_yaml(file_path, data):
    with open(file_path, 'w') as file:
        yaml.dump(data, file, default_flow_style=False)
        print("Dane zapisane do pliku YAML pomyślnie")

def main():
    parser = argparse.ArgumentParser(description='Konwersja plików między formatami .xml, .json i .yml.')
    parser.add_argument('input_file', type=str, help='Ścieżka do pliku wejściowego')
    parser.add_argument('output_file', type=str, help='Ścieżka do pliku wyjściowego')
    
    args = parser.parse_args()
    
    print(f'Plik wejściowy: {args.input_file}')
    print(f'Plik wyjściowy: {args.output_file}')

    data = None
    if args.input_file.endswith('.json'):
        data = read_json(args.input_file)
    elif args.input_file.endswith('.xml'):
        data = read_xml(args.input_file)
    elif args.input_file.endswith('.yaml') or args.input_file.endswith('.yml'):
        data = read_yaml(args.input_file)
    
    if data is None:
        print("Błąd podczas odczytu danych.")
        return

    if args.output_file.endswith('.json'):
        write_json(args.output_file, data)
    elif args.output_file.endswith('.xml'):
        write_xml(args.output_file, data)
    elif args.output_file.endswith('.yaml') or args.output_file.endswith('.yml'):
        write_yaml(args.output_file, data)
    else:
        print("Nieobsługiwany format pliku wyjściowego.")

if __name__ == "__main__":
    main()
