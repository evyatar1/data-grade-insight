def calculate_average(data):
    """
    Calculate the average grade from the provided data.

    Args:
        data (dict): A dictionary representing the data from the CSV file.

    Returns:
        float: The average grade.
    """
    total_grades = sum(data.values())
    num_grades = len(data)
    return total_grades / num_grades
