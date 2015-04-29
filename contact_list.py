__author__ = "Stephen Diniz"
__version__ = "1.0.0"
__email__ = "DizzyThermal"

import csv
import tkinter
import tkinter.font
from tkinter import ttk

tree_columns = ("Name", "Number", "Email")

def sortby(tree, col, descending):
    """Sort tree contents when a column is clicked on."""
    # Grab Values to Sort
    data = [(tree.set(child, col), child) for child in tree.get_children('')]

    # Reorder Data of Selected Column
    data.sort(reverse=descending)
    for index, item in enumerate(data):
        tree.move(item[1], '', index)

    # Switch the Heading to Sort opposite direction next time
    tree.heading(col, command=lambda col=col: sortby(tree, col, int(not descending)))

class App(object):
    def __init__(self):
        self.tree = None
        self._setup_widgets()
        self._build_tree()

    def _setup_widgets(self):
        container = ttk.Frame()
        container.pack(fill='both', expand=True)

        # XXX Sounds like a good support class would be one for constructing
        #     a treeview with scrollbars.
        self.tree = ttk.Treeview(columns=tree_columns, show="headings")
        vsb = ttk.Scrollbar(orient="vertical", command=self.tree.yview)
        hsb = ttk.Scrollbar(orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        self.tree.grid(column=0, row=0, sticky='nsew', in_=container)
        vsb.grid(column=1, row=0, sticky='ns', in_=container)
        hsb.grid(column=0, row=1, sticky='ew', in_=container)

        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)

    def _build_tree(self):
        for col in tree_columns:
            self.tree.heading(col, text=col.title(),
                command=lambda c=col: sortby(self.tree, c, 0))
            # XXX tkFont.Font().measure expected args are incorrect according
            #     to the Tk docs
            self.tree.column(col, width=tkinter.font.Font().measure(col.title()))

        my_list = []
        with open("contacts.csv", newline="") as csvfile:
            reader = csv.reader(csvfile, delimiter=",")
            for row in reader:
                my_list.append(row)

        for item in my_list:
            self.tree.insert('', 'end', values=item)

            # adjust columns lenghts if necessary
            for indx, val in enumerate(item):
                ilen = tkinter.font.Font().measure(val)
                if self.tree.column(tree_columns[indx], width=None) < ilen:
                    self.tree.column(tree_columns[indx], width=ilen)

def main():
    root = tkinter.Tk()
    root.wm_title("Stephen's Contact List")
    root.wm_iconname("mclist")

    app = App()
    root.mainloop()

if __name__ == "__main__":
    main()