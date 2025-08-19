Modular Shopping Cart System with Admin Dashboard & SQLite Integration

A backend-driven shopping cart system architected with Python and SQLite, designed to reflect software development lifecycle (SDLC) best practices. This project demonstrates modular design, transactional integrity, and real-time data visibility—ideal for showcasing consultative impact and scalable architecture in SDE and software consulting roles.

Project Overview
This system was developed through a structured SDLC approach:
- Requirements Analysis: Identified core user workflows—cart operations, user management, and order tracking.
- System Design: Architected encapsulated modules with clear separation of concerns and reusable components.
- Implementation: Developed Python-based modules with SQLite integration for persistent storage and transactional workflows.
- Testing & Validation: Verified CRUD operations, checkout integrity, and dashboard accuracy across edge cases.
- Deployment & Documentation: Packaged for local execution with schema initialization and CLI-based interaction.
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


Project Structure
├── cart/
│   ├── cart.py
│   └── utils.py
├── users/
│   ├── user_manager.py
│   └── auth.py
├── products/
│   ├── catalog.py
│   └── inventory.py
├── dashboard/
│   └── admin_view.py
├── checkout/
│   └── transaction.py
├── db/
│   └── schema.sql
└── main.py


Getting Started
- Clone the repository:
git clone https://github.com/your-username/modular-cart-system.git


cd modular-cart-system
- Initialize the SQLite database:
sqlite3 db/cart.db < db/schema.sql
- Run the main application:
python main.py
