import os
import yaml

# Define the required keys
REQUIRED_KEYS = {"name", "github", "bio", "interests"}

def validate_member_file(filepath):
    with open(filepath, 'r') as file:
        content = yaml.safe_load(file)

    # Check if all required keys are present
    missing_keys = REQUIRED_KEYS - content.keys()
    if missing_keys:
        raise ValueError(f"Missing keys in {filepath}: {', '.join(missing_keys)}")

    # Additional validations can be added here
    if not isinstance(content.get("interests"), list):
        raise ValueError(f"'interests' must be a list in {filepath}")

# Scan the members directory
members_dir = "members"
for filename in os.listdir(members_dir):
    if filename.endswith(".md"):
        try:
            validate_member_file(os.path.join(members_dir, filename))
            print(f"✅ {filename} passed validation.")
        except Exception as e:
            print(f"❌ {filename} failed validation: {e}")
            exit(1)

