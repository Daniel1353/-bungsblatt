import tkinter as tk

def say_hi():
    name = entry.get()
    output_label.config(text=f"Herzlich Willkommen {name} und einen schönen Tag wünscht dir dein Betriebssystem")

def say_unfriendly():
    name = entry.get()
    output_label.config(text=f"Hallo {name}, dein Betriebssystem hat keine Lust, heute mit dir zu sprechen.")

# Erstellen des Hauptfensters
root = tk.Tk()
root.title("Begrüßung")

# Label für die Aufforderung
prompt_label = tk.Label(root, text="Wie lautet dein Name?")
prompt_label.pack()

# Eingabefeld für den Namen
entry = tk.Entry(root)
entry.pack()

# Knopf zum Ausführen der freundlichen Funktion
button_hi = tk.Button(root, text="Freundliche Begrüßung", command=say_hi)
button_hi.pack()

# Knopf zum Ausführen der unfreundlichen Funktion
button_unfriendly = tk.Button(root, text="Unfreundliche Begrüßung", command=say_unfriendly)
button_unfriendly.pack()

# Label für die Ausgabe
output_label = tk.Label(root, text="")
output_label.pack()

# Starten der Ereignisschleife
root.mainloop() 
