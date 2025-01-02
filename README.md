# Food Ordering System

This is a Django-based food ordering system that allows users to view, add, edit, and delete food items. Users can also place orders for available food items.

## Features

- View a list of food items
- View detailed information about each food item
- Add new food items
- Edit existing food items
- Delete food items
- Place orders for food items

## Technologies Used

- Django
- Bootstrap

## Setup Instructions

### Prerequisites

- Python 3.6+
- Django 3.2+
- Git

### Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/krishna-shah-07/foodordering.git
    cd foodordering
    ```

2. Create and activate a virtual environment:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

4. Apply migrations:

    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Create a superuser to access the Django admin:

    ```sh
    python manage.py createsuperuser
    ```

6. Run the development server:

    ```sh
    python manage.py runserver
    ```

7. Open your browser and go to `http://127.0.0.1:8000/admin` to log in to the admin site and start adding food items.

## Usage

### Viewing Food Items

- Go to `http://127.0.0.1:8000/products/` to view the list of food items.

### Adding a New Food Item

- Click on the "Add New Food Item" button on the food list page.
- Fill in the form and submit to add a new food item.

### Editing a Food Item

- Click on the "Edit" button next to a food item on the food list page.
- Update the form and submit to save changes.

### Deleting a Food Item

- Click on the "Delete" button next to a food item on the food list page.
- Confirm the deletion.

### Placing an Order

- Click on a food item to view its details.
- Fill in the order quantity and submit the form to place an order.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Contact

For any questions or inquiries, please contact [krishnashah131103@gmail.com](mailto:krishnashah131103@gmail.com).