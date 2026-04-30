# ZenCommerce

## 🛒 Full-Stack E-Commerce Platform

This project is a full-stack e-commerce web application built using **Django (Python)** for the backend and **HTML, CSS, and JavaScript** for the frontend. It provides a complete online shopping experience, including user authentication, product browsing, cart management, and secure payment processing.

---

## 🚀 Features

### 🔐 User Authentication

* Secure user registration and login system
* Session-based authentication for maintaining user state
* Protected routes for authenticated users

### 📦 Product & Catalog Management

* Dynamic product listing with categories
* Category-based filtering for easy navigation
* Detailed product view for better decision-making

### 🛍️ Shopping Cart

* Add, update, and remove items from the cart
* Session-based cart persistence
* Seamless user experience during shopping

### 💳 Payment Integration

* Integrated Razorpay payment gateway
* Supports UPI, credit/debit cards, and net banking
* Real-time payment verification and order confirmation

### 🗄️ Database Design

* Built using Django ORM with SQLite
* Models include:

  * Products
  * Categories
  * Customers
  * Orders
* Maintains relationships and payment status tracking

### 🎨 Responsive UI

* Built with HTML, CSS, and JavaScript
* Clean and modern design
* Smooth checkout flow
* Error handling for better UX

---

## 🛠️ Tech Stack

* **Backend:** Django, Python
* **Frontend:** HTML, CSS, JavaScript
* **Database:** SQLite
* **Payment Gateway:** Razorpay

---

## ⚙️ Installation & Setup

1. Clone the repository:
   git clone https://github.com/Chandan2597/ZenCommerce

2. Navigate to the project directory:
   cd your-repo-name

3. Create a virtual environment:
   python -m venv venv

4. Activate the virtual environment:

* Windows: venv\Scripts\activate
* Mac/Linux: source venv/bin/activate

5. Install dependencies:
   pip install -r requirements.txt

6. Apply migrations:
   python manage.py migrate

7. Create a superuser (optional):
   python manage.py createsuperuser

8. Run the development server:
   python manage.py runserver

9. Open in browser:
   http://127.0.0.1:8000/

---

### ⚠️ Note

* Add your Razorpay API keys in `settings.py` to enable the payment functionality.



