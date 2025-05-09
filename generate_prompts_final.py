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

def extract_all_scenes(content):
    """Extract all scene descriptions from a character file"""
    scenes = {}
    
    # First extract the Scene Variations section
    scene_variations = extract_section(content, "Scene Variations")
    if scene_variations:
        # Extract each scene by its header
        scene_headers = {
            "plain_background": "Plain Background",
            "tower_setting": "Tower Setting",
            "countryside_setting": "Countryside Setting",
            "tavern_setting": "Tavern Setting"
        }
        
        for scene_type, header in scene_headers.items():
            pattern = fr"### {header}\s*\n(.*?)(?=\s*###|\s*##|\s*$)"
            match = re.search(pattern, scene_variations, re.DOTALL)
            if match:
                scene_text = match.group(1).strip()
                scenes[scene_type] = scene_text
    
    # Extract the Spotlight Scene separately as it's its own section
    spotlight_section = extract_section(content, "Spotlight Scene")
    if spotlight_section:
        scenes["spotlight_scene"] = spotlight_section.strip()
    
    return scenes

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
            
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Extract all scenes for this character
                scene_prompts = extract_all_scenes(content)
                
                if not scene_prompts:
                    print(f"No scenes found for {character_name}")
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
            
            except Exception as e:
                print(f"Error processing {character_name}: {e}")
    
    print(f"All prompts generated and saved to {output_dir}")

if __name__ == "__main__":
    process_all_characters()
