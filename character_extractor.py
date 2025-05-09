import re

def print_scene_sections(file_path):
    """Print the Scene Variations section structure to debug extraction issues"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print(f"Analyzing file: {file_path}")
    
    # Extract the Scene Variations section
    scene_section_pattern = r"## Scene Variations\s*\n(.*?)(?=\s*##|$)"
    scene_section_match = re.search(scene_section_pattern, content, re.DOTALL)
    
    if scene_section_match:
        scene_section = scene_section_match.group(1).strip()
        print("\nFound Scene Variations section:")
        print("-" * 40)
        print(scene_section)
        print("-" * 40)
        
        # Look for individual scene subsections
        subsection_pattern = r"### ([^\n]+)\s*\n(.*?)(?=\s*###|\s*##|\s*$)"
        subsections = re.finditer(subsection_pattern, scene_section, re.DOTALL)
        
        for i, match in enumerate(subsections):
            header = match.group(1).strip()
            content = match.group(2).strip()
            print(f"\nSubsection {i+1}: {header}")
            print("-" * 40)
            print(content)
            print("-" * 40)
    else:
        print("Could not find Scene Variations section!")
    
    # Extract the Spotlight Scene section
    spotlight_pattern = r"## Spotlight Scene\s*\n(.*?)(?=\s*##|$)"
    spotlight_match = re.search(spotlight_pattern, content, re.DOTALL)
    
    if spotlight_match:
        spotlight_section = spotlight_match.group(1).strip()
        print("\nFound Spotlight Scene section:")
        print("-" * 40)
        print(spotlight_section)
        print("-" * 40)
    else:
        print("Could not find Spotlight Scene section!")

# Check a few character files to understand the structure
print_scene_sections("characters/broderick.md")
