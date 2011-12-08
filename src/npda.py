# This is the NDPA object file, dig it.

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
