def get_cats_info(path):
    try:
        result = []
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                try:
                    id, name, age = line.split(',')
                    result.append({'id': id, 'name': name, 'age': age})
                except ValueError:
                    print(f'error in line:{line}')
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
