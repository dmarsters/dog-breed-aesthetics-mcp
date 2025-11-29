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

Dal Marsters - Lushy.app
