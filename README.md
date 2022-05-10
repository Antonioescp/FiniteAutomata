# FiniteAutomata
Deterministic and Non-Deterministic Finite Automata implementation

# How to use
We have two classes, **DeterministicFiniteAutomata** and **NonDeterministicFiniteAutomata** which share the same interface, they have:

- states
- transitions
- alphabet
- start states
- acceptance/final states

# Example
Here we will create a DFA for **(01\*0)\*01\***:

## DFA
```python
from fa import DeterministicFiniteAutomata

# create the automata
automata = DeterministicFiniteAutomata()

automata.states = 2

#  from_state       input        to_state
#      └─────────┐    |     ┌───────┘
# list of tuple[int, str, int]
automata.transitions = [
  (0, '0', 1),
  (1, '0', 0),
  (1, '1', 1)
]

automata.start_state = 0
automata.acceptance_states = {1}

input = "01"
result = automata.test_string(input)

print("Alphabet:")
for character in automata.alphabet:
  print(character)
 
print("string", input, "is", result)
```

Here we will create a NFA for **(a | b)\*ab**:

```python
from fa import NonDeterministicFiniteAutomata

# create the automata
automata = NonDeterministicFiniteAutomata()

automata.states = 3

#  from_state       input      to_states set
#      └─────────┐    |     ┌───────┘
# list of tuple[int, str, set[int]]
# the difference here is the set of target states to transition to
automata.transitions = [
  (0, 'a', {0, 1}),
  (0, 'b', {0}),
  (1, 'b', {2})
]

automata.start_state = 0
automata.acceptance_states = {2}

input = "abbba"
result = automata.test_string(input)

print("Alphabet:")
for character in automata.alphabet:
  print(character)
 
print("string", input, "is", result)
```

You could realize that we only need to implement a NFA class to do everything that an NFA and a DFA could do, since the NFAs are a generalization of DFAs,
this implementation can be reduced to one class, or two with slightly changed interfaces, resulting in less code.

# Last step
*Have fun!*
