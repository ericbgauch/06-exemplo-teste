class PhoneBook():
    def __init__(self):
        self.entries = []

    def add_entry(self, name, phone):
        entry = {
            'name': name,
            'phone': phone
        }
        
        self.entries.append(entry)
