from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def handle_convert(request):
    result = None

    if request.method == "POST":
        category = request.POST.get("category")
        value = float(request.POST.get("value"))
        from_unit = request.POST.get("from_unit")
        to_unit = request.POST.get("to_unit")
        converted = 0

        # ---------- LENGTH ----------
        if category == "length":
            to_meter = {
                "mm": 0.001,
                "cm": 0.01,
                "m": 1,
                "km": 1000,
                "inch": 0.0254,
                "ft": 0.3048,
                "yd": 0.9144,
                "mi": 1609.34
            }

            value_m = value * to_meter[from_unit]
            converted = value_m / to_meter[to_unit]

        # ---------- WEIGHT ----------
        elif category == "weight":
            to_kg = {
                "mg": 0.000001,
                "g": 0.001,
                "kg": 1,
                "oz": 0.0283495,
                "lb": 0.453592
            }

            value_kg = value * to_kg[from_unit]
            converted = value_kg / to_kg[to_unit]

        # ---------- TEMPERATURE ----------
        elif category == "temperature":
            # Convert to Celsius first
            if from_unit == "c":
                temp_c = value
            elif from_unit == "f":
                temp_c = (value - 32) * 5 / 9
            else:  # kelvin
                temp_c = value - 273.15

            # Convert from Celsius to target
            if to_unit == "c":
                converted = temp_c
            elif to_unit == "f":
                converted = (temp_c * 9 / 5) + 32
            else:
                converted = temp_c + 273.15

        result = f"{value} {from_unit.upper()} = {round(converted, 2)} {to_unit.upper()}"

    return render(request, "index.html", {"result": result})