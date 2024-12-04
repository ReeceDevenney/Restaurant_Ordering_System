INSERT INTO users (user_id, role, name, username, password) 
VALUES
(101, 'customer', 'Guest', 'Guest', 'Guest'),
(102, 'owner', 'Jane Smith', 'janesmith', 'ownerpass456'),
(103, 'customer', 'Emily Johnson', 'emilyj', 'custpass789'),
(104, 'staff', 'Michael Brown', 'mikeb', 'staffpass321'),
(105, 'staff', 'Sarah Lee', 'sarahlee', 'staffpass654');

INSERT INTO menu_items (name, description, price) 
VALUES 
('Burger', 'Juicy grilled burger with cheese', 8.99),
('Pizza', 'Cheesy pepperoni pizza', 12.49),
('Salad', 'Fresh garden salad, Gluten Free, Vegan', 6.75),
('Pasta', 'Creamy Alfredo pasta', 10.50),
('Soup', 'Hot and spicy tomato soup, Gluten Free, Vegan', 5.25);

INSERT INTO resource_management (id, item, amount) 
VALUES
(1, 'Tomatoes', 100),
(2, 'Cheese', 50),
(3, 'Lettuce', 200),
(4, 'Flour', 150),
(5, 'Chicken', 80);

INSERT INTO recipes (menu_item, ingredient, amount) 
VALUES
(1, 1, 5),   -- Burger using 5 Tomatoes
(2, 2, 10),  -- Pizza using 10 Cheese
(3, 3, 15),  -- Salad using 15 Lettuce
(4, 4, 20),  -- Pasta using 20 Flour
(5, 5, 8);   -- Soup using 8 Chicken

INSERT INTO promotions (code, discount, isActive, expirationDate) 
VALUES
('SUMMER20', 0.20, TRUE, '2024-08-31 23:59:59'),
('WINTER15', 0.15, TRUE, '2024-12-31 23:59:59'),
('SPRING10', 0.10, TRUE, '2025-03-31 23:59:59'),
('FALL25', 0.25, FALSE, '2024-10-31 23:59:59'),
('BLACKFRIDAY30', 0.30, TRUE, '2024-11-29 23:59:59');

INSERT INTO Payment_information (cardNumber, cardExpirationDate, transactionStatus, paymentType) 
VALUES
('1234-5678-9012-3456', '2025-12-31 23:59:59', 'Completed', 'Credit'),
('9876-5432-1098-7654', '2026-03-31 23:59:59', 'Pending', 'Debit'),
('1111-2222-3333-4444', '2027-05-15 23:59:59', 'Failed', 'Credit'),
('5555-6666-7777-8888', '2025-06-30 23:59:59', 'Completed', 'Debit'),
('9999-0000-1111-2222', '2028-01-01 23:59:59', 'Completed', 'Credit');

INSERT INTO orders (order_date, description, order_status, menu_item_id, users_id) 
VALUES
('2024-12-02 12:00:00', 'pickup', 'Received', 1, 101),
('2024-12-03 12:05:00', 'dine-in', 'In Progress', 2, 102),
('2024-12-04 12:10:00', 'delivery', 'Delivered', 3, 103),
('2024-12-05 12:15:00', 'dine-in', 'In Progress', 4, 104),
('2024-12-05 12:20:00', 'pickup', 'Received', 5, 105);

