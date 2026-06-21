# ByteBites Spec

## Client Feature Request

We need to build the backend logic for the ByteBites app.

The system needs to manage customers, tracking their names and their past purchase history so the system can verify they are real users.

Customers need to browse food items, so we must track the name, price, category, and popularity rating for every item we sell.

We need a menu, which is a digital list that holds all items and lets us filter by category such as Drinks or Desserts.

When a user picks items, we need to group them into a single transaction. This transaction should store the selected items and compute the total cost.

## Candidate Classes

1. Customer
2. MenuItem
3. Menu
4. Order