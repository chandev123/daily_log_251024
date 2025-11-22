import argparse
import json
import os
import datetime
from pathlib import Path

# Configuration
TEMP_LOG_FILE = ".daily_log_temp.json"
TEMPLATE_FILE = "daily_report_template.md"
BASE_DIR = Path(__file__).parent

# Section Mapping
SECTIONS = {
    "goal": "1. 오늘의 목표",
    "act": "2. 수행 내용",
    "res": "3. 결과 / 진척도",
    "issue": "4. 문제점 및 개선방안",
    "insight": "5. 분석 / 인사이트",
    "plan": "6. 내일 계획"
}

SECTION_ALIASES = {
    "goals": "goal",
    "activities": "act",
    "activity": "act",
    "results": "res",
    "result": "res",
    "issues": "issue",
    "problems": "issue",
    "insights": "insight",
    "plans": "plan"
}

def load_logs():
    if os.path.exists(TEMP_LOG_FILE):
        with open(TEMP_LOG_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {key: [] for key in SECTIONS.keys()}

def save_logs(logs):
    with open(TEMP_LOG_FILE, 'w', encoding='utf-8') as f:
        json.dump(logs, f, ensure_ascii=False, indent=4)

def add_log(content, section):
    section = SECTION_ALIASES.get(section, section)
    if section not in SECTIONS:
        print(f"Error: Invalid section '{section}'. Available sections: {', '.join(SECTIONS.keys())}")
        return

    logs = load_logs()
    logs[section].append(content)
    save_logs(logs)
    print(f"Added to [{SECTIONS[section]}]: {content}")

def generate_report():
    logs = load_logs()
    
    # Read Template
    if not os.path.exists(TEMPLATE_FILE):
        print(f"Error: Template file '{TEMPLATE_FILE}' not found.")
        return

    with open(TEMPLATE_FILE, 'r', encoding='utf-8') as f:
        template = f.read()

    # Prepare Date
    today = datetime.date.today()
    date_str_dot = today.strftime("%Y.%m.%d")
    date_str_dash = today.strftime("%Y-%m-%d")
    
    # Fill Template
    content = template.replace("{{YYYY.MM.DD}}", date_str_dot)
    
    import re
    
    for key, header in SECTIONS.items():
        items = logs.get(key, [])
        list_content = ""
        for item in items:
            list_content += f"- {item}\n"
        
        if items:
            # Regex to match the header and the following bullet point line
            # Matches: ## Header [optional whitespace] newline - [optional whitespace]
            pattern = r"(## " + re.escape(header) + r"[ \t]*\n)- [ \t]*"
            
            # Check if pattern exists
            if re.search(pattern, content):
                content = re.sub(pattern, f"\\1\n{list_content}", content, count=1)

    
    # Determine Output Path
    # Structure: 2025/11_November/daily/YYYY-MM-DD.md
    year = today.strftime("%Y")
    month_name = today.strftime("%m_%B") # 11_November
    
    output_dir = BASE_DIR / year / month_name / "daily"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    output_file = output_dir / f"{date_str_dash}.md"
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Report generated: {output_file}")

def clear_logs():
    if os.path.exists(TEMP_LOG_FILE):
        os.remove(TEMP_LOG_FILE)
        print("Logs cleared.")
    else:
        print("No logs to clear.")

def main():
    parser = argparse.ArgumentParser(description="Daily Report Generator")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Add Command
    add_parser = subparsers.add_parser("add", help="Add a log entry")
    add_parser.add_argument("content", help="The content to log")
    add_parser.add_argument("-s", "--section", default="act", help="The section to add to (default: act). Options: goal, act, res, issue, insight, plan")

    # Generate Command
    subparsers.add_parser("generate", help="Generate the daily report")

    # Clear Command
    subparsers.add_parser("clear", help="Clear the current day's logs")

    args = parser.parse_args()

    if args.command == "add":
        add_log(args.content, args.section)
    elif args.command == "generate":
        generate_report()
    elif args.command == "clear":
        clear_logs()

if __name__ == "__main__":
    main()
