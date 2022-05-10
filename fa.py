from argparse import ArgumentError

class DeterministicFiniteAutomata:

    def __init__(self):
        self._states: int = 0
        self._transitions: dict[int, dict[str, int]] = dict()
        self._alphabet: set[str] = set()
        self.start_state: int = None
        self.acceptance_states: set[int] = None

    @property
    def alphabet(self) -> set[str]:
        return self._alphabet

    @alphabet.setter
    def alphabet(self, elements: list[str]) -> None:
        raise AttributeError("alphabet is a read only property for DeterministicFiniteAutomata class.")

    @property
    def states(self) -> int:
        return self._states

    @states.setter
    def states(self, quantity: int) -> None:
        if quantity <= 0:
            raise ArgumentError("The states quantity must be a positive number.")

        self._states = quantity

        self._alphabet.clear()
        self._transitions = dict()
        for i in range(0, self._states):
            self._transitions[i] = dict()

    @property
    def transitions(self) -> dict[int, dict[str, int]]:
        return self._transitions

    @transitions.setter
    def transitions(self, transitions: list[tuple[int, str, int]]) -> None:
        for from_state in self._transitions:
            self._transitions[from_state].clear()

        self._alphabet.clear()
        for (from_state, input, to_state) in transitions:
            self._transitions[from_state][input] = to_state
            self._alphabet.add(input)

    def test_string(self, string: str) -> bool:
        current_state = self.start_state

        for character in string:
            if character in self._transitions[current_state]:
                current_state = self._transitions[current_state][character]
            else:
                return False

        return current_state in self.acceptance_states


class NonDeterministicFiniteAutomata(DeterministicFiniteAutomata):

    def __init__(self):
        super().__init__()
        self._transitions: dict[int, dict[str, set[int]]] = dict()

    @property
    def transitions(self) -> dict[int, dict[str, int]]:
        return self._transitions

    @transitions.setter
    def transitions(self, transitions: list[tuple[int, str, set[int]]]) -> None:
        for from_state in self._transitions:
            self._transitions[from_state].clear()

        self._alphabet.clear()
        for (from_state, input, to_states) in transitions:
            self._transitions[from_state][input] = set()
            for state in to_states:
                self._transitions[from_state][input].add(state)
            self.alphabet.add(input)

    def test_string(self, string: str) -> bool:
        current_states: set[int] = set()
        current_states.add(self.start_state)
        target_states: set[int] = set()

        for character in string:
            for from_state in current_states:
                if character in self._transitions[from_state]:
                    for to_state in self._transitions[from_state][character]:
                        target_states.add(to_state)

            if len(target_states) > 0:
                current_states.clear()
                for state in target_states:
                    current_states.add(state)
                target_states.clear()
            else:
                break

        for state in current_states:
            if state in self.acceptance_states:
                return True

        return False