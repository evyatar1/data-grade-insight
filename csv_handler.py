def read_csv(file_path):
    """
    Read data from a CSV file and return it as a dictionary.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        dict: A dictionary representing the data in the CSV file.
    """
    data = {}  # Store data as a dictionary

    try:
        with open(file_path, 'r') as csvfile:
            for line in csvfile:
                key, value = line.strip().split(',')  # Split each line into key and value
                data[key] = int(value)  # Assuming values are integers, convert to int if needed
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except ValueError as ve:
        print(f"Error: {ve}. Please ensure values in CSV file are valid.")
    except Exception as e:
        print(f"An error occurred while reading the CSV file: {e}")

    return data
