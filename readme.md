
# Product categorization and product recommendation using Machine Learning

This is an E-Commerce web application based on django framework.
It provides basic e-commerce functionalities to users and also includes techniques of product categorization using Naive base classification and product recommendation using Co-sine similarity algorithm.


## Authors

- [Harshad Rane](https://github.com/harshadrane67)
- [Prem Mevada](https://github.com/PremMevada)
- [Tejas Mandhare](https://github.com/mandharet)
- [Omkar Suryawanshi](#)


## Website Overview:

This e-Shop website offers a seamless experience for both buyers and sellers. Users can explore our products, conveniently categorized for easy navigation. If they decide to make a purchase, registration as a customer is required, providing necessary information before proceeding to checkout.

**Buyer's Experience:**

- **Product Categorization:** Our website employs an intelligent product categorization system for an organized shopping experience.
- **Registration:** Buyers need to register to complete purchases, ensuring a personalized shopping journey.
- **Recommendation System:** Utilizing Cosine Similarity, our platform suggests products based on user browsing and order history, enhancing the shopping experience.

**Seller's Experience:**

- **Vendor Registration:** Sellers can register as vendors, providing essential company details. They can add products suitable for a fashion e-commerce platform.
- **Automated Categorization:** Our system automates product categorization, streamlining the seller's workflow.
- **Product and Order Management:** Sellers manage registered products and handle customer orders efficiently.
- **Payment Processing:** Sellers update order statuses for payment release, ensuring a smooth transaction process.

**Key Objectives Achieved:**

1. **Efficient Categorization:** Our automated product categorization simplifies the listing process for sellers.
2. **Personalized Recommendations:** The recommendation system enhances the buyer's journey, suggesting relevant products.
3. **Vendor Management:** Sellers can seamlessly manage products, orders, and payments on our platform.

-----

## Installation using docker

<details>

### 1. Clone the Repository

```bash
git clone https://github.com/TwoPointerr/ProductRecommendation.git
cd ./ProductRecommendation
```

### 2. Configure Databse
configure database as per project_clean/settings.py or adjust project_clean/settings.py as per your database configuration
https://github.com/TwoPointerr/ProductRecommendation/blob/7f048f3f546e83706b7424c02e95fd5742c1f7ad/eshop/settings.py#L98-L113

### 3. Spin up Containers
```bash
docker-compose up
```
- Make sure docker is running

</details>


## Installation on Local

<details>

### 1. Clone the Repository

```bash
git clone https://github.com/TwoPointerr/ProductRecommendation.git
cd ./ProductRecommendation
```

### 2. Create a Virtual Environment (Optional but Recommended)

```bash
# Install virtualenv if not already installed
pip install virtualenv

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On Unix or MacOS
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

This command installs all the required Python packages specified in the `requirements.txt` file.

### 4. Configure Databse
configure database as per project_clean/settings.py or adjust project_clean/settings.py as per your database configuration
https://github.com/TwoPointerr/ProductRecommendation/blob/7f048f3f546e83706b7424c02e95fd5742c1f7ad/eshop/settings.py#L98-L113


### 5. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

This command applies any pending database migrations.

### 6. Create a Superuser (Optional)

```bash
python manage.py createsuperuser
```

This command creates a superuser account for administrative access to the Django admin interface.

### 7. Run the Development Server

```bash
python manage.py runserver
```
</details>

-----

**Conclusion:**

This e-Shop platform aims to provide a user-friendly and efficient environment for buyers and sellers alike. With streamlined processes, personalized recommendations, and effective vendor management, we strive to offer a comprehensive and satisfying online shopping experience.


## Acknowledgements

 - [Cartzilla Theme](https://cartzilla.createx.studio/docs/dev-setup.html)
 
