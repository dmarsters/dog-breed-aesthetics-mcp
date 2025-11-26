#!/bin/bash
# Standard MCP Server Setup Pattern - Structure Verification Script
# Validates directory structure and required files

set -e

PROJECT_NAME="dog-breed-aesthetics-mcp"
PACKAGE_NAME="dog_breed_aesthetics_mcp"

echo "Verifying MCP Server structure for: $PROJECT_NAME"
echo "================================================="
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

errors=0
warnings=0

# Function to check if file exists
check_file() {
    if [ -f "$1" ]; then
        echo -e "${GREEN}✓${NC} $1"
        return 0
    else
        echo -e "${RED}✗${NC} $1 (missing)"
        ((errors++))
        return 1
    fi
}

# Function to check if directory exists
check_dir() {
    if [ -d "$1" ]; then
        echo -e "${GREEN}✓${NC} $1/"
        return 0
    else
        echo -e "${RED}✗${NC} $1/ (missing)"
        ((errors++))
        return 1
    fi
}

# Function to check file content for pattern
check_content() {
    local file=$1
    local pattern=$2
    local description=$3
    
    if [ ! -f "$file" ]; then
        return 1
    fi
    
    if grep -q "$pattern" "$file"; then
        echo -e "  ${GREEN}✓${NC} $description"
        return 0
    else
        echo -e "  ${YELLOW}⚠${NC} $description (not found)"
        ((warnings++))
        return 1
    fi
}

echo "Checking directory structure..."
echo "-------------------------------"
check_dir "$PACKAGE_NAME"
check_dir "tests"
echo ""

echo "Checking required configuration files..."
echo "----------------------------------------"
check_file "pyproject.toml"
check_file ".gitignore"
check_file "README.md"
echo ""

echo "Checking package files..."
echo "-------------------------"
check_file "$PACKAGE_NAME/__init__.py"
check_file "$PACKAGE_NAME/__main__.py"

# Check for large files (manual additions)
if check_file "$PACKAGE_NAME/server.py"; then
    check_content "$PACKAGE_NAME/server.py" "from fastmcp import FastMCP" "FastMCP import"
    check_content "$PACKAGE_NAME/server.py" "def get_server()" "get_server() function"
    check_content "$PACKAGE_NAME/server.py" "@mcp.tool()" "Tool decorators"
fi

if check_file "$PACKAGE_NAME/breed_data.py"; then
    check_content "$PACKAGE_NAME/breed_data.py" "BREED_DATABASE" "BREED_DATABASE dict"
    check_content "$PACKAGE_NAME/breed_data.py" "def normalize_breed_name" "normalize_breed_name function"
fi
echo ""

echo "Checking test files..."
echo "----------------------"
check_file "tests/__init__.py"
check_file "tests/run_tests.sh"

if [ -f "tests/run_tests.sh" ]; then
    if [ ! -x "tests/run_tests.sh" ]; then
        echo -e "  ${YELLOW}⚠${NC} tests/run_tests.sh not executable (run: chmod +x tests/run_tests.sh)"
        ((warnings++))
    fi
fi

# Check for test files (manual additions)
if check_file "tests/test_breed_data.py"; then
    check_content "tests/test_breed_data.py" "def test_" "Test functions"
fi

if [ -f "tests/test_server_tools.py" ]; then
    check_file "tests/test_server_tools.py"
    check_content "tests/test_server_tools.py" "def test_" "Test functions"
fi
echo ""

echo "Checking pyproject.toml configuration..."
echo "----------------------------------------"
if [ -f "pyproject.toml" ]; then
    check_content "pyproject.toml" "dependencies = \[\]" "Empty dependencies"
    check_content "pyproject.toml" "fastmcp" "FastMCP in dev dependencies"
    check_content "pyproject.toml" "requires-python = \">=3.10\"" "Python version requirement"
fi
echo ""

echo "Checking documentation files..."
echo "--------------------------------"
# These are optional but nice to have
optional_docs=(
    "START_HERE.md"
    "INDEX.md"
    "QUICK_REFERENCE.md"
    "EXAMPLES.md"
    "ARCHITECTURE.md"
    "DEPLOYMENT.md"
    "DEPLOYMENT_CHECKLIST.md"
)

for doc in "${optional_docs[@]}"; do
    if [ -f "$doc" ]; then
        echo -e "${GREEN}✓${NC} $doc (optional)"
    else
        echo -e "  ${NC}○${NC} $doc (optional, not present)"
    fi
done
echo ""

# Summary
echo "Verification Summary"
echo "===================="
if [ $errors -eq 0 ] && [ $warnings -eq 0 ]; then
    echo -e "${GREEN}All checks passed!${NC} ✓"
    echo ""
    echo "Next steps:"
    echo "1. If server.py or breed_data.py are missing, copy them manually"
    echo "2. Run: pip install -e \".[dev]\""
    echo "3. Run: ./tests/run_tests.sh"
    echo "4. Deploy: fastmcp deploy"
    exit 0
elif [ $errors -eq 0 ]; then
    echo -e "${YELLOW}Structure valid with $warnings warning(s)${NC} ⚠"
    echo ""
    echo "Warnings can usually be ignored if you haven't added large files yet."
    echo ""
    echo "Next steps:"
    echo "1. Address warnings if needed"
    echo "2. Copy large Python files if missing"
    echo "3. Run: pip install -e \".[dev]\""
    echo "4. Run: ./tests/run_tests.sh"
    exit 0
else
    echo -e "${RED}Structure validation failed with $errors error(s) and $warnings warning(s)${NC} ✗"
    echo ""
    echo "Fix the errors above and run this script again."
    exit 1
fi