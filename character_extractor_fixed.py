import re

def print_file_structure(file_path):
    """Print the complete file structure to debug extraction issues"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print(f"Analyzing file: {file_path}")
    
    # Print all section headers in the file
    headers = re.findall(r"^#+\s+(.+)$", content, re.MULTILINE)
    print("\nAll headers found in file:")
    for i, header in enumerate(headers):
        print(f"{i+1}. {header}")
    
    # Check the Scene Variations section with different regex
    variations_pattern = r"## Scene Variations(.*?)(?=^## |\Z)"
    match = re.search(variations_pattern, content, re.DOTALL | re.MULTILINE)
    
    if match:
        scene_section = match.group(1).strip()
        print("\nFound Scene Variations section using alternative pattern:")
        print("-" * 40)
        print(scene_section)
        print("-" * 40)
    else:
        print("\nCould not find Scene Variations section with alternative pattern!")
    
    # Check Plain Background subsection specifically
    plain_bg_pattern = r"###\s+Plain Background\s*\n(.*?)(?=###|\Z)"
    plain_match = re.search(plain_bg_pattern, content, re.DOTALL)
    
    if plain_match:
        plain_section = plain_match.group(1).strip()
        print("\nFound Plain Background subsection:")
        print("-" * 40)
        print(plain_section)
        print("-" * 40)
    else:
        print("\nCould not find Plain Background subsection!")

# Check Broderick's file
print_file_structure("characters/broderick.md")
