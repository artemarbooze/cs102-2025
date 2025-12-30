"""GUI for maze generation and solving using tkinter."""

import tkinter as tk
from tkinter import ttk
from typing import List

from maze import add_path_to_grid, bin_tree_maze, solve_maze


def draw_cell(x: int, y: int, color: str, size: int = 10) -> None:
    """
    Draw a single cell on the canvas.

    :param x: X coordinate
    :param y: Y coordinate
    :param color: Cell color
    :param size: Cell size in pixels
    :return: None
    """
    x *= size
    y *= size
    x1 = x + size
    y1 = y + size
    canvas.create_rectangle(x, y, x1, y1, fill=color)


def draw_maze(grid: List[List[str]], size: int = 10) -> None:
    """
    Draw the entire maze on the canvas.

    :param grid: The maze grid
    :param size: Cell size in pixels
    :return: None
    """
    for x, row in enumerate(grid):
        for y, cell in enumerate(row):
            if cell == " ":
                color = "White"
            elif cell == "■":
                color = "black"
            elif cell == "X":
                color = "green"
            else:
                color = "White"
            draw_cell(y, x, color, size)


def show_solution() -> None:
    """
    Solve the maze and display the solution.

    :return: None
    """
    maze_solved, path = solve_maze(GRID)
    maze_result = add_path_to_grid(GRID, path)
    if path:
        draw_maze(maze_result, CELL_SIZE)
    else:
        tk.messagebox.showinfo("Message", "No solutions")


if __name__ == "__main__":
    GRID = None
    CELL_SIZE = 10
    N, M = 51, 77
    CELL_SIZE = 10

    while True:
        candidate = bin_tree_maze(N, M)
        marked, path = solve_maze(candidate)
        if path:
            GRID = candidate
            break

    window = tk.Tk()
    window.title("Maze")
    window.geometry(f"{M * CELL_SIZE + 100}x{N * CELL_SIZE + 100}")
    canvas = tk.Canvas(window, width=M * CELL_SIZE, height=N * CELL_SIZE)
    canvas.pack()
    draw_maze(GRID, CELL_SIZE)
    ttk.Button(window, text="Solve", command=show_solution).pack(pady=20)
    window.mainloop()
