
from backend.agents.planner import planner
from backend.tools.clinical_extraction_tool import (
    extract_clinical_data
)

MAX_STEPS = 10


def run_agent(state, document_store):
    """
    Main agent execution loop.

    Responsibilities:
    - Planning
    - Tool execution
    - State updates
    - Trace logging
    - Failure handling
    - Step cap enforcement
    """

    combined_text = "\n".join(
        document_store.values()
    )

    steps = 0

    while steps < MAX_STEPS:

        action = planner(state)

        if action == "finish":
            break

        if action == "extract_clinical_data":

            try:

                result = extract_clinical_data(
                    combined_text
                )

                state.diagnoses = result.get(
                    "diagnoses",
                    []
                )

                state.medications = result.get(
                    "medications",
                    []
                )

                state.pending_results = result.get(
                    "pending_results",
                    []
                )

                state.hospital_course = result.get(
                    "hospital_course",
                    "MISSING"
                )

                state.followup = result.get(
                    "followup",
                    []
                )

                state.demographics = result.get(
                    "demographics",
                    {}
                )

                state.dates = result.get(
                    "dates",
                    {}
                )

                state.allergies = result.get(
                    "allergies",
                    []
                )

                state.procedures = result.get(
                    "procedures",
                    []
                )

                state.condition_at_discharge = result.get(
                    "condition_at_discharge",
                    "MISSING"
                )

                state.completed_tasks.append(
                    "clinical_data"
                )

                state.trace.append(
                    {
                        "step": steps + 1,
                        "action": action,
                        "result": (
                            "Clinical data extracted"
                        )
                    }
                )

            except Exception as e:

                state.flags.append(
                    {
                        "type": "tool_failure",
                        "message": str(e)
                    }
                )

                state.trace.append(
                    {
                        "step": steps + 1,
                        "action": action,
                        "result": (
                            f"FAILED: {str(e)}"
                        )
                    }
                )

                break

        steps += 1

    
    

    return state
