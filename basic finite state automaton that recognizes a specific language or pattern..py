class FiniteStateAutomaton:
    def __init__(self):
        self.start_state = 0
        self.state_a = 1
        self.accept_state = 2
        self.current_state = self.start_state
    def reset(self):
        """Reset the automaton to the initial state."""
        self.current_state = self.start_state

    def transition(self, char):
        """Define transitions based on the input character and current state."""
        if self.current_state == self.start_state:
            if char == 'a':
                self.current_state = self.state_a
        elif self.current_state == self.state_a:
            if char == 'b':
                self.current_state = self.accept_state
            elif char == 'a':
                self.current_state = self.state_a
            else:
                self.current_state = self.start_state
        else: 
            if char == 'a':
                self.current_state = self.state_a
            else:
                self.current_state = self.start_state

    def accepts(self, string):
        """Process the input string and check if it's accepted by the automaton."""
        self.reset()
        for char in string:
            self.transition(char)
        return self.current_state == self.accept_state
fsa = FiniteStateAutomaton()
test_strings = ["a", "ab", "cab", "dab", "ababc", "xyzab"]

for s in test_strings:
    result = fsa.accepts(s)
    print(f"The string '{s}' is {'accepted' if result else 'rejected'} by the automaton.")
