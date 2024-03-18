import sys
from pathlib import Path
from colorama import Fore, Style

def visualize_directory_structure(directory_path, indent=0):
    path = Path(directory_path)
    if not path.is_dir():
        print(f"{Fore.RED}Invalid directory path{Style.RESET_ALL}")
        return

    print(f"{Fore.BLUE}{path}{Style.RESET_ALL}")
    for item in path.iterdir():
        if item.is_dir():
            print(f"{' ' * indent} {Fore.GREEN}+ {item.name}{Style.RESET_ALL}")
            visualize_directory_structure(item, indent + 4)
        else:
            print(f"{' ' * indent} {Fore.WHITE}- {item.name}{Style.RESET_ALL}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python visualize_directory_structure.py <directory_path>")
        sys.exit(1)

    directory_path = sys.argv[1]
    visualize_directory_structure(directory_path)