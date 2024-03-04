Hours = int(input("Hours: "))
Status = input("Are you a member? ").lower()

if Status == 'yes':
    Tax = Hours * 2 * 1.1
else:
    Tax = Hours * 5 * 1.2

print(f"The user is{' not' if Status != 'yes' else ''} a member "
      f"stayed {Hours} hours for {2 if Status == 'yes' else 5}$/hour "
      f"plus the {10 if Status == 'yes' else 20}% the total amount is {Tax}$")