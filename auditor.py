#Smart Inventory Auditor
# 1. Initialize inventory and tracking counters to zero at start
total_inventory = 0
units_processed = 0
failed_entries = 0

print("=== Inventory Auditor ===")
print("Enter stock quantity for each delivery. Type 'quit' to finish.\n")

# 2. Continuous loop until user types 'quit'
# (a while loop is the right fit here since we don't know in advance
#  how many entries the user will make)
while True:
    entry = input("Enter stock quantity: ").strip()

    # Exit condition
    if entry.lower() == "quit":
        break

    # 4. Handle invalid (non-numeric) input using .isdigit()
    # .isdigit() only returns True for strings made up of digits (0-9),
    # so it naturally rejects text AND negative numbers (since '-' isn't a digit)
    if not entry.isdigit():
        print(f"Error: '{entry}' is not a valid whole number. Entry rejected.\n")
        failed_entries += 1
        continue

    # 3. Convert to integer now that we know it's valid digits
    quantity = int(entry)

    # 5. Enforce business rules: reject negatives
    # (isdigit() already filters out negative signs, but this makes the
    #  business rule explicit and future-proof, e.g. if input parsing changes)
    if quantity < 0:
        print(f"Error: Negative values are not allowed. Entry rejected.\n")
        failed_entries += 1
        continue
    else:
        # 6. Valid entry -> update running totals
        total_inventory += quantity
        units_processed += quantity
        print(f"Accepted. Current total inventory: {total_inventory}\n")

    # 7. Overstock alert: stop immediately if capacity exceeded
    if total_inventory > 500:
        print("OVERSTOCK ALERT: Inventory has exceeded 500 units! Halting entry.\n")
        break

# 8. Final report
print("=== End of Session Report ===")
print(f"Total Units Processed: {units_processed}")
print(f"Number of Failed/Rejected Entries: {failed_entries}")