import os
import json
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///payments.db'
app.config['SECRET_KEY'] = 'your-secret-key'
db = SQLAlchemy(app)

# Payment Model
class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    guest_name = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    payment_method = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

def initialize_database():
    """Create tables and load seed data on first run"""
    db.create_all()
    
    # Check if database is empty and seed_data.json exists
    if Payment.query.first() is None and os.path.exists('seed_data.json'):
        try:
            with open('seed_data.json', 'r') as f:
                seed_data = json.load(f)
            
            if seed_data:  # Only load if there's data
                for item in seed_data:
                    payment = Payment(
                        guest_name=item.get('guest_name', 'Unknown'),
                        amount=float(item.get('amount', 0)),
                        payment_method=item.get('payment_method', 'Cash'),
                        description=item.get('description', ''),
                        created_at=datetime.fromisoformat(item['created_at']) if 'created_at' in item else datetime.utcnow()
                    )
                    db.session.add(payment)
                
                db.session.commit()
                print(f"✓ Database initialized with {len(seed_data)} payment records!")
        except Exception as e:
            print(f"Warning: Could not load seed data: {e}")

def export_seed_data():
    """Export current payments to seed_data.json"""
    try:
        payments = Payment.query.all()
        data = [{
            'id': p.id,
            'guest_name': p.guest_name,
            'amount': p.amount,
            'payment_method': p.payment_method,
            'description': p.description,
            'created_at': p.created_at.isoformat() if p.created_at else None
        } for p in payments]
        
        with open('seed_data.json', 'w') as f:
            json.dump(data, f, indent=2)
    except Exception as e:
        print(f"Warning: Could not export seed data: {e}")

# Create database and initialize
with app.app_context():
    initialize_database()


@app.route('/')
def home():
    return redirect(url_for('list_payments'))


# List + Add
@app.route('/payments', methods=['GET', 'POST'])
def list_payments():
    if request.method == 'POST':
        guest = request.form.get('guest_name')
        amount = request.form.get('amount')
        method = request.form.get('payment_method')
        desc = request.form.get('description')

        if not (guest and amount and method):
            flash('Guest, amount, and method are required.', 'danger')
        else:
            p = Payment(
                guest_name=guest,
                amount=float(amount),
                payment_method=method,
                description=desc
            )
            db.session.add(p)
            db.session.commit()
            export_seed_data()  # Auto-export after adding
            flash('Payment added.', 'success')
            return redirect(url_for('list_payments'))

    payments = Payment.query.order_by(Payment.created_at.desc()).all()
    return render_template('list.html', payments=payments)


# Edit
@app.route('/payments/<int:pid>/edit', methods=['GET', 'POST'])
def edit_payment(pid):
    p = Payment.query.get_or_404(pid)

    if request.method == 'POST':
        p.guest_name = request.form.get('guest_name')
        p.amount = float(request.form.get('amount'))
        p.payment_method = request.form.get('payment_method')
        p.description = request.form.get('description')
        db.session.commit()
        export_seed_data()  # Auto-export after editing
        flash('Payment updated.', 'success')
        return redirect(url_for('list_payments'))

    return render_template('edit.html', payment=p)


# Delete
@app.route('/payments/<int:pid>/delete', methods=['POST'])
def delete_payment(pid):
    p = Payment.query.get_or_404(pid)
    db.session.delete(p)
    db.session.commit()
    export_seed_data()  # Auto-export after deleting
    flash('Payment deleted.', 'success')
    return redirect(url_for('list_payments'))


# Report
@app.route('/report')
def report():
    payments = Payment.query.order_by(Payment.created_at.desc()).all()
    total_amount = sum(p.amount for p in payments)
    payment_count = len(payments)
    
    payments_by_method = {}
    for payment in payments:
        if payment.payment_method not in payments_by_method:
            payments_by_method[payment.payment_method] = {'count': 0, 'total': 0}
        payments_by_method[payment.payment_method]['count'] += 1
        payments_by_method[payment.payment_method]['total'] += payment.amount
    
    return render_template('report.html', 
                         payments=payments,
                         total_amount=total_amount,
                         payment_count=payment_count,
                         payments_by_method=payments_by_method)


if __name__ == '__main__':
    app.run(debug=True)