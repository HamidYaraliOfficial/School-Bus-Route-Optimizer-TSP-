# English - School Bus Route Optimizer (TSP)

## Project Overview
The School Bus Route Optimizer is a Python application designed to solve the Traveling Salesman Problem (TSP) for optimizing school bus routes. It calculates the shortest possible route for a school bus to pick up students from various locations and return to the school. The application features a professional graphical user interface (GUI) built with PyQt6, supporting both Brute Force and Nearest Neighbor algorithms. It provides a multilingual interface in English, Persian, Chinese, and Russian for enhanced accessibility.

## Features
- **Route Optimization**: Computes the shortest path for picking up students using Brute Force or Nearest Neighbor algorithms.
- **Interactive GUI**: User-friendly interface to input student and school coordinates and visualize the route.
- **Multilingual Support**: Interface and messages available in English, Persian, Chinese, and Russian.
- **Visualization**: Displays the bus route with student locations (blue circles) and school (red square) using a graphical plot.
- **Flexible Input**: Allows users to input coordinates via a table and select the algorithm for solving TSP.

## Prerequisites
- Python 3.8 or higher
- Required libraries:
  - `PyQt6`
  - `matplotlib`
- No external APIs or services are required.

## Installation and Setup
1. Download the repository.
2. Install the required libraries:
   ```bash
   pip install PyQt6 matplotlib
   ```
3. Run the `tsp_school_service_gui.py` file:
   ```bash
   python tsp_school_service_gui.py
   ```

## Usage
1. Launch the application to access the GUI.
2. Enter the school coordinates in the format `x,y` (e.g., `0,0`).
3. Input student coordinates in the table (X and Y columns).
4. Select the desired algorithm (Brute Force or Nearest Neighbor) from the dropdown menu.
5. Click the "Solve TSP" button to compute and display the shortest route and total distance.
6. View the visualized route on the graphical display, showing the school, student locations, and the optimized path.

## Developer
Developed by Hamid Yarali  
- GitHub: https://github.com/HamidYaraliOfficial  
- Instagram: https://www.instagram.com/hamidyaraliofficial?igsh=MWpxZjhhMHZuNnlpYQ==  
- Telegram: @Hamid_Yarali  

## License
This project is licensed under the MIT License.

---

# فارسی - بهینه‌ساز مسیر سرویس مدرسه (TSP)

## معرفی پروژه
بهینه‌ساز مسیر سرویس مدرسه یک برنامه پایتونی است که برای حل مسئله فروشنده دوره‌گرد (TSP) جهت بهینه‌سازی مسیر سرویس مدرسه طراحی شده است. این برنامه کوتاه‌ترین مسیر ممکن را برای سرویس مدرسه جهت سوار کردن دانش‌آموزان از مکان‌های مختلف و بازگشت به مدرسه محاسبه می‌کند. این برنامه دارای یک رابط کاربری گرافیکی (GUI) حرفه‌ای ساخته‌شده با PyQt6 است و از الگوریتم‌های بروت‌فورس و نزدیک‌ترین همسایه پشتیبانی می‌کند. رابط کاربری چندزبانه (فارسی، انگلیسی، چینی و روسی) برای دسترسی بهتر ارائه شده است.

## ویژگی‌ها
- **بهینه‌سازی مسیر**: محاسبه کوتاه‌ترین مسیر برای سوار کردن دانش‌آموزان با استفاده از الگوریتم‌های بروت‌فورس یا نزدیک‌ترین همسایه.
- **رابط کاربری تعاملی**: رابط کاربری ساده برای وارد کردن مختصات دانش‌آموزان و مدرسه و نمایش مسیر.
- **پشتیبانی چندزبانه**: رابط کاربری و پیام‌ها به زبان‌های فارسی، انگلیسی، چینی و روسی.
- **نمایش بصری**: نمایش مسیر سرویس با مکان‌های دانش‌آموزان (دوایر آبی) و مدرسه (مربع قرمز) در یک نمودار گرافیکی.
- **ورودی انعطاف‌پذیر**: امکان وارد کردن مختصات از طریق جدول و انتخاب الگوریتم برای حل TSP.

## پیش‌نیازها
- پایتون نسخه 3.8 یا بالاتر
- کتابخانه‌های مورد نیاز:
  - `PyQt6`
  - `matplotlib`
- نیازی به API یا سرویس خارجی نیست.

## نصب و راه‌اندازی
1. مخزن را دانلود کنید.
2. کتابخانه‌های مورد نیاز را نصب کنید:
   ```bash
   pip install PyQt6 matplotlib
   ```
3. فایل `tsp_school_service_gui.py` را اجرا کنید:
   ```bash
   python tsp_school_service_gui.py
   ```

## استفاده
1. برنامه را اجرا کنید تا رابط کاربری گرافیکی باز شود.
2. مختصات مدرسه را به‌صورت `x,y` (مانند `0,0`) وارد کنید.
3. مختصات دانش‌آموزان را در جدول (ستون‌های X و Y) وارد کنید.
4. الگوریتم مورد نظر (بروت‌فورس یا نزدیک‌ترین همسایه) را از منوی کشویی انتخاب کنید.
5. روی دکمه "حل TSP" کلیک کنید تا کوتاه‌ترین مسیر و مسافت کل محاسبه و نمایش داده شود.
6. مسیر بهینه‌شده را در نمایش گرافیکی مشاهده کنید که شامل مدرسه، مکان‌های دانش‌آموزان و مسیر بهینه است.

## توسعه‌دهنده
توسعه داده شده توسط حمید یارعلی  
- GitHub: https://github.com/HamidYaraliOfficial  
- Instagram: https://www.instagram.com/hamidyaraliofficial?igsh=MWpxZjhhMHZuNnlpYQ==  
- Telegram: @Hamid_Yarali  

## لایسنس
این پروژه تحت مجوز MIT منتشر شده است.

---

# 中文 - 校车路线优化器 (TSP)

## 项目概述
校车路线优化器是一个基于 Python 的应用程序，旨在通过解决旅行推销员问题 (TSP) 来优化校车路线。它计算校车从不同地点接送学生并返回学校的最短路径。该应用程序配备了使用 PyQt6 构建的专业图形用户界面 (GUI)，支持暴力算法和最近邻算法，并提供多语言界面（中文、波斯语、英语和俄语），以增强可访问性。

## 功能
- **路线优化**：使用暴力算法或最近邻算法计算接送学生的最短路径。
- **交互式 GUI**：用户友好的界面，用于输入学生和学校坐标并可视化路线。
- **多语言支持**：界面和消息支持中文、波斯语、英语和俄语。
- **可视化**：通过图形展示校车路线，学生位置（蓝色圆圈）和学校（红色方块）。
- **灵活输入**：允许用户通过表格输入坐标并选择解决 TSP 的算法。

## 前提条件
- Python 3.8 或更高版本
- 所需库：
  - `PyQt6`
  - `matplotlib`
- 无需外部 API 或服务。

## 安装与设置
1. 下载存储库。
2. 安装所需库：
   ```bash
   pip install PyQt6 matplotlib
   ```
3. 运行 `tsp_school_service_gui.py` 文件：
   ```bash
   python tsp_school_service_gui.py
   ```

## 使用方法
1. 启动应用程序以打开图形用户界面。
2. 以 `x,y` 格式输入学校坐标（例如，`0,0`）。
3. 在表格中输入学生坐标（X 和 Y 列）。
4. 从下拉菜单中选择所需的算法（暴力算法或最近邻算法）。
5. 点击“解决 TSP”按钮以计算并显示最短路线和总距离。
6. 在图形显示中查看优化后的路线，显示学校、学生位置和最优路径。

## 开发者
由 Hamid Yarali 开发  
- GitHub: https://github.com/HamidYaraliOfficial  
- Instagram: https://www.instagram.com/hamidyaraliofficial?igsh=MWpxZjhhMHZuNnlpYQ==  
- Telegram: @Hamid_Yarali  

## 许可证
本项目采用 MIT 许可证发布。