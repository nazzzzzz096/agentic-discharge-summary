import json

from backend.agents.state import AgentState
from backend.agents.agent_loop import run_agent
from backend.tools.summary_generator import generate_summary
from backend.tools.review_flags import generate_flags
from backend.tools.conflict_detector import detect_conflicts
from backend.tools.reconciliation_tool import reconcile_medications
from backend.tools.conflict_detector import detect_conflicts
with open(
    "output/document_store.json",
    "r",
    encoding="utf-8"
) as f:

    document_store = json.load(f)

state = AgentState()

state = run_agent(
    state,
    document_store
)
state.flags = generate_flags(state)
state.conflicts = detect_conflicts(state)

state.reconciliation = (
    reconcile_medications(
        state.admission_medications,
        state.medications
    )
)

state.conflicts = (
    detect_conflicts(state)
)
summary=generate_summary(state,document_store)
print("\n=== DIAGNOSES ===")
print(state.diagnoses)

print("\n=== MEDICATIONS ===")
print(state.medications)

print("\n=== PENDING RESULTS ===")
print(state.pending_results)

print("\n=== HOSPITAL COURSE ===")
print(state.hospital_course)

print("\n=== FOLLOWUP ===")
print(state.followup)

print("\n=== FLAGS ===")
print(state.flags)

print("\n=== TRACE ===")
print(state.trace)
print("\n=== DEMOGRAPHICS ===")
print(state.demographics)

print("\n=== DATES ===")
print(state.dates)

print("\n=== ALLERGIES ===")
print(state.allergies)

print("\n=== PROCEDURES ===")
print(state.procedures)

print("\n=== CONFLICTS ===")
print(state.conflicts)

print("\n=== RECONCILIATION ===")
print(state.reconciliation)
print("\n=== SUMMARY ===")
print(summary)