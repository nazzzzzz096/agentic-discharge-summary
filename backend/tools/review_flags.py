def generate_flags(state):

    flags = []

    if state.pending_results:

        flags.append(
            {
                "type":
                "pending_result",

                "message":
                "Pending results require review"
            }
        )

    if state.conflicts:

        flags.append(
            {
                "type":
                "conflict",

                "message":
                "Conflicting information detected"
            }
        )

    if state.reconciliation:

        if state.reconciliation.get(
            "status"
        ):

            flags.append(
                {
                    "type":
                    "reconciliation",

                    "message":
                    state.reconciliation[
                        "status"
                    ]
                }
            )
        if state.reconciliation.get("needs_review"):

            flags.append(
            {
                "type": "reconciliation",
                "message": (
                "Medication reconciliation incomplete"
            )
        }
    )

    return flags