# **Politician Stock Tracker**

Politician Stock Tracker is an open-source web application that tracks the stock trades of US politicians. It is built with Python, Django, and Django Rest Framework.

## **Features**

- Retrieve information on politicians, stocks, and trades
- Filter trades by politician
- Access data through a RESTful API

## **Getting Started**

These instructions will help you set up the project on your local machine for development and testing purposes.

### **Prerequisites**

- Python 3.7 or later
- pip (Python package manager)

### **Installation**

1. Clone the repository:

```bash

git clone https://github.com/yourusername/politracker.git

```

1. Change to the project directory:

```bash
cd politracker
```

1. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # For Unix-based systems
venv\Scripts\activate  # For Windows
```

1. Install the required packages:

```bash
pip install -r requirements.txt
```

1. Apply the database migrations:

```bash
python manage.py migrate
```

1. Load initial data (if you have any fixtures or data import scripts):

```bash
python manage.py loaddata initial_data.json  # Replace with your fixture filename
```

1. Run the development server:

```bash
python manage.py runserver
```

Now, you can access the application at **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**.

## **API Endpoints**

- **`/api/politicians/`**: List all politicians, create a new politician
- **`/api/politicians/<id>/`**: Retrieve, update, or delete a specific politician by ID
- **`/api/stocks/`**: List all stocks, create a new stock
- **`/api/stocks/<id>/`**: Retrieve, update, or delete a specific stock by ID
- **`/api/trades/`**: List all trades, create a new trade
- **`/api/trades/<id>/`**: Retrieve, update, or delete a specific trade by ID

## **Contributing**

We welcome contributions from the community! Please read our ______ file for guidelines on how to contribute to this project.

## **License**

This project is licensed under the