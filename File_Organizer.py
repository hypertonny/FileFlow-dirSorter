import os
import shutil
import logging

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("file_organizer.log"),
        logging.StreamHandler()
    ]
)

class FileOrganizer:
    def __init__(self):
        # Define file extensions for each category
        self.categories = {
            'Music': ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma', '.m4a'],
            'Code': ['.py', '.java', '.html', '.css', '.js', '.cpp', '.c', '.php', '.go', '.rb', '.ts'],
            'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp', '.tiff'],
            'Videos': ['.mp4', '.avi', '.mov', '.mkv', '.wmv', '.flv', '.webm', '.m4v'],
            'Zip': ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2', '.xz'],
            'Documents': ['.txt', '.docx', '.doc', '.pdf', '.ppt', '.pptx', '.xlsx', '.xls', '.csv', 
                         '.odt', '.rtf', '.md']
        }
        
        # Add 'Others' category for uncategorized files
        self.categories['Others'] = []
    
    def get_user_input(self):
        """Get source and destination directories from user input"""
        try:
            print("\n=== FILE ORGANIZER | GUTHUB - hypertonny | TG - @bnh_02 ===")
            print("This tool will organize files into categories based on file extensions.\n")
            
            source_dir = input("Enter the directory path to organize (press Enter for current directory): ").strip()
            if not source_dir:
                source_dir = os.getcwd()
            
            if not os.path.exists(source_dir):
                logging.error(f"Source directory '{source_dir}' does not exist.")
                return None, None
            
            if not os.path.isdir(source_dir):
                logging.error(f"'{source_dir}' is not a directory.")
                return None, None
            
            dest_dir = input("Enter destination directory (press Enter to use source directory): ").strip()
            if not dest_dir:
                dest_dir = source_dir
            
            if not os.path.exists(dest_dir):
                create = input(f"Destination directory '{dest_dir}' does not exist. Create it? (y/n): ")
                if create.lower() == 'y':
                    try:
                        os.makedirs(dest_dir, exist_ok=True)
                    except Exception as e:
                        logging.error(f"Failed to create destination directory: {str(e)}")
                        return None, None
                else:
                    logging.info("Operation canceled by user.")
                    return None, None
            
            return source_dir, dest_dir
        except KeyboardInterrupt:
            logging.info("\nOperation canceled by user.")
            return None, None
        except Exception as e:
            logging.error(f"Error getting user input: {str(e)}")
            return None, None

    def create_category_folders(self, dest_dir):
        """Create category folders in the destination directory"""
        try:
            for category in self.categories:
                category_path = os.path.join(dest_dir, category)
                os.makedirs(category_path, exist_ok=True)
                logging.info(f"Folder created/verified: {category_path}")
        except Exception as e:
            logging.error(f"Error creating category folders: {str(e)}")
            return False
        return True

    def get_category(self, file_extension):
        """Determine the category based on file extension"""
        file_extension = file_extension.lower()
        for category, extensions in self.categories.items():
            if file_extension in extensions:
                return category
        return "Others"  # Default category for uncategorized files

    def organize_files(self, source_dir, dest_dir):
        """Organize files from source directory to destination directory"""
        try:
            if not self.create_category_folders(dest_dir):
                return
            
            # Get all files in the source directory (non-recursive)
            files = [f for f in os.listdir(source_dir) 
                    if os.path.isfile(os.path.join(source_dir, f))]
            
            if not files:
                logging.info(f"No files found in {source_dir}")
                return
            
            # Counter for statistics
            stats = {category: 0 for category in self.categories}
            skipped = 0
            
            # Process each file
            for file_name in files:
                try:
                    source_path = os.path.join(source_dir, file_name)
                    
                    # Skip the log file itself if it's in the same directory
                    if file_name == "file_organizer.log" and os.path.samefile(
                            os.path.dirname(source_path), os.path.dirname(os.path.abspath("file_organizer.log"))):
                        skipped += 1
                        continue
                    
                    # Get file extension and determine category
                    _, file_extension = os.path.splitext(file_name)
                    category = self.get_category(file_extension)
                    
                    # Create destination path
                    dest_path = os.path.join(dest_dir, category, file_name)
                    
                    # Handle file name collision
                    counter = 1
                    while os.path.exists(dest_path):
                        name, ext = os.path.splitext(file_name)
                        new_name = f"{name}_{counter}{ext}"
                        dest_path = os.path.join(dest_dir, category, new_name)
                        counter += 1
                    
                    # Move the file
                    shutil.move(source_path, dest_path)
                    stats[category] += 1
                    logging.info(f"Moved: {file_name} -> {category}/")
                    
                except PermissionError:
                    logging.error(f"Permission denied for file: {file_name}")
                    skipped += 1
                except Exception as e:
                    logging.error(f"Error processing file {file_name}: {str(e)}")
                    skipped += 1
            
            # Display statistics
            print("\n=== Organization Complete ===")
            for category, count in stats.items():
                if count > 0:
                    print(f"{category}: {count} files")
            if skipped > 0:
                print(f"Skipped: {skipped} files (check log for details)")
                
        except Exception as e:
            logging.error(f"Error during organization process: {str(e)}")

    def run(self):
        """Run the file organizer"""
        try:
            print("\nWelcome to File Organizer!")
            source_dir, dest_dir = self.get_user_input()
            
            if source_dir and dest_dir:
                print(f"\nOrganizing files from: {source_dir}")
                print(f"Destination directory: {dest_dir}\n")
                
                confirm = input("Continue with organizing files? (y/n): ")
                if confirm.lower() == 'y':
                    self.organize_files(source_dir, dest_dir)
                    print("\nFile organization complete! Check file_organizer.log for details.")
                else:
                    print("Operation canceled by user.")
        except KeyboardInterrupt:
            print("\nOperation canceled by user.")
        except Exception as e:
            logging.error(f"Unexpected error: {str(e)}")
            print(f"An unexpected error occurred. Check file_organizer.log for details.")

if __name__ == "__main__":
    organizer = FileOrganizer()
    organizer.run()
