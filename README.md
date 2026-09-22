# SMS Spam Detection System

![v0.2.1 Coming Soon](https://img.shields.io/badge/🚧_Coming_Soon-v0.2.1-blue?style=for-the-badge)

A production-grade, end-to-end machine learning application designed to classify SMS messages as spam or ham (legitimate). This project utilizes a **decoupled architecture**, separating the machine learning inference engine from the user interface to ensure high performance, scalability, and clean separation of concerns.

### 🔗 Project Resources
* **Live Application:** [https://spam-detection-azien.streamlit.app](https://spam-detection-azien.streamlit.app)
* **Backend API Documentation:** [https://spam-detection-api-cpzy.onrender.com/docs](https://spam-detection-api-cpzy.onrender.com/docs)

---

## 📸 Interface Preview

![Application Demo](assets/demo.png)

---

## 🏗️ System Architecture

The project is architected as a distributed web system, hosted across two cloud platforms to simulate a real-world production environment:

* **Inference Engine (Backend):** A RESTful API built with **FastAPI** and deployed on **Render**. It handles the core logic, text preprocessing, and serves a **Multinomial Naive Bayes** model.
* **User Interface (Frontend):** A reactive web dashboard developed with **Streamlit** and deployed on **Streamlit Cloud**. It communicates with the backend via secure HTTP POST requests.

---

## 🧪 Tech Stack

| Component | Technologies Used |
| :--- | :--- |
| **Machine Learning** | Python, Scikit-Learn, Pandas, Joblib |
| **API Development** | FastAPI, Uvicorn, Pydantic |
| **Web Interface** | Streamlit, Requests |
| **Cloud & DevOps** | Render, Streamlit Cloud, Git/GitHub |

---

## ⚙️ Key Features

* **Real-time Classification:** High-speed inference providing immediate results upon user input.
* **Probability-Based Confidence:** Displays the model's mathematical certainty for every prediction.
* **Risk Analysis (Explainable AI):** Identifies and highlights specific keywords that triggered the spam classification.
* **Asynchronous Communication:** The UI remains responsive while handling API requests and responses from the backend.

---

## 📊 Methodology & Pipeline

1.  **Text Normalization:** Input data is converted to lowercase and cleared of non-alphanumeric noise to ensure consistency.
2.  **Vectorization:** The system employs **TF-IDF (Term Frequency-Inverse Document Frequency)** to transform raw text into high-dimensional numerical vectors.
3.  **Probabilistic Modeling:** A Naive Bayes classifier calculates the statistical likelihood of the "Spam" class based on trained word distributions.
4.  **Data Exchange:** The API transmits structured JSON data containing the prediction, probability score, and risk factors back to the client interface.

---

## 🚀 Local Development

### Prerequisites
* Python 3.9 or higher
* Git installed on your system

### Installation & Setup
1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/mdhukka/spam-detection-ml-system.git](https://github.com/mdhukka/spam-detection-ml-system.git)
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd spam-detection-ml-system
    ```
3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### Execution
1.  **Start the Backend API:**
    ```bash
    uvicorn main:app --reload
    ```
2.  **Start the Frontend UI (in a separate terminal):**
    ```bash
    streamlit run app.pyS
    ```

---

## 🛠️ Roadmap & Future Enhancements

**🔜 Coming in v0.2.1:**
* [ ] **Performance Optimizations:** Backend tuning to deliver even faster inference and API response times.
* [ ] **UI/UX Overhaul:** A redesigned, modern interface for a smoother and more intuitive user experience.
* [ ] **Deeper Semantic Understanding:** Upgrading the NLP pipeline for more accurate, nuanced spam detection and deeper risk analysis.

---

**Developed by Azien** | *Focused on building scalable, data-driven solutions.*
