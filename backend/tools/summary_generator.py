from google import genai

from backend.config import (
    GEMINI_API_KEY,
    MODEL_NAME
)

client = genai.Client(
    api_key=GEMINI_API_KEY
)

def generate_summary(state, document_store):
    """
    Generate discharge summary from
    extracted agent state.
    """
    print(state.diagnoses)
    principal_dx = (
        state.diagnoses[0]
        if state.diagnoses
        else "MISSING"
    )

    secondary_dx = "\n".join(
        f"- {dx}"
        for dx in state.diagnoses[1:]
    )

    procedures = "\n".join(
        f"- {proc}"
        for proc in state.procedures
    ) or "MISSING"

    pending_results = "\n".join(
        f"- {result}"
        for result in state.pending_results
    ) or "None"

    followup = "\n".join(
        f"- {item}"
        for item in state.followup
    ) or "MISSING"
    allergies = "\n".join(
       f"- {a}"
       for a in state.allergies
    ) or "MISSING"
    conflicts = "\n".join(
        f"- {c}"
        for c in state.conflicts
    ) or "None detected"
    medications = "\n".join(
        [
            f"- {med['name']} | "
            f"Dose: {med.get('dose') or 'MISSING'} | "
            f"Frequency: {med.get('frequency') or 'MISSING'} | "
            f"Duration: {med.get('duration') or 'MISSING'}"
            for med in state.medications
        ]
    ) or "MISSING"

    flags = "\n".join(
        [
            f"- {flag['message']}"
            for flag in state.flags
        ]
    ) or "None"
    
    reconciliation = f"""
Added:
{', '.join(state.reconciliation.get('added', [])) or 'None'}

Removed:
{', '.join(state.reconciliation.get('removed', [])) or 'None'}

Needs Review:
{', '.join(state.reconciliation.get('needs_review', [])) or 'None'}
"""
    summary = f"""
# ⚠ DRAFT DISCHARGE SUMMARY

This document was generated automatically and
requires clinician review before clinical use.
# Patient Demographics

Patient Name: {state.demographics.get('patient_name', 'MISSING')}
Age: {state.demographics.get('age', 'MISSING')}
Gender: {state.demographics.get('gender', 'MISSING')}

# Admission Date

{state.dates.get('admission_date', 'MISSING')}

# Discharge Date

{state.dates.get('discharge_date', 'MISSING')}
# Allergies

{allergies}
# Principal Diagnosis

{principal_dx}

# Secondary Diagnoses

{secondary_dx if secondary_dx else 'None'}

# Hospital Course

{state.hospital_course}

# Procedures

{procedures}

# Condition at Discharge

{state.condition_at_discharge or 'MISSING'}

# Discharge Medications

{medications}

# Medication Reconciliation

{reconciliation}
# Documentation Conflicts

{conflicts}
# Pending Results

{pending_results}

# Follow-up Instructions

{followup}

# Review Flags

{flags}
"""

    return summary