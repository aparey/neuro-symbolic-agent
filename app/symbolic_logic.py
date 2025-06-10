# pip install pyswip
from pyswip import Prolog

class SymbolicLogicReasoner:
    def __init__(self):
        """
        Initialize the Prolog engine.
        """
        self.prolog = Prolog()

    def add_fact(self, fact):
        """
        Add a fact to the Prolog knowledge base.
        Example: fact = "taller(bob, john)"
        """
        self.prolog.assertz(fact)

    def add_rule(self, rule):
        """
        Add a rule to the Prolog knowledge base.
        Example: rule = "taller(X, Y) :- taller(X, Z), taller(Z, Y)"
        """
        self.prolog.assertz(rule)

    def query(self, query_str):
        """
        Query the Prolog knowledge base.
        Example: query_str = "taller(bob, john)"
        Returns a list of solutions (dictionaries).
        """
        return list(self.prolog.query(query_str))

# Sample usage (for testing or demonstration)
if __name__ == "__main__":
    reasoner = SymbolicLogicReasoner()
    # Add facts
    reasoner.add_fact("taller(bob, john)")
    reasoner.add_fact("taller(stuart, john)")
    reasoner.add_fact("taller(bob, stuart)")
    # Add transitive rule
    reasoner.add_rule("taller(X, Y) :- taller(X, Z), taller(Z, Y)")
    # Query
    print("Is bob taller than john?", bool(reasoner.query("taller(bob, john)")))
    print("Is stuart taller than bob?", bool(reasoner.query("taller(stuart, bob)")))
    print("Is bob taller than john (transitive)?", bool(reasoner.query("taller(bob, john)")))
