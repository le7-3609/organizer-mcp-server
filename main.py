"""
Organizer MCP Server - Intelligent file organization using Model Context Protocol.

This MCP server provides tools for analyzing and organizing computer files and folders.
It can scan directory trees, identify duplicates, suggest meaningful filenames,
and automatically organize files into logical folders based on content analysis.
"""

from __future__ import annotations

import asyncio
from pathlib import Path
from typing import Optional, Dict, List
from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv

from services.organizer_service import OrganizerService
from services.file_operations_service import FileOperationsService
from models.organizer_models import (
    OrganizeIn, ReadFileIn, RenameFileIn, FindDuplicatesIn,
    SuggestNamesIn, CreateJunkFolderIn
)
from models.result import ToolResult, ErrorInfo
from utils import errors
from utils.validate import validate_folder_path, validate_file_path

# Load environment variables
load_dotenv()

# Initialize MCP server
mcp = FastMCP("organizer-mcp-server")

# Initialize services
organizer_service = OrganizerService()
file_ops_service = FileOperationsService()


@mcp.tool(description="""
Read and analyze a file's content and metadata.

Use when:
- You need to examine file content to decide on a new name
- You want to understand what a file contains before organizing it
- You need file information to detect duplicates

Inputs:
- file_path: Absolute path to the file to read
- max_size: Maximum bytes to read (default: 50000)

Returns (ToolResult):
- ok=true: data contains file_name, file_path, content, size, is_text, file_type
- ok=false: error with details about what went wrong
""")
async def read_file(file_path: str, max_size: int = 50000) -> dict:
    """Read a file and return its metadata and content."""
    try:
        _ = ReadFileIn(file_path=file_path, max_size=max_size)
        res = await asyncio.to_thread(file_ops_service.read_file, file_path, max_size)
        return res.model_dump()
    except Exception as e:
        return ToolResult(
            ok=False,
            error=ErrorInfo(code="read_error", message=str(e))
        ).model_dump()


@mcp.tool(description="""
Rename a file to a more meaningful name.

Use when:
- A file has a generic name (like 'Document1.pdf' or 'unnamed.txt')
- You've analyzed the content and want to give it a descriptive name
- You want to standardize naming conventions

Inputs:
- file_path: Absolute path to the file to rename
- new_name: New filename (must include extension)

Returns (ToolResult):
- ok=true: data contains old_name, new_name, old_path, new_path
- ok=false: error with details about what went wrong
""")
async def rename_file(file_path: str, new_name: str) -> dict:
    """Rename a file to a new name."""
    try:
        _ = RenameFileIn(file_path=file_path, new_name=new_name)
        res = await asyncio.to_thread(file_ops_service.rename_file, file_path, new_name)
        return res.model_dump()
    except Exception as e:
        return ToolResult(
            ok=False,
            error=ErrorInfo(code="rename_error", message=str(e))
        ).model_dump()


@mcp.tool(description="""
Organize files in a folder by creating categories and moving files.

Use when:
- You want to automatically organize a folder structure
- You've analyzed files and have a plan for how to organize them
- You want to create a logical folder structure

Inputs:
- folder_path: Absolute path to the root folder to organize
- organization_map: Dictionary mapping file paths to folder names (e.g., {'/path/file.txt': 'Documents'})
- create_categories: Whether to auto-create category folders (default: true)

Returns (ToolResult):
- ok=true: data contains summary, files_moved, folders_created, redirect_file_path
- ok=false: error with details about what went wrong

Note: A Redirect.txt file is always created showing all changes made.
""")
async def organize_folder(
    folder_path: str,
    organization_map: Optional[Dict[str, str]] = None,
    create_categories: bool = True
) -> dict:
    """Organize files in a folder based on provided organization map."""
    try:
        _ = OrganizeIn(folder_path=folder_path)
        res = await asyncio.to_thread(
            organizer_service.organize_files,
            folder_path,
            organization_map,
            create_categories
        )
        return res.model_dump()
    except Exception as e:
        return ToolResult(
            ok=False,
            error=ErrorInfo(code="organize_error", message=str(e))
        ).model_dump()


@mcp.tool(description="""
Find duplicate files in a folder based on content hash.

Use when:
- You want to identify duplicate files to clean up disk space
- You need to know which files are identical before deleting
- You want to consolidate duplicate files

Inputs:
- folder_path: Absolute path to the root folder to scan
- include_hidden: Whether to include hidden files (default: false)
- min_size: Minimum file size in bytes to check (default: 1024)

Returns (ToolResult):
- ok=true: data contains duplicate_groups list with paths and hashes
- ok=false: error with details about what went wrong

Each duplicate group shows all identical files found together.
""")
async def find_duplicates(
    folder_path: str,
    include_hidden: bool = False,
    min_size: int = 1024
) -> dict:
    """Find duplicate files in a folder."""
    try:
        _ = FindDuplicatesIn(folder_path=folder_path, include_hidden=include_hidden)
        res = await asyncio.to_thread(
            organizer_service.find_duplicates,
            folder_path,
            include_hidden,
            min_size
        )
        return res.model_dump()
    except Exception as e:
        return ToolResult(
            ok=False,
            error=ErrorInfo(code="duplicate_error", message=str(e))
        ).model_dump()


@mcp.tool(description="""
Suggest meaningful names for files based on their content.

Use when:
- Files have generic names like 'Document1.pdf' or 'NewFile.txt'
- You want to auto-suggest descriptive names based on file content
- You need help deciding what to rename files to

Inputs:
- file_path: Absolute path to the file
- max_content_size: Maximum bytes of content to analyze (default: 10000)

Returns (ToolResult):
- ok=true: data contains current_name, suggested_names (list of options), analysis
- ok=false: error with details about what went wrong
""")
async def suggest_filename(file_path: str, max_content_size: int = 10000) -> dict:
    """Suggest meaningful filenames based on content analysis."""
    try:
        _ = SuggestNamesIn(file_path=file_path)
        res = await asyncio.to_thread(
            organizer_service.suggest_filename,
            file_path,
            max_content_size
        )
        return res.model_dump()
    except Exception as e:
        return ToolResult(
            ok=False,
            error=ErrorInfo(code="suggest_error", message=str(e))
        ).model_dump()


@mcp.tool(description="""
Create a 'junk' folder and move duplicate/unwanted files into it.

Use when:
- You've identified duplicate or unwanted files
- You want to quarantine files before deletion
- You want to review files before permanent removal

Inputs:
- folder_path: Absolute path where the junk folder should be created
- files_to_move: List of absolute file paths to move into junk folder
- folder_name: Name for the junk folder (default: '_junk')

Returns (ToolResult):
- ok=true: data contains junk_folder_path, files_moved, total_size_moved
- ok=false: error with details about what went wrong

The junk folder is created in the root of the specified folder_path.
""")
async def create_junk_folder(
    folder_path: str,
    files_to_move: List[str],
    folder_name: str = "_junk"
) -> dict:
    """Create a junk folder and move files into it."""
    try:
        _ = CreateJunkFolderIn(folder_path=folder_path, files_to_move=files_to_move)
        res = await asyncio.to_thread(
            file_ops_service.create_junk_folder,
            folder_path,
            files_to_move,
            folder_name
        )
        return res.model_dump()
    except Exception as e:
        return ToolResult(
            ok=False,
            error=ErrorInfo(code="junk_error", message=str(e))
        ).model_dump()


@mcp.tool(description="""
Scan a folder and get a complete analysis report.

Use when:
- You want a full overview of a folder's contents
- You need statistics about file types, sizes, and organization
- You want to understand the folder structure before organizing

Inputs:
- folder_path: Absolute path to the folder to analyze
- include_hidden: Whether to include hidden files (default: false)

Returns (ToolResult):
- ok=true: data contains total_files, file_types, duplicates, generic_names, statistics
- ok=false: error with details about what went wrong
""")
async def scan_folder(folder_path: str, include_hidden: bool = False) -> dict:
    """Scan and analyze a folder structure."""
    try:
        res = await asyncio.to_thread(
            organizer_service.scan_folder,
            folder_path,
            include_hidden
        )
        return res.model_dump()
    except Exception as e:
        return ToolResult(
            ok=False,
            error=ErrorInfo(code="scan_error", message=str(e))
        ).model_dump()


def main():
    """Run the MCP server."""
    mcp.run()


if __name__ == "__main__":
    main()
