import json
from datetime import datetime

# Define data protection regulation requirements
regulation_requirements = {
    "GDPR": {
        "data_processing": [
            "Ensure lawful, fair, and transparent processing of personal data.",
            "Obtain explicit consent from data subjects.",
            "Provide data subjects with access to their data and the right to correct or delete it."
        ],
        "data_security": [
            "Implement appropriate technical and organizational measures.",
            "Ensure encryption and pseudonymization of data.",
            "Maintain data integrity and confidentiality."
        ],
        "compliance_monitoring": [
            "Conduct regular data protection impact assessments (DPIA).",
            "Maintain records of processing activities.",
            "Appoint a Data Protection Officer (DPO) if required."
        ]
    },
    "HIPAA": {
        "privacy_rule": [
            "Ensure protected health information (PHI) is safeguarded.",
            "Provide patients with rights over their PHI.",
            "Limit disclosures of PHI to the minimum necessary."
        ],
        "security_rule": [
            "Implement administrative safeguards (e.g., training, risk analysis).",
            "Establish physical safeguards (e.g., facility access controls).",
            "Use technical safeguards (e.g., encryption, access control)."
        ],
        "breach_notification_rule": [
            "Notify affected individuals within 60 days of discovering a breach.",
            "Report breaches affecting more than 500 individuals to the Department of Health and Human Services."
        ]
    }
}

# Function to develop a compliance plan
def develop_compliance_plan(regulation, selected_requirements):
    if regulation not in regulation_requirements:
        print(f"Regulation '{regulation}' not recognized.")
        return

    print(f"\nDeveloping Compliance Plan for {regulation}...\n")
    selected_plan = {}
    for category, requirements in regulation_requirements[regulation].items():
        if category in selected_requirements:
            selected_plan[category] = requirements

    return selected_plan

# Function to generate a compliance plan report
def generate_report(regulation, compliance_plan):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_filename = f"compliance_plan_{regulation}_{timestamp}.json"

    report_content = {
        "timestamp": timestamp,
        "regulation": regulation,
        "compliance_plan": compliance_plan
    }

    with open(report_filename, "w") as report_file:
        json.dump(report_content, report_file, indent=4)

    print(f"\nCompliance plan report generated: {report_filename}")
    return report_filename

# Main execution
if __name__ == "__main__":
    print("Available Regulations:")
    for regulation in regulation_requirements.keys():
        print(f" - {regulation}")

    regulation = input("\nEnter the regulation to comply with (e.g., GDPR, HIPAA): ").strip().upper()

    if regulation in regulation_requirements:
        print(f"\nCategories for {regulation}:")
        for category in regulation_requirements[regulation].keys():
            print(f" - {category}")

        selected_categories = input(
            "\nEnter the categories to include in the compliance plan (comma-separated): "
        ).strip().split(",")

        selected_categories = [cat.strip().lower() for cat in selected_categories]
        compliance_plan = develop_compliance_plan(regulation, selected_categories)

        if compliance_plan:
            print("\nCompliance Plan:")
            for category, actions in compliance_plan.items():
                print(f" - {category.capitalize()}:")
                for action in actions:
                    print(f"   * {action}")

            generate_report(regulation, compliance_plan)
    else:
        print(f"Regulation '{regulation}' is not supported.")
