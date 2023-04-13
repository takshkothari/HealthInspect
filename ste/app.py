from flask import Flask, render_template, request,redirect, url_for
import base64
from google.cloud import aiplatform
from google.cloud.aiplatform.gapic.schema import predict
app=Flask(__name__)
@app.route('/',methods=['GET'])
def hello_world():
    print("hello")
    return render_template('index.html')

@app.route('/index.html',methods=['GET'])
def hell_world():
    print("hell")
    return render_template('index.html')

@app.route('/about.html',methods=['GET'])
def helo_world():
    print("helo")
    return render_template('about.html')

@app.route('/contact.html',methods=['GET'])
def heltlo_world():
    print("heltlo")
    return render_template('contact.html')

@app.route('/product.html',methods=['GET'])
def helleo_world():
    print("helleo")
    return render_template('product.html')

@app.route('/results.html',methods=['GET'])
def hellwo_world():
    print("hellwo")
    return render_template('results.html')

@app.route('/results.html',methods=['POST'])
def predict_image_classification_sample(
    project="738477523269",
    endpoint_id="5132357550737457152",
    location="us-central1",
    api_endpoint= "us-central1-aiplatform.googleapis.com"):
    filename=request.files["fileipt"].read()
    # The AI Platform services require regional API endpoints.
    client_options = {"api_endpoint": api_endpoint}
    # Initialize client that will be used to create and send requests.
    # This client only needs to be created once, and can be reused for multiple requests.
    print("connecting client..")
    client = aiplatform.gapic.PredictionServiceClient(client_options=client_options)
    print("connected")
    #with open(filename, "rb") as f:
       #file_content = f.read()

    # The format of each instance should conform to the deployed model's prediction input schema.
    encoded_content = base64.b64encode(filename).decode("utf-8")
    instance = predict.instance.ImageClassificationPredictionInstance(
        content=encoded_content,
    ).to_value()
    instances = [instance]
    # See gs://google-cloud-aiplatform/schema/predict/params/image_classification_1.0.0.yaml for the format of the parameters.
    parameters = predict.params.ImageClassificationPredictionParams(
        confidence_threshold=0.1, max_predictions=5,
    ).to_value()
    endpoint = client.endpoint_path(
        project=project, location=location, endpoint=endpoint_id
    )
    response = client.predict(
        endpoint=endpoint, instances=instances, parameters=parameters
    )
    print("response")
    print(" deployed_model_id:", response.deployed_model_id)
    # See gs://google-cloud-aiplatform/schema/predict/prediction/image_classification_1.0.0.yaml for the format of the predictions.
    predictions = response.predictions
    #for prediction in predictions:
        #print(" prediction:", dict(prediction))
    pred=dict(predictions[0]);
    return render_template('results.html',value=pred)
print("starting..")

if __name__=='__main__':
    app.run(port=3000,debug=True)

#[C:\Users\bhamb\AppData\Roaming\gcloud\application_default_credentials.json]