# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description

        self.n_to = None
        self.s_to = None
        self.w_to = None
        self.e_to = None

        self.items = []

    def build_directions(self):
        final = ""
        if self.n_to:
            final = f"n: {self.n_to.name}"
        if self.s_to:
            final += f", s: {self.s_to.name}" if len(
                final) != 0 else f"s: {self.s_to.name}"
            # if len(final) != 0:
            #     final += f", s: {self.s_to.name}"
            # else:
            #     final = f"s: {self.s_to.name}"
        if self.w_to:
            final += f", w: {self.w_to.name}" if len(
                final) != 0 else f"w: {self.w_to.name}"
        if self.e_to:
            final += f", e: {self.e_to.name}" if len(
                final) != 0 else f"e: {self.e_to.name}"
        return final

    def __str__(self):
        return f"""Name: {self.name}, 
Description: {self.description}, 
Directions: {self.build_directions()}"""

    def __repr__(self):
        return f"Item({repr(self.name)})"
