def get_cats_info(path: str) -> list:
    cats_list = []
    # First, we create a block for handling errors 
    try:
        # Start reading file
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            # We iterate over each row and divide the row into parts
            for line in lines:
                cats_info = line.strip().split(',')
                # Сreated a dictionary and add all the parameters of our file there
                cats_dict = {
                    'id': cats_info[0],
                    'name': cats_info[1],
                    'age': cats_info[2]
                }
                # Add dictionaries to list  
                cats_list.append(cats_dict)
        return cats_list

    except FileNotFoundError:
        print(f'File {path} not found')
    
    except Exception as e:
        print(f'An error occured {e}')


cats_info = get_cats_info('cats.txt')
print(cats_info)