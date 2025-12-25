from .alpha_beta_pruning import make_decision

def make_smart_decision(options: list) -> str:
    """
    Make a smart decision using Alpha-Beta pruning.
    """
    if not options:
        return "No options available to make a decision."
    
    if len(options) == 1:
        return options[0]
    
    return make_decision(options) 