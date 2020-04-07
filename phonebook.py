class PhoneBook():
    def __init__(self):
        self.entries = []

    def add_entry(self, name, phone):
        entry = {
            'name': name,
            'phone': phone
        }
        
        self.entries.append(entry)

    def find_by_name(self, name):
        for entry in self.entries:
            if entry['name'] == name:
                return entry

        return None
