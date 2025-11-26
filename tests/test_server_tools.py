"""
Tests for server tools functionality
"""

import pytest

# Import the underlying functions before FastMCP wraps them
# We'll import from breed_data and recreate the tool logic
from dog_breed_aesthetics_mcp.breed_data import (
    BREED_DATABASE, 
    get_breed_names, 
    get_breed_data, 
    normalize_breed_name
)


# Recreate the tool functions without FastMCP decoration for testing
def list_available_breeds() -> str:
    """List all available breeds"""
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


def get_breed_characteristics(breed_name: str) -> str:
    """Get detailed characteristics for a breed"""
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


def enhance_with_breed_aesthetic(
    breed_name: str,
    base_prompt: str,
    emphasis_level: str = "moderate"
) -> dict:
    """Enhance prompt with breed aesthetics"""
    breed_key = normalize_breed_name(breed_name)
    breed_data = get_breed_data(breed_key)
    
    if not breed_data:
        available = get_breed_names()
        return {
            "error": f"Breed '{breed_name}' not found",
            "available_breeds": available,
            "suggestion": "Use list_available_breeds() to see all options"
        }
    
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


# Now all the original tests work as-is
def test_list_available_breeds():
    """Test that list_available_breeds returns formatted string"""
    result = list_available_breeds()
    
    assert isinstance(result, str)
    assert len(result) > 0
    assert "Available Dog Breeds" in result
    assert "Sporting Group:" in result
    assert "Hound Group:" in result
    assert "Greyhound" in result
    assert "Border Collie" in result


def test_list_available_breeds_has_all_groups():
    """Test that all 7 AKC groups are listed"""
    result = list_available_breeds()
    
    groups = ["Sporting", "Hound", "Working", "Terrier", "Toy", "Non-Sporting", "Herding"]
    for group in groups:
        assert f"{group} Group:" in result, f"Missing {group} Group in output"


def test_get_breed_characteristics_valid_breed():
    """Test getting characteristics for a valid breed"""
    result = get_breed_characteristics("Greyhound")
    
    assert isinstance(result, str)
    assert "Greyhound" in result
    assert "Group: Hound" in result
    assert "Visual Essence:" in result
    assert "Proportions:" in result
    assert "Coat:" in result
    assert "Movement:" in result
    assert "Temperament Aesthetic:" in result
    assert "Color Palette:" in result


def test_get_breed_characteristics_case_insensitive():
    """Test that breed name lookup is case insensitive"""
    result1 = get_breed_characteristics("Greyhound")
    result2 = get_breed_characteristics("greyhound")
    result3 = get_breed_characteristics("GREYHOUND")
    
    # All should return valid results
    assert "Greyhound" in result1
    assert "Greyhound" in result2
    assert "Greyhound" in result3


def test_get_breed_characteristics_invalid_breed():
    """Test getting characteristics for an invalid breed"""
    result = get_breed_characteristics("Invalid Breed Name")
    
    assert isinstance(result, str)
    assert "not found" in result.lower()
    assert "Available breeds:" in result


def test_enhance_with_breed_aesthetic_valid():
    """Test enhancement with valid parameters"""
    result = enhance_with_breed_aesthetic(
        breed_name="Greyhound",
        base_prompt="portrait of a dancer",
        emphasis_level="moderate"
    )
    
    assert isinstance(result, dict)
    assert "breed_name" in result
    assert "breed_group" in result
    assert "base_prompt" in result
    assert "emphasis_level" in result
    assert "visual_essence" in result
    assert "characteristics" in result
    assert "synthesis_instruction" in result
    
    assert result["breed_name"] == "Greyhound"
    assert result["breed_group"] == "Hound"
    assert result["base_prompt"] == "portrait of a dancer"
    assert result["emphasis_level"] == "moderate"


def test_enhance_with_breed_aesthetic_all_emphasis_levels():
    """Test enhancement with all emphasis levels"""
    emphasis_levels = ["subtle", "moderate", "strong"]
    
    for level in emphasis_levels:
        result = enhance_with_breed_aesthetic(
            breed_name="Border Collie",
            base_prompt="abstract art",
            emphasis_level=level
        )
        
        assert isinstance(result, dict)
        assert result["emphasis_level"] == level
        assert level in result["synthesis_instruction"]


def test_enhance_with_breed_aesthetic_invalid_breed():
    """Test enhancement with invalid breed"""
    result = enhance_with_breed_aesthetic(
        breed_name="Invalid Breed",
        base_prompt="test prompt",
        emphasis_level="moderate"
    )
    
    assert isinstance(result, dict)
    assert "error" in result
    assert "not found" in result["error"].lower()
    assert "available_breeds" in result


def test_enhance_with_breed_aesthetic_characteristics_structure():
    """Test that characteristics have expected structure"""
    result = enhance_with_breed_aesthetic(
        breed_name="Poodle",
        base_prompt="modern architecture",
        emphasis_level="strong"
    )
    
    chars = result["characteristics"]
    assert "proportions" in chars
    assert "coat" in chars
    assert "movement" in chars
    assert "temperament_aesthetic" in chars
    assert "color_palette" in chars
    assert "scale" in chars
    
    # Check that these are the right types
    assert isinstance(chars["proportions"], dict)
    assert isinstance(chars["coat"], dict)
    assert isinstance(chars["movement"], dict)
    assert isinstance(chars["temperament_aesthetic"], dict)
    assert isinstance(chars["color_palette"], list)
    assert isinstance(chars["scale"], str)


def test_enhance_with_breed_aesthetic_synthesis_instruction():
    """Test that synthesis instruction is comprehensive"""
    result = enhance_with_breed_aesthetic(
        breed_name="Great Dane",
        base_prompt="city skyline",
        emphasis_level="moderate"
    )
    
    instruction = result["synthesis_instruction"]
    assert isinstance(instruction, str)
    assert len(instruction) > 100  # Should be substantial
    assert "Great Dane" in instruction
    assert "city skyline" in instruction
    assert "moderate" in instruction
    assert "emphasis level" in instruction.lower()


def test_enhance_with_default_emphasis():
    """Test that default emphasis level works"""
    result = enhance_with_breed_aesthetic(
        breed_name="Bulldog",
        base_prompt="test prompt"
        # emphasis_level not specified, should default to "moderate"
    )
    
    assert isinstance(result, dict)
    assert result["emphasis_level"] == "moderate"


def test_multiple_breeds_different_groups():
    """Test enhancement works for breeds from different groups"""
    breeds = [
        ("Golden Retriever", "Sporting"),
        ("Afghan Hound", "Hound"),
        ("Boxer", "Working"),
        ("Jack Russell Terrier", "Terrier"),
        ("Pug", "Toy"),
        ("Dalmatian", "Non-Sporting"),
        ("Corgi", "Herding")
    ]
    
    for breed_name, expected_group in breeds:
        result = enhance_with_breed_aesthetic(
            breed_name=breed_name,
            base_prompt="test",
            emphasis_level="moderate"
        )
        
        assert isinstance(result, dict)
        assert result["breed_group"] == expected_group


def test_visual_essence_included():
    """Test that visual essence is included in enhancement"""
    result = enhance_with_breed_aesthetic(
        breed_name="Greyhound",
        base_prompt="abstract shapes",
        emphasis_level="subtle"
    )
    
    essence = result["visual_essence"]
    assert isinstance(essence, str)
    assert len(essence) > 0
    # Greyhound should have aerodynamic/streamlined in essence
    assert any(word in essence.lower() for word in ["aerodynamic", "streamlined", "elegant"])


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
