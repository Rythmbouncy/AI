class FOL:

    def __init__(self):
        self.facts = set()
        self.rules = []

    def add_fact(self, fact):
        self.facts.add(fact)

    def add_rule(self, premise, conclusion):
        self.rules.append((premise, conclusion))

    def backward_chaining(self, goal):
        if goal in self.facts:
            return True
        for rule in self.rules:
            premise, conclusion = rule
            if conclusion == goal and all(self.backward_chaining(p) for p in premise):
                return True
        return False

# Create the knowledge base
kb = FOL()

# Add facts
kb.add_fact("Robert is an American citizen")
kb.add_fact("Selling weapons to hostile nations is a crime")
kb.add_fact("Country A is an enemy of America")

# Add rules
kb.add_rule(["Robert is an American citizen"], "Selling weapons to hostile nations is a crime")
kb.add_rule(["Selling weapons to hostile nations is a crime", "Country A is an enemy of America"], "Robert is a criminal")
kb.add_rule(["Robert is a criminal"], "Robert is guilty")

# Backward chaining to prove "Robert is a criminal"
proof = kb.backward_chaining("Robert is a criminal")
print("Can we prove that Robert is a criminal?", proof)