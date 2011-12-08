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
