"""
Dog Breed Aesthetics MCP Server

Translates dog breed characteristics into visual aesthetic parameters
for AI image generation prompts.
"""

from fastmcp import FastMCP
from typing import Literal

# Use absolute imports for FastMCP Cloud compatibility
from dog_breed_aesthetics_mcp.breed_data import (
    BREED_DATABASE, 
    get_breed_names, 
    get_breed_data, 
    normalize_breed_name
)

# Initialize FastMCP server
mcp = FastMCP("dog-breed-aesthetics")

@mcp.tool()
def list_available_breeds() -> str:
    """
    List all available dog breeds that can be used for aesthetic enhancement.
    
    Returns a formatted list of 21 breeds organized by AKC group:
    - Sporting: Golden Retriever, Pointer, Cocker Spaniel
    - Hound: Greyhound, Basset Hound, Afghan Hound
    - Working: Siberian Husky, Great Dane, Boxer
    - Terrier: Jack Russell Terrier, Scottish Terrier, Bull Terrier
    - Toy: Pomeranian, Italian Greyhound, Pug
    - Non-Sporting: Poodle, Bulldog, Dalmatian
    - Herding: Border Collie, German Shepherd, Corgi
    """
    breeds_by_group = {}
    for breed_key, breed_data in BREED_DATABASE.items():
        group = breed_data["group"]
        if group not in breeds_by_group:
            breeds_by_group[group] = []
        breeds_by_group[group].append(breed_data["name"])
    
    output = ["Available Dog Breeds for Aesthetic Enhancement:\n"]
    
    group_order = ["Sporting", "Hound", "Working", "Terrier", "Toy", "Non-Sporting", "Herding"]
    
    for group in group_order:
        if group in breeds_by_group:
            output.append(f"\n{group} Group:")
            for breed in sorted(breeds_by_group[group]):
                output.append(f"  • {breed}")
    
    output.append("\n\nUsage: Call enhance_with_breed_aesthetic() with a breed name and your base prompt.")
    
    return "\n".join(output)


@mcp.tool()
def get_breed_characteristics(breed_name: str) -> str:
    """
    Get detailed visual characteristics for a specific dog breed.
    
    Returns the breed's physical proportions, coat qualities, movement characteristics,
    temperament aesthetics, color palette, and visual essence - all the data that will
    be used to enhance prompts.
    
    Args:
        breed_name: Name of the breed (e.g., "Golden Retriever", "Greyhound")
    """
    breed_key = normalize_breed_name(breed_name)
    breed_data = get_breed_data(breed_key)
    
    if not breed_data:
        available = get_breed_names()
        return f"Breed '{breed_name}' not found. Available breeds:\n" + "\n".join(f"  • {b}" for b in available)
    
    output = [
        f"=== {breed_data['name']} ===",
        f"Group: {breed_data['group']}",
        f"Scale: {breed_data['scale']}",
        "",
        "Visual Essence:",
        f"  {breed_data['visual_essence']}",
        "",
        "Proportions:",
    ]
    
    for key, value in breed_data['proportions'].items():
        output.append(f"  • {key.replace('_', ' ').title()}: {value}")
    
    output.append("\nCoat:")
    for key, value in breed_data['coat'].items():
        output.append(f"  • {key.replace('_', ' ').title()}: {value}")
    
    output.append("\nMovement:")
    for key, value in breed_data['movement'].items():
        output.append(f"  • {key.replace('_', ' ').title()}: {value}")
    
    output.append("\nTemperament Aesthetic:")
    for key, value in breed_data['temperament_aesthetic'].items():
        output.append(f"  • {key.replace('_', ' ').title()}: {value}")
    
    output.append("\nColor Palette:")
    output.append("  " + ", ".join(breed_data['color_palette']))
    
    return "\n".join(output)


@mcp.tool()
def enhance_with_breed_aesthetic(
    breed_name: str,
    base_prompt: str,
    emphasis_level: Literal["subtle", "moderate", "strong"] = "moderate"
) -> dict:
    """
    Enhance an image generation prompt with dog breed aesthetic characteristics.
    
    Takes a base prompt and infuses it with the visual qualities of a specific dog breed.
    The breed's physical proportions, movement qualities, coat textures, and temperament
    are translated into aesthetic parameters for image generation.
    
    This tool returns structured data that should be passed to Claude for final synthesis
    into an enhanced prompt. The enhancement preserves the user's original intent while
    adding breed-specific visual qualities.
    
    Args:
        breed_name: Name of the breed to draw aesthetics from (e.g., "Greyhound", "Corgi")
        base_prompt: The original image prompt to enhance
        emphasis_level: How strongly to apply breed characteristics:
            - "subtle": Light touch, gentle influence
            - "moderate": Balanced integration (default)
            - "strong": Pronounced breed aesthetic
    
    Returns:
        Dictionary containing:
        - breed_name: The selected breed
        - breed_group: AKC group classification
        - base_prompt: Original prompt
        - emphasis_level: Selected emphasis
        - visual_essence: Core aesthetic summary
        - characteristics: Detailed breed characteristics organized by category
        - synthesis_instruction: Instructions for Claude to create final prompt
    """
    breed_key = normalize_breed_name(breed_name)
    breed_data = get_breed_data(breed_key)
    
    if not breed_data:
        available = get_breed_names()
        return {
            "error": f"Breed '{breed_name}' not found",
            "available_breeds": available,
            "suggestion": "Use list_available_breeds() to see all options"
        }
    
    # Package all the deterministic breed data for Claude to synthesize
    enhancement_data = {
        "breed_name": breed_data["name"],
        "breed_group": breed_data["group"],
        "base_prompt": base_prompt,
        "emphasis_level": emphasis_level,
        "visual_essence": breed_data["visual_essence"],
        "characteristics": {
            "proportions": breed_data["proportions"],
            "coat": breed_data["coat"],
            "movement": breed_data["movement"],
            "temperament_aesthetic": breed_data["temperament_aesthetic"],
            "color_palette": breed_data["color_palette"],
            "scale": breed_data["scale"]
        },
        "synthesis_instruction": f"""
Create an enhanced image generation prompt by weaving {breed_data['name']} aesthetic characteristics into the base prompt.

Base prompt: "{base_prompt}"

Emphasis level: {emphasis_level}
- subtle: Gentle influence, mostly preserve original tone
- moderate: Balanced integration of breed aesthetics
- strong: Pronounced breed characteristics throughout

Key aesthetic qualities to integrate:
{breed_data['visual_essence']}

Draw from these breed characteristics as appropriate:
- Physical proportions and build
- Coat texture and qualities  
- Movement and energy
- Temperament and mood
- Color palette suggestions

Requirements:
1. Preserve the core intent and subject of the base prompt
2. Weave in breed aesthetics naturally, not literally (don't add actual dogs)
3. Match the emphasis level - subtle should be light touch, strong should be pronounced
4. Focus on translating breed qualities into visual/compositional/tonal elements
5. Keep the enhanced prompt concise and coherent (2-4 sentences typically)

Return only the enhanced prompt text, ready to use for image generation.
"""
    }
    
    return enhancement_data


def main():
    """Entry point for local development"""
    mcp.run()


# For FastMCP Cloud deployment - return the server object
def get_server():
    """Entry point for FastMCP Cloud"""
    return mcp
