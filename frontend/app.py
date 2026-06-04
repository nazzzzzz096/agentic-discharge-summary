import streamlit as st
import requests

st.set_page_config(
    page_title="Agentic Discharge Summary",
    layout="wide"
)

st.title(
    "🏥 Agentic Discharge Summary Generator"
)

st.write(
    "Upload a patient PDF and generate a discharge summary draft."
)

uploaded_file = st.file_uploader(
    "Upload Patient PDF",
    type=["pdf"]
)

if uploaded_file:

    st.success(
        f"Uploaded: {uploaded_file.name}"
    )

    if st.button(
        "Generate Summary"
    ):

        with st.spinner(
            "Generating summary..."
        ):

            try:

                response = requests.post(
                    "http://127.0.0.1:8000/generate-summary",
                    files={
                        "file": (
                            uploaded_file.name,
                            uploaded_file.getvalue(),
                            "application/pdf"
                        )
                    },
                    timeout=300
                )

                if response.status_code != 200:

                    st.error(
                        f"API Error: {response.text}"
                    )

                else:

                    data = response.json()

                    with st.expander(
                        "Generated Summary",
                        expanded=True
                    ):

                        st.markdown(
                            data["summary"]
                        )

                    st.download_button(
                        label="📥 Download Summary",
                        data=data["summary"],
                        file_name="discharge_summary.txt",
                        mime="text/plain"
                    )

                    st.subheader(
                        "Review Flags"
                    )

                    if data["flags"]:

                        for flag in data["flags"]:

                            st.warning(
                                flag["message"]
                            )

                    else:

                        st.success(
                            "No review flags"
                        )

                    with st.expander(
                        "Execution Trace"
                    ):

                        for step in data["trace"]:

                            st.write(
                                f"Step {step['step']} | "
                                f"Action: {step['action']} | "
                                f"Result: {step['result']}"
                            )

            except requests.exceptions.Timeout:

                st.error(
                    "Request timed out."
                )

            except Exception as e:

                st.error(
                    f"Error: {str(e)}"
                )