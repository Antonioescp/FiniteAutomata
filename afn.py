from fa import NonDeterministicFiniteAutomata
from sys import argv

def main():
    if len(argv) == 1:
        print("Enter at least one string to test.")
        return 0

    automata = NonDeterministicFiniteAutomata()

    automata.states = 3
    automata.transitions = [
        (0, 'a', {0, 1}),
        (0, 'b', {0}),
        (1, 'b', {2})
    ]
    automata.start_state = 0
    automata.acceptance_states = {2}

    for e in argv[1:]:
        print(e, "pertenece." if automata.test_string(e) else "no pertenece.")

    return 0

if __name__ == "__main__":
    main()