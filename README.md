
# HealthInspect
HealthInspect is a web-based application that allows users to upload images of diseases and receive accurate, reliable information about their condition in just seconds. The uploaded image is processed through a powerful Ai model, which uses deep learning algorithms and advanced image recognition techniques to analyze the image and identify any signs of disease.

# Objective
The objective of HealthInspect is to provide users with a user-friendly, accessible tool for self-diagnosing skin conditions. With HealthInspect, users can take images of their skin diseases from the comfort of their own home using just their smartphone camera and receive accurate, reliable information about their condition in just seconds. This information is presented in a clear, easy-to-understand format that anyone can follow, making it an ideal solution 24/7 or for individuals who may not have immediate access to a healthcare provider.

# Methodology and Results
HealthInspect is built on a Google Cloud Platform, which is a powerful, scalable platform for building web applications. The application uses a Vertex Ai Model deployed on an endpoint, trained on the dermnet dataset stored in a Cloud Storage Bucket.<br><br>
Classifying skin diseases is a complicated task in medicine due to the similarities between different diseases.<br><br>
Our model identifies 21 different classes of skin diseases with an average accuracy of 77.7%, which is the highest number of classes a model has been accurately trained on according to various research papers, providing a large coverage of common types.

The web application is built using Flask, a Python web framework. The application is deployed on a compute engine instance in Google Cloud that runs on AMD EPYC Milan platform with a t2d type machine. The web app is deployed using mod apache2 with WSGI used to connect the Flask app to the external IP of the VM. The site is accessible via the external IP.<br><br>
The front-end of the application is built using JavaScript, HTML, CSS, and Bootstrap for designing. The website also handles compression on large images to ensure quick and smooth processing.

# Instructions
To use HealthInspect, simply go to the following website: [HealthInspect](http://34.131.86.88/).<br>
On the homepage, users can upload an image of the affected area on our super lightweight and user-friendly platform. The uploaded image is then processed through our powerful Vertex AI model, which is deployed on the Google Cloud platform. Once the diagnosis is displayed, our system provides a description of the symptoms, causes, and possible home remedies for the identified disease.<br><br>

For more information on how to use HealthInspect, please watch: [demovideo](https://drive.google.com/file/d/1Cr7YgfLb548d1vDmk5BNjzpCjQo6k1ls/view?usp=share_link/)

# Conclusion
We are confident that HealthInspect will continue to have a positive impact on the lives of people around the world. The application is hosted on the Google Cloud Platform, which ensures its reliability and scalability. Furthermore, our mobile-friendly and blazingly fast interface, makes it easy for anyone to use the application, regardless of their technical expertise. We had the opportunity to present this to Dr. M.S. Narula from Chandigarh, and this was what he had to say: [testimony](https://drive.google.com/file/d/1Lx8OLG0jyWXLrOKIuwWSLcG70_Tva8Qz/view?usp=share_link).<br>
We believe that HealthInspect has the potential to become a valuable tool in the fight against skin diseases and more, and we are excited to continue to develop and improve and exand the application in the future.
