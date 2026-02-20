def total_salary(path):
    try:
        with open(path, 'r',encoding='utf-8') as file:
            salaries = []
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                if not line:
                    continue
                _, salary = line.split(',')
                salaries.append(int(salary))       
        total = sum(salaries)
        average = int(total/len(salaries))
        return total, average
   
    except FileNotFoundError:
        print('File not found')   
        return 0, 0 
    except Exception as e:
        print(f'Error: {e}')
        return 0, 0

if __name__ == "__main__":  
    total, average = total_salary('C:\My_Repo\goit-pycore-hm-04\path.txt')
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

  
