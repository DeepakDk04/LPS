# Loyalty Point System (LPS)

The Loyalty Point System (LPS) is a Django-based web application designed to enable vendors to manage and issue loyalty points to their customers. Customers can accumulate points for purchases and later redeem them for gift cards and other rewards.

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

## Project Overview

LPS aims to provide a seamless way for vendors to boost customer engagement by rewarding loyal customers. Vendors can register their accounts on the platform, submit order details, and request loyalty points for each order placed. The system then calculates and assigns loyalty points to the customer associated with the order. Customers can log in, view their accumulated points, and redeem them for gift cards.

### Features

Vendor Account Management: Vendors can create and manage their accounts.
Order-Based Points Request: Vendors can submit orders to request loyalty points for their customers.
Customer Account: Customers can log in to view their loyalty points balance.
Point Redemption: Customers can redeem points for various gift cards available on the platform.
Admin Dashboard: For monitoring and managing vendor requests, customer accounts, and point allocations.

### Tech Stack

Backend: Django, Django REST Framework for API endpoints
Database: SQLite (or your chosen database)
Frontend: HTML, CSS, JavaScript (optional: React or other JS frameworks)
Authentication: Django's built-in authentication for user (vendor and customer) login

#### Installation and Setup

Clone the Repository:

```bash
git clone https://github.com/DeepakDk04/LPS.git
cd LPS
```

Install Requirements:

```bash
pip install -r requirements.txt
```

Database Setup: Update the database settings in settings.py, then run migrations:

```bash
python manage.py migrate
```

Run Server:

```bash
python manage.py runserver
```

### Environment Variables

To run this project, you will need to add the following environment variables to your **.env** file

`LOYPT_SECRET_KEY`

### Usage

Vendor: Register an account and submit order details to request points for customers.
Customer: Login to view loyalty points and redeem them for rewards.
