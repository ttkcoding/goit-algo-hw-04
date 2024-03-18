def totaly_salary_function(path: str) -> tuple:
    total_salary = 0
    num_salaries = 0
    # First, we create a block for handling errors 
    try:
        # Open file for reading every lines
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            # We iterate over each row and divide the row into parts. Calculate the obtained values
            for line in lines:
                items = line.strip().split(',')
                salary = int(items[1])
                total_salary += salary
                num_salaries += 1
        # We calculate the average salary
        average_salary = total_salary // num_salaries if num_salaries > 0 else 0
        return total_salary, average_salary
    # Erroes exeption
    except FileNotFoundError:
        print(f"File '{path}' not found.")
        return 0, 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0, 0
            


total, average = totaly_salary_function("salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")