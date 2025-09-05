from django.shortcuts import render, redirect
from .utils import calculate_combinations
import openpyxl
import os

def home(request):
    results = None
    message = None
    cloth_name = None
    total = door = window = None

    if request.method == "POST":
        cloth_name = request.POST.get("cloth_name")
        total_str = request.POST.get("total")
        door_str = request.POST.get("door")
        window_str = request.POST.get("window")
        selected = request.POST.get("selected_case")

        # Agar user ne calculate karna hai
        if total_str and door_str and window_str and not selected:
            try:
                total = float(total_str)
                door = float(door_str)
                window = float(window_str)
                results = calculate_combinations(total, door, window)
            except ValueError:
                message = "❌ Invalid number entered!"

        # Agar user ne save karna hai
        elif selected and cloth_name:
            try:
                total = float(total_str)
                door = float(door_str)
                window = float(window_str)
                results = calculate_combinations(total, door, window)

                save_to_excel(cloth_name, total, door, window, results[selected])
                # ✅ Redirect hone se form reset hoga
                return redirect("home")
            except Exception as e:
                message = f"❌ Error: {str(e)}"

    return render(request, "calculator/index.html", {
        "results": results,
        "cloth_name": cloth_name,
        "total": total,
        "door": door,
        "window": window,
        "message": message,
    })


def save_to_excel(cloth_name, total, door, window, data):
    file_name = "waste_results.xlsx"

    # Agar file exist nahi karti to new workbook banao
    if not os.path.exists(file_name):
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        sheet.append([
            "Cloth Name",
            "Total Cloth (m)",
            "Door Size (m)",
            "Window Size (m)",
            "Case",
            "Doors",
            "Windows",
            "Wastage"
        ])
        workbook.save(file_name)

    # Open existing workbook
    workbook = openpyxl.load_workbook(file_name)
    sheet = workbook.active

    # Ab saari details add karenge
    sheet.append([
        cloth_name,
        total,
        door,
        window,
        data["type"],
        data["doors"],
        data["windows"],
        data["wastage"]
    ])

    workbook.save(file_name)
