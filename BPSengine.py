import tkinter as tk
import tkinter.ttk as ttk
import webbrowser

class SimpleBrowser(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simple Browser")

        self.create_widgets()

    def create_widgets(self):
        # Entry for search/query input
        self.query_entry = ttk.Entry(self, width=50)
        self.query_entry.pack(side="top", fill="x", padx=5, pady=5)

        # Button to search
        self.search_button = ttk.Button(self, text="Search", command=self.search_query)
        self.search_button.pack(side="top", padx=5, pady=5)

        # Button to open Chrome
        self.chrome_button = ttk.Button(self, text="Open Chrome", command=self.open_chrome)
        self.chrome_button.pack(side="top", padx=5, pady=5)

    def search_query(self):
        query = self.query_entry.get()
        if query:
            search_url = "https://www.google.com/search?q=" + query
            webbrowser.open_new_tab(search_url)

    def open_chrome(self):
        chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"  # Adjust path accordingly
        webbrowser.get(chrome_path).open_new_tab("https://www.google.com")

if __name__ == "__main__":
    app = SimpleBrowser()
    app.mainloop()







