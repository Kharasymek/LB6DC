import argparse

def main():
    # Tworzenie parsera argumentów
    parser = argparse.ArgumentParser(description='Konwersja plików między formatami .xml, .json i .yml.')
    parser.add_argument('input_file', type=str, help='Ścieżka do pliku wejściowego')
    parser.add_argument('output_file', type=str, help='Ścieżka do pliku wyjściowego')
    
    args = parser.parse_args()
    
    # Wyświetlanie przekazanych argumentów
    print(f'Plik wejściowy: {args.input_file}')
    print(f'Plik wyjściowy: {args.output_file}')

if __name__ == "__main__":
    main()