import json
import re
from llm import generate_response

TEST_FILE = "tests/test_cases.json"


def normalize_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    return " ".join(text.split())


def keyword_matches(text: str, keyword: str) -> bool:
    text = normalize_text(text)
    keyword = normalize_text(keyword)

    if keyword in text:
        return True

    words = keyword.split()

    if len(words) == 1:
        return any(
            word.startswith(keyword) or keyword.startswith(word)
            for word in text.split()
        )

    return all(word in text.split() for word in words)


def evaluate_response(answer: str, expected_keywords: list[str]) -> dict:
    matched = [
        keyword
        for keyword in expected_keywords
        if keyword_matches(answer, keyword)
    ]

    score = (
        round((len(matched) / len(expected_keywords)) * 100)
        if expected_keywords
        else 0
    )

    return {
        "score": score,
        "matched": matched,
        "total_keywords": len(expected_keywords),
    }


def main():
    with open(TEST_FILE, "r", encoding="utf-8") as file:
        cases = json.load(file)

    results = []

    for case in cases:
        answer = generate_response(case["input"])

        evaluation = evaluate_response(
            answer,
            case["expected_keywords"]
        )

        results.append({
            "id": case["id"],
            "score": evaluation["score"],
            "matched": evaluation["matched"],
            "total_keywords": evaluation["total_keywords"],
            "answer": answer,
        })

    average = round(
        sum(item["score"] for item in results) / len(results),
        2
    )

    print(f"Average keyword coverage: {average}%")

    for item in results:
        print(
            f"\n{item['id']}: "
            f"{item['score']}% "
            f"({len(item['matched'])}/{item['total_keywords']} keywords)"
        )
        print(f"Matched: {item['matched']}")
        print(item["answer"])


if __name__ == "__main__":
    main()

