from build_document_store import (
    build_document_store
)

document_store = build_document_store(
    "data/patient_2.pdf"
)

print(
    document_store.keys()
)