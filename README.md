# Django Product API

This Django application provides a simple API for managing products.

## Models

### Product

The `Product` model represents a product with the following fields:

- `product_title`: CharField - maximum length of 100 characters
- `product_description`: TextField
- `product_price`: DecimalField - maximum digits of 10 with 2 decimal places
- `trace_date`: DateTimeField - automatically set to the current date and time when the product is created
- `trace_count`: IntegerField - default value of 0

## Serializers

### ProductSerializer

The `ProductSerializer` is responsible for serializing and deserializing `Product` instances. It includes the fields: `id`, `product_title`, `product_description`, `product_price`, `trace_date`, and `trace_count`.

## Views

### ProductView

#### `POST /api/products/`

Creates a new product.

#### `PUT /api/products/{pk}/`

Updates an existing product identified by its primary key (`pk`).

#### `GET /api/products/`

Lists all products.

#### `DELETE /api/products/{pk}/`

Deletes an existing product identified by its primary key (`pk`).

### ProductTraceView

#### `GET /api/products/top-products/{duration}/`

Gets the top products based on the specified duration. Valid durations: `all`, `lastDay`, `lastWeek`.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yasmeenahilal/productManagement.git
   pip install -r requirements.txt
