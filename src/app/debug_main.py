from debug_models import Contact, InvalidContactError
from debug_services import ContactBook


def main():
    book = ContactBook()

    # Add contacts
    book.add(
        Contact(name="Alice", email="alice@test.com", phone="5551234567", tags=["work"])
    )
    book.add(
        Contact(name="Bob", email="bob@test.com", phone="+15551234567", tags=["family"])
    )
    book.add(Contact(name="Charlie", email="charlie@test.com", tags=["work", "friend"]))

    # Test 1: find by email
    alice = book.find_by_email("alice@test.com")
    print(f"Found: {alice}")
    # Expected: Alice's contact — but might get None

    # Test 2: tags should be independent
    alice_contact = book.contacts[0]
    alice_contact.tags.append("vip")
    charlie_contact = book.contacts[2]
    print(f"Alice tags: {alice_contact.tags}")
    print(f"Charlie tags: {charlie_contact.tags}")
    # Expected: Alice has ["work", "vip"], Charlie has ["work", "friend"]
    # But something is wrong...

    # Test 3: remove and check
    book.remove("bob@test.com")
    print(f"After remove: {[c.name for c in book.contacts]}")
    # Expected: ["Alice", "Charlie"]

    # Test 4: invalid phone
    for bad in [
        {"name": "Dave", "email": "dave@test.com", "phone": "+15559876543"},
        {"name": "", "email": "empty@test.com"},
    ]:
        try:
            book.add(Contact(**bad))
            print(f"BUG: should have been rejected")
        except InvalidContactError as e:
            print(f"Caught: {e}")


if __name__ == "__main__":
    main()
