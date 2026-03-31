import collections

with open("../logs/user_access.log", "r") as f:
    lines = f.readlines()

summary = collections.defaultdict(list)

for line in lines:
    parts = line.strip().split(" - ")
    if len(parts) < 4:
        continue
    user = parts[1].split(": ")[1]
    resource = parts[2].split(": ")[1]
    result = parts[3].split(": ")[1]
    summary[user].append((resource, result))

with open("../audit/audit_summary.md", "w") as f:
    f.write("# Audit Summary\n")
    f.write("Project: Zero Trust IAM & GRC Program\n")
    f.write("Author: Miguel Carrillo\n\n")
    for user, actions in summary.items():
        f.write(f"## User: {user}\n")
        for resource, result in actions:
            f.write(f"- Resource: {resource} | Result: {result}\n")
        f.write("\n")