📁 Django File Explorer Application
This project is a simple Django-based file explorer application that allows users to manage files and folders within the system.

🔧 Features

📄 Upload files

📥 Download files

✏️ Edit file content

🗑️ Delete files

📂 Create folders

📋 Copy files

📦 Move files

📁 List files inside folders




🚀 Installation & Run
1. Clone the repository
   
   git clone https://github.com/your-username/file_explorer.git
   cd file_explorer

2. Create a Virtual Environment (optional but recommended)
   
    python -m venv venv
    venv\Scripts\activate  # On Windows
    source venv/bin/activate  # On macOS/Linux

3. Install Dependencies
   
    pip install django

4. Apply Migrations
   
    python manage.py migrate

5. Run the Development Server
    
    python manage.py runserver 8010

Visit the app in your browser at:

👉 http://127.0.0.1:8010


🗂️ Project Structure

📁 explorer/models.py

Defines the File model containing file name, type, and content.

📁 explorer/forms.py

Includes forms for file upload, edit, folder creation, and move actions.

📁 explorer/views.py

Handles all core logic:
list_files, upload_file, edit_file, delete_file, download_file, create_folder, copy_file, move_file, etc.

📁 explorer/urls.py

Maps URLs to their respective views.
