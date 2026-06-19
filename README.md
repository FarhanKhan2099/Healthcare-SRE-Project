# Healthcare Management System - Software Re-Engineering Project

Course Project for Software Re-Engineering
Department of Software Engineering, SMIU

## Project By
- Farhan Ahmed Khan

## Project Overview
This project re-engineers a legacy PHP Healthcare Management System into a 
modern Python Flask application with PostgreSQL, REST API integration, 
Stripe payment gateway, and EasyPaisa payment confirmation with email notifications.

## Modules
- **patient_module/** - Patient management REST API (Flask, port 5001)
- **billing_module/** - Billing, payments, and notifications (Flask, port 5005)

## Technologies Used
- Python Flask
- PostgreSQL
- Stripe Payment Gateway
- EasyPaisa (manual transaction verification)
- SMTP Email Notifications

## How to Run
1. Create virtual environment: `python3 -m venv venv`
2. Activate: `source venv/bin/activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Run: `python app.py`
