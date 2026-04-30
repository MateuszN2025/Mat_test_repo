import tkinter as tk
from tkinter import ttk


class ComboTemplateApp:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Python GUI Template")
        self.root.geometry("420x220")
        self.root.resizable(False, False)

        container = ttk.Frame(root, padding=16)
        container.pack(fill="both", expand=True)

        ttk.Label(container, text="Description:").pack(anchor="w")
        self.description_entry = ttk.Entry(container)
        self.description_entry.pack(fill="x", pady=(4, 12))
        self.description_entry.insert(0, "Type a short description here")

        ttk.Label(container, text="Choose an option:").pack(anchor="w")
        self.selected_option = tk.StringVar(value="Option 1")
        self.combo = ttk.Combobox(
            container,
            textvariable=self.selected_option,
            state="readonly",
            values=["Option 1", "Option 2", "Option 3"],
        )
        self.combo.pack(fill="x", pady=(4, 12))

        self.show_button = ttk.Button(
            container,
            text="Show selected option",
            command=self.show_selection,
        )
        self.show_button.pack(fill="x", pady=(0, 12))

        ttk.Label(container, text="Selected value:").pack(anchor="w")
        self.result_text = tk.StringVar()
        self.result_entry = ttk.Entry(
            container,
            textvariable=self.result_text,
            state="readonly",
        )
        self.result_entry.pack(fill="x", pady=(4, 0))

    def show_selection(self) -> None:
        self.result_text.set(self.selected_option.get())


def main() -> None:
    root = tk.Tk()
    ComboTemplateApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
