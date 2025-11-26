"""
Tests for breed_data module
"""

import pytest
from dog_breed_aesthetics_mcp.breed_data import (
    BREED_DATABASE,
    get_breed_names,
    get_breed_data,
    normalize_breed_name
)


def test_breed_database_exists():
    """Test that BREED_DATABASE is defined and non-empty"""
    assert BREED_DATABASE is not None
    assert len(BREED_DATABASE) > 0


def test_breed_database_structure():
    """Test that all breeds have required fields"""
    required_keys = [
        "name", "group", "proportions", "coat", "movement",
        "temperament_aesthetic", "color_palette", "scale", "visual_essence"
    ]
    
    for breed_key, breed_data in BREED_DATABASE.items():
        for key in required_keys:
            assert key in breed_data, f"Breed {breed_key} missing key: {key}"


def test_breed_count():
    """Test that we have expected number of breeds (21)"""
    assert len(BREED_DATABASE) == 21, f"Expected 21 breeds, got {len(BREED_DATABASE)}"


def test_breeds_by_group():
    """Test that we have 3 breeds per group (7 groups)"""
    groups = {}
    for breed_data in BREED_DATABASE.values():
        group = breed_data["group"]
        groups[group] = groups.get(group, 0) + 1
    
    assert len(groups) == 7, f"Expected 7 groups, got {len(groups)}"
    
    for group, count in groups.items():
        assert count == 3, f"Group {group} should have 3 breeds, has {count}"


def test_normalize_breed_name():
    """Test breed name normalization"""
    # Test standard case
    assert normalize_breed_name("Golden Retriever") == "golden_retriever"
    
    # Test case insensitivity
    assert normalize_breed_name("GOLDEN RETRIEVER") == "golden_retriever"
    assert normalize_breed_name("golden retriever") == "golden_retriever"
    
    # Test with hyphens
    assert normalize_breed_name("golden-retriever") == "golden_retriever"
    
    # Test single word
    assert normalize_breed_name("Greyhound") == "greyhound"


def test_normalize_breed_name_variations():
    """Test breed name variation handling"""
    # Corgi variations
    assert normalize_breed_name("Pembroke Welsh Corgi") == "corgi"
    assert normalize_breed_name("Welsh Corgi") == "corgi"
    
    # Poodle variations
    assert normalize_breed_name("Standard Poodle") == "poodle"


def test_get_breed_data():
    """Test breed data retrieval"""
    # Test valid breed
    greyhound = get_breed_data("greyhound")
    assert greyhound is not None
    assert greyhound["name"] == "Greyhound"
    assert greyhound["group"] == "Hound"
    
    # Test invalid breed
    invalid = get_breed_data("invalid_breed")
    assert invalid is None


def test_get_breed_names():
    """Test getting list of breed names"""
    names = get_breed_names()
    assert len(names) == 21
    assert "Greyhound" in names
    assert "Border Collie" in names
    assert sorted(names) == names  # Should be sorted


def test_visual_essence_present():
    """Test that all breeds have visual essence defined"""
    for breed_key, breed_data in BREED_DATABASE.items():
        assert "visual_essence" in breed_data
        assert len(breed_data["visual_essence"]) > 0
        assert isinstance(breed_data["visual_essence"], str)


def test_color_palette_present():
    """Test that all breeds have color palette defined"""
    for breed_key, breed_data in BREED_DATABASE.items():
        assert "color_palette" in breed_data
        assert len(breed_data["color_palette"]) > 0
        assert isinstance(breed_data["color_palette"], list)


def test_proportions_structure():
    """Test that proportions dict has expected keys"""
    expected_keys = {"body_ratio", "build", "head", "legs"}
    
    for breed_key, breed_data in BREED_DATABASE.items():
        proportions = breed_data["proportions"]
        assert isinstance(proportions, dict)
        assert set(proportions.keys()) == expected_keys, \
            f"Breed {breed_key} has unexpected proportions keys"


def test_coat_structure():
    """Test that coat dict has expected keys"""
    expected_keys = {"texture", "length", "qualities"}
    
    for breed_key, breed_data in BREED_DATABASE.items():
        coat = breed_data["coat"]
        assert isinstance(coat, dict)
        assert set(coat.keys()) == expected_keys, \
            f"Breed {breed_key} has unexpected coat keys"


def test_movement_structure():
    """Test that movement dict has expected keys"""
    expected_keys = {"gait", "energy", "qualities"}
    
    for breed_key, breed_data in BREED_DATABASE.items():
        movement = breed_data["movement"]
        assert isinstance(movement, dict)
        assert set(movement.keys()) == expected_keys, \
            f"Breed {breed_key} has unexpected movement keys"


def test_temperament_structure():
    """Test that temperament_aesthetic dict has expected keys"""
    expected_keys = {"mood", "presence", "character"}
    
    for breed_key, breed_data in BREED_DATABASE.items():
        temperament = breed_data["temperament_aesthetic"]
        assert isinstance(temperament, dict)
        assert set(temperament.keys()) == expected_keys, \
            f"Breed {breed_key} has unexpected temperament keys"


def test_specific_breeds_present():
    """Test that expected specific breeds are present"""
    expected_breeds = [
        "golden_retriever", "greyhound", "border_collie",
        "pomeranian", "bulldog", "great_dane"
    ]
    
    for breed_key in expected_breeds:
        assert breed_key in BREED_DATABASE, f"Expected breed {breed_key} not found"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
