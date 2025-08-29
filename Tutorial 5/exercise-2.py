# movie_ticket_sales.py

# Movie prices
movies = {
    "Dune": 12.5,
    "Barbie": 11.0,
    "Oppenheimer": 13.0,
    "Spirited Away": 10.0
}

purchases = []  # list of (title, qty, price_each)

# --- Functions ---
def show_movies():
    print("\nAvailable movies and prices:")
    for title, price in movies.items():
        print(f"- {title}: ${price:.2f}")

def get_movie_choice():
    show_movies()
    return input("Which movie would you like to watch? (or 'done' to finish): ").strip()

def get_quantity(title):
    while True:
        try:
            qty = int(input(f"How many tickets for {title}? "))
            if qty > 0:
                return qty
            print("Quantity must be positive.")
        except ValueError:
            print("Invalid number. Try again.")

def apply_group_discount(qty, price_each):
    """Apply 10% discount for 4 or more tickets."""
    return price_each * 0.9 if qty >= 4 else price_each

def apply_member_discount(total, is_member):
    """Apply 5% discount if member."""
    return total * 0.95 if is_member else total

# --- Part A: Input loop ---
while True:
    title = get_movie_choice()
    if title.lower() == 'done':
        break
    if title not in movies:
        print("Movie not available. Please choose from the list.")
        continue
    
    qty = get_quantity(title)
    price_each = apply_group_discount(qty, movies[title])
    
    purchases.append((title, qty, price_each))
    print(f"Added {qty} x {title} @ ${price_each:.2f} each.")

if not purchases:
    print("No tickets purchased.")
    exit()

# --- Part B: Receipt ---
print("\n--- Receipt ---")
grand_total = 0
print(f"{'Movie':20} {'Qty':>3} {'Price':>7} {'Total':>8}")
print("-" * 40)
for title, qty, price_each in purchases:
    line_total = qty * price_each
    grand_total += line_total
    print(f"{title:20} {qty:>3} ${price_each:>6.2f} ${line_total:>7.2f}")

# Member discount
member = input("\nDo you have a member code? (yes/no): ").strip().lower() == 'yes'
grand_total = apply_member_discount(grand_total, member)
print(f"\nGrand Total: ${grand_total:.2f}")

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
print("\nMovies sorted by revenue:")
for title, revenue in sorted_by_rev:
    print(f"{title}: ${revenue:.2f}")

# Average tickets per purchase
total_tickets = sum(qty for _, qty, _ in purchases)
avg_tickets = total_tickets / len(purchases)
print(f"\nAverage tickets per purchase: {avg_tickets:.2f}")
