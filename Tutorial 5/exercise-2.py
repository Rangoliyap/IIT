# movie_ticket_sales.py

# Movie prices
movies = {
    "Dune": 12.5,
    "Barbie": 11.0,
    "Oppenheimer": 13.0,
    "Spirited Away": 10.0
}

purchases = []  # list of (title, qty, price_each)

# --- Part A: Input loop ---
while True:
    title = input("Enter movie title (or 'done' to finish): ")
    if title.lower() == 'done':
        break
    if title not in movies:
        print("Movie not available. Choose from:", ", ".join(movies.keys()))
        continue
    
    # Quantity input with validation
    try:
        qty = int(input(f"How many tickets for {title}? "))
        if qty <= 0:
            print("Quantity must be positive.")
            continue
    except ValueError:
        print("Invalid number. Try again.")
        continue

    price_each = movies[title]
    
    # Part D: Group discount (10% off for 4+ tickets)
    if qty >= 4:
        price_each *= 0.9  # 10% discount per ticket
    
    purchases.append((title, qty, price_each))
    print(f"Added {qty} x {title} @ ${price_each:.2f} each.")

# --- Part B: Receipt ---
print("\n--- Receipt ---")
grand_total = 0
for title, qty, price_each in purchases:
    line_total = qty * price_each
    grand_total += line_total
    print(f"{qty} x {title} @ ${price_each:.2f} = ${line_total:.2f}")

# Part D: Member discount
member_code = input("Do you have a member code? (yes/no): ").strip().lower()
if member_code == 'yes':
    grand_total *= 0.95  # extra 5% off

print(f"Grand Total: ${grand_total:.2f}")

# --- Part C: Sales summary ---
tickets_by_movie = {}
revenue_by_movie = {}

for title, qty, price_each in purchases:
    tickets_by_movie[title] = tickets_by_movie.get(title, 0) + qty
    revenue_by_movie[title] = revenue_by_movie.get(title, 0) + (qty * price_each)

print("\n--- Sales Summary ---")
print(f"{'Movie':20} {'Tickets':7} {'Revenue':10}")
for title in movies.keys():
    tickets = tickets_by_movie.get(title, 0)
    revenue = revenue_by_movie.get(title, 0)
    print(f"{title:20} {tickets:<7} ${revenue:<10.2f}")

# --- Part E: Analytics ---
# Top-selling movie by tickets
top_title = None
top_qty = -1
for title, qty in tickets_by_movie.items():
    if qty > top_qty:
        top_title, top_qty = title, qty
print(f"\nTop-selling movie by tickets: {top_title} ({top_qty} tickets)")

# Sort titles by revenue
sorted_by_rev = sorted(revenue_by_movie.items(), key=lambda kv: kv[1], reverse=True)
print("Movies sorted by revenue:")
for title, revenue in sorted_by_rev:
    print(f"{title}: ${revenue:.2f}")

# Average tickets per purchase
total_tickets = sum(qty for _, qty, _ in purchases)
avg_tickets = total_tickets / len(purchases) if purchases else 0
print(f"Average tickets per purchase: {avg_tickets:.2f}")
