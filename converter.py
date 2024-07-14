import argparse
import json

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

def main():
    parser = argparse.ArgumentParser(description='Konwersja plików między formatami .xml, .json i .yml.')
    parser.add_argument('input_file', type=str, help='Ścieżka do pliku wejściowego')
    parser.add_argument('output_file', type=str, help='Ścieżka do pliku wyjściowego')
    
    args = parser.parse_args()
    
    print(f'Plik wejściowy: {args.input_file}')
    print(f'Plik wyjściowy: {args.output_file}')

    if args.input_file.endswith('.json'):
        data = read_json(args.input_file)
        if data is None:
            return

    if args.output_file.endswith('.json'):
        write_json(args.output_file, data)

if __name__ == "__main__":
    main()
