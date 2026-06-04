from fastapi import (
    FastAPI,
    UploadFile,
    File,
    HTTPException
)

import shutil
from pathlib import Path

from backend.agents.state import AgentState
from backend.agents.agent_loop import run_agent

from backend.tools.summary_generator import (
    generate_summary
)

from backend.tools.review_flags import (
    generate_flags
)

from backend.tools.reconciliation_tool import (
    reconcile_medications
)

from backend.tools.conflict_detector import (
    detect_conflicts
)

from backend.build_document_store import (
    build_document_store
)

app = FastAPI(
    title="Agentic Discharge Summary API"
)

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


@app.get("/")
def health():
    """
    Health check endpoint.
    """

    return {
        "status": "healthy"
    }


@app.post("/generate-summary")
async def generate_summary_api(
    file: UploadFile = File(...)
):
    """
    Upload a patient PDF and generate
    a discharge summary draft.
    """

    try:

        # Save uploaded PDF
        file_path = (
            UPLOAD_DIR / file.filename
        )

        with open(
            file_path,
            "wb"
        ) as buffer:

            shutil.copyfileobj(
                file.file,
                buffer
            )

        # Build OCR document store
        document_store = (
            build_document_store(
                str(file_path)
            )
        )

        # Run agent
        state = AgentState()

        state = run_agent(
            state,
            document_store
        )
        print("AGENT COMPLETE")

        print("RUNNING RECONCILIATION")
        # Reconciliation
        state.reconciliation = (
            reconcile_medications(
                state.admission_medications,
                state.medications
            )
        )
        state.trace.append({
           "step": 2,
           "action": "reconcile_medications",
           "result": "Medication reconciliation completed"
        })
        print("RECONCILIATION COMPLETE")

        print("RUNNING CONFLICT DETECTOR")
        # Conflict detection
        state.conflicts = (
            detect_conflicts(state)
        )
        state.trace.append({
           "step": 3,
           "action": "detect_conflicts",
           "result": f"Found {len(state.conflicts)} conflicts"
        })
        print("CONFLICT DETECTOR COMPLETE")

        print("RUNNING REVIEW FLAGS")
        # Review flags
        state.flags = (
            generate_flags(state)
        )
        state.trace.append({
            "step": 4,
            "action": "generate_review_flags",
            "result": f"Generated {len(state.flags)} review flags"
        })
        print("REVIEW FLAGS COMPLETE")
        state.trace.append({
            "step": 5,
            "action": "finish",
            "result": "Agent execution completed"
         })
        print("RUNNING SUMMARY")

        # Generate summary
        summary = generate_summary(
            state,
            document_store
        )

        return {

            "summary": summary,

            "flags": state.flags,

            "trace": state.trace,

            "demographics":
                state.demographics,

            "dates":
                state.dates,

            "allergies":
                state.allergies,

            "procedures":
                state.procedures,

            "reconciliation":
                state.reconciliation,

            "conflicts":
                state.conflicts
        }

    except Exception as e:

        print(
            f"API ERROR: {str(e)}"
        )

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )