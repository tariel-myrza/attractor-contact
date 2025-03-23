class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def to_list(self):
        return [self.name, self.phone]

    def to_dict(self):
        return {"name": self.name, "phone": self.phone}
