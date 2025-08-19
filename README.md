Title: Modular Shopping Cart Ecommerce application logic with transactional checkout and secure storage of customer purchase details.

A backend-driven shopping cart system architected with core Python and secure SQLite database storage for the purpose of redesigning the cart system with dynamic updates in Django-powered robust and scalable backend design and development.
This project demonstrates modular design, transactional integrity, and real-time data visibility—ideal for showcasing consultative impact and scalable architecture in SDE and software consulting roles.

Project Overview

This system was developed using a structured Software Development Life Cycle (SDLC) approach:

Requirements Analysis – Identified core workflows such as shopping cart operations, user management, and order tracking.

System Design – Architected encapsulated modules with clear separation of concerns and reusable components.

Implementation – Developed Django-based modules with SQLite integration for persistent storage and transactional workflows.

Testing & Validation – Verified CRUD operations, checkout integrity, and dashboard accuracy across multiple edge cases.

Features
1. Encapsulated & Reusable Shopping Cart

Designed a Cart class encapsulating cart operations (add, remove, update).

Maintains session-based state, ensuring prices and quantities remain consistent across checkout.

2. Modular Database Design with Django ORM

Implemented Django ORM models (e.g., ItemsPurchased) to represent cart and order entities.

Ensures a layered architecture where schema details remain abstracted behind class definitions.

Promotes clean object-relational mapping and database integrity.
Key Features
| SDLC Phase | Feature Description | 
| Design | Encapsulated shopping cart using Python dictionaries for dynamic data handling | 
| Architecture | Modular system for user management, product catalog, and purchase history | 
| Visualization | Admin dashboard with real-time order tracking and advanced filtering | 
| Transaction | Checkout workflow with SQLite-backed integrity and rollback safety | 
| Optimization | Analytical problem-solving to streamline CRUD and retrieval workflows | 


Tech Stack
| Layer | Technology | 
| Language | Python 3.x | 
| Database | SQLite | 
| Architecture | Modular, loosely coupled | 
| Interface | CLI-based dashboard | 

