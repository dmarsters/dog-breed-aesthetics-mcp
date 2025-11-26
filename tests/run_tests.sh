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
