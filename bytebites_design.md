# ByteBites Final UML Design

## Classes

### Customer
- name: string
- purchase_history: list

### Order
- items: list[MenuItem]
- total_cost: float

### MenuItem
- name: string
- price: float
- category: string
- popularity_rating: int

### Menu
- items: list[MenuItem]

## Relationships

Customer -> Order
(Customer places Orders)

Order -> MenuItem
(Order contains selected MenuItems and computes total cost)

Menu -> MenuItem
(Menu contains all MenuItems and supports filtering by category)

## Design Notes

- Only four classes were used.
- Attributes come directly from the feature request.
- No authentication, payment, database, or inventory classes were added.
- Relationships reflect the required system behavior.

