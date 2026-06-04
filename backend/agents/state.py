from dataclasses import dataclass, field

@dataclass
class AgentState:
    """
    Shared state object used by the discharge-summary agent.

    Stores extracted clinical information,
    agent execution trace,
    review flags,
    and reconciliation results.
    """

    diagnoses: list = field(default_factory=list)

    medications: list =field(default_factory=list)

    pending_results: list =field(default_factory=list)

    flags: list = field(default_factory=list)

    trace: list =field(default_factory=list)

    completed_tasks: list = field(default_factory=list)
   
    hospital_course: str = ""

    followup: list = field(default_factory=list)

    admission_medications: list = field(default_factory=list)

    discharge_medications: list = field(default_factory=list)

    reconciliation: dict = field(default_factory=dict)

    conflicts: list = field(default_factory=list)
   
    demographics: dict = field(default_factory=dict)

    dates: dict = field(default_factory=dict)

    allergies: list = field(default_factory=list)

    procedures: list = field(default_factory=list)

    condition_at_discharge: str = ""