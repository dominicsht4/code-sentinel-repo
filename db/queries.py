
# Intentional N+1 query pattern for testing
from models import User, Order

def get_user_orders(user_ids):
    users = []
    for user_id in user_ids:
        # PERFORMANCE ISSUE: N+1 query — one DB call per user
        user = User.objects.get(id=user_id)
        orders = Order.objects.filter(user_id=user_id)
        users.append({"user": user, "orders": list(orders)})
    return users
