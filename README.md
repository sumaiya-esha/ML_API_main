# ML_API_main

An API code to fetch data from ThingSpeak storage environment and pass it into the respective ML model.

In the API program, the ML model is loaded at first. After the user requests on the web interface homepage for the prediction of symptoms, the API goes into the ‘predict’ route and ‘post’ method. Next, the API requests the measured steady data from ThingSpeak which ThingSpeak provides. Then, the fetched data are inputted into the ML model. The ML model predicts the nature of symptoms and sends the prediction state to the API. The API sends the output from the ML model to the web interface in order to publish. The user can then know the nature of symptoms according to the measured vital data from that user.
