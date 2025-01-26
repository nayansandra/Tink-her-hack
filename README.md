
 Memora
Description:  
An innovative web application designed to manage and share photos of college events. Students can upload event photos, search by event name, date, or location, and access an organized gallery of memories.

Key Features:  
 EventBased Photo Categorization: Photos are organized by event names for easy retrieval.  
 Event Timeline View: A timeline to browse events chronologically.  
 MultiUser Upload Credits: Tracks who uploaded each photo.  
 Search Functionality: Keywordbased search for events by name, date, or location.  
 Secure User Authentication: Log in using secure authentication methods.  
 Photo Upload with Tagging: Users can upload and tag photos with relevant event details.  
 Responsive Design: Works seamlessly on mobile and desktop devices.  

Technologies Used:  
 Frontend & Backend: Django  
 Database: PostgreSQL for metadata, Firebase for photo storage  
 Cloud Storage: AWS S3 or Firebase for hosting images  

Target Users:  
 Students  
 Event organizers  
 College administrators  

Team Name: homies to techies
Team Members  
 Member 1: Devika Saji  
 Member 2: NayanSandra M  

 Hosted Project Link
https://tink-her-hack-sopg.vercel.app/
 Project Description  
The project is a webbased platform designed to manage and share photos from college events. It enables students, event organizers, and faculty members to upload, organize, and access eventrelated photos effortlessly. The platform allows users to search for photos by event name, date, or location and view them in a categorized gallery. With secure user authentication, a responsive design, and advanced search functionality, the app creates a central hub for preserving and sharing campus memories.
 Problem Statement  
In many colleges, photos captured during events are often scattered across personal devices, social media platforms, or remain inaccessible to the majority of students and faculty. This fragmentation leads to lost memories, difficulty in retrieving eventspecific photos, and a lack of a centralized repository for media assets.  
Challenges include:  
 Lack of centralized storage for event photos.  
 Inability to search for event photos by specific attributes like event name, date, or location.  
 Limited accessibility to photos for students who didn't capture or receive them directly.  
 Difficulty in sharing photos across the student community.

 Solution  
The proposed solution is a web application that acts as a centralized photo repository for all college events.  

Key features of the solution include:  
1. Centralized Photo Storage: A secure platform where all eventrelated photos are uploaded and stored in one place.  
2. EventBased Categorization: Photos are tagged and categorized by event name, date, and location for easy access.  
3. Search Functionality: Advanced keyword search allows users to find photos using event names, dates, or locations.  
4. Event Timeline View: A visual timeline displays events in chronological order, making it easy to explore past events.  
5. MultiUser Uploads: Students and organizers can upload their photos, ensuring comprehensive coverage of events.  
6. Secure User Access: Only authorized users can access or upload photos, ensuring privacy and safety.  
7. Responsive Design: Works seamlessly across devices, ensuring easy access for everyone.  

By addressing these challenges, the platform ensures that all students and faculty have equal access to event photos, fostering a sense of community and preserving campus memories in an organized and accessible way.
 Technical Details
 Technologies/Components Used
 For Software:
 Languages used: Python, JavaScript
 Frameworks used: Django, Bootstrap
 Libraries used: Pyrebase (for Firebase integration), jQuery
 Tools used: Visual Studio Code
  
 Tools required:
   Web browser (Chrome, Firefox)

 Implementation
 For Software:
 Installation
To set up the project locally, use the following commands:

```bash
git clone https://github.com/yourusername/photodashboard.git
cd photodashboard
python m venv env
source env/bin/activate   On Windows use: env\Scripts\activate
pip install r requirements.txt
```

 Run
To start the development server:

```bash
python manage.py runserver
```

 Project Documentation

 For Software:

 Screenshots 
 ![Screenshot 2025-01-26 092003](https://github.com/user-attachments/assets/535fb18c-9009-4105-be20-52acca79faeb)

 
This shows the homepage of the Photo Dashboard where users can see all their uploaded events.

 ![Screenshot 2025-01-26 092024](https://github.com/user-attachments/assets/a516b978-cc2c-4fb1-8dff-e6ba51bb3a9b)

 Displays all available photos of the selected event. 

![Screenshot 2025-01-26 092039](https://github.com/user-attachments/assets/b1e2752f-1368-4c54-99af-2276557814ac)

This screenshot displays the upload form where users can drag and drop files or select them manually.

 
 
 Diagrams
Workflow 
This diagram illustrates the workflow of the application from photo upload to retrieval.
[Start] 
   ↓
[User Accesses Upload Page]
   ↓
[User Inputs Event Name]
   ↓
[User Selects File]
   ↓
[File Validation] -- No --> [Show Error Message]
   ↓
Yes
   ↓
[File Upload to Firebase Storage]
   ↓
[Save Metadata]
   ↓
[Success Response]
   ↓
[User Views Uploaded Photos]
   ↓
[User Can Retrieve Photos]
   ↓
[End]
 Project Demo
 

https://www.loom.com/share/f6e373ade2ce465b978660e664d9ebbd?sid=0a4b8418-2e34-48d2-98a0-b76929fd4db0
 

This video demonstrates how to upload photos, manage them, and utilize tags effectively.

 Additional Demos
https://github.com/tinkerhub/tink-her-hack-3-temp.git

Made with ❤️ at TinkerHub



