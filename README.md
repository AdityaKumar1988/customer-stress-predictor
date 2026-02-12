<h1 align="center">🤖 AI Customer Support Intelligence Dashboard</h1>

<p align="center">
Real-time prediction of customer resolution time and customer abandonment risk using Machine Learning.
</p>

<p align="center">
🌐 <b>Live Demo:</b><br>
<a href="https://customer-stress-predictor-aditya-kumar-jha.streamlit.app/" target="_blank">
https://customer-stress-predictor-aditya-kumar-jha.streamlit.app/
</a>
</p>

<hr>

<h2>📌 Project Overview</h2>

<p>
This project is an AI-powered web application designed to predict:
</p>

<ul>
<li>⏳ Estimated Resolution Time (Regression)</li>
<li>⚠️ Customer Abandonment Probability (Classification)</li>
<li>📊 Risk Category (Safe / High Risk)</li>
</ul>

<p>
The system uses a <b>dual Random Forest architecture</b> to provide real-time decision intelligence for customer support operations.
</p>

<hr>

<h2>🖥 Application Preview</h2>

<p align="center">
<img src="dashboard-preview.png" width="90%">
</p>

<hr>

<h2>🚨 High Risk Example</h2>

<p align="center">
<img src="high-risk-example.png" width="90%">
</p>

<hr>

<h2>🧠 Model Architecture</h2>

<ul>
<li>🌳 Random Forest Regressor → Predicts resolution time</li>
<li>🌳 Random Forest Classifier → Predicts abandonment probability</li>
<li>🏷 Feature Encoding using LabelEncoder</li>
<li>📦 Serialized Models (.pkl) for efficient inference</li>
</ul>

<hr>

<h2>📊 Model Performance</h2>

<h3>🔹 Regression Metrics</h3>

<p align="center">
<img src="model-metrics.png" width="80%">
</p>

<ul>
<li>Mean Absolute Error (MAE)</li>
<li>Root Mean Squared Error (RMSE)</li>
</ul>

<h3>🔹 Confusion Matrix</h3>

<p align="center">
<img src="confusion-matrix.png" width="70%">
</p>

<h3>🔹 Feature Importance</h3>

<h4>Classification Model</h4>
<p align="center">
<img src="feature-importance-classification.png" width="70%">
</p>

<h4>Regression Model</h4>
<p align="center">
<img src="feature-importance-regression.png" width="70%">
</p>

<hr>

<h2>🚀 Key Features</h2>

<ul>
<li>🎯 Dual ML Models (Regression + Classification)</li>
<li>📈 Real-time Abandonment Probability Gauge</li>
<li>🧠 Risk Categorization (Safe / High Risk)</li>
<li>⚡ Instant Inference from Serialized Models</li>
<li>🎨 Modern Dark-Themed Interactive Dashboard</li>
<li>🌐 Public Cloud Deployment</li>
</ul>

<hr>

<h2>🛠 Tech Stack</h2>

<ul>
<li><b>Machine Learning:</b> Scikit-learn, Pandas, NumPy</li>
<li><b>Frontend:</b> Streamlit</li>
<li><b>Visualization:</b> Plotly</li>
<li><b>Deployment:</b> Streamlit Cloud</li>
</ul>

<hr>

<h2>⚙️ Run Locally</h2>

<pre>
git clone https://github.com/AdityaKumar1988/customer-stress-predictor.git
cd customer-stress-predictor
pip install -r requirements.txt
streamlit run app.py
</pre>

<hr>

<h2>📁 Project Structure</h2>

<pre>
customer-stress-predictor/
│
├── app.py
├── reg_model.pkl
├── clf_model.pkl
├── encoder_priority.pkl
├── encoder_channel.pkl
├── requirements.txt
├── dashboard-preview.png
├── high-risk-example.png
├── confusion-matrix.png
├── feature-importance-classification.png
├── feature-importance-regression.png
├── model-metrics.png
└── README.md
</pre>

<hr>

<h2>🔮 Future Improvements</h2>

<ul>
<li>🔍 SHAP Model Explainability</li>
<li>📊 ROC Curve Visualization</li>
<li>🌍 REST API Integration (FastAPI)</li>
<li>🐳 Docker Deployment</li>
</ul>

<hr>

<h2>👨‍💻 Author</h2>

<p>
<b>Aditya Kumar Jha</b><br>
🔗 <a href="https://www.linkedin.com/in/aditya-kumar-jha-13661828a/">LinkedIn</a><br>
💻 <a href="https://github.com/AdityaKumar1988">GitHub</a><br>
🌐 <a href="https://aditya-portfolio-website-woad.vercel.app/">Portfolio</a>
</p>
