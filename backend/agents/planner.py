def planner(state):

    if "clinical_data" not in state.completed_tasks:
        return "extract_clinical_data"

    return "finish"