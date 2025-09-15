# DreamNode: OMSN Teaching Manual

A comprehensive teaching manual and resource collection for creative mathematics education in alternative learning environments.

## Project Overview

This DreamNode serves as the development space for a teaching manual designed to guide David's role as a teaching assistant at an alternative school. The focus is on transforming traditional mathematics education (grades 5-9) through visual metaphors, creative projects, and integrated learning approaches.

### Core Mission
- **Visual Mathematics**: Creating visual metaphors and intuitive explanations for mathematical concepts
- **Project Integration**: Connecting mathematical learning to hands-on creative projects
- **Spiral Curriculum**: Touching on all subjects quickly, then deepening through repeated exposure
- **Bilingual Support**: Operating in Portuguese/English environment with universal mathematical language

### Teaching Philosophy
- Start with core intuitions and visual understanding
- Show real-world applications and future possibilities
- Balance engaging creativity with necessary academic requirements
- Emphasize problem-solving and dynamic thinking over rote memorization

## Structure & Approach

### Teaching Schedule
- **Primary Days**: Tuesday and Wednesday (2 hours each)
- **Preparation**: Flexible scheduling for lesson planning and material creation
- **Support Tasks**: Additional time for 3D printing, technical fixes, and video creation

### Curriculum Coverage (Grades 5-9)
- **Mathematics Core**: Algebra, geometry, fractions, equations, problem-solving
- **Future Integration**: Physics and chemistry concepts for grade 7+
- **Visual Materials**: Posters, presentations, and interactive demonstrations
- **Project Resources**: Hands-on activities connecting math to real-world applications

### Collaboration Framework
- **Primary Teacher**: Danielle (handles main instruction and exercises)
- **David's Role**: Visual presentations, conceptual explanations, specialized math support
- **Student Consultation**: Available for project-specific mathematical questions
- **Manual Development**: Creating organized reference materials for student consultation

### Student-Centered Design
- **Current Students**: Maria, Pietro, Victor, Julia, Suri (mixed experience levels)
- **Learning Styles**: Accommodating both creative and traditional learning preferences
- **Portfolio Requirements**: Balancing bureaucratic needs with engaging content
- **Trust-Based Approach**: Honest communication about necessary but boring tasks

## Development Phases

### Phase 1: Foundation (Current)
- Extract and organize math curriculum requirements from official programs
- Create subject checklist for systematic coverage tracking
- Develop initial visual teaching materials and presentations

### Phase 2: Implementation
- Begin teaching sessions with integrated visual approach
- Test project-based learning connections with mathematical concepts
- Refine teaching methods based on student engagement and feedback

### Phase 3: Expansion
- Create comprehensive consultation manual for student reference
- Develop video content for fundraising and documentation
- Integrate physics/chemistry concepts for advanced students

### Phase 4: Documentation & Sharing
- Document successful teaching approaches and materials
- Create replicable framework for alternative mathematics education
- Contribute to broader educational innovation community

## Official Curriculum References

### Portuguese Education System Requirements (Grades 5-9)

**Mathematics Curriculum**
- **Source**: [Aprendizagens Essenciais de Matemática](https://www.dge.mec.pt/noticias/aprendizagens-essenciais-de-matematica)
- **Coverage**: Complete mathematics requirements for 5th-9th grade
- **Purpose**: Ensures alignment with official Portuguese mathematics education standards

**Natural Sciences (Chemistry & Physics)**
- **Source**: [Metas Curriculares - Ciências Físico-Químicas](https://www.dge.mec.pt/sites/default/files/ficheiros/eb_cfq_metas_curriculares_3c_0.pdf)
- **Coverage**: Chemistry and physics topics for grades 5-9 (clustered as "natural sciences" in Portuguese system)
- **Purpose**: Official curriculum goals for physical and chemical sciences education

**Exercise Resources**
- **Source**: [O Bichinho do Saber](https://www.obichinhodosaber.com/)
- **Purpose**: Official exam preparation exercises across all topics
- **Strategy**: Use proven exercises rather than creating from scratch to ensure students can pass required exams

## 📖 Available Manuals

This repository contains comprehensive teaching manuals organized thematically:

### Mathematics Manual (Grades 5-9)
- **File**: `Unified_Mathematics_Manual_Grade5-9.md`
- **Content**: Complete Portuguese mathematics curriculum organized by themes
- **Features**: Progression matrices, visual teaching suggestions, assessment frameworks
- **Format**: Thematic organization (Numbers & Operations, Algebra & Patterns, Data & Probability, Geometry & Measurement)

### Individual Grade Summaries
- `Grade_5_Math_Curriculum_Summary.md` through `Grade_9_Math_Curriculum_Summary.md`
- **Purpose**: Detailed grade-specific learning objectives and key skills
- **Source**: Official Portuguese mathematics curriculum (Aprendizagens Essenciais)

## 🌐 Website Presentation System

### **Dynamic Manual Presentation**

This repository includes a **zero-maintenance website generator** that automatically converts any markdown manual into a beautiful, interactive website.

### Quick Start
```bash
# Generate beautiful website from all manuals
cd website
./build.sh

# Generate and serve locally at http://localhost:8000
./build.sh serve

# Clean all generated files
./build.sh clean
```

### Features
- **🔄 Fully Automatic**: Discovers any `*Manual*.md` files and converts them
- **📱 Responsive Design**: Works perfectly on desktop, tablet, and mobile
- **🎨 Modern Interface**: Clean, educational aesthetic with dark/light themes
- **🧭 Smart Navigation**: Auto-generated table of contents with progress tracking
- **🔍 Search**: Real-time search within documents
- **📊 Interactive Elements**: Collapsible sections, copy buttons, visual markers
- **📄 Print-Ready**: Optimized CSS for physical handouts
- **⚡ Zero Dependencies**: Pure HTML/CSS/JavaScript output

### How It Works
1. **Automatic Discovery**: Scans for markdown files containing "Manual" in the name
2. **Content Processing**: Converts markdown to enhanced HTML with navigation
3. **Theme Enhancement**: Adds visual markers for teaching elements (📊 📚 🔗)
4. **Website Generation**: Creates index page + individual manual pages
5. **Serve Locally**: Optional local web server for immediate viewing

### Future-Proof Design
- ✅ **Content Agnostic**: Works with any markdown manual structure
- ✅ **No Maintenance**: Add new manuals, run `./build.sh` - done!
- ✅ **Scalable**: Handles unlimited number of manuals
- ✅ **Portable**: Static HTML works anywhere (GitHub Pages, local server, etc.)

### Directory Structure
```
website/
├── generator.py      # Main conversion script
├── template.html     # Beautiful HTML template
├── build.sh         # One-click build script
└── output/          # Generated website files
    ├── index.html   # Manual collection page
    └── *.html       # Individual manual pages
```

### Adding New Manuals

The system automatically works with any new manual you create:

1. **Create your manual**: Write your content in markdown format
2. **Use "Manual" in filename**: e.g., `Chemistry_Teaching_Manual.md`, `Physics_Manual_Grade7-8.md`
3. **Build website**: Run `./build.sh` and your new manual appears automatically
4. **No configuration needed**: The system discovers and processes all manuals

**Example for Chemistry/Physics:**
```bash
# Create your new manual
echo "# Chemistry Teaching Manual\nYour content here..." > Chemistry_Teaching_Manual.md

# Generate website (automatically includes new manual)
cd website
./build.sh

# Your chemistry manual is now available at:
# website/output/chemistry_teaching_manual.html
```

### Customization

The system is designed to work out-of-the-box, but you can customize:
- **Template styling**: Edit `website/template.html` to modify appearance
- **Processing logic**: Edit `website/generator.py` to change conversion behavior
- **File discovery**: System looks for `*Manual*.md` and `*manual*.md` patterns

## Resources & Tools

- **Visual Creation**: 3D printing, animations, interactive demonstrations
- **Curriculum References**: Official Portuguese education programs (grades 5-9) - see links above
- **Project Integration**: Hands-on activities connecting math to real applications
- **Assessment**: Portfolio-based evaluation balancing creativity with requirements
- **Website System**: Dynamic presentation pipeline for beautiful manual display

## License

This DreamNode is shared under the **GNU Affero General Public License v3.0** - a strong copyleft license ensuring this knowledge remains free and open for all.

## InterBrain Connection

Part of the **InterBrain** ecosystem: applying collective knowledge gardening principles to educational innovation and creative teaching methodologies.