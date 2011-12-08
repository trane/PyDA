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
        pda = {
            "q0": "s0",
            "F": [ "s2" ],
            "Q": [ "s0", "s1", "s2", "s2" ],
            "Delta": {
                "s2": { "1": { "1": [ [ "s2", "s1" ], "0" ], "0": [ [ "s1" ], "0" ] },
                        "0": { "1": [ [ "s2" ], "0" ], "0": [ [ "s1" ], "0" ] } },
                "s1": { "1": { "1": [ [ "s2" ], "0" ], "0": [ [ "s1" ], "0" ] },
                        "0": { "1": [ [ "s2" ], "0" ], "0": [ [ "s1" ], "0" ] } },
                "s0": { "1": { "1": [ [ "s2" ], "0" ], "0": [ [ "s1" ], "0" ] },
                        "0": { "1": [ [ "s2" ], "0" ], "0": [ [ "s1" ], "0" ] } }
            },
            "Z": "z",
            "Sigma": [ "0", "1" ],
            "Gamma": [ "0", "1", "z" ]
        };
        """
        verify(pda);
        self.inpt = string;
        self.stack = pda['Z'];

    def normalize(pda):
        """ While JSON datastructure allows us portability, we will convert this
        into a more functional construct.
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
                ('s1', '1', '0', 's1', '0'),
                ('s2', '1', '0', 's1', '0'),
                ('s0', '0', '1', 's2', '0'),
                ('s2', '1', '1', 's2', '0'),
                ('s2', '1', '1', 's1', '0'),
                ('s0', '1', '1', 's2', '0'),
                ('s2', '0', '1', 's2', '0'),
                ('s1', '0', '0', 's1', '0'),
                ('s1', '1', '1', 's2', '0')
            },
            'q0': 's0',
            'Z': 'Z'
        }
        """
        npda = dict()
        npda['Q'] = set(pda['Q'])
        npda['Sigma'] = set(pda['Sigma'])
        npda['Gamma'] = set(pda['Gamma'])
        delta = set()
        for init,inputs in pda['Delta'].items():
            for inpt,stack in inputs.items():
                for stack_t,dest in stack.items():
                    for state in dest[0]:
                        delta.add((init, inpt, stack_t, state, dest[1]))
        npda['Delta'] = delta
        npda['F'] = set(pda['F'])
        npda['q0'] = pda['q0']
        return npda

    def verify(pda):
        """Ensures that this is a valid PDA"""
        assert pda['Sigma'] != {}, "Sigma cannot be empty"
        assert "" not in pda['Sigma'], "Sigma must not contain an empty string"
        assert pda['q0'] in pda['Q'], "q0 not in Q"
        assert pda['F'] <= pda['Q'], "Final state set too large"
        assert pda['Z'] in pda['Gamma'], "Initial stack symbol, not in Gamma"
        assert domain(pda['Delta']) <= product(pda['Gamma'],
            product(pda['Sigma']|set(""), pda['Q'])), "Delta too large"


    def domain(delta):
        """Compute the domain"""
        return set(delta.keys)

    def product(S1, S2):
        """Compute the Cartesian product of S1 x S2"""
        return set((a, b) for a in S1 for b in S2)


# Steps though every stepper that we have by 1 step
def step_all(npda):
    # The new list of valid states after we step every stepper by 1
    new_valid_states = list()

    # Step every stepper by 1, and create a list of the new valid states
    for s in npda.stepper_list:
        valid_states = step_stepper(s)
        new_valid_states.extends(valid_states)

    # Set the new valid states to be the npda.stepper_list
    npda.stepper_list = list(new_valid_states)
    return

# Steps through this stepper by 1 step, and returns a list of all valid states
# after this step
def step_stepper():
    return;
