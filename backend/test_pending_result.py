from backend.tools.pending_result_tool import extract_pending_results

with open(
    "output/page_2.txt",
    "r",
    encoding="utf-8"
) as f:

    text = f.read()

result = extract_pending_results(text)

print(result)