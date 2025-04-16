import tkinter as tk
import time

class HanoiGUI:
    def __init__(self, root, num_disks):
        self.root = root
        self.root.title("Tower of Hanoi")

        self.canvas_width = 600
        self.canvas_height = 400
        self.canvas = tk.Canvas(root, width=self.canvas_width, height=self.canvas_height, bg="white")
        self.canvas.pack()

        self.num_disks = num_disks
        self.disk_height = 20
        self.peg_width = 10
        self.peg_height = 200
        self.peg_positions = [150, 300, 450]
        self.pegs = [[], [], []]

        # Create pegs
        for x in self.peg_positions:
            self.canvas.create_rectangle(x - self.peg_width // 2, self.canvas_height - self.peg_height,
                                         x + self.peg_width // 2, self.canvas_height, fill="black")

        # Create disks
        for i in range(num_disks, 0, -1):
            width = i * 20
            x = self.peg_positions[0]
            y = self.canvas_height - (num_disks - len(self.pegs[0])) * self.disk_height
            disk = self.canvas.create_rectangle(x - width // 2, y - self.disk_height,
                                                x + width // 2, y, fill="skyblue")
            self.pegs[0].append(disk)

        # Start solving
        self.root.after(500, lambda: self.solve(num_disks, 0, 2, 1))

    def move_disk(self, from_peg, to_peg):
        disk = self.pegs[from_peg].pop()
        self.pegs[to_peg].append(disk)

        # Update GUI
        self.canvas.update()
        self.canvas.after(500)

        disk_index = len(self.pegs[to_peg]) - 1
        width = (self.num_disks - disk_index) * 20
        x = self.peg_positions[to_peg]
        y = self.canvas_height - disk_index * self.disk_height
        self.canvas.coords(disk, x - width // 2, y - self.disk_height, x + width // 2, y)

    def solve(self, n, source, target, auxiliary):
        if n == 1:
            self.move_disk(source, target)
        else:
            self.solve(n - 1, source, auxiliary, target)
            self.move_disk(source, target)
            self.solve(n - 1, auxiliary, target, source)

# Run the GUI
if __name__ == "__main__":
    root = tk.Tk()
    num_disks = int(input("Enter number of disks: "))
    app = HanoiGUI(root, num_disks)
    root.mainloop()
