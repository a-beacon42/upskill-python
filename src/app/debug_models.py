from dataclasses import dataclass, field


class InvalidContactError(ValueError):
    pass


@dataclass
class Contact:
    name: str
    email: str
    phone: str | None = None
    tags: list[str] = field(default_factory=list)

    def __post_init__(self):
        if not self.name:
            raise InvalidContactError(f"Contact name cannot be empty")
        if "@" not in self.email:
            raise InvalidContactError(f"Invalid email: {self.email}")
        if self.phone:
            processed = _process_phone(self.phone)
            if len(_process_phone(self.phone)) != 10:
                raise InvalidContactError(f"Phone must be 10 digits, got: {self.phone}")
            self.phone = processed


def _process_phone(phone: str):
    if phone.startswith("+"):
        return phone[-10:]
    return "".join([char for char in phone if char.isdigit()])
