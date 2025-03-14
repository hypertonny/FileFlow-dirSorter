# 🗂️ FileFlow - Intelligent File Organizer

![FileFlow Banner](https://img.shields.io/badge/FileFlow-Organize%20Your%20Digital%20Life-blue?style=for-the-badge)
[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/yourusername/FileFlow/graphs/commit-activity)


![FileFlow Logo](https://v3.fal.media/files/koala/x6ue9jmYEvKjQ-wcUuW9D.png)

## 📋 Overview

FileFlow is an intelligent file organization tool that brings order to your digital chaos. With just a few keystrokes, transform cluttered directories into a neatly categorized file system. FileFlow automatically sorts files based on their types into appropriate folders, saving you hours of manual organization.

## ✨ Features

- **🤖 Intelligent Categorization**: Automatically sorts files based on file extensions
- **🎮 Interactive CLI**: User-friendly command-line interface with clear prompts
- **🎯 Customizable Destinations**: Choose source and destination directories
- **🛡️ Comprehensive Error Handling**: Gracefully manages permissions, duplicates, and more
- **📊 Detailed Logging**: Keeps track of all operations with both console and file logs
- **📈 Organization Statistics**: Get a summary of categorized files after completion
- **🔄 Duplicate Protection**: Smart handling of filename conflicts

## 🗂️ File Categories

FileFlow organizes your files into the following categories:

| Category | File Types |
|----------|------------|
| 🎵 Music | .mp3, .wav, .flac, .aac, .ogg, .wma, .m4a |
| 💻 Code | .py, .java, .html, .css, .js, .cpp, .c, .php, .go, .rb, .ts |
| 🖼️ Images | .jpg, .jpeg, .png, .gif, .bmp, .svg, .webp, .tiff |
| 🎬 Videos | .mp4, .avi, .mov, .mkv, .wmv, .flv, .webm, .m4v |
| 🗜️ Zip | .zip, .rar, .7z, .tar, .gz, .bz2, .xz |
| 📄 Documents | .txt, .docx, .doc, .pdf, .ppt, .pptx, .xlsx, .xls, .csv, .odt, .rtf, .md |
| 📁 Others | Any uncategorized files |

## 🚀 Installation

```bash
# Clone the repository
git clone https://github.dev/hypertonny/FileFlow-dirSorter.git

# Navigate to the project directory
cd FileFlow-dirSorter

# Run the script
python File_Organizer.py
```

## 💡 Usage

```bash
python File_Organizer.py
```

Follow the interactive prompts:
1. Enter the source directory path (or press Enter for current directory)
2. Enter the destination directory path (or press Enter to use source directory)
3. Confirm the operation
4. Watch as FileFlow organizes your files!

## 📋 Example

```
=== FILE ORGANIZER ===
This tool will organize files into categories based on file extensions.

Enter the directory path to organize (press Enter for current directory): ~/Downloads
Enter destination directory (press Enter to use source directory): 

Organizing files from: /home/user/Downloads
Destination directory: /home/user/Downloads

Continue with organizing files? (y/n): y

[INFO] Folder created/verified: /home/user/Downloads/Music
[INFO] Folder created/verified: /home/user/Downloads/Code
[INFO] Folder created/verified: /home/user/Downloads/Images
[INFO] Folder created/verified: /home/user/Downloads/Videos
[INFO] Folder created/verified: /home/user/Downloads/Zip
[INFO] Folder created/verified: /home/user/Downloads/Documents
[INFO] Folder created/verified: /home/user/Downloads/Others
[INFO] Moved: document.pdf -> Documents/
[INFO] Moved: presentation.pptx -> Documents/
[INFO] Moved: image.jpg -> Images/
[INFO] Moved: song.mp3 -> Music/
...

=== Organization Complete ===
Music: 5 files
Code: 2 files
Images: 12 files
Videos: 3 files
Zip: 1 files
Documents: 7 files
Others: 2 files

File organization complete! Check file_organizer.log for details.
```

## 🛠️ Requirements

- Python 3.6+
- Standard libraries (os, shutil, sys, pathlib, logging)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔮 Future Enhancements

- [ ] Recursive directory scanning
- [ ] GUI interface for easier interaction
- [ ] Option to copy instead of move files
- [ ] Custom category definitions via config file
- [ ] File preview functionality
- [ ] Undo last organization operation
- [ ] Advanced filtering options

## 🙏 Acknowledgements

- Inspired by the need for digital organization in a cluttered world
- Built with love and coffee ☕

---

<p align="center">
  Made with ❤️ by <a href="https://github.com/hypertonny">Rahul Purohit | hypertonny | BNH </a>
</p>