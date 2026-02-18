# Organizer MCP Server

An intelligent **Model Context Protocol (MCP)** server for organizing your computer files and folders automatically using AI. This server analyzes file content, identifies duplicates, suggests meaningful filenames, and helps organize files into logical folders.

## 🎯 What This MCP Does

The Organizer MCP provides **AI-powered intelligent file organization** with context awareness:

### Core Features

1. **Read File** - AI analyzes file content to understand context
   - Read and extract semantic meaning from files
   - Get full content for intelligent analysis
   - Automatic encoding detection for text files

2. **Understand Context** - AI extracts meaning and purpose
   - Analyze keywords and topics
   - Understand relationships between files
   - Identify file categories by actual content

3. **Suggest Organization** - Dynamic folder creation based on intelligence
   - AI creates folders based on CONTENT UNDERSTANDING, not templates
   - Examples: "Q4_Financial_Reports", "Vacation_Photos_2024", "Project_Alpha_Documents"
   - Smart grouping of related files
   - Meaningful folder hierarchies

4. **Organize Intelligently** - Execute AI's organization plan
   - Move files to AI-created categories
   - Create folder structures that make sense
   - No predefined patterns or rigid rules

5. **Find Duplicates** - Content-based duplicate detection
   - Identify exact duplicate files using hashing
   - Group identical files together
   - Calculate wasted disk space

6. **Suggest Filenames** - Context-aware naming suggestions
   - Extract key information from file content
   - Generate multiple meaningful options
   - Help rename generic files

7. **Create Junk Folder** - Safe quarantine for unwanted files
   - Move duplicates to a protected location
   - Review before permanent deletion

8. **Scan Folder** - Get complete folder intelligence
   - File statistics and composition
   - Identify files needing attention
   - Understand folder structure

## 📋 How It Works - Intelligent Context-Based Organization

The Organizer MCP enables **semantic understanding of files** by AI:

### The Intelligence Flow

1. **Scan** - AI gets overview using `scan_folder`
   - Identifies all files and their types
   - Detects generic filenames needing help

2. **Analyze Content** - AI reads and understands files with `read_file`
   - Extracts actual content, not just filenames
   - Understands purpose, context, and relationships
   - Groups related files mentally

3. **Extract Meaning** - AI creates intelligent categories
   - Analyzes keywords and themes
   - Understands file relationships
   - Creates smart folder names based on CONTENT (not templates!)

4. **Build Plan** - AI creates organization_map
   - Maps each file to a semantically appropriate folder
   - Examples:
     - "quarterly_report.pdf" + "revenue_analysis.xlsx" → "Financial_Reports"
     - "vacation_hawaii.jpg" + "beach_photos.jpg" → "Vacations/Hawaii_2024"
     - "auth_module.py" + "oauth_integration.py" → "Authentication_System"

5. **Execute** - AI calls `organize_folder` with its intelligent plan
   - Files move to AI-created categories
   - Folder structure reflects actual content organization

6. **Verify** - Check `REDIRECT.txt` showing all mappings

### Real-World Example

```
Before Organization:
Downloads/
  ├── Document1.pdf          (generic)
  ├── File2.xlsx             (generic)
  ├── Untitled.doc           (generic)
  ├── Photo_123.jpg
  ├── IMG_456.jpg
  ├── 2024-02-18_travel.jpg

AI Analysis:
  - Reads Document1.pdf → "Quarterly Sales Report"
  - Reads File2.xlsx → "Revenue Analysis Q4"
  - Reads Untitled.doc → "Product Requirements Document"
  - Images → "Trip to Costa Rica, 2024"

AI Creates Plan:
  Document1.pdf → Financial_Reports/
  File2.xlsx → Financial_Reports/
  Untitled.doc → Product_Documentation/
  Photo_123.jpg → Personal/Travel/Costa_Rica_2024/
  IMG_456.jpg → Personal/Travel/Costa_Rica_2024/
  2024-02-18_travel.jpg → Personal/Travel/Costa_Rica_2024/

After Organization:
Downloads/
  ├── Financial_Reports/
  │   ├── Document1.pdf (renamed: Quarterly_Sales_Report.pdf)
  │   └── File2.xlsx (renamed: Revenue_Analysis_Q4.xlsx)
  ├── Product_Documentation/
  │   └── Untitled.doc (renamed: Product_Requirements.doc)
  ├── Personal/Travel/Costa_Rica_2024/
  │   ├── Photo_123.jpg
  │   ├── IMG_456.jpg
  │   └── 2024-02-18_travel.jpg
  └── REDIRECT.txt (shows all changes)
```

### Key Principle

**NO RIGID TEMPLATES** - Folders are created based on what AI understands about your actual files. Each organization is unique and intelligent.

## 🚀 Installation

### Prerequisites

- **Python 3.11 or higher** (required for MCP support)
- **pip** or **uv** (Python package manager)
- **Git** (for cloning the repository)

### Steps

1. **Clone or extract the project**
   ```bash
   cd organizer-mcp-server
   ```

2. **Create a Python virtual environment** (recommended)
   ```bash
   # Using venv
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   
   # Or using uv (faster)
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   # Or with uv
   uv pip install -r requirements.txt
   ```

## ▶️ Running the Server

### What is MCP (Model Context Protocol)?

**MCP** is a protocol that enables AI models (like Claude) to use tools and access resources provided by a server. The Organizer MCP Server acts as a bridge between Claude and your file system, allowing Claude to:

- Read and analyze your files
- Understand their content and purpose
- Suggest intelligent file organization
- Execute file operations safely
- Find duplicates and organize folders

Think of MCP as a standardized way for AI to extend its capabilities beyond text generation.

### Quick Start - Direct Execution

```bash
# Direct Python execution
python main.py
```

The server will start and listen for incoming MCP requests via stdin/stdout.

### 🔍 Testing with MCP Inspector

The **MCP Inspector** is a built-in testing tool that lets you interact with your MCP server directly without needing Claude Desktop.

#### Installation & Setup

```bash
# Install globally (one time)
npm install -g @modelcontextprotocol/inspector

# Or use npx without installation (recommended)
npx @modelcontextprotocol/inspector
```

#### Using the Inspector

**Option 1: Simple approach**
```bash
# Terminal 1 - Start the server
python main.py

# Terminal 2 - Start the inspector (in another terminal, same directory)
npx @modelcontextprotocol/inspector python main.py
```

**Option 2: Direct approach (Inspector starts the server)**
```bash
# Single command - Inspector manages the server
npx @modelcontextprotocol/inspector python main.py
```

The Inspector opens a web interface where you can:
- ✅ View all available tools
- ✅ Test tools with parameters
- ✅ See request/response payloads
- ✅ Debug MCP communication
- ✅ Validate your server configuration

**Inspector Web UI Features:**
- **Resources Tab** - View all available resources
- **Tools Tab** - List and test all tools
- **Prompts Tab** - Test AI prompts
- **Messages Tab** - Raw MCP protocol messages
- **Test Tool** - Execute tools with custom parameters

### 📋 Step-by-Step: Using the Inspector

1. **Open two terminals** in the project directory

2. **Terminal 1 - Start the MCP Server:**
   ```bash
   python main.py
   ```
   You should see output indicating the server is running.

3. **Terminal 2 - Start the Inspector:**
   ```bash
   npx @modelcontextprotocol/inspector python main.py
   ```

4. **Open the Inspector Web UI:**
   - The terminal will display: `Inspector available at http://localhost:5173`
   - Open that URL in your browser
   - You'll see a web interface showing:
     - All 7 available tools
     - Tool descriptions and parameters
     - Input/output examples

5. **Test a Tool:**
   - Click on `scan_folder` in the Tools tab
   - Enter a valid folder path: `G:\practicode\test_organize` (or any folder)
   - Click "Execute"
   - See the response with folder statistics

### Running with Claude Desktop

1. **Locate your Claude Desktop configuration file:**
   - **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
   - **Linux**: `~/.config/Claude/claude_desktop_config.json`

2. **Add the Organizer MCP to your config:**
   ```json
   {
     "mcpServers": {
       "organizer": {
         "command": "python",
         "args": ["/absolute/path/to/organizer-mcp-server/main.py"]
       }
     }
   }
   ```

   On Windows, use forward slashes or escape backslashes:
   ```json
   {
     "mcpServers": {
       "organizer": {
         "command": "python",
         "args": ["C:/Users/YourName/path/to/organizer-mcp-server/main.py"]
       }
     }
   }
   ```

3. **Restart Claude Desktop** to enable the MCP

4. **Verify it's working** - You should see a hammer icon (🔨) in Claude, indicating available tools

## 🔄 Typical Workflow - Step by Step

Follow this workflow to organize any folder intelligently:

### Step 1: Scan the Folder
**Goal**: Get an overview of what you're working with

```bash
# Use scan_folder to understand the folder structure
Tool: scan_folder
Parameters:
  - folder_path: "G:/my_downloads"
  - include_hidden: false

# Returns:
# - Total files: 150
# - File types: PDF, JPEG, XLSX, etc.
# - Files with generic names: 23
# - Duplicate groups: 3
```

**What to do:**
- Check how many files need attention
- Look for generic filenames (Document1, Untitled, etc.)
- Note duplicate groups to clean up

### Step 2: Find Duplicates (Optional)
**Goal**: Identify wasted space from duplicate files

```bash
Tool: find_duplicates
Parameters:
  - folder_path: "G:/my_downloads"
  - include_hidden: false
  - min_size: 1024

# Returns duplicate groups with:
# - File hash (identical content)
# - File paths of duplicates
# - Total wasted space
```

**What to do:**
- Review duplicate groups
- Decide which copies to keep
- Use create_junk_folder to quarantine extras

### Step 3: Analyze Files with Generic Names
**Goal**: Understand what files need better names

```bash
Tool: read_file
Parameters:
  - file_path: "G:/my_downloads/Document1.pdf"
  - max_size: 50000

# Returns:
# - file_name: "Document1.pdf"
# - file_type: ".pdf"
# - content: (first 50000 bytes)
# - size: (file size)
```

**What to do:**
- Read files with generic names
- Understand their actual content
- Prepare to rename them meaningfully

### Step 4: Get Filename Suggestions
**Goal**: Generate better names based on content

```bash
Tool: suggest_filename
Parameters:
  - file_path: "G:/my_downloads/Document1.pdf"
  - max_content_size: 10000

# Returns:
# - current_name: "Document1.pdf"
# - suggested_names: [
#     "Q4_2024_Financial_Report.pdf",
#     "quarterly_report.pdf",
#     "report.pdf"
#   ]
# - analysis: "Content suggests Q4 financial report"
```

**What to do:**
- Review suggestions
- Choose the best option or use a custom name

### Step 5: Rename Files (Optional)
**Goal**: Give files meaningful names before organizing

```bash
Tool: rename_file
Parameters:
  - file_path: "G:/my_downloads/Document1.pdf"
  - new_name: "Q4_2024_Financial_Report.pdf"

# Returns:
# - old_path: "G:/my_downloads/Document1.pdf"
# - new_path: "G:/my_downloads/Q4_2024_Financial_Report.pdf"
```

**What to do:**
- Rename files one by one or in batches
- Use suggestions or custom names
- Verify each rename was successful

### Step 6: Build Organization Map
**Goal**: Create a plan for how to organize files

```
This is where YOU tell the AI what folders to create.

Example organization_map:
{
  "G:/my_downloads/Q4_Financial_Report.pdf": "Finance/2024_Reports",
  "G:/my_downloads/Revenue_Analysis.xlsx": "Finance/2024_Reports",
  "G:/my_downloads/Vacation_Photo1.jpg": "Personal/Photos/2024_Vacation",
  "G:/my_downloads/Invoice_123.pdf": "Finance/Invoices",
  "G:/my_downloads/Project_Brief.docx": "Projects/Project_Alpha"
}

Format: { "full_file_path": "destination_folder" }
```

**What to do:**
- Use insights from steps 1-5
- Map each file to a logical folder
- Create a clear folder hierarchy

### Step 7: Execute Organization
**Goal**: Move files to their new locations

```bash
Tool: organize_folder
Parameters:
  - folder_path: "G:/my_downloads"
  - organization_map: (from Step 6)
  - create_categories: true

# Returns:
# - files_moved: 45
# - folders_created: 8
# - redirect_file_path: "G:/my_downloads/REDIRECT.txt"
```

**What to do:**
- Execute the organization plan
- Check the REDIRECT.txt file for a complete log
- Verify all files moved to correct locations

### Step 8: Clean Up Duplicates (Optional)
**Goal**: Move duplicate files to junk folder for review

```bash
Tool: create_junk_folder
Parameters:
  - folder_path: "G:/my_downloads"
  - files_to_move: [
      "G:/my_downloads/duplicate_photo1.jpg",
      "G:/my_downloads/duplicate_photo2.jpg"
    ]
  - folder_name: "_junk"

# Returns:
# - junk_folder_path: "G:/my_downloads/_junk"
# - files_moved: 2
# - total_size_moved: 52428800
```

**What to do:**
- Move identified duplicates to _junk folder
- Review before permanent deletion
- Delete junk folder contents when confident

### Step 9: Verify Results
**Goal**: Confirm organization was successful

```bash
Tool: scan_folder (again)
Parameters:
  - folder_path: "G:/my_downloads"

# Compare with original scan:
# - Total files: same (not counting _junk)
# - Files with generic names: should be lower
# - Folder structure: should be organized
```

**What to do:**
- Run scan_folder again
- Verify file count (minus moved duplicates)
- Check new folder structure is as expected
- Look for any remaining generic filenames

## 📚 Available Tools

### `read_file`
Read and analyze a file's content and metadata.

**Parameters:**
- `file_path` (string): Absolute path to the file
- `max_size` (integer, default: 50000): Maximum bytes to read

**Returns:**
```python
{
  "file_name": "document.pdf",
  "file_path": "/full/path/document.pdf",
  "size": 2048576,
  "is_text": false,
  "file_type": ".pdf",
  "content": "Binary file - cannot display content",
  "truncated": false
}
```

### `rename_file`
Rename a file to a more meaningful name.

**Parameters:**
- `file_path` (string): Absolute path to the file
- `new_name` (string): New filename with extension

**Returns:**
```python
{
  "old_name": "Document1.pdf",
  "new_name": "Q4_Financial_Report.pdf",
  "old_path": "/path/Document1.pdf",
  "new_path": "/path/Q4_Financial_Report.pdf"
}
```

### `find_duplicates`
Find duplicate files based on content hash.

**Parameters:**
- `folder_path` (string): Root folder to scan
- `include_hidden` (boolean, default: false): Include hidden files
- `min_size` (integer, default: 1024): Minimum file size in bytes

**Returns:**
```python
{
  "total_files": 150,
  "duplicate_groups": [
    {
      "file_hash": "a1b2c3d4...",
      "file_size": 1048576,
      "file_count": 3,
      "file_paths": ["/path/file1.jpg", "/path/file2.jpg", "/path/file3.jpg"]
    }
  ],
  "total_duplicate_files": 5,
  "total_wasted_space": 5242880
}
```

### `suggest_filename`
Generate intelligent filename suggestions based on content.

**Parameters:**
- `file_path` (string): Path to the file
- `max_content_size` (integer, default: 10000): Maximum bytes to analyze

**Returns:**
```python
{
  "current_name": "Untitled1.txt",
  "suggested_names": [
    "Project_Charter_2024.txt",
    "project_charter.txt",
    "charter.txt"
  ],
  "analysis": "Content-based suggestion from first line and keywords",
  "confidence": 0.75
}
```

### `organize_folder`
Organize files into categories based on a provided map.

**Parameters:**
- `folder_path` (string): Root folder to organize
- `organization_map` (object): Mapping of file paths to category folders
- `create_categories` (boolean, default: true): Auto-create folders

**Example organization_map:**
```python
{
  "/path/file1.pdf": "Documents",
  "/path/file2.jpg": "Images",
  "/path/file3.mp3": "Music"
}
```

**Returns:**
```python
{
  "folder_path": "/path",
  "files_moved": 3,
  "folders_created": 3,
  "changes": [
    {
      "file_path": "/path/file1.pdf",
      "new_location": "Documents",
      "status": "moved",
      "message": "Moved to Documents/"
    }
  ],
  "redirect_file_path": "/path/REDIRECT.txt",
  "summary": "Organized 3 files into 3 categories"
}
```

### `create_junk_folder`
Create a junk folder and move unwanted files into it.

**Parameters:**
- `folder_path` (string): Root folder where junk folder is created
- `files_to_move` (array): List of file paths to move
- `folder_name` (string, default: "_junk"): Junk folder name

**Returns:**
```python
{
  "junk_folder_path": "/path/_junk",
  "files_moved": 5,
  "total_size_moved": 52428800
}
```

### `scan_folder`
Get complete analysis of a folder structure.

**Parameters:**
- `folder_path` (string): Folder to analyze
- `include_hidden` (boolean, default: false): Include hidden files

**Returns:**
```python
{
  "total_files": 250,
  "total_folders": 45,
  "total_size": 1073741824,
  "file_types": [
    {"extension": ".pdf", "count": 45, "total_size": 524288000},
    {"extension": ".jpg", "count": 120, "total_size": 314572800}
  ],
  "duplicate_groups": 3,
  "files_with_generic_names": 23,
  "text_files": 85,
  "binary_files": 165,
  "hidden_files": 2
}
```

## ⚙️ Configuration

### Environment Variables

Create a `.env` file in the project root (optional):

```env
# Log level (DEBUG, INFO, WARNING, ERROR)
LOG_LEVEL=INFO

# Maximum file size to read (bytes)
MAX_FILE_READ_SIZE=50000

# Minimum file size for duplicate detection (bytes)
MIN_DUPLICATE_SIZE=1024

# File extensions to treat as text
TEXT_EXTENSIONS=.txt,.md,.py,.json,.yaml,.csv
```

## 🧪 Testing

```bash
# Install test dependencies
pip install pytest pytest-asyncio

# Run tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=. -v
```

## 🔒 Security Considerations

### Safe Operations

- ✅ Files are never deleted, only moved to `_junk` folder
- ✅ Cannot navigate outside the root folder (path traversal protection)
- ✅ Invalid filenames are automatically sanitized
- ✅ Existing files are never overwritten (automatic renaming on conflicts)
- ✅ All operations are logged for audit trail

### Best Practices

1. **Always backup** before organizing large directories
2. **Review** the generated `REDIRECT.txt` before automation
3. **Start small** - test on a single folder first
4. **Check junk folder** before permanent deletion
5. **Monitor logs** for any issues

## 📖 MCP Protocol Compliance

This server fully implements the Model Context Protocol (MCP) specification:

✅ **Proper Tool Definitions** - All tools follow MCP schema requirements
✅ **Input Validation** - All inputs validated using Pydantic models
✅ **Error Handling** - Comprehensive error codes and messages
✅ **Async Support** - All operations support async/await
✅ **STDIO Transport** - Proper stdio server implementation
✅ **Tool Descriptions** - Detailed descriptions for AI understanding

Reference: [MCP Documentation](https://modelcontextprotocol.io/docs/develop/build-server)

## 🐛 Troubleshooting

### "Permission Denied" Errors

**Solution**: Run with appropriate permissions or use folders you own.

```bash
# On macOS/Linux
sudo chmod -R u+rw /path/to/folder

# On Windows
# Right-click folder → Properties → Security → Edit permissions
```

### "File Not Found" on Windows Paths

**Solution**: Use forward slashes or escape backslashes:
```python
# Good
"/Users/name/Downloads"
"C:/Users/name/Downloads"
"C:\\Users\\name\\Downloads"  # Escaped

# Bad
"C:\Users\name\Downloads"  # Unescaped
```

### MCP Not Showing in Claude Desktop

**Solution**: 
1. Verify the path in config is absolute
2. Test the server directly: `python main.py`
3. Check Claude logs in `~/Library/Logs/Claude/`
4. Restart Claude Desktop

### Encoding Errors When Reading Files

**Solution**: The server automatically tries UTF-8, Latin-1, and CP1252. Files with unusual encodings may need manual handling.

## 🛠️ Development

### Project Structure

```
organizer-mcp-server/
├── main.py                      # MCP server entry point
├── pyproject.toml               # Project configuration
├── requirements.txt             # Dependencies
├── models/                      # Data models
│   ├── result.py               # Response models
│   └── organizer_models.py     # Input validation models
├── services/                    # Business logic
│   ├── organizer_service.py    # File analysis & organization
│   └── file_operations_service.py  # File operations
├── utils/                       # Utilities
│   ├── file_utils.py           # File handling
│   ├── errors.py               # Error classes
│   └── validate.py             # Input validation
├── tests/                       # Test suite
├── DEVELOPMENT.md              # Development guide
└── README.md                   # This file
```

### Code Quality

```bash
# Format code
black .

# Lint
pylint main.py models/ services/ utils/

# Type checking
mypy main.py --strict
```

## 📝 License

MIT License - Feel free to use in your projects

## 🤝 Contributing

Contributions welcome! Areas for improvement:

- [ ] Additional file type detection
- [ ] Machine learning-based categorization
- [ ] Integration with cloud storage
- [ ] Batch processing optimization
- [ ] Additional file metadata extraction

## 📞 Support

For issues or questions:

1. Check [DEVELOPMENT.md](DEVELOPMENT.md) for detailed guides
2. Review error messages in logs
3. Test with a small folder first
4. Check existing files/issues

---

**Happy Organizing!** 🎉

Made with ❤️ for AI-powered file management
