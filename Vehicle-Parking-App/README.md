# 🚗 Vehicle Parking App - V1

A Flask-based multi-user parking system with admin and user roles. 
It uses SQLite for the database and shows parking summaries with charts.


### ✅ Admin Features:
- 🛠️ Add, Edit, and Delete Parking Lots  
- 📊 View all parking lots with status of each spot  
- 👥 View all registered users  
- 📈 See parking summary using charts:
  - Occupied vs Free Spots  
  - Total Income per Lot  
- ❌ **Prevent deletion of parking lots if any spot is currently occupied**

### ✅ User Features:
- 🔐 Register/Login with email and password  
- 📍 Search parking lots by pin code  
- 🚗 Book the first available spot (auto-allocation)  
- 🔓 Release spot with preview of time and price  
- 📜 View personal booking history  
- 📅 Weekly spending summary in bar chart  


## 🔧 Technologies Used

- Python 3.12.10
- Flask
- Flask-SQLAlchemy
- SQLite
- Matplotlib
- HTML & CSS
- Jinja2 (Templating)

---
VEHICLE-PARKING-APP/
│
├── pycache/ # Compiled Python files
│
├── instance/
│ └── parking.db # SQLite database
│
├── static/ # Static files (CSS, images, etc.)
│
├── templates/ # HTML templates
│ ├── add_parking.html
│ ├── admin_dashboard.html
│ ├── admin_summary.html
│ ├── book_spot.html
│ ├── edit_parking.html
│ ├── edit_user.html
│ ├── landing.html
│ ├── release_spot.html
│ ├── signup.html
│ ├── user_dashboard.html
│ ├── user_summary.html
│ ├── view_parking.html
│ └── view_users.html
│
├── venv/ # Virtual environment
│
├── app.py # Main application file
├── README.md # Project documentation
└── requirements.txt # Python dependencies




---

## 🧩 Entity-Relationship (ER) Model

### 🧍‍♂️ User
| Column      | Type        | Details                    |
|-------------|-------------|----------------------------|
| id          | Integer     | Primary Key, AutoIncrement |
| email       | String(80)  | Unique, Required           |
| password    | String(30)  | Required                   |
| name        | String(30)  | Required                   |
| address     | String(100) | Required                   |
| pin_code    | String(6)   | Required                   |
| is_admin    | Boolean     | Default = False            |

**Relationships:**
- Has many `ParkingSpots` (via `user_id`)
- Has many `History` records

---

### 🅿️ Parking_lot
| Column             | Type         | Details                    |
|--------------------|--------------|----------------------------|
| id                 | Integer      | Primary Key, AutoIncrement |
| parking_lot_name   | String(100)  | Required                   |
| address            | String(150)  | Required                   |
| pin_code           | String(6)    | Required                   |
| price_per_hour     | Integer      | Required                   |
| total_capacity     | Integer      | Required                   |
| avilable_capacity  | Integer      | Required                   |

**Relationships:**
- Has many `ParkingSpots` (via `id → lot_id`)

---

### 🔢 ParkingSpot
| Column         | Type        | Details                          |
|----------------|-------------|----------------------------------|
| id             | Integer     | Primary Key                      |
| lot_id         | Integer     | Foreign Key → Parking_lot(id)    |
| spot_number    | String(10)  | Required                         |
| is_occupied    | Boolean     | Default = False                  |
| user_id        | Integer     | Foreign Key → User(id), Nullable|
| vehicle_number | String(20)  | Optional                         |
| start_time     | DateTime    | Optional                         |
| end_time       | DateTime    | Optional                         |

**Relationships:**
- Belongs to one `Parking_lot`
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



### 🔗 Relationships Summary







