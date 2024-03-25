import tkinter as tk
from tkinter import filedialog
from csv_handler import read_csv
from pdf_generator import generate_pdf
from data_visualization import visualize_data
from statistics_calculator import calculate_average
import subprocess


class GradeInsightApp:
    def __init__(self, master):
        self.master = master
        self.data = None

        self.create_widgets()

    def create_widgets(self):
        self.master.title("Grade Insight")

        self.label = tk.Label(self.master, text="Grade Insight")
        self.label.pack()

        self.load_button = tk.Button(self.master, text="Load CSV", command=self.load_csv)
        self.load_button.pack()

        self.visualize_button = tk.Button(self.master, text="Visualize Data", command=self.visualize_data,
                                          state=tk.DISABLED)
        self.visualize_button.pack()

        self.calculate_button = tk.Button(self.master, text="Calculate Statistics", command=self.calculate_statistics,
                                           state=tk.DISABLED)
        self.calculate_button.pack()

        self.result_text = tk.Text(self.master, height=10, width=50)
        self.result_text.pack()

        self.pdf_button = tk.Button(self.master, text="Generate PDF Report", command=self.generate_pdf)
        self.pdf_button.pack()

    def load_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            self.data = read_csv(file_path)
            self.display_data()

    def display_data(self):
        self.result_text.delete(1.0, tk.END)
        for key, value in self.data.items():
            self.result_text.insert(tk.END, f"{key}: {value}\n")
        self.visualize_button["state"] = tk.NORMAL
        self.calculate_button["state"] = tk.NORMAL

    def visualize_data(self):
        visualize_data(self.data)

    def calculate_statistics(self):
        average = calculate_average(self.data)
        self.result_text.insert(tk.END, f"\nAverage Grade: {average:.2f}\n")

    def generate_pdf(self):
        if self.data:
            file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
            if file_path:
                generate_pdf(self.data, file_path)
                subprocess.Popen([file_path], shell=True)


def main():
    root = tk.Tk()
    app = GradeInsightApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
