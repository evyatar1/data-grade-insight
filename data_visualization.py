import matplotlib.pyplot as plt


def visualize_data(data):
    """
    Visualize the data using a bar chart.

    Args:
        data (dict): A dictionary representing the data from the CSV file.
    """
    keys = list(data.keys())
    values = list(data.values())

    plt.bar(keys, values)
    plt.xlabel('Subjects')
    plt.ylabel('Grades')
    plt.title('Grades Visualization')
    plt.show()
