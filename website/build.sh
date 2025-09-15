#!/bin/bash

# OMSN Teaching Manual Website Builder
# One-click script to generate beautiful websites from markdown manuals
#
# Usage:
#   ./build.sh           # Generate website from all manuals
#   ./build.sh serve     # Generate and serve locally
#   ./build.sh clean     # Clean output directory
#
# Author: OMSN Teaching Manual Project
# License: GNU Affero General Public License v3.0

set -e  # Exit on any error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Get script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
OUTPUT_DIR="$SCRIPT_DIR/output"

# Print header
print_header() {
    echo -e "${PURPLE}"
    echo "╔════════════════════════════════════════════════════════════════╗"
    echo "║                  OMSN TEACHING MANUAL                         ║"
    echo "║                    Website Generator                           ║"
    echo "║                                                                ║"
    echo "║          Dynamic, Content-Agnostic Static Site Generator      ║"
    echo "╚════════════════════════════════════════════════════════════════╝"
    echo -e "${NC}"
}

# Check dependencies
check_dependencies() {
    echo -e "${CYAN}🔍 Checking dependencies...${NC}"

    # Check Python 3
    if ! command -v python3 &> /dev/null; then
        echo -e "${RED}❌ Python 3 is required but not installed${NC}"
        exit 1
    fi

    # Check if markdown2 is available (will be auto-installed by generator if needed)
    echo -e "${GREEN}✅ Python 3 found: $(python3 --version)${NC}"

    # Verify generator script exists
    if [[ ! -f "$SCRIPT_DIR/generator.py" ]]; then
        echo -e "${RED}❌ Generator script not found: $SCRIPT_DIR/generator.py${NC}"
        exit 1
    fi

    # Verify template exists
    if [[ ! -f "$SCRIPT_DIR/template.html" ]]; then
        echo -e "${RED}❌ Template not found: $SCRIPT_DIR/template.html${NC}"
        exit 1
    fi

    echo -e "${GREEN}✅ All dependencies satisfied${NC}"
}

# Clean output directory
clean_output() {
    echo -e "${YELLOW}🧹 Cleaning output directory...${NC}"
    if [[ -d "$OUTPUT_DIR" ]]; then
        rm -rf "$OUTPUT_DIR"
        echo -e "${GREEN}✅ Output directory cleaned${NC}"
    else
        echo -e "${BLUE}ℹ️  Output directory already clean${NC}"
    fi
}

# Generate website
generate_website() {
    echo -e "${CYAN}🚀 Generating website...${NC}"
    echo -e "${BLUE}📁 Project root: $PROJECT_ROOT${NC}"
    echo -e "${BLUE}📁 Output directory: $OUTPUT_DIR${NC}"
    echo ""

    # Run the Python generator
    cd "$SCRIPT_DIR"
    python3 generator.py

    echo ""
    echo -e "${GREEN}🎉 Website generation complete!${NC}"

    # List generated files
    if [[ -d "$OUTPUT_DIR" ]]; then
        echo -e "${CYAN}📄 Generated files:${NC}"
        ls -la "$OUTPUT_DIR" | grep -E '\.(html)$' | while read -r line; do
            filename=$(echo "$line" | awk '{print $NF}')
            echo -e "${GREEN}   ✅ $filename${NC}"
        done
    fi
}

# Serve website locally
serve_website() {
    if [[ ! -d "$OUTPUT_DIR" ]]; then
        echo -e "${YELLOW}⚠️  No website found. Generating first...${NC}"
        generate_website
    fi

    echo -e "${CYAN}🌐 Starting local web server...${NC}"
    echo -e "${BLUE}📂 Serving from: $OUTPUT_DIR${NC}"

    # Try different Python HTTP servers
    cd "$OUTPUT_DIR"

    # Check if we're in a Python 3 environment
    if command -v python3 &> /dev/null; then
        SERVER_CMD="python3 -m http.server"
        PORT=8000
    elif command -v python &> /dev/null; then
        # Fallback to python (might be Python 2)
        python_version=$(python --version 2>&1)
        if [[ $python_version =~ Python\ 3 ]]; then
            SERVER_CMD="python -m http.server"
            PORT=8000
        else
            SERVER_CMD="python -m SimpleHTTPServer"
            PORT=8000
        fi
    else
        echo -e "${RED}❌ No Python found for serving${NC}"
        exit 1
    fi

    echo -e "${GREEN}🚀 Server starting...${NC}"
    echo -e "${PURPLE}🌍 Open in browser: ${YELLOW}http://localhost:$PORT${NC}"
    echo -e "${CYAN}💡 Press Ctrl+C to stop the server${NC}"
    echo ""

    # Start server
    $SERVER_CMD $PORT 2>/dev/null || {
        echo -e "${YELLOW}⚠️  Port $PORT might be in use, trying port 8080...${NC}"
        $SERVER_CMD 8080
    }
}

# Show usage
show_usage() {
    echo -e "${CYAN}Usage:${NC}"
    echo "  ./build.sh           Generate website from all manuals"
    echo "  ./build.sh serve     Generate and serve locally"
    echo "  ./build.sh clean     Clean output directory"
    echo "  ./build.sh help      Show this help message"
    echo ""
    echo -e "${CYAN}Examples:${NC}"
    echo "  ./build.sh           # Generate static website"
    echo "  ./build.sh serve     # Generate and view at http://localhost:8000"
    echo "  ./build.sh clean     # Remove all generated files"
}

# Main execution
main() {
    print_header

    case "${1:-}" in
        "clean")
            clean_output
            ;;
        "serve")
            check_dependencies
            generate_website
            serve_website
            ;;
        "help"|"-h"|"--help")
            show_usage
            ;;
        "")
            check_dependencies
            generate_website
            echo ""
            echo -e "${PURPLE}💡 Tip: Run './build.sh serve' to view the website locally${NC}"
            echo -e "${PURPLE}💡 Or open: $OUTPUT_DIR/index.html${NC}"
            ;;
        *)
            echo -e "${RED}❌ Unknown option: $1${NC}"
            echo ""
            show_usage
            exit 1
            ;;
    esac
}

# Make script executable and run
chmod +x "$0" 2>/dev/null || true
main "$@"