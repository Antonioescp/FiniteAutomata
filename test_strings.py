from fa import DeterministicFiniteAutomata
from sys import argv

def main():
    if len(argv) == 1:
        print("Enter at least one string to test.")
        return 0

    automata = DeterministicFiniteAutomata()

    automata.states = 2
    automata.transitions = [
        (0, '0', 1),
        (1, '0', 0),
        (1, '1', 1)
    ]
    automata.start_state = 0
    automata.acceptance_states = {1}

    for e in argv[1:]:
        print(e, "pertenece." if automata.test_string(e) else "no pertenece.")

    return 0

if __name__ == "__main__":
    main()