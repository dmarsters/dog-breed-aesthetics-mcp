#!/bin/bash
# Standard MCP Server Setup Pattern - Structure Creation Script
# Generates all directories and small files automatically

set -e

PROJECT_NAME="dog-breed-aesthetics-mcp"
PACKAGE_NAME="dog_breed_aesthetics_mcp"

echo "Creating MCP Server structure for: $PROJECT_NAME"
echo "================================================"

# Create directory structure
echo "Creating directories..."
mkdir -p "$PACKAGE_NAME"
mkdir -p tests

# Create pyproject.toml
echo "Creating pyproject.toml..."
cat > pyproject.toml << 'EOF'
[project]
name = "dog-breed-aesthetics-mcp"
version = "0.1.0"
description = "MCP server for translating dog breed characteristics into visual aesthetic parameters"
authors = [
    {name = "Dal Marsters"}
]
readme = "README.md"
requires-python = ">=3.10"
dependencies = []

[project.optional-dependencies]
dev = [
    "fastmcp",
    "pytest",
    "pytest-asyncio"
]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project.scripts]
dog-breed-aesthetics-mcp = "dog_breed_aesthetics_mcp.server:main"
EOF

# Create package __init__.py
echo "Creating package __init__.py..."
cat > "$PACKAGE_NAME/__init__.py" << 'EOF'
"""Dog Breed Aesthetics MCP Server"""

from .server import mcp, get_server

__all__ = ["mcp", "get_server"]
EOF

# Create package __main__.py
echo "Creating package __main__.py..."
cat > "$PACKAGE_NAME/__main__.py" << 'EOF'
"""Local development entry point"""

from .server import main

if __name__ == "__main__":
    main()
EOF

# Create .gitignore
echo "Creating .gitignore..."
cat > .gitignore << 'EOF'
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual environments
venv/
ENV/
env/

# IDEs
.vscode/
.idea/
*.swp
*.swo
*~

# Testing
.pytest_cache/
.coverage
htmlcov/

# OS
.DS_Store
Thumbs.db
EOF

# Create tests/__init__.py
echo "Creating tests/__init__.py..."
touch tests/__init__.py

# Create tests/run_tests.sh
echo "Creating tests/run_tests.sh..."
cat > tests/run_tests.sh << 'EOF'
#!/bin/bash
# Run all tests for dog-breed-aesthetics-mcp

set -e

echo "Running Dog Breed Aesthetics MCP Tests"
echo "======================================="
echo ""

# Run pytest if available
if command -v pytest &> /dev/null; then
    echo "Running pytest..."
    pytest tests/ -v
else
    echo "pytest not available, running Python tests directly..."
    python -m tests.test_breed_data
    python -m tests.test_server_tools
fi

echo ""
echo "All tests passed! ✓"
EOF
chmod +x tests/run_tests.sh

# Create README.md
echo "Creating README.md..."
cat > README.md << 'EOF'
# Dog Breed Aesthetics MCP Server

Translate dog breed characteristics into visual aesthetic parameters for AI image generation.

## Quick Start
```bash
# Install in development mode
pip install -e ".[dev]"

# Run tests
./tests/run_tests.sh

# Run server locally
python -m dog_breed_aesthetics_mcp

# Deploy to FastMCP Cloud
fastmcp deploy
```

## Setup Pattern

This project follows the Standard MCP Server Setup Pattern:

1. `./create_structure.sh` - Generate directories and small files
2. `./verify_structure.sh` - Validate structure
3. Manual: Copy large Python files (server.py, breed_data.py, tests)
4. `pip install -e ".[dev]"` - Install in dev mode
5. `./tests/run_tests.sh` - Validate everything works

## Architecture

Three-layer olog pattern for cost optimization:

1. **Deterministic Layer**: Breed lookup (zero cost)
2. **Structured Parameters**: Organized data (zero cost)
3. **Single LLM Call**: Creative synthesis only

**Cost savings**: ~60-80% vs pure LLM approach

## Available Breeds

21 breeds across 7 AKC groups (3 per group):
- Sporting, Hound, Working, Terrier, Toy, Non-Sporting, Herding

See documentation for complete breed list and characteristics.

## Tools

1. `list_available_breeds()` - List all 21 breeds
2. `get_breed_characteristics(breed_name)` - Get breed details
3. `enhance_with_breed_aesthetic(breed_name, base_prompt, emphasis_level)` - Enhance prompts

## Documentation

- `START_HERE.md` - Quick start guide
- `INDEX.md` - File navigation
- `QUICK_REFERENCE.md` - Fast lookup
- `EXAMPLES.md` - Prompt enhancement examples
- `ARCHITECTURE.md` - System design
- `DEPLOYMENT.md` - Deploy guide

## Author

Dal Marsters - Lushy AI
EOF

echo ""
echo "Structure created successfully!"
echo ""
echo "Next steps:"
echo "1. Run ./verify_structure.sh to validate"
echo "2. Manually copy large files:"
echo "   - dog_breed_aesthetics_mcp/server.py"
echo "   - dog_breed_aesthetics_mcp/breed_data.py"
echo "   - tests/test_breed_data.py"
echo "   - tests/test_server_tools.py"
echo "3. pip install -e \".[dev]\""
echo "4. ./tests/run_tests.sh"
echo ""