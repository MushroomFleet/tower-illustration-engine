import json
import os
import re
import datetime

def load_config():
    """Load configuration from config.json"""
    with open('config.json', 'r') as f:
        return json.load(f)

def extract_section(content, section_name):
    """Extract a specific section from the markdown content"""
    pattern = fr"## {section_name}\s*\n\s*(.*?)(?=\s*##|\s*$)"
    match = re.search(pattern, content, re.DOTALL)
    if match:
        return match.group(1).strip()
    return None

def extract_scene_description(content, scene_type):
    """Extract a specific scene description from the Scene Variations section"""
    scene_headers = {
        "plain_background": "Plain Background",
        "tower_setting": "Tower Setting",
        "countryside_setting": "Countryside Setting",
        "tavern_setting": "Tavern Setting"
    }
    
    # Handle spotlight scene separately as it's its own section
    if scene_type == "spotlight_scene":
        # Extract the Spotlight Scene section
        spotlight_section = extract_section(content, "Spotlight Scene")
        if spotlight_section:
            # Find the line that starts with "depiction of T0W3R style"
            lines = spotlight_section.split('\n')
            for line in lines:
                if line.strip().startswith("depiction of T0W3R style"):
                    return line.strip()
        return None
    
    # For other scene types, look in the Scene Variations section
    header = scene_headers.get(scene_type)
    if not header:
        return None
    
    scene_section = extract_section(content, "Scene Variations")
    if not scene_section:
        return None
    
    # Find the specific scene subsection
    pattern = fr"### {header}\s*\n\s*(.*?)(?=\s*###|\s*##|\s*$)"
    match = re.search(pattern, scene_section, re.DOTALL)
    if match:
        # Find the line that starts with "depiction of T0W3R style"
        lines = match.group(1).split('\n')
        for line in lines:
            if line.strip().startswith("depiction of T0W3R style"):
                return line.strip()
    
    return None

def parse_prompt(prompt):
    """Extract components from a full prompt"""
    if not prompt:
        return None, None, None
    
    # Use regex to extract parts more reliably
    match = re.match(r"depiction of T0W3R style, ([^,]+), ([^,]+), ([^,]+), (.+)", prompt)
    if match:
        trigger = match.group(1)
        char_desc = match.group(2)
        outfit_desc = match.group(3)
        scene_desc = match.group(4)
        return char_desc, outfit_desc, scene_desc
    
    # Fallback to simple splitting if regex doesn't match
    parts = prompt.split(', ', 4)
    if len(parts) >= 4:
        return parts[1], parts[2], parts[3]
    
    return None, None, None

def parse_character_file(file_path):
    """Extract necessary information from a character markdown file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        scene_prompts = {}
        for scene_type in ["plain_background", "tower_setting", "countryside_setting", "tavern_setting", "spotlight_scene"]:
            prompt = extract_scene_description(content, scene_type)
            if prompt:
                scene_prompts[scene_type] = prompt
        
        return scene_prompts
    except Exception as e:
        print(f"Error parsing {file_path}: {e}")
        return {}

def ensure_directory(directory):
    """Ensure that the specified directory exists"""
    if not os.path.exists(directory):
        os.makedirs(directory)

def save_prompts(character_name, prompts, output_dir):
    """Save the generated prompts to output files"""
    character_dir = os.path.join(output_dir, character_name)
    ensure_directory(character_dir)
    
    # Save individual scene prompts
    for scene_type, prompt in prompts.items():
        file_path = os.path.join(character_dir, f"{scene_type}.txt")
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(prompt)
    
    # Save all prompts to a single file
    all_prompts_path = os.path.join(character_dir, "all_prompts.txt")
    with open(all_prompts_path, 'w', encoding='utf-8') as f:
        f.write(f"# {character_name.capitalize()} Prompts\n")
        f.write(f"Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        for scene_type, prompt in prompts.items():
            f.write(f"## {scene_type}\n")
            f.write(f"{prompt}\n\n")

def process_all_characters():
    """Process all characters and generate all prompts"""
    config = load_config()
    output_dir = config.get("output_directory")
    ensure_directory(output_dir)
    
    # Create a summary file for all characters
    summary_path = os.path.join(output_dir, "all_character_prompts.txt")
    with open(summary_path, 'w', encoding='utf-8') as summary_file:
        summary_file.write(f"# All Character Prompts\n")
        summary_file.write(f"Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        # Process each character
        for character_name, file_path in config.get("character_files", {}).items():
            print(f"Processing {character_name}...")
            scene_prompts = parse_character_file(file_path)
            
            if not scene_prompts:
                print(f"Failed to parse prompts for {character_name}")
                continue
            
            # Add to summary file
            summary_file.write(f"# {character_name.capitalize()}\n\n")
            
            for scene_type, prompt in scene_prompts.items():
                # Add to summary file
                summary_file.write(f"## {scene_type}\n")
                summary_file.write(f"{prompt}\n\n")
            
            # Save the prompts for this character
            save_prompts(character_name, scene_prompts, output_dir)
            print(f"Generated prompts for {character_name}")
            
            summary_file.write("\n---\n\n")
    
    print(f"All prompts generated and saved to {output_dir}")

if __name__ == "__main__":
    process_all_characters()
