import random
from calendar import weekday
from datetime import datetime, timedelta

# def generate_tickets(t):
#     tickets = []
#     for _ in range(t):
#         date = datetime.now() - timedelta(days=random.randint(0, 60))
#         price = random.randint(50,200)
#         tickets.append(f"INSERT INTO Tickets (date, price) VALUES ('{date.date()}',{price})")
#     return tickets
# with open()

def ticket_price(date):
    busy_days = [4, 5, 6]
    normal_days = [1, 2, 3]
    slow_days = [0]
    weekday = date.weekday()

    if weekday in busy_days:
        return random.randint(120, 200)
    elif weekday in normal_days:
        return random.randint(80, 119)
    elif weekday in slow_days:
        return random.randint(50,79)

def generate_tickets(t):
    tickets = []
    for _ in range(t):
        date = datetime.now() - timedelta(days=random.randint(0, 60))
        price = ticket_price(date)
        tickets.append(f"INSERT INTO Tickets (date, price) VALUES ('{date.date()}',{price})")
    return tickets
with open("insert_tickets.sql","w") as file:
    file.write("\n".join(generate_tickets(11)))
