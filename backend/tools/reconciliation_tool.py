def reconcile_medications(
    admission,
    discharge
):
    """
    Compare admission and discharge medications.

    If admission medications are unavailable,
    reconciliation cannot be completed and
    should be flagged for clinician review.
    """

    if not admission:

        return {
            "added": [],
            "removed": [],
            "changed": [],
            "needs_review": [
                "Admission medications unavailable. Medication reconciliation could not be completed."
            ]
        }

    admission_names = {
        med.get("name", "").lower()
        if isinstance(med, dict)
        else str(med).lower()
        for med in admission
    }

    discharge_names = {
        med.get("name", "").lower()
        if isinstance(med, dict)
        else str(med).lower()
        for med in discharge
    }

    return {

        "added": list(
            discharge_names -
            admission_names
        ),

        "removed": list(
            admission_names -
            discharge_names
        ),

        "changed": [],

        "needs_review": []
    }