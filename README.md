# CHATBOT_RAG
This code implements a Chatbot with Streamlit that acts as a virtual assistant for the company DATABiQ, being able to process PDF documents through a RAG technique (Retrieval Augmented Generation) to answer questions based on its knowledge base.

![Logo](https://images.contentstack.io/v3/assets/bltefdd0b53724fa2ce/blt1496b19e4c6f9e66/66ba412a46b3f4241b969f48/rag-in-action.jpeg)

## This code implements a Chatbot with Streamlit that acts as a virtual assistant for the company DATABiQ, being able to process PDF documents through a RAG technique (Retrieval Augmented Generation) to answer questions based on its knowledge base.

## Features

- **Set Up the Application:** Configure the Streamlit app with a title, layout, and initial sidebar state. Add a logo at the top left using HTML and CSS.
- **Load and Display Image:** Implement a file uploader for users to upload images. Load and display the uploaded image in a format usable by OpenCV.
- **Face Identification and Analysis:** Compare the uploaded image with images in a specified directory using DeepFace to identify faces. Perform facial analysis to detect age, gender, race, and emotion, and display the results.
- **User Interface and Results Visualization:** Design a user-friendly interface with centered text and headers. Display the analysis results, including drawing rectangles around detected faces and showing detailed information.
- **Footer with Developer Info:** Add a footer with the developer’s contact information and social media icons.

## Technologies used

- **Streamlit:** Used to create the web application interface, handle user interactions, and display results.
- **OpenCV:** Utilized for image processing tasks, such as loading, converting, and displaying images.
- **DeepFace:** Employed for facial recognition and analysis, including identifying faces and detecting age, gender, race, and emotions.
- **NumPy:** Used for handling arrays and converting image data for processing with OpenCV.
- **os:** Utilized for file and directory operations, such as checking if a directory exists and iterating through files.
- **HTML and CSS:** Used to enhance the visual presentation of the app, including adding a logo and styling text.
- **st_social_media_links:** A Streamlit component used to add social media icons and links to the footer of the app.

## **Documentation**
! https://omes-va.com/reconocimiento-facial-python-opencv/
! https://www.youtube.com/watch?v=CPZvEgxKoJk
