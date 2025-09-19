# Traveling Salesman Problem (TSP) for School Bus Route Optimization with PyQt6 GUI
# Developed by Hamid Yarali
# GitHub: https://github.com/HamidYaraliOfficial
# Instagram: https://www.instagram.com/hamidyaraliofficial?igsh=MWpxZjhhMHZuNnlpYQ==
# Telegram: @Hamid_Yarali

import math
import random
from itertools import permutations
import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                            QPushButton, QLineEdit, QLabel, QTableWidget, QTableWidgetItem,
                            QComboBox, QMessageBox, QGraphicsView, QGraphicsScene)
from PyQt6.QtCore import Qt, QPointF
from PyQt6.QtGui import QPainter, QPen, QColor

class TSPSchoolService:
    def __init__(self, locations, school_location):
        """Initialize with student locations and school location."""
        self.locations = locations
        self.school = school_location
        self.num_points = len(locations)
        self.distances = self.calculate_distances()

    def calculate_distances(self):
        """Calculate Euclidean distance matrix between all points."""
        all_points = self.locations + [self.school]
        n = len(all_points)
        distances = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j:
                    x1, y1 = all_points[i]
                    x2, y2 = all_points[j]
                    distances[i][j] = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        return distances

    def calculate_path_distance(self, path):
        """Calculate total distance of a given path."""
        total_distance = 0
        total_distance += self.distances[self.num_points][path[0]]
        for i in range(len(path) - 1):
            total_distance += self.distances[path[i]][path[i + 1]]
        total_distance += self.distances[path[-1]][self.num_points]
        return total_distance

    def brute_force_tsp(self):
        """Solve TSP using brute force."""
        min_distance = float('inf')
        best_path = None
        for perm in permutations(range(self.num_points)):
            distance = self.calculate_path_distance(perm)
            if distance < min_distance:
                min_distance = distance
                best_path = perm
        return best_path, min_distance

    def nearest_neighbor_tsp(self):
        """Solve TSP using Nearest Neighbor heuristic."""
        current = 0
        path = [current]
        unvisited = set(range(self.num_points)) - {current}
        total_distance = self.distances[self.num_points][current]
        while unvisited:
            min_dist = float('inf')
            next_node = None
            for node in unvisited:
                if self.distances[current][node] < min_dist:
                    min_dist = self.distances[current][node]
                    next_node = node
            path.append(next_node)
            total_distance += min_dist
            unvisited.remove(next_node)
            current = next_node
        total_distance += self.distances[current][self.num_points]
        return path, total_distance

class TSPGraphicsView(QGraphicsView):
    def __init__(self, locations, school_location):
        super().__init__()
        self.scene = QGraphicsScene()
        self.setScene(self.scene)
        self.locations = locations
        self.school = school_location
        self.path = None

    def draw_route(self, path):
        """Draw the TSP route."""
        self.scene.clear()
        scale = 50
        offset = 20
        all_points = self.locations + [self.school]

        # Draw student points (blue circles)
        for i, (x, y) in enumerate(self.locations):
            self.scene.addEllipse((x * scale) + offset, (y * scale) + offset, 8, 8, 
                                QPen(Qt.GlobalColor.black), QColor(Qt.GlobalColor.blue))
            self.scene.addText(f"S{i+1}", ).setPos((x * scale) + offset + 10, (y * scale) + offset)

        # Draw school point (red square)
        school_x, school_y = self.school
        self.scene.addRect((school_x * scale) + offset, (school_y * scale) + offset, 10, 10, 
                          QPen(Qt.GlobalColor.black), QColor(Qt.GlobalColor.red))
        self.scene.addText("School").setPos((school_x * scale) + offset + 10, (school_y * scale) + offset)

        # Draw route if provided
        if path:
            pen = QPen(QColor(Qt.GlobalColor.green), 2, Qt.PenStyle.DashLine)
            path_points = [self.locations[i] for i in path] + [self.school]
            path_points = [self.school] + path_points  # Start from school
            for i in range(len(path_points) - 1):
                x1, y1 = path_points[i]
                x2, y2 = path_points[i + 1]
                self.scene.addLine((x1 * scale) + offset + 4, (y1 * scale) + offset + 4,
                                 (x2 * scale) + offset + 4, (y2 * scale) + offset + 4, pen)
            # Close the loop
            x1, y1 = path_points[-1]
            x2, y2 = path_points[0]
            self.scene.addLine((x1 * scale) + offset + 4, (y1 * scale) + offset + 4,
                             (x2 * scale) + offset + 4, (y2 * scale) + offset + 4, pen)

class TSPMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("School Bus Route Optimization - TSP")
        self.setGeometry(100, 100, 800, 600)
        self.init_ui()

    def init_ui(self):
        """Initialize the GUI components."""
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QHBoxLayout()
        main_widget.setLayout(layout)

        # Left panel: Inputs and controls
        left_panel = QVBoxLayout()
        layout.addLayout(left_panel)

        # School coordinates
        left_panel.addWidget(QLabel("School Coordinates (x,y):"))
        self.school_input = QLineEdit("0,0")
        left_panel.addWidget(self.school_input)

        # Student coordinates
        left_panel.addWidget(QLabel("Student Coordinates (x,y):"))
        self.student_table = QTableWidget()
        self.student_table.setRowCount(5)
        self.student_table.setColumnCount(2)
        self.student_table.setHorizontalHeaderLabels(["X", "Y"])
        for row in range(5):
            self.student_table.setItem(row, 0, QTableWidgetItem(str(row + 1)))
            self.student_table.setItem(row, 1, QTableWidgetItem(str(row)))
        left_panel.addWidget(self.student_table)

        # Algorithm selection
        left_panel.addWidget(QLabel("Select Algorithm:"))
        self.algo_combo = QComboBox()
        self.algo_combo.addItems(["Brute Force", "Nearest Neighbor"])
        left_panel.addWidget(self.algo_combo)

        # Solve button
        self.solve_button = QPushButton("Solve TSP")
        self.solve_button.clicked.connect(self.solve_tsp)
        left_panel.addWidget(self.solve_button)

        # Result display
        self.result_label = QLabel("Result: Waiting to solve...")
        left_panel.addWidget(self.result_label)

        # Right panel: Visualization
        self.graphics_view = TSPGraphicsView(self.get_student_locations(), self.get_school_location())
        layout.addWidget(self.graphics_view, stretch=2)

    def get_school_location(self):
        """Parse school coordinates from input."""
        try:
            x, y = map(float, self.school_input.text().split(','))
            return (x, y)
        except:
            QMessageBox.warning(self, "Invalid Input", "Please enter valid school coordinates (x,y).")
            return (0, 0)

    def get_student_locations(self):
        """Parse student coordinates from table."""
        locations = []
        for row in range(self.student_table.rowCount()):
            try:
                x = float(self.student_table.item(row, 0).text())
                y = float(self.student_table.item(row, 1).text())
                locations.append((x, y))
            except:
                continue
        return locations if locations else [(1,1), (2,4), (5,3), (6,1), (3,5)]

    def solve_tsp(self):
        """Solve TSP and display results."""
        tsp = TSPSchoolService(self.get_student_locations(), self.get_school_location())
        algo = self.algo_combo.currentText()

        if algo == "Brute Force":
            path, distance = tsp.brute_force_tsp()
        else:
            path, distance = tsp.nearest_neighbor_tsp()

        path_str = " -> ".join([f"S{i+1}" for i in path])
        self.result_label.setText(f"Result:\nPath: School -> {path_str} -> School\nDistance: {distance:.2f}")
        self.graphics_view.locations = self.get_student_locations()
        self.graphics_view.school = self.get_school_location()
        self.graphics_view.draw_route(path)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TSPMainWindow()
    window.show()
    sys.exit(app.exec())
