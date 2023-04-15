
# HealthInspect
HealthInspect is a web-based application that allows users to upload images of skin conditions and receive accurate, reliable information about their condition in just seconds. The uploaded image is processed through a powerful Vertex AI model, which uses deep learning algorithms and advanced image recognition techniques to analyze the image and identify any signs of disease.

# Objective
The objective of HealthInspect is to provide users with a user-friendly, accessible tool for self-diagnosing skin conditions. With HealthInspect, users can take images of their skin diseases from the comfort of their own home using just their smartphone camera and receive accurate, reliable information about their condition in just seconds. This information is presented in a clear, easy-to-understand format that anyone can follow, making it an ideal solution for individuals who may not have immediate access to a healthcare provider.

# Methodology and Results
HealthInspect is built on a Google Cloud Platform, which is a powerful, scalable platform for building web applications. The application uses a deep learning model trained on the dermnet dataset from Kaggle to identify 21 different classes of skin diseases with an accuracy of 77.7%.

The web application is built using Flask, a Python web framework. The application is deployed on a compute engine instance in Google Cloud that runs on AMD EPYC Milan platform with a t2d type machine. The web app is deployed using mod apache2 with WSGI used to connect the Flask app to the external IP of the VM. The site is accessible via the external IP.

The front-end of the application is built using JavaScript, HTML, CSS, and Bootstrap for designing. The website also handles compression on large images to ensure quick and smooth processing.

# Instructions
To use HealthInspect, simply go to the following website address: http://34.131.86.88/. On the homepage, users can upload an image of the affected area on our super lightweight and user-friendly platform. The uploaded image is then processed through our powerful Vertex AI model, which is deployed on the Google Cloud platform. Once the diagnosis is displayed, our system provides a description of the symptoms, causes, and possible home remedies for the identified disease.

For more information on how to use HealthInspect, please watch the demo video on our website.

# Conclusion
HealthInspect is a revolutionary tool for self-diagnosing skin conditions. With its powerful deep learning algorithms and user-friendly interface, anyone can use it to get accurate, reliable information about their skin condition in just seconds. We believe that HealthInspect has the potential to make a significant impact in the field of healthcare and we are excited to see its potential grow in the future.
