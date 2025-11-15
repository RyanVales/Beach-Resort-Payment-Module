Group 3
Booc, Jose
Gatab, Giofranco
Lavina, Lorenzo
Orcejola, Ken
Orcine, Jessa
Vales, Justin


## Key Functionalities & Use Cases

### 1. **Record Payment (UC-001)**
- Receptionist can add new payment records for guests
- Input fields: Guest Name, Amount, Payment Method, Description
- Payment methods supported: Cash, GCash, Credit Card
- Automatic timestamp recording for each payment
- Form validation ensures data integrity

### 2. **View Payment List (UC-002)**
- Display all recorded payments in a responsive table format
- Shows: Payment ID, Guest Name, Amount, Payment Method, Date Created, Description
- Quick access to edit and delete functions for each payment
- Add new payment form available at the top of the list page
- Responsive design works on desktop and mobile devices

### 3. **Edit Payment (UC-003)**
- Receptionist can modify payment details after recording
- Edit form pre-populated with existing payment data
- Editable fields: Guest Name, Amount, Payment Method, Description
- Changes are validated before saving
- Secure form accessible only through the list page

### 4. **Delete Payment (UC-004)**
- Remove incorrect or duplicate payment records
- Confirmation dialog prevents accidental deletion
- Deleted records are permanently removed from database
- Returns to updated list after successful deletion

### 5. **Generate Payment Report (UC-005)**
- Generate comprehensive payment reports with summaries
- **Report includes:**
  - Total payment amount (in PHP)
  - Total number of transactions
  - Average payment amount
  - Breakdown by payment method (Cash, GCash, Credit Card)
  - Detailed payment list with all records
- Print-friendly report format
- Export capability for financial analysis
