# SlideShare Content Extraction Strategy

## Research Summary

### What We've Discovered

**SlideShare Technical Details:**
- Content hosted on `image.slidesharecdn.com` CDN
- Individual slides available as JPEG images
- URL pattern: `https://image.slidesharecdn.com/[presentation-id]/95/slide-[number]-1024.jpg`
- Higher resolution available: `-2048.jpg` suffix
- Page is JavaScript-rendered (React-based frontend)

**Existing Tools & Libraries:**
1. **Python-based scrapers** (BeautifulSoup + Requests)
   - Parses `<picture data-testid="slide-image-picture">` elements
   - Extracts `srcset` attributes for image URLs
   - **Challenge:** Requires JavaScript execution for modern SlideShare

2. **Selenium-based scrapers** (Browser automation)
   - Full browser rendering for JavaScript content
   - Can scroll through presentation and capture images
   - More resource-intensive but more reliable

3. **JSON oEmbed approach** (Older method)
   - Some presentations expose metadata via JSON
   - May not work on modern SlideShare interface

**OCR Options for Text Extraction:**
- **Tesseract OCR** (pytesseract): Most popular, 100+ languages
- **EasyOCR**: Deep learning-based, 80+ languages, better accuracy
- Both support Portuguese text recognition

## Recommended Automated Approach

### Option 1: Selenium + Image Download + OCR (Most Reliable)

**Pros:**
- Handles JavaScript-rendered content
- Can navigate through slides programmatically
- Proven approach from multiple GitHub projects

**Cons:**
- Requires browser driver (ChromeDriver/GeckoDriver)
- Slower than direct HTTP requests
- More dependencies

**Implementation:**
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
from PIL import Image
import pytesseract

def extract_slideshare_text(url):
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(3)  # Wait for JS to load

    # Find all slide images
    pictures = driver.find_elements(By.CSS_SELECTOR, 'picture[data-testid="slide-image-picture"]')

    text_content = []
    for i, pic in enumerate(pictures):
        source = pic.find_element(By.TAG_NAME, 'source')
        srcset = source.get_attribute('srcset')
        # Extract highest resolution URL
        urls = srcset.split(',')
        high_res_url = urls[-1].split()[0]

        # Download image
        img_response = requests.get(high_res_url)
        img = Image.open(io.BytesIO(img_response.content))

        # OCR extraction
        text = pytesseract.image_to_string(img, lang='por')
        text_content.append(f"## Slide {i+1}\n\n{text}\n")

    driver.quit()
    return '\n'.join(text_content)
```

**Dependencies:**
```bash
pip install selenium pillow pytesseract
brew install tesseract tesseract-lang  # For Portuguese
```

### Option 2: Direct Image URL Pattern + OCR (Faster if we know slide count)

**Pros:**
- No browser automation needed
- Faster execution
- Simpler code

**Cons:**
- Need to know total slide count beforehand
- URL pattern may vary per presentation
- May miss slides if numbering isn't sequential

**Implementation:**
```python
import requests
from PIL import Image
import pytesseract
import io

def extract_by_pattern(presentation_id, total_slides, base_url):
    text_content = []

    for i in range(1, total_slides + 1):
        img_url = f"{base_url}/95/slide-{i}-1024.jpg"
        try:
            response = requests.get(img_url)
            if response.status_code == 200:
                img = Image.open(io.BytesIO(response.content))
                text = pytesseract.image_to_string(img, lang='por')
                text_content.append(f"## Slide {i}\n\n{text}\n")
        except Exception as e:
            print(f"Failed to process slide {i}: {e}")

    return '\n'.join(text_content)
```

### Option 3: Hybrid - Use Claude to Extract from Screenshots

**Pros:**
- Claude can read images directly
- No OCR library needed
- Better context understanding than OCR
- Can extract structured information

**Cons:**
- Still need to get slide images (Selenium or manual)
- Token usage for image processing
- Need to process each slide

**Implementation:**
```python
# After downloading slide images with Selenium
def extract_with_claude(image_path):
    # Read image and pass to Claude via Read tool
    # Claude extracts structured text content
    pass
```

## Practical Workflow for Our Use Case

### Step 1: Inventory All PowerPoint URLs
Create a list of all SlideShare presentations we need:
- Geografia 8º ano: Chapters 6-10 (5 presentations)
- História: Crises XIV (1 presentation)

### Step 2: Choose Extraction Method Based on Volume
**For 6 presentations (estimated ~100-150 total slides):**

**Recommended: Selenium + Claude Image Reading**
1. Use Selenium to navigate to each presentation
2. Save high-resolution slide images
3. Use Claude's Read tool to extract text from each image
4. Format extracted content into markdown

**Why this approach:**
- We already have Claude available
- No OCR setup needed
- Better text extraction quality
- Can handle mixed content (text + diagrams)
- Only 100-150 slides total (manageable)

### Step 3: Automation Script

```python
# slideshare_extractor.py
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

def download_presentation_slides(url, output_dir):
    """Download all slides from a SlideShare presentation"""
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(5)

    # Find slide images
    pictures = driver.find_elements(By.CSS_SELECTOR, 'img[class*="slide"]')

    os.makedirs(output_dir, exist_ok=True)

    for i, img in enumerate(pictures):
        src = img.get_attribute('src')
        if 'slidesharecdn.com' in src:
            # Download image
            response = requests.get(src)
            with open(f"{output_dir}/slide_{i+1:03d}.jpg", 'wb') as f:
                f.write(response.content)

    driver.quit()
    return len(pictures)

# Usage
presentations = {
    'recursos_naturais': 'https://pt.slideshare.net/diogomateus174/os-recursos-naturais-62582508',
    'agricultura': '...',
    'industria': '...',
    # ... more presentations
}

for name, url in presentations.items():
    print(f"Downloading {name}...")
    slide_count = download_presentation_slides(url, f'slides/{name}')
    print(f"Downloaded {slide_count} slides")
```

### Step 4: Content Extraction with Claude
After downloading images, use Task agent or direct Read tool to:
1. Read each slide image
2. Extract all text content
3. Identify structure (headings, bullet points, etc.)
4. Format into markdown matching pipeline expectations

## BREAKTHROUGH: Third-Party Download Services (RECOMMENDED!)

**Discovery:** Multiple free online tools exist (like YouTube downloaders for SlideShare)

### Available Services (2024-2025):
- **SlideSaver.app** - Download as PDF, PPTX, or ZIP (JPEG images)
- **SlidesDownloader.co** - PDF and PPT formats
- **SlideGrabber.com** - PDF, PPT, PPTX formats
- **GetMyPPT.com** - PowerPoint and PDF formats
- **MyDocDownloader.com** - PPT, PDF, image files

### Key Features:
- ✅ No login/registration required
- ✅ Unlimited free downloads
- ✅ No watermarks
- ✅ Original quality preserved
- ✅ Multiple format options
- ⚠️ One presentation at a time (must repeat for each)

### Best Strategy for Our Use Case:

**Download as PDF from third-party service, then:**

**Option A: Use Claude to Extract from PDF (SIMPLEST!)**
1. Download each presentation as PDF using third-party service
2. Use Claude's Read tool (supports PDF) to extract text
3. Format extracted content into markdown
4. No OCR needed, no coding required!

**Option B: Download as PPTX + python-pptx**
1. Get original PowerPoint file
2. Use python-pptx library to extract text programmatically
3. No OCR needed if text is selectable

**Option C: Download as ZIP (JPEG images) + Claude**
1. Get slide images as JPEG files
2. Use Claude's Read tool on each image
3. Extract and format content

### Time Estimate with Third-Party Tools:
- Download 6 presentations manually: ~15 minutes
- Extract text with Claude from PDFs: 1-2 hours
- Format into pipeline markdown: 1 hour
- **Total: ~3 hours** (vs. 4+ hours with Selenium)

## Alternative: Manual Verification Approach

Since we only have ~6 presentations:
1. **Try third-party download as PDF first** - Simplest approach!
2. **Check if ChatGPT content is accurate** - Compare 1-2 slides manually
3. **If ChatGPT content is good enough** - Keep it and just verify accuracy
4. **If not** - Use PDF extraction with Claude for all

## UPDATED Recommendation for This Project

**Recommended Workflow:**
1. ✅ Use third-party downloader (SlideSaver.app or similar)
2. ✅ Download all 6 presentations as PDF
3. ✅ Use Claude Read tool to extract text from PDFs
4. ✅ Format extracted content into pipeline-compatible markdown
5. ✅ Review and clean up extracted content

**Time estimate:**
- Download all PDFs manually: ~15 minutes
- Claude PDF extraction + formatting: 2-3 hours
- Total: ~3 hours (no coding, no setup, no dependencies!)

**Next action:** Test one presentation download and extraction?
