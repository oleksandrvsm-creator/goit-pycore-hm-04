def get_cats_info(path: str) -> list[dict[str, str]]:
    try:
        result = []
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                try:
                    cat_id, name, age = line.split(',')
                    result.append({'id': cat_id, 'name': name, 'age': age})
                except ValueError:
                    print(f'Error in line: {line}')
                    continue
        return result
    except FileNotFoundError:
        print('File not found')
        return []
    except Exception as e:
        print(f'Error: {e}')
        return []


if __name__ == '__main__':
    cats_info = get_cats_info("cat_info.txt")
    print(cats_info)