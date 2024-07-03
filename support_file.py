import streamlit as st
import sqlite3

### User-defined functions for DataBase ###
            
def get_db_connection():
    conn = sqlite3.connect('expense_register.db')
    return conn

def initialize_db():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            purchase_date NUMERIC NOT NULL,
            bill_number TEXT NOT NULL,
            provider_name TEXT NOT NULL,
            purchase_category TEXT NOT NULL,
            pretax_amount NUMERIC NOT NULL,
            tax_amount NUMERIC NOT NULL,
            comments TEXT
        )
    ''')
    conn.commit()
    cur.close()
    conn.close()

def save_expenses(purchase_date, bill_number, provider_name, purchase_category, pretax_amount, tax_amount, comments):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO expenses (purchase_date, bill_number, provider_name, purchase_category, pretax_amount, tax_amount, comments) VALUES (?, ?, ?, ?, ?, ?, ?)",
        (purchase_date, bill_number, provider_name, purchase_category, pretax_amount, tax_amount, comments)
    )
    conn.commit()
    cur.close()
    conn.close()

def fetch_expenses(bill_number):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM expenses WHERE bill_number = ?", (bill_number,))
    result = cur.fetchone()
    cur.close()
    conn.close()
    return result

def update_expenses(purchase_date, bill_number, provider_name, purchase_category, pretax_amount, tax_amount):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE notes SET purchase_date=?, provider_name=?, purchase_category=?, pretax_amount=?, tax_amount=? WHERE bill_number=?",
        (purchase_date, provider_name, purchase_category, pretax_amount, tax_amount, bill_number)
    )
    conn.commit()
    cur.close()
    conn.close()