#!/usr/bin/env python3
from app import app, db, Payment
import json

with app.app_context():
    # Get all payments
    payments = Payment.query.all()
    print(f"Found {len(payments)} payments")
    
    # Convert to dict
    data = []
    for p in payments:
        data.append({
            'id': p.id,
            'guest_name': p.guest_name,
            'amount': p.amount,
            'payment_method': p.payment_method,
            'description': p.description,
            'created_at': p.created_at.isoformat() if p.created_at else None
        })
    
    # Save to JSON
    with open('seed_data.json', 'w') as f:
        json.dump(data, f, indent=2)
    
    print(f"✓ Exported {len(data)} records to seed_data.json")
    
    if data:
        print("\nSample record:")
        print(json.dumps(data[0], indent=2))
