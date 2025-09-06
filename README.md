# 🚗 Vehicle Parking App - V1

A **Flask-based multi-user parking management system** with separate **Admin** and **User** roles.  
It uses **SQLite** as the database and generates **parking summaries with interactive charts**.  

---

## ✨ Features

### 👨‍💼 Admin Features
- 🛠️ Manage Parking Lots (Add, Edit, Delete)  
- 📊 View all parking lots with live spot status  
- 👥 Manage registered users  
- 📈 Generate parking analytics with charts:
  - Occupied vs Free Spots  
  - Income per Parking Lot  
- ❌ Prevent deletion of lots if any spot is occupied  

### 👤 User Features
- 🔐 Register & Login with email and password  
- 📍 Search parking lots by **PIN code**  
- 🚗 Auto-allocate the first available parking spot  
- 🔓 Release a spot (preview total time & price before confirming)  
- 📜 View booking history  
- 📅 Weekly spending summary in **bar chart**  

---

## 🛠️ Tech Stack

- **Backend:** Python (Flask, Flask-SQLAlchemy)  
- **Database:** SQLite  
- **Frontend:** HTML, CSS, Jinja2 Templates  
- **Visualization:** Matplotlib  
- **Environment:** Python venv  

---
## 📂 Project Structure

```bash
VEHICLE-PARKING-APP/
│
├── app.py                # Main Flask application
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
│
├── instance/             # Instance folder (auto-created by Flask)
│   └── parking.db        # SQLite database
│
├── static/               # Static assets (CSS, images, JS)
│   └── style.css         # Example CSS file
│
├── templates/            # Jinja2 HTML templates
│   ├── admin/            # Admin pages
│   │   ├── admin_dashboard.html
│   │   ├── admin_summary.html
│   │   ├── add_parking.html
│   │   ├── edit_parking.html
│   │   ├── view_parking.html
│   │   └── view_users.html
│   │
│   ├── user/             # User pages
│   │   ├── user_dashboard.html
│   │   ├── user_summary.html
│   │   ├── book_spot.html
│   │   ├── release_spot.html
│   │   └── signup.html
│   │
│   └── shared/           # Common/landing pages
│       ├── landing.html
│       └── edit_user.html
│
├── venv/                 # Virtual environment (not pushed to GitHub)
│
└── __pycache__/          # Compiled Python files

---

## 🧩 Entity-Relationship (ER) Model

### 🧍 User
| Column   | Type        | Details                    |
|----------|-------------|----------------------------|
| id       | Integer     | Primary Key, AutoIncrement |
| email    | String(80)  | Unique, Required           |
| password | String(30)  | Required                   |
| name     | String(30)  | Required                   |
| address  | String(100) | Required                   |
| pin_code | String(6)   | Required                   |
| is_admin | Boolean     | Default = False            |

**Relationships:**  
- Has many `ParkingSpots` (via `user_id`)  
- Has many `History` records  

---

### 🅿️ ParkingLot
| Column            | Type         | Details                    |
|-------------------|--------------|----------------------------|
| id                | Integer      | Primary Key, AutoIncrement |
| parking_lot_name  | String(100)  | Required                   |
| address           | String(150)  | Required                   |
| pin_code          | String(6)    | Required                   |
| price_per_hour    | Integer      | Required                   |
| total_capacity    | Integer      | Required                   |
| available_capacity| Integer      | Required                   |

**Relationships:**  
- Has many `ParkingSpots` (via `id → lot_id`)  

---

### 🔢 ParkingSpot
| Column         | Type        | Details                          |
|----------------|-------------|----------------------------------|
| id             | Integer     | Primary Key                      |
| lot_id         | Integer     | Foreign Key → ParkingLot(id)     |
| spot_number    | String(10)  | Required                         |
| is_occupied    | Boolean     | Default = False                  |
| user_id        | Integer     | Foreign Key → User(id), Nullable|
| vehicle_number | String(20)  | Optional                         |
| start_time     | DateTime    | Optional                         |
| end_time       | DateTime    | Optional                         |

**Relationships:**  
- Belongs to one `ParkingLot`  
- Optionally linked to one `User`  
- Has many `History` records  

---

### 📄 History
| Column         | Type        | Details                              |
|----------------|-------------|--------------------------------------|
| id             | Integer     | Primary Key                          |
| user_id        | Integer     | Foreign Key → User(id)               |
| spot_id        | Integer     | Foreign Key → ParkingSpot(id)        |
| vehicle_number | String(20)  | Required                             |
| start_time     | DateTime    | Required                             |
| end_time       | DateTime    | Optional                             |
| total_time     | String(50)  | Optional (formatted duration string) |
| total_price    | Float       | Optional (calculated on release)     |

**Relationships:**  
- Belongs to `User`  
- Belongs to `ParkingSpot`  

---

## 🔗 Relationships Summary
- **User → ParkingSpots → History**  
- **ParkingLot → ParkingSpots → History**  
- **History** acts as a transaction log for bookings and releases.  

---

git clone https://github.com/24f2000396/vehicle-parking-app.git
cd vehicle-parking-app

# Create virtual environment
python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows

# Install dependencies
pip install -r requirements.txt

# Run Flask server
flask run

