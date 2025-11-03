INF = 99999

def floyd_warshall(graph):
    n = len(graph)
    dist = [row[:] for row in graph]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    print("\nShortest distances between every pair of cities:\n")
    for i in range(n):
        for j in range(n):
            print(dist[i][j], end="\t")
        print()

cities = ["Delhi", "Mumbai", "Kolkata", "Chennai", "Bangalore", "Hyderabad"]

graph = [
    [0, 10, 40, 30, 60, 25],   # Delhi
    [10, 0, 50, 35, 40, 20],   # Mumbai
    [40, 50, 0, 45, 10, 30],   # Kolkata
    [30, 35, 45, 0, 25, 30],   # Chennai
    [60, 40, 10, 25, 0, 15],   # Bangalore
    [25, 20, 30, 30, 15, 0]    # Hyderabad
]

print("Cities:", cities)
floyd_warshall(graph)

#member 2
import tkinter as tk
from tkinter import ttk, messagebox

# === Floyd–Warshall Algorithm ===
def floyd_warshall(graph):
    n = len(graph)
    dist = [row[:] for row in graph]  # copy graph
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist


# === Data ===
cities = ["Delhi", "Mumbai", "Kolkata", "Chennai", "Bangalore", "Hyderabad"]
graph = [
    [0, 10, 40, 30, 60, 25],
    [10, 0, 50, 35, 40, 20],
    [40, 50, 0, 35, 10, 25],
    [30, 35, 45, 0, 25, 30],
    [60, 40, 10, 25, 0, 15],
    [25, 20, 25, 30, 15, 0]
]

dist_matrix = floyd_warshall(graph)


# === GUI ===
root = tk.Tk()
root.title("City Shortest Path Finder")
root.geometry("500x400")
root.configure(bg="#f0f0f0")

tk.Label(root, text="Select Source City:", bg="#f0f0f0", font=("Arial", 11)).pack(pady=5)
source_cb = ttk.Combobox(root, values=cities, state="readonly")
source_cb.pack(pady=5)

tk.Label(root, text="Select Destination City:", bg="#f0f0f0", font=("Arial", 11)).pack(pady=5)
dest_cb = ttk.Combobox(root, values=cities, state="readonly")
dest_cb.pack(pady=5)

result_label = tk.Label(root, text="", bg="#f0f0f0", font=("Arial", 12, "bold"))
result_label.pack(pady=20)


def find_shortest_path():
    src = source_cb.get()
    dest = dest_cb.get()
    if not src or not dest:
        messagebox.showwarning("Warning", "Please select both cities!")
        return
    if src == dest:
        result_label.config(text="You are already in the same city!")
        return

    i, j = cities.index(src), cities.index(dest)
    distance = dist_matrix[i][j]
    result_label.config(text=f"Shortest distance from {src} to {dest}: {distance} km")


ttk.Button(root, text="Find Shortest Path", command=find_shortest_path).pack(pady=10)

# Display distance matrix
tk.Label(root, text="Shortest distances between cities:", bg="#f0f0f0", font=("Arial", 11, "bold")).pack(pady=10)
text_box = tk.Text(root, height=8, width=60)
text_box.pack()
for i, city in enumerate(cities):
    text_box.insert(tk.END, f"{city}: {dist_matrix[i]}\n")
text_box.config(state="disabled")

root.mainloop()

