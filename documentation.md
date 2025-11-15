# Beach Resort Booking System - Payment Module Documentation

## System Overview
**Full System Name:** Beach Resort Booking Management System
**Subsystem:** Payment Module
**Purpose:** Manage and track guest payments for resort bookings

## Use Cases & Actors

### Actor: Receptionist
- Records guest payments
- Views payment history
- Edits payment information
- Deletes incorrect payment records
- Generates payment reports

### Actor: Manager
- Views payment reports
- Analyzes payment data
- Monitors payment methods

## Use Cases Implemented

| Use Case ID | Use Case Name | Actor | Description |
|---|---|---|---|
| UC-001 | Record Payment | Receptionist | Create a new payment record for a guest |
| UC-002 | View Payment List | Receptionist, Manager | Display all recorded payments with details |
| UC-003 | Edit Payment | Receptionist | Update payment details after recording |
| UC-004 | Delete Payment | Receptionist | Remove incorrect or duplicate payment records |
| UC-005 | Generate Payment Report | Manager, Receptionist | Generate and print payment reports |

## Mini Events Table

### UC-001: Record Payment
| Event # | Event Name | Trigger | Description |
|---|---|---|---|
| 1 | Payment Form Display | Receptionist clicks "Add Payment" | Display form to input payment details |
| 2 | Guest Name Input | User enters guest name | Validate guest name is provided |
| 3 | Amount Input | User enters payment amount | Validate amount format and value |
| 4 | Payment Method Selection | User selects payment method | Choose from Cash, GCash, Credit Card |
| 5 | Description Input | User enters payment description | Optional field for payment notes |
| 6 | Submit Payment | User clicks "Save" button | Validate and store payment in database |
| 7 | Payment Confirmation | Payment saved successfully | Display success message and redirect to list |

### UC-002: View Payment List
| Event # | Event Name | Trigger | Description |
|---|---|---|---|
| 1 | Navigate to List | User clicks "Payments" in navbar | Load all payments from database |
| 2 | Display Payments | Page loads | Show all payment records in table format |
| 3 | Show Attributes | List renders | Display ID, Guest Name, Amount, Method, Date |
| 4 | Pagination Ready | Large datasets | Prepare for future pagination implementation |

### UC-003: Edit Payment
| Event # | Event Name | Trigger | Description |
|---|---|---|---|
| 1 | Edit Link Click | User clicks "Edit" button | Fetch payment record by ID |
| 2 | Load Payment Form | Payment data retrieved | Populate form with current payment details |
| 3 | Modify Guest Name | User changes guest name | Update guest_name field |
| 4 | Modify Amount | User changes amount | Update amount with validation |
| 5 | Modify Payment Method | User selects different method | Update payment_method field |
| 6 | Modify Description | User updates description | Update description field |
| 7 | Save Changes | User clicks "Save" button | Update record in database |
| 8 | Confirmation | Update successful | Display success message and return to list |

### UC-004: Delete Payment
| Event # | Event Name | Trigger | Description |
|---|---|---|---|
| 1 | Delete Link Click | User clicks "Delete" button | Show confirmation dialog |
| 2 | Confirm Deletion | User confirms delete action | Remove payment record from database |
| 3 | Deletion Success | Record deleted | Display success message |
| 4 | List Refresh | Deletion complete | Return to list page with updated records |

### UC-005: Generate Payment Report
| Event # | Event Name | Trigger | Description |
|---|---|---|---|
| 1 | Report Page Navigate | User clicks "Report" in navbar | Load report page |
| 2 | Calculate Totals | Page loads | Sum all payment amounts |
| 3 | Group by Method | Data processing | Organize payments by payment method |
| 4 | Display Report | Report renders | Show payment summary statistics |
| 5 | Print Report | User clicks "Print" button | Trigger browser print dialog |

## Model Schema

### Payment Entity
```
Payment
├── id (Integer, Primary Key)
├── guest_name (String, Required)
├── amount (Float, Required)
├── payment_method (String, Required) [Cash, GCash, Credit Card]
├── description (String, Optional)
└── created_at (DateTime, Auto-generated)
```

## Technology Stack
- **Backend:** Python Flask
- **Database:** SQLite with SQLAlchemy ORM
- **Frontend:** HTML5, Bootstrap 5, Jinja2 Templates
- **Features:** CRUD operations, Report generation, Print functionality