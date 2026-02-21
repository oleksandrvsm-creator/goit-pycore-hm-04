import sys
from pathlib import Path
from colorama import init, Fore, Style


init(autoreset=True)


def visualize_directory_structure(path: Path, indent: str = "") -> None:
    """Рекурсивно виводить структуру директорії з кольоровим маркуванням."""
    try:
        items = sorted(path.iterdir(), key=lambda x: (x.is_file(), x.name.lower()))
        
        for index, item in enumerate(items):
            is_last = (index == len(items) - 1)
            connector = "┗ " if is_last else "┣ "
            
            if item.is_dir():
                print(f"{indent}{connector}{Fore.BLUE}{Style.BRIGHT}📂 {item.name}")
                new_indent = indent + ("  " if is_last else "┃ ")
                visualize_directory_structure(item, new_indent)
            else:
                print(f"{indent}{connector}{Fore.GREEN}📜 {item.name}")
                
    except PermissionError:
        print(f"{indent}{Fore.RED}![Доступ заборонено]!")
    except OSError as e:
        print(f"{indent}{Fore.RED}![Помилка: {e}]!")


def main() -> None:
    if len(sys.argv) < 2:
        print(f"{Fore.YELLOW}Використання: python main.py /шлях/до/директорії")
        return

    root_path = Path(sys.argv[1])

    if not root_path.exists():
        print(f"{Fore.RED}Помилка: Шлях '{root_path}' не існує.")
        return
    
    if not root_path.is_dir():
        print(f"{Fore.RED}Помилка: Шлях '{root_path}' не є директорією.")
        return

    print(f"{Fore.CYAN}{Style.BRIGHT}📦 {root_path.name}")
    visualize_directory_structure(root_path)


if __name__ == "__main__":
    main()