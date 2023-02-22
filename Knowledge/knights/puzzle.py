from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

#A is a Knight or Knave but not both
A_rule = And(Or(AKnight, AKnave), Not(And(AKnight, AKnave)))

#B is a Knight or Knave but not both
B_rule = And(Or(BKnight, BKnave), Not(And(BKnight, BKnave)))

#C is a Knight or Knave but not both
C_rule = And(Or(CKnight, CKnave), Not(And(CKnight, CKnave)))


# Puzzle 0
# A says "I am both a knight and a knave."
A_says = And(AKnave, AKnight)
knowledge0 = And(
    # A is a knight or a knave but not both:
    A_rule,

    # True for Knights:
    Implication(AKnight, A_says),
    # False for Knaves:
    Implication(AKnave, Not(A_says))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
A_says1 = And(AKnave, BKnave)
knowledge1 = And(
    # A and B is a Knave or a Knight but not both
    A_rule,
    B_rule,

    #If A is a Knight, then what he says its true
    Implication(AKnight, A_says1),

    #If A is a Knave, then what he says is not true
    Implication(AKnave, Not(A_says1))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
A_says2 = Or(And(AKnight, BKnight), And(AKnave, BKnave))
B_says2 = Or(And(AKnight, BKnave), And(AKnave, BKnight))
knowledge2 = And(
    A_rule,
    B_rule,

    Implication(AKnave, Not(A_says2)),
    Implication(BKnave, Not(B_says2)),
    Implication(BKnight, B_says2),
    Implication(AKnight, B_says2)
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
A1_says3 = And(Implication(AKnight, AKnight), Implication(AKnave, Not(AKnight)))
A2_says3 = And(Implication(AKnight, AKnave), Implication(AKnave, Not(AKnave)))
C_says3 = AKnight

knowledge3 = And(

    A_rule,
    B_rule,
    C_rule,
    
    Or(A1_says3, A2_says3),
    Implication(CKnave, Not(C_says3)),
    Implication(CKnight, C_says3),
    Implication(BKnight, And(A2_says3, CKnave)),
    Implication(BKnave, And(Not(A2_says3), Not(CKnave))),

)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
