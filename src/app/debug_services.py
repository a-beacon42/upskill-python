from debug_models import Contact, InvalidContactError


class ContactBook:
    def __init__(self):
        self.contacts: list[Contact] = []

    def add(self, contact: Contact) -> None:
        for existing in self.contacts:
            if existing.email == contact.email:
                raise InvalidContactError(f"Duplicate email: {contact.email}")
        self.contacts.append(contact)

    def find_by_email(self, email: str) -> Contact | None:
        for contact in self.contacts:
            if contact.email == email:
                return contact
        return None

    def remove(self, email: str) -> Contact | None:
        for i, contact in enumerate(self.contacts):
            if contact.email == email:
                del self.contacts[i]
                return contact
        return None

    def all_with_tag(self, tag: str) -> list[Contact]:
        return [c for c in self.contacts if tag in c.tags]
