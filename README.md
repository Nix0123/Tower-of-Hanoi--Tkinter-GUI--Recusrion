# 🗼 Tower of Hanoi

A Python-based graphical simulation of the classic **Tower of Hanoi** puzzle, built using `tkinter`. This project was developed as a mini project for the **Masters of Computer Applications** program at **Chandigarh University**.

---

## 📖 About the Project

The Tower of Hanoi (also known as the Tower of Brahma or Lucas Tower) is a classic mathematical puzzle consisting of three rods and a number of disks of varying sizes. The goal is to move the entire stack of disks from the source rod to the destination rod, following a strict set of rules.

This project implements the puzzle using a **recursive algorithm** and visualizes each move step-by-step through a graphical user interface (GUI).

---

## 🎯 Puzzle Rules

- Only **one disk** can be moved at a time.
- A disk can only be moved if it is the **topmost disk** on a rod.
- **No larger disk** may be placed on top of a smaller disk.

---

## ⚙️ How It Works

The solution is based on a **recursive divide-and-conquer approach**:

1. Move a sub-tower of height `n-1` from the source rod to the auxiliary rod.
2. Move the largest (remaining) disk directly to the destination rod.
3. Move the sub-tower of height `n-1` from the auxiliary rod to the destination rod.

The **minimum number of moves** required to solve the puzzle is `2ⁿ - 1`, where `n` is the number of disks.

---

## 🖥️ Features

- Interactive **Tkinter GUI** that animates disk movements in real time.
- Supports a **custom number of disks** (entered at runtime).
- Visual representation of all three rods and disk states after every move.
- Automatic solving — no manual input required after setup.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- `tkinter` (comes pre-installed with standard Python distributions)

### Running the Project

```bash
git clone https://github.com/your-username/tower-of-hanoi.git
cd tower-of-hanoi
python Code.py
```

When prompted, enter the number of disks you want to simulate. The GUI will launch and animate the solution automatically.

---

## 🧠 Algorithm (Core Logic)

```python
def solve(self, n, source, target, auxiliary):
    if n == 1:
        self.move_disk(source, target)
    else:
        self.solve(n - 1, source, auxiliary, target)
        self.move_disk(source, target)
        self.solve(n - 1, auxiliary, target, source)
```

---

## 📚 Applications

- Used in **psychological research** on human problem-solving.
- Serves as a foundational example for teaching **recursive algorithms**.
- Applied as a **backup rotation scheme** in data management systems.
- Used by **neuropsychologists** to evaluate frontal lobe function.

---

## 🏛️ Origin & History

The puzzle was invented by French mathematician **Édouard Lucas in 1883**. It is inspired by a legend about a temple in Kashi Vishwanath, India, where 64 golden disks are being moved by Brahmin priests. According to the legend, when the last move is completed, the world will end. At one move per second, this would take approximately **585 billion years**.

---

## 👨‍💻 Author

**Taranjeet Singh**
+91-9878770515
taran.pvt@gmail.com
University Institute of Computing, Chandigarh University

---

## 📄 License

This project is intended for academic and educational purposes.
