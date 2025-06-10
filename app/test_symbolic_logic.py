from symbolic_logic import SymbolicLogicReasoner

def test_height_relationships():
    reasoner = SymbolicLogicReasoner()
    # Add facts
    reasoner.add_fact("taller(alice, bob)")
    reasoner.add_fact("taller(bob, charlie)")
    # Add transitive rule
    reasoner.add_rule("taller(X, Y) :- taller(X, Z), taller(Z, Y)")

    # Queries
    print("Is Alice taller than Bob?", bool(reasoner.query("taller(alice, bob)")), "(Expected: True)")
    print("Is Bob taller than Charlie?", bool(reasoner.query("taller(bob, charlie)")), "(Expected: True)")
    print("Is Alice taller than Charlie?", bool(reasoner.query("taller(alice, charlie)")), "(Expected: True)")
    print("Is Charlie taller than Alice?", bool(reasoner.query("taller(charlie, alice)")), "(Expected: False)")

if __name__ == "__main__":
    test_height_relationships() 