# Unit Converter Web Application

## 📌 Project Description
The **Unit Converter Web Application** is a simple web-based tool that allows users to convert values between different units of measurement.  
It supports **Length**, **Weight**, and **Temperature** conversions using a clean and user-friendly interface.

This project does **not use any database**. All conversions are processed on the server after form submission.

---

## 🎯 Features
- Convert units of **Length**, **Weight**, and **Temperature**
- Separate sections/pages for each unit type
- Simple HTML form-based UI
- Server-side conversion logic
- Converted result displayed on the same page
- No database required

---

## 📐 Supported Units

### 🔹 Length
- Millimeter (mm)
- Centimeter (cm)
- Meter (m)
- Kilometer (km)
- Inch (inch)
- Foot (ft)
- Yard (yd)
- Mile (mile)

### 🔹 Weight
- Milligram (mg)
- Gram (g)
- Kilogram (kg)
- Ounce (oz)
- Pound (lb)

### 🔹 Temperature
- Celsius (°C)
- Fahrenheit (°F)
- Kelvin (K)

---

## 🛠️ Technologies Used
- **Frontend**
  - HTML
  - CSS

- **Backend**
  - Python
  - Django

---

## ⚙️ How the Application Works
1. User enters a value to convert.
2. User selects:
   - Unit to convert **from**
   - Unit to convert **to**
3. The form is submitted using the `POST` method.
4. The backend:
   - Receives the submitted data
   - Performs unit conversion
   - Sends the converted result back to the template
5. The converted value is displayed on the same webpage.

---

## 📂 Project Structure
<details> <summary><strong>Click to expand folder tree</strong></summary>
<br> <pre>

unit_converter/
│
├── templates/
│   └── index.html
│
├── views.py
├── urls.py
├── README.md
└── manage.py


</pre></details>


---

## ▶️ How to Run the Project

1. Clone the repository
    ```bash
    python manage.py migrate
2. Navigate to the project directory
    ```bash
    python manage.py runserver
3. Start the Django development server
   ```bash
   python manage.py runserver

link: https://roadmap.sh/projects/unit-converter


