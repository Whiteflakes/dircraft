import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from pathlib import Path
import pprint
from dircraft.generator import load_structure, generate_structure

class DirCraftGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Structurify")
        self.root.geometry("700x500")
        
        style = ttk.Style()
        style.theme_use("clam")  
        
        input_frame = ttk.Frame(root, padding="10 10 10 10")
        input_frame.grid(row=0, column=0, sticky=(tk.W, tk.E))
        
        # Input Source
        ttk.Label(input_frame, text="Input Source (YAML/TXT file or direct string):").grid(row=0, column=0, sticky=tk.W)
        self.input_entry = ttk.Entry(input_frame, width=60)
        self.input_entry.grid(row=1, column=0, padx=5, pady=5)
        ttk.Button(input_frame, text="Browse", command=self.browse_input_file).grid(row=1, column=1, padx=5)
        
        # Target Directory
        ttk.Label(input_frame, text="Target Directory:").grid(row=2, column=0, sticky=tk.W)
        self.target_entry = ttk.Entry(input_frame, width=60)
        self.target_entry.grid(row=3, column=0, padx=5, pady=5)
        ttk.Button(input_frame, text="Browse", command=self.browse_target_dir).grid(row=3, column=1, padx=5)
        
        # Buttons Frame
        btn_frame = ttk.Frame(root, padding="10 10 10 10")
        btn_frame.grid(row=1, column=0, sticky=(tk.W, tk.E))
        ttk.Button(btn_frame, text="Preview Structure", command=self.preview_structure).grid(row=0, column=0, padx=5)
        ttk.Button(btn_frame, text="Generate Structure", command=self.generate_structure).grid(row=0, column=1, padx=5)
        ttk.Button(btn_frame, text="Exit", command=root.quit).grid(row=0, column=2, padx=5)
        
        # Output Text
        output_frame = ttk.Frame(root, padding="10 10 10 10")
        output_frame.grid(row=2, column=0, sticky=(tk.N, tk.S, tk.E, tk.W))
        self.output_text = tk.Text(output_frame, height=15, width=80, wrap="word")
        self.output_text.grid(row=0, column=0, sticky=(tk.N, tk.S, tk.E, tk.W))
        
        # Make output frame expandable
        output_frame.columnconfigure(0, weight=1)
        output_frame.rowconfigure(0, weight=1)
        root.columnconfigure(0, weight=1)
        root.rowconfigure(2, weight=1)

    def browse_input_file(self):
        filename = filedialog.askopenfilename(filetypes=[("YAML/TXT Files", "*.yaml *.yml *.txt")])
        if filename:
            self.input_entry.delete(0, tk.END)
            self.input_entry.insert(0, filename)

    def browse_target_dir(self):
        foldername = filedialog.askdirectory()
        if foldername:
            self.target_entry.delete(0, tk.END)
            self.target_entry.insert(0, foldername)

    def preview_structure(self):
        input_source = self.input_entry.get().strip()
        if not input_source:
            messagebox.showwarning("Warning", "Please specify an input source.")
            return
        
        try:
            structure = load_structure(input_source)
            preview = pprint.pformat(structure, indent=2)
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, f"Parsed structure:\n{preview}\n")
        except Exception as e:
            messagebox.showerror("Error", f"Error parsing structure: {e}")

    def generate_structure(self):
        input_source = self.input_entry.get().strip()
        target_dir = self.target_entry.get().strip()
        if not input_source or not target_dir:
            messagebox.showwarning("Warning", "Please specify both input source and target directory.")
            return
        
        try:
            target_path = Path(target_dir)
            generate_structure(input_source, target_path)
            messagebox.showinfo("Success", f"File structure generated in {target_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Error generating structure: {e}")

def main():
    root = tk.Tk()
    app = DirCraftGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
