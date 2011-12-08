# This is the NDPA object file, dig it.

# Steps though every stepper that we have by 1 step.
# Returns true if there are more states that can be stepped through, and
# false if we cannot do any more stepping (ie if the string is not accepted
# by the pda)
def step_all(npda):
    # The new list of valid states after we step every stepper by 1
    new_valid_states = list()

    # Step every stepper by 1, and create a list of the new valid states
    for s in npda.stepper_list:
        valid_states = step_stepper(s)
        new_valid_states.extends(valid_states)

    # Set the new valid states to be the npda.stepper_list
    npda.stepper_list = list(new_valid_states)

    # Return true if we can step again after this call, false otherwise
    if not npda.stepper_list:
        return False
    return True


# Returns true if this string has been accepted (ie, if the string has been
# fully run through the pda and ends on a final state)
def string_accepts(npda):
    for s in npda.stepper_list:
        if s.input == "":
            if s.curr_state in npda.pda[f]:
                return True
    return False


# Steps through this stepper by 1 step, and returns a list of all valid states
# after this step
def step_stepper(s):
    return;
