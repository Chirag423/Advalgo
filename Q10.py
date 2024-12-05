import json
from datetime import datetime

# Define ethical considerations categories and questions
ethical_topics = {
    "Privacy vs Security": [
        "How should organizations balance individual privacy with the need for security?",
        "What measures can be implemented to protect privacy without compromising security?",
        "What are examples of when privacy and security have conflicted?"
    ],
    "Impact on Marginalized Communities": [
        "How can data collection practices disproportionately affect marginalized communities?",
        "What steps can be taken to ensure inclusivity and fairness in data analysis?",
        "Are there cases where biased data has caused harm? If so, how could it have been prevented?"
    ],
    "Role of Data Ethics in Technology Development": [
        "What ethical principles should guide the development of data-driven technologies?",
        "How can organizations ensure accountability in the use of AI and machine learning?",
        "What are the consequences of neglecting data ethics in technology development?"
    ]
}

# Collect responses from users
def collect_responses():
    print("\nExploring Ethical Considerations in Data Privacy...\n")
    responses = {}
    for topic, questions in ethical_topics.items():
        print(f"Topic: {topic}")
        topic_responses = []
        for question in questions:
            print(f"\n - {question}")
            response = input("Your response: ").strip()
            topic_responses.append({"question": question, "response": response})
        responses[topic] = topic_responses
        print("\n" + "-" * 50 + "\n")
    return responses

# Generate a summary report
def generate_report(responses):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_filename = f"ethical_considerations_summary_{timestamp}.json"

    with open(report_filename, "w") as report_file:
        json.dump(responses, report_file, indent=4)

    print(f"\nSummary report generated: {report_filename}")
    return report_filename

# Display a summary of discussions
def display_summary(responses):
    print("\nSummary of Ethical Considerations:")
    for topic, answers in responses.items():
        print(f"\nTopic: {topic}")
        for answer in answers:
            print(f" - {answer['question']}")
            print(f"   * {answer['response']}")
    print("\n" + "-" * 50 + "\n")

# Main script execution
if __name__ == "__main__":
    responses = collect_responses()
    display_summary(responses)
    generate_report(responses)
