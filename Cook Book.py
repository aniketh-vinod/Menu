import tkinter as tk
from tkinter import messagebox, ttk

MENU_PRICES = {
    "Idly Vada": 60,
    "Puri Chana": 80,
    "Peanut Butter and Jelly Sandwich": 120,
    "Waffles with Chocolate/Maple Syrup": 150,
    "Mini Mystery Meals": 100,
    "Mini English Mystery Meals": 180,
}

TAX_RATE = 0.05

root = tk.Tk()
root.title("Che LA Vu Hotel | Menu")
root.geometry("540x690")
root.minsize(480, 620)
root.configure(bg="#f3f5f7")

style = ttk.Style(root)
style.configure("Title.TLabel", font=("Arial", 22, "bold"), foreground="#17324d")
style.configure("Subtitle.TLabel", font=("Arial", 10), foreground="#5c6b78")
style.configure("Section.TLabelframe.Label", font=("Arial", 11, "bold"))
style.configure("Menu.TCheckbutton", font=("Arial", 10))
style.configure("Price.TLabel", font=("Arial", 10, "bold"), foreground="#17324d")
style.configure("Order.TButton", font=("Arial", 11, "bold"), padding=8)
style.configure("Clear.TButton", padding=8)

item_vars = {}


header = ttk.Frame(root, padding=(22, 18, 22, 10))
header.pack(fill="x")

ttk.Label(header, text="Che LA Vu Hotel", style="Title.TLabel").pack(anchor="w")
ttk.Label(
    header,
    text="Choose your meal and payment method",
    style="Subtitle.TLabel",
).pack(anchor="w", pady=(3, 0))

menu_box = ttk.LabelFrame(
    root, text="  Menu  ", style="Section.TLabelframe", padding=12
)
menu_box.pack(fill="x", padx=22, pady=10)

for row, (item, price) in enumerate(MENU_PRICES.items()):
    var = tk.BooleanVar(value=False)
    item_vars[item] = var

    ttk.Checkbutton(
        menu_box,
        text=item,
        variable=var,
        style="Menu.TCheckbutton",
    ).grid(row=row, column=0, sticky="w", padx=(4, 12), pady=7)

    ttk.Label(
        menu_box,
        text=f"₹{price:.2f}",
        style="Price.TLabel",
    ).grid(row=row, column=1, sticky="e", padx=4, pady=7)

menu_box.columnconfigure(0, weight=1)


payment_box = ttk.LabelFrame(
    root, text="  Payment Method  ", style="Section.TLabelframe", padding=12
)
payment_box.pack(fill="x", padx=22, pady=10)

payment_method = tk.StringVar(value="")

ttk.Radiobutton(
    payment_box, text="Cash", variable=payment_method, value="Cash"
).pack(side="left", padx=(4, 24), pady=4)

ttk.Radiobutton(
    payment_box, text="UPI", variable=payment_method, value="UPI"
).pack(side="left", padx=4, pady=4)


receipt_box = ttk.LabelFrame(
    root, text="  Order Receipt  ", style="Section.TLabelframe", padding=12
)
receipt_box.pack(fill="both", expand=True, padx=22, pady=10)

receipt_text = tk.StringVar(
    value="Your order details will appear here after you place your order."
)

ttk.Label(
    receipt_box,
    textvariable=receipt_text,
    justify="left",
    anchor="nw",
    font=("Arial", 10),
).pack(fill="both", expand=True)


def place_order():
    selected_items = [
        item for item, var in item_vars.items() if var.get()
    ]

    if not selected_items:
        messagebox.showwarning(
            "Missing Information",
            "Please select at least one menu item.",
        )
        return

    payment = payment_method.get()
    if not payment:
        messagebox.showwarning(
            "Missing Information",
            "Please select a payment method.",
        )
        return

    subtotal = sum(MENU_PRICES[item] for item in selected_items)
    tax = subtotal * TAX_RATE
    total = subtotal + tax

    lines = ["SELECTED ITEMS", "─" * 30]
    lines.extend(
        f"{item}\n    ₹{MENU_PRICES[item]:.2f}"
        for item in selected_items
    )
    lines.extend([
        "",
        "─" * 30,
        f"Subtotal:         ₹{subtotal:.2f}",
        f"Tax ({TAX_RATE:.0%}):            ₹{tax:.2f}",
        f"Payment:          {payment}",
        f"TOTAL:            ₹{total:.2f}",
    ])

    receipt_text.set("\n".join(lines))


def clear_order():
    for var in item_vars.values():
        var.set(False)

    payment_method.set("")
    receipt_text.set(
        "Your order details will appear here after you place your order."
    )


button_row = ttk.Frame(root, padding=(22, 2, 22, 18))
button_row.pack(fill="x")

ttk.Button(
    button_row,
    text="Clear",
    command=clear_order,
    style="Clear.TButton",
).pack(side="right")

ttk.Button(
    button_row,
    text="Place Order",
    command=place_order,
    style="Order.TButton",
).pack(side="right", padx=(0, 10))

root.mainloop()