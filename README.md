# Phonebook Application

This is a simple phonebook application built with Django. It allows you to add contacts with multiple phone numbers, list all contacts, and view contact details.

## Features

- Add a contact with multiple phone numbers
- List all contacts
- View contact details

## Database Schema

The schema for this application includes two main models:

- **Contact**: Stores the name of the contact.
- **PhoneNumber**: Stores phone numbers associated with each contact.

The relationship is one-to-many: one contact can have multiple phone numbers.

+-------------+ +-----------------+
| Contact | 1 --- * | PhoneNumber |
+-------------+ +-----------------+
| id (PK) | | id (PK) |
| name | | contact_id (FK) |
+-------------+ | number |
+-----------------+

## Running the Application

### Using Docker

1. **Build the Docker image:**

    ```sh
    docker build -t phonebook-app .
    ```

2. **Run the Docker container:**

    ```sh
    docker run -p 8000:8000 phonebook-app
    ```

The application will be available at `http://localhost:8000`.
