class NPDA(object):
    """
    NPDA is an object representing a Non-Deterministic Pushdown Automata.

    To create an NPDA object, you must give a dictionary object containing
        Q: a finite set of states
        Sigma: a finite input alphabet
        Gamma: a finite stack alphabet
        Delta: a mapping of Q x (Sigma \cup {""}) x Gamma to finite subset of
            QxGamma* (the transition relation).
        q0: the start state (must exist in Q)
        Z: the initial stack symbol (must exist in Gamma)
        F: set of accepting states (must be a subset of Q)
    And the string to run
    """
    def __init__(self, pda, string):
        """
        PDAs will look like this:
        {
            'Q': {'s2', 's1', 's0'},
            'F': {'s2'},
            'Sigma': {'1', '0'},
            'Gamma': {'1', '0', 'Z'},
            'Delta': {
                ('s0', '1', '0', 's1', '0'),
                ('s2', '0', '0', 's1', '0'),
                ('s0', '0', '0', 's1', '0'),
                ('s1', '0', '1', 's2', '0'),
                ('s2', '0', '1', 's2', '0'),
                ('s1', '0', '0', 's1', '0'),
                ('s1', '1', '1', 's2', '0')
            },
            'q0': 's0',
            'Z': 'Z'
        }
        """
        self.verify(pda)
        self.inpt = string;
        self.stack = pda['Z']
        self.pda = pda
        initial_stepper = Stepper(self.inpt, self.pda['q0'], self.pda['Z'])
        self.stepper_list = [initial_stepper]

    def verify(self, pda):
        """Ensures that this is a valid PDA"""
        assert pda['Sigma'] != {}, "Sigma cannot be empty"
        assert "" not in pda['Sigma'], "Sigma must not contain an empty string"
        assert pda['q0'] in pda['Q'], "q0 not in Q"
        assert pda['F'] <= pda['Q'], "F not a subset of Q"
        assert pda['F'] & pda['Q'] == pda['F'], "F is not subset of Q"
        assert pda['Z'] in pda['Gamma'], "Initial stack symbol, not in Gamma"
        for inpt in pda['Delta']:
            assert inpt[1] in pda['Sigma']|set("@"), "Invalid input in Delta"
        assert self.domain(pda['Delta']) <= self.product(
            self.product(
                pda['Sigma']|set("@"), pda['Q']), pda['Gamma']|set("@")), "Delta too large"

    def domain(self, delta):
        """Maps the (p, a, A, q, alpha) -> ((a, p), A)
        where a is input, p is state and A is the top of the stack"""
        domain = set()
        for f in delta:
            domain.add(((f[1], f[0]), f[2]))
        return domain

    def product(self, S1, S2):
        """Compute the Cartesian product of S1 x S2"""
        return set((a, b) for a in S1 for b in S2)

    def step_all(self):
        """
        Steps though every stepper that we have by 1 step.
        Returns true if there are more states that can be stepped through, and
        false if we cannot do any more stepping (ie if the string is not accepted
        by the pda)
        """
        # The new list of valid states after we step every stepper by 1
        new_valid_states = list()

        # Step every stepper by 1, and create a list of the new valid states
        for s in self.stepper_list:
            valid_states = s.step(self)
            new_valid_states.extend(valid_states)

        # Set the new valid states to be the npda.stepper_list
        self.stepper_list = list(new_valid_states)

        # Return True if we can step again after this call, False otherwise
        if not self.stepper_list: # An empty list registers as False
            return False
        return True

    def accepts(self):
        """
        Returns true if this string has been accepted (ie, if the string has
        been fully run through the pda and ends on a final state) and the stack
        either is empty or consists only of the "Z" character as defined in the
        NPDA.
        """
        for s in self.stepper_list:
            if s.input == "":
                if s.state in self.pda['F']:
                    if len(s.stack) <= 1:
                        return True
        return False


    class Stepper(object):

        def __init__(self, inpt, state, stack):
            """
            Initialize the new Stepper object given an input string
            (representing the remaining input to be processed), the current
            state, and the current stack (represented as a string).
            """
            self.inpt = inpt
            self.state = state
            self.stack = stack

        def step(self, npda):
            """
            Steps the current Stepper object, returning a list of new Stepper
            objects resulting from any transitions, based on the given npda
            """
            steppers = list()

            for d in npda.pda['Delta']:
                if d[0] == self.state:
                    if d[1] == self.inpt[:1] or d[1] == '@':
                        # Top of stack is the end of the string, and so we also
                        # have to reverse the result using [::-1]
                        if d[2] == self.stack[-len(d[2]):][::-1] or d[2] == '@':
                            new_stack = self.stack[:]
                            # Pop the specified characters from the stack
                            if not d[2] == '@':
                                new_stack = new_stack[:-len(d[2])]
                            # Push the new characters to the stack
                            if not d[4] == '@':
                                new_stack = new_stack.extend(d[4][::-1])
                            # Consume input character (if not eps (@))
                            if not d[1] == '@':
                                new_inpt = self.inpt[1:]
                            # Create the new Stepper object including new state
                            # and add to the steppers list
                            steppers.append(Stepper(inpt, self.state, new_stack))

            # Return finished list of steppers
            return steppers;
