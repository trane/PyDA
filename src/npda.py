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

    def verify(self, pda):
        """Ensures that this is a valid PDA"""
        assert pda['Sigma'] != {}, "Sigma cannot be empty"
        assert "" not in pda['Sigma'], "Sigma must not contain an empty string"
        assert pda['q0'] in pda['Q'], "q0 not in Q"
        assert pda['F'] <= pda['Q'], "Final state set too large"
        assert pda['Z'] in pda['Gamma'], "Initial stack symbol, not in Gamma"
        assert self.domain(pda['Delta']) <= self.product(
            self.product(pda['Sigma']|set(""), pda['Q']), pda['Gamma']), "Delta too large"


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
