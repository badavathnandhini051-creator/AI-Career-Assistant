import json
from llm import generate_response

TEST_FILE = "tests/test_cases.json"


def evaluate_response(answer: str, expected_keywords: list[str]) -> dict:
    text = answer.lower()
    matched = [keyword for keyword in expected_keywords if keyword.lower() in text]
    score = round((len(matched) / len(expected_keywords)) * 100) if expected_keywords else 0
    return {"score": score, "matched": matched}


def main():
    with open(TEST_FILE, "r", encoding="utf-8") as file:
        cases = json.load(file)

    results = []
    for case in cases:
        answer = generate_response(case["input"])
        evaluation = evaluate_response(answer, case["expected_keywords"])
        results.append({
            "id": case["id"],
            "score": evaluation["score"],
            "matched": evaluation["matched"],
            "answer": answer,
        })

    average = round(sum(item["score"] for item in results) / len(results), 2)
    print(f"Average keyword coverage: {average}%")
    for item in results:
        print(f"\n{item['id']}: {item['score']}%")
        print(item["answer"])


if __name__ == "__main__":
    main()
