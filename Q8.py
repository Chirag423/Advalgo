import os
import json
import datetime

# Define audit categories
audit_criteria = {
    "data_collection": [
        "Are users informed about data collection?",
        "Is data collection limited to what's necessary?",
        "Are consent mechanisms in place?"
    ],
    "data_storage": [
        "Is data encrypted at rest?",
        "Is sensitive data stored securely?",
        "Are backup policies in place?"
    ],
    "data_access": [
        "Is access to data restricted based on roles?",
        "Are access logs maintained and monitored?",
        "Are strong authentication mechanisms used?"
    ],
    "compliance": [
        "Is the organization GDPR compliant?",
        "Are data retention policies clearly defined?",
        "Is there a process for handling data subject requests?"
    ]
}

# Sample responses for vulnerabilities
responses = {}

def collect_responses():
    print("Starting Data Privacy Audit...\n")
    for category, questions in audit_criteria.items():
        print(f"Category: {category.upper()}")
        category_responses = []
        for question in questions:
            response = input(f" - {question} (Yes/No): ").strip().lower()
            while response not in ["yes", "no"]:
                print("Please enter 'Yes' or 'No'.")
                response = input(f" - {question} (Yes/No): ").strip().lower()
            category_responses.append({"question": question, "response": response})
        responses[category] = category_responses
        print("\n")

def analyze_responses():
    print("\nAnalyzing Responses...\n")
    vulnerabilities = {}
    for category, answers in responses.items():
        category_vulnerabilities = [item["question"] for item in answers if item["response"] == "no"]
        vulnerabilities[category] = category_vulnerabilities

    return vulnerabilities

def generate_report(vulnerabilities):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_filename = f"data_privacy_audit_report_{timestamp}.json"

    report_content = {
        "timestamp": timestamp,
        "audit_results": responses,
        "vulnerabilities": vulnerabilities
    }

    with open(report_filename, "w") as report_file:
        json.dump(report_content, report_file, indent=4)

    print(f"\nAudit report generated: {report_filename}")
    return report_filename

def display_summary(vulnerabilities):
    print("\nSummary of Findings:")
    for category, issues in vulnerabilities.items():
        print(f" - {category.upper()}: {len(issues)} issues identified.")
        for issue in issues:
            print(f"   * {issue}")

# Main script execution
if __name__ == "__main__":
    collect_responses()
    vulnerabilities = analyze_responses()
    display_summary(vulnerabilities)
    generate_report(vulnerabilities)
