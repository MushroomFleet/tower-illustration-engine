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
        "tavern_setting": "Tavern Setting",
        "spotlight_scene": "Spotlight Scene"
    }
    
    header = scene_headers.get(scene_type)
    if not header:
        return None
    
    # First locate the Scene Variations section
    scene_section = extract_section(content, "Scene Variations")
    if not scene_section and scene_type == "spotlight_scene":
        # For spotlight scene, look for it as its own section
        scene_section = extract_section(content, "Spotlight Scene")
        if scene_section:
            # Extract just the prompt line (assuming it's the first paragraph)
            lines = scene_section.split('\n')
            for line in lines:
                if line.startswith("depiction of T0W3R style"):
                    return line
            return scene_section
    
    if not scene_section:
        return None
    
    # Now find the specific scene within the section
    if scene_type == "spotlight_scene":
        pattern = fr"## {header}\s*\n\s*(.*?)(?=\s*##|\s*$)"
    else:
        pattern = fr"### {header}\s*\n\s*(.*?)(?=\s*###|\s*##|\s*$)"
    
    match = re.search(pattern, scene_section, re.DOTALL)
    if match:
        # Extract just the prompt line (assuming it's the first paragraph)
        lines = match.group(1).split('\n')
        for line in lines:
            if line.startswith("depiction of T0W3R style"):
                return line
        return match.group(1).strip()
    
    return None

def parse_scene_prompt(prompt):
    """Extract the scene description part from a full prompt"""
    if not prompt:
        return None
    
    parts = prompt.split(', ', 3)  # Split into up to 4 parts
    if len(parts) >= 4:
        # The last part should be the scene description
        return parts[-1]
    return None

def parse_character_file(file_path):
    """Extract necessary information from a character markdown file"""
    try:
        with open(file_path, 'r') as f:
            content = f.read()
            
        # Extract the basic character information
        character_description = extract_section(content, "Character Description")
        outfit_description = extract_section(content, "Clothing/Outfit Description")
        
        # Extract descriptions for each scene
        scene_descriptions = {}
        for scene_type in ["plain_background", "tower_setting", "countryside_setting", "tavern_setting", "spotlight_scene"]:
            prompt = extract_scene_description(content, scene_type)
            scene_descriptions[scene_type] = parse_scene_prompt(prompt)
        
        return {
            "character_description": character_description,
            "outfit_description": outfit_description,
            "scene_descriptions": scene_descriptions
        }
    except Exception as e:
        print(f"Error parsing {file_path}: {e}")
        return None

def extract_character_and_outfit(character_data):
    """Extract the character and outfit descriptions in a format suitable for prompts"""
    character_desc = character_data.get("character_description", "")
    outfit_desc = character_data.get("outfit_description", "")
    
    # Extract the first sentence or two for a concise description
    character_summary = ""
    if character_desc:
        # Extract the first paragraph
        paragraphs = character_desc.split('\n\n')
        if paragraphs:
            first_para = paragraphs[0]
            # Extract the first sentence that contains key physical attributes
            sentences = re.split(r'(?<=[.!?])\s+', first_para)
            character_summary = sentences[0]
            if len(sentences) > 1 and len(character_summary) < 100:
                character_summary += " " + sentences[1]
    
    # Extract the first sentence for the outfit
    outfit_summary = ""
    if outfit_desc:
        paragraphs = outfit_desc.split('\n\n')
        if paragraphs:
            first_para = paragraphs[0]
            sentences = re.split(r'(?<=[.!?])\s+', first_para)
            outfit_summary = sentences[0]
    
    return character_summary, outfit_summary

def generate_prompt(template, trigger, character_desc, outfit_desc, scene_desc):
    """Generate a complete prompt following the template"""
    return template.format(
        trigger=trigger,
        character_description=character_desc,
        outfit_description=outfit_desc,
        scene_description=scene_desc
    )

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
        with open(file_path, 'w') as f:
            f.write(prompt)
    
    # Save all prompts to a single file
    all_prompts_path = os.path.join(character_dir, "all_prompts.txt")
    with open(all_prompts_path, 'w') as f:
        f.write(f"# {character_name.capitalize()} Prompts\n")
        f.write(f"Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        for scene_type, prompt in prompts.items():
            f.write(f"## {scene_type}\n")
            f.write(f"{prompt}\n\n")

def process_all_characters():
    """Process all characters and generate all prompts"""
    config = load_config()
    template = config.get("template")
    output_dir = config.get("output_directory")
    ensure_directory(output_dir)
    
    # Create a summary file for all characters
    summary_path = os.path.join(output_dir, "all_character_prompts.txt")
    with open(summary_path, 'w') as summary_file:
        summary_file.write(f"# All Character Prompts\n")
        summary_file.write(f"Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        # Process each character
        for character_name, file_path in config.get("character_files", {}).items():
            print(f"Processing {character_name}...")
            character_data = parse_character_file(file_path)
            
            if not character_data:
                print(f"Failed to parse data for {character_name}")
                continue
            
            trigger = config.get("character_triggers", {}).get(character_name)
            character_desc, outfit_desc = extract_character_and_outfit(character_data)
            
            # Generate prompts for each scene
            prompts = {}
            summary_file.write(f"# {character_name.capitalize()}\n\n")
            
            for scene_type in config.get("scene_types", []):
                scene_desc = character_data.get("scene_descriptions", {}).get(scene_type)
                
                if scene_desc:
                    prompt = generate_prompt(template, trigger, character_desc, outfit_desc, scene_desc)
                    prompts[scene_type] = prompt
                    
                    # Add to summary file
                    summary_file.write(f"## {scene_type}\n")
                    summary_file.write(f"{prompt}\n\n")
            
            # Save the prompts for this character
            save_prompts(character_name, prompts, output_dir)
            print(f"Generated prompts for {character_name}")
            
            summary_file.write("\n---\n\n")
    
    print(f"All prompts generated and saved to {output_dir}")

if __name__ == "__main__":
    process_all_characters()
