import itertools

# Banner
def print_banner():
    banner = """
    **************************************
    * Password List Generator by Saurabh *
    **************************************
    """
    print(banner)

# Get user input
def get_user_input():
    print("Enter the following details:")
    victim_name = input("Victim's Name: ").strip()
    victim_surname = input("Victim's Surname: ").strip()
    victim_nickname = input("Victim's Nickname: ").strip()
    victim_dob = input("Victim's DOB (DDMMYYYY): ").strip()
    partner_name = input("Partner's Name (optional): ").strip()
    partner_surname = input("Partner's Surname (optional): ").strip()
    partner_nickname = input("Partner's Nickname (optional): ").strip()
    partner_dob = input("Partner's DOB (DDMMYYYY, optional): ").strip()

    return (
        victim_name, victim_surname, victim_nickname, victim_dob,
        partner_name, partner_surname, partner_nickname, partner_dob
    )

# Generate password combinations
def generate_passwords(data):
    victim_name, victim_surname, victim_nickname, victim_dob, \
    partner_name, partner_surname, partner_nickname, partner_dob = data

    # Extract initials (only if the name is not empty)
    victim_initial = victim_name[0].lower() if victim_name else ""
    partner_initial = partner_name[0].lower() if partner_name else ""

    # Define special characters
    special_chars = ["@", "#", "$", "!", "*", "&"]

    # Define date formats
    date_formats = [
        victim_dob,  # DDMMYYYY
        victim_dob[:4],  # DDMM
        victim_dob[4:],  # YYYY
        victim_dob[::-1],  # YYYYMMDD
    ]

    # Add partner's DOB formats if provided
    if partner_dob:
        date_formats.extend([
            partner_dob,  # DDMMYYYY
            partner_dob[:4],  # DDMM
            partner_dob[4:],  # YYYY
            partner_dob[::-1],  # YYYYMMDD
        ])

    # Generate combinations
    passwords = set()

    # Combine names, nicknames, and dates with special characters
    for name in [victim_name, victim_surname, victim_nickname, partner_name, partner_surname, partner_nickname]:
        if not name:  # Skip empty names
            continue
        for date in date_formats:
            for char in special_chars:
                # Combination 1: name + special char + date
                password = f"{name}{char}{date}"
                if 8 <= len(password) <= 16:
                    passwords.add(password)
                # Combination 2: initial + special char + date
                if name:  # Ensure name is not empty
                    password = f"{name[0]}{char}{date}"
                    if 8 <= len(password) <= 16:
                        passwords.add(password)

    # Add leet format for "a" = "@"
    leet_passwords = set()
    for password in passwords:
        leet_password = password.replace("a", "@").replace("A", "@")
        leet_passwords.add(leet_password)

    # Combine all passwords
    all_passwords = passwords.union(leet_passwords)

    # Add capital and small first letter variations
    final_passwords = set()
    for password in all_passwords:
        final_passwords.add(password.capitalize())
        final_passwords.add(password.lower())

    # Filter passwords by length
    final_passwords = [p for p in final_passwords if 8 <= len(p) <= 16]

    return final_passwords

# Main function
def main():
    print_banner()
    user_data = get_user_input()
    passwords = generate_passwords(user_data)

    # File naming
    victim_name, victim_surname = user_data[0], user_data[1]
    file_name = f"{victim_name}_{victim_surname}.txt" if victim_name and victim_surname else "password_list.txt"
    file_name = file_name.replace(" ", "_")  # Replace spaces with underscores in file name

    # Save passwords to file
    with open(file_name, "w") as file:
        for password in passwords:
            file.write(f"{password}\n")

    # Print confirmation and summary
    print(f"\nGenerated Passwords saved to '{file_name}'.")
    print(f"Total Passwords Generated: {len(passwords)}")

if __name__ == "__main__":
    main()
