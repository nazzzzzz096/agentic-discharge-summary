def detect_conflicts(state):

    conflicts = []

    diagnoses = state.diagnoses

    if len(set(diagnoses)) != len(diagnoses):

        conflicts.append(
            {
                "field":"diagnosis",
                "issue":
                "Duplicate diagnoses detected"
            }
        )

    return conflicts