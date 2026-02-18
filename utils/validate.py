"""Validation utilities."""

from pathlib import Path
from utils.errors import FolderAccessError, FileAccessError, ValidationError
import os


def validate_folder_path(folder_path: str) -> Path:
    """
    Validate that a folder path is accessible and is a directory.
    
    Args:
        folder_path: Path to validate
        
    Returns:
        Path object
        
    Raises:
        FolderAccessError: If path is invalid or not a directory
    """
    path = Path(folder_path).expanduser().absolute()

    if not path.exists():
        raise FolderAccessError(f"Folder does not exist: {folder_path}")

    if not path.is_dir():
        raise FolderAccessError(f"Path is not a directory: {folder_path}")

    # Check if readable
    if not os.access(path, os.R_OK):
        raise FolderAccessError(f"Folder is not readable: {folder_path}")

    return path


def validate_file_path(file_path: str) -> Path:
    """
    Validate that a file path exists and is a file.
    
    Args:
        file_path: Path to validate
        
    Returns:
        Path object
        
    Raises:
        FileAccessError: If path is invalid or not a file
    """
    path = Path(file_path).expanduser().absolute()

    if not path.exists():
        raise FileAccessError(f"File does not exist: {file_path}")

    if not path.is_file():
        raise FileAccessError(f"Path is not a file: {file_path}")

    return path


def validate_filename(filename: str) -> str:
    """
    Validate that a filename is safe.
    
    Args:
        filename: Filename to validate
        
    Returns:
        Validated filename
        
    Raises:
        ValidationError: If filename is invalid
    """
    if not filename or len(filename) == 0:
        raise ValidationError("Filename cannot be empty")

    # Check for path separators
    if "/" in filename or "\\" in filename or ".." in filename:
        raise ValidationError("Filename cannot contain path separators")

    # Check for invalid characters (Windows)
    invalid_chars = '<>:"|?*'
    if any(char in filename for char in invalid_chars):
        raise ValidationError(f"Filename contains invalid characters: {invalid_chars}")

    # Check length
    if len(filename) > 255:
        raise ValidationError("Filename is too long (max 255 characters)")

    return filename
