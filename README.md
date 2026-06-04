# Agentic AI for Discharge Summary Generation

## Overview

This project implements an agentic AI system that generates structured discharge-summary drafts from raw patient source-note PDFs. The system is designed with a strong emphasis on clinical safety, traceability, and robustness.

The agent reads admission notes, progress notes, laboratory reports, and medication records, then produces a clinician-reviewable discharge summary while explicitly handling missing information, pending results, medication reconciliation issues, and potential documentation conflicts.

**Important:** The generated summary is always a draft and requires clinician review before clinical use.

---

# System Architecture

PDF Documents
↓
PDF to Images
↓
OCR Extraction
↓
Document Store
↓
Agent Loop
↓
Clinical Data Extraction
↓
Medication Reconciliation
↓
Conflict Detection
↓
Review Flag Generation
↓
Discharge Summary Draft

---

# Agent Loop Design

The system uses an agent loop with:

* Agent State
* Planner
* Tool Execution
* Trace Logging
* Step Control

The planner decides the next action based on the current state and completed tasks.

Example workflow:

1. Extract clinical information
2. Reconcile medications
3. Detect documentation conflicts
4. Generate review flags
5. Finish

A hard iteration limit (`MAX_STEPS = 10`) prevents infinite execution.

---

# Tools Used

## OCR Tool

Purpose:

* Extract text from PDF pages

Input:

* PDF page image

Output:

* Raw extracted text

---

## Clinical Extraction Tool

Purpose:

* Extract structured clinical information

Extracts:

* Diagnoses
* Medications
* Procedures
* Allergies
* Dates
* Follow-up instructions
* Pending results
* Hospital course
* Discharge condition

---

## Medication Reconciliation Tool

Purpose:

* Compare admission medications against discharge medications

Outputs:

* Added medications
* Removed medications
* Items requiring review

The system never invents medication changes.

---

## Conflict Detection Tool

Purpose:

* Detect contradictory information across source documents

Examples:

* Conflicting diagnoses
* Conflicting discharge conditions
* Conflicting medication information

Conflicts are surfaced for clinician review.

---

## Review Flag Tool

Purpose:

Generate safety flags when:

* Information is missing
* Results are pending
* Medication reconciliation cannot be completed
* Tool failures occur

---

# No-Fabrication Guardrail

Clinical safety is the highest priority.

The agent never invents:

* Diagnoses
* Medications
* Allergies
* Procedures
* Follow-up plans

If information cannot be found:

* "MISSING" is displayed

If information is pending:

* "PENDING" is displayed

The system always escalates uncertainty rather than guessing.

---

# Handling Missing and Pending Data

Examples:

* Missing patient name
* Missing discharge date
* Pending laboratory results
* Missing admission medication list

Such items are explicitly surfaced in the generated summary and review flags.

---

# Failure Handling

The system includes robust failure handling.

Possible failures:

* OCR failure
* Empty document
* Tool failure
* LLM response failure

Behavior:

* Exceptions are caught
* Tool failures are logged
* Review flags are generated
* The system does not silently continue

---

# Observability

Every execution produces a step trace.

Example:

Step 1:
Action: extract_clinical_data
Result: Clinical data extracted

Step 2:
Action: reconcile_medications
Result: Medication reconciliation completed

Step 3:
Action: detect_conflicts
Result: Found 0 conflicts

Step 4:
Action: generate_review_flags
Result: Generated 2 review flags

Step 5:
Action: finish
Result: Agent execution completed

This provides transparency and debugging capability.

---

# Example Output Sections

Generated discharge summaries include:

* Patient Demographics
* Admission Date
* Discharge Date
* Allergies
* Principal Diagnosis
* Secondary Diagnoses
* Hospital Course
* Procedures
* Condition at Discharge
* Discharge Medications
* Medication Reconciliation
* Documentation Conflicts
* Pending Results
* Follow-Up Instructions
* Review Flags

---

# Technologies Used

Backend:

* FastAPI

Frontend:

* Streamlit

Language:

* Python

OCR:

* EasyOCR

LLM:

* Gemini

Data Handling:

* Dataclasses
* JSON

---

# Running the Project

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Start FastAPI

```bash
uvicorn backend.api:app --reload
```

## Start Streamlit

```bash
streamlit run frontend/app.py
```

## Open UI

```text
http://localhost:8501
```

Upload a patient PDF and generate a discharge-summary draft.

---

# Limitations

* OCR quality depends on document quality.
* Conflict detection currently uses rule-based checks and can be expanded.
* Medication reconciliation is limited when admission medication records are unavailable.
* The system generates drafts only and is not intended for autonomous clinical use.

---

# Future Improvements

* Multi-step dynamic planning and replanning.
* Drug interaction lookup integration.
* Stronger conflict reasoning.
* Structured medical knowledge validation.
* Reinforcement learning from clinician edits.
* Human-in-the-loop review workflow.

---

# Clinical Safety Statement

This system is intended only to assist clinicians by generating draft discharge summaries.

It must not be used to make autonomous clinical decisions and always requires clinician review before use.

Part 2 Status

Part 2 was not implemented due to time constraints.

With additional time, I would implement:
- Simulated clinician reviewer
- Draft/corrected summary dataset generation
- Edit-distance reward metric
- Correction memory system
- Evaluation on held-out patients