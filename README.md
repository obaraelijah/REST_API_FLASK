## ROUTES TO IMPLEMENT
| METHOD |ROUTE | FUNCTIONALITY |ACCESS|
| --------| ---------- | ------- | ---------|
| *POST* | ```/auth/signup/ ```| _Register new user_| All users_|
| *POST* | ```/auth/login/ ```| Login new user_| All users_|
| *POST* | ```/orders/order/ ```| _place an order| All users_|
| *PUT* | ```/orders/order/update/{order_id}/ ```| _update an order| All users_|
| *PUT* | ```/orders/order/status/{order_id}/ ```| _update order status_| _Superuser_|
| *DELETE* | ```/orders/order/delete/{order_id}/ ```| Delete/Remove an _order| All users_|
| *GET* | ```/orders/user/orders/ ```| _Get user's  orders_| _ALL users_|
| *GET* | ```/orders/orders/ ```| _List all orders made_| _Superuser_|
| *GET* | ```/orders/orders/{order_id} ```| _Retrieve an order_| _Superuser_|
| *GET* | ```/orders/user/order/{order_id} ```| _Get user's speific order_|
| *GET* | ```/docs/ ```| _view API documentation_| _All users_|