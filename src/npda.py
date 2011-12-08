# This is the NDPA object file, dig it.
'''
'Q': ('s0', 's1', 's2'),
'Sigma': ('0', '1'),
'Gamma': ('0','1','Z'),
'Delta': {
    's0': {
        '0': { '0': ['s1', '0'], '1': ['s2', '0'] },
        '1': { '0': ['s1', '0'], '1': ['s2', '0'] }
    },
    's1': {
        '0': { '0': ['s1', '0'], '1': ['s2', '0'] },
        '1': { '0': ['s1', '0'], '1': ['s2', '0'] }
    },
    's2': {
        '0': { '0': ['s1', '0'], '1': ['s2', '0'] },
        '1': { '0': ['s1', '0'], '1': ['s2', '0'] }
    }
},
'q0': 's0',
'Z': 'Z',
'F': ('s2')
}
'''
import json

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

    """
    def __init__(self, pda):
        """
        pda = {
        'Q': ['s0', 's1', 's2'],
        'Sigma': ['0', '1'],
        'Gamma': ['0','1','Z'],
        'Delta': {
            's0': {
                '0': { '0': ['s1', '0'], '1': ['s2', '0'] },
                '1': { '0': ['s1', '0'], '1': ['s2', '0'] }
            },
            's1': {
                '0': { '0': ['s1', '0'], '1': ['s2', '0'] },
                '1': { '0': ['s1', '0'], '1': ['s2', '0'] }
            },
            's2': {
                '0': { '0': ['s1', '0'], '1': ['s2', '0'] },
                '1': { '0': ['s1', '0'], '1': ['s2', '0'] }
            }
        },
        'q0': 's0',
        'Z': 'Z',
        'F': ['s2']
        } };
        """
        pda = normalize(pda)
        verify(pda);

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
        return npda

    def verify(pda):
        """Ensures that this is a valid PDA"""
        assert Sigma != (), "Sigma cannot be empty"
        assert "" not in Sigma, "Sigma must not contain an empty string"
        assert q0 in Q
