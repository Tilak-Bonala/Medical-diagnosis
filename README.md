# 🧠 Medical Image Diagnosis Assistant
An AI-powered assistant that analyzes medical images to help identify possible diseases, suggest diagnoses, and recommend next steps — all through a user-friendly Streamlit interface. Powered by **Google's Gemini Vision API**.

<img width="443" alt="image" src="https://github.com/user-attachments/assets/b5e45bef-5644-46e1-8148-86ce08e2db9d" />



---

## 🚀 Features

- 🖼️ Upload medical images (X-ray, MRI, CT, etc.)
- 🤖 AI-assisted diagnosis using Google Gemini models
- 📄 Structured medical analysis based on clinical prompts
- ⚠️ Highlight of potential red-flag findings
- 📝 Downloadable report (optional)
- 🔒 HIPAA-friendly design with disclaimers
- 🌍 Multilingual support (optional)

---

## 🏗️ Tech Stack

| Tool         | Purpose                      |
|--------------|------------------------------|
| Python       | Core backend logic            |
| Streamlit    | Frontend UI framework         |
| Gemini 1.5   | Vision & language model       |
| Pillow       | Image handling                |
| Google Generative AI SDK | Gemini API integration |

---

## 🧪 How It Works

1. User uploads a medical image (e.g., chest X-ray)
2. The image is converted to a byte stream and passed to Gemini
3. A **medical prompt** instructs Gemini on how to structure the diagnosis
4. The AI returns:
   - Structured medical observations
   - Possible diagnoses
   - Suggested treatments or next steps
5. The results are displayed in the app and can be exported

---

## 📁 Project Structure

```bash
medical-diagnosis-app/
│
├── app.py                     # Streamlit frontend + logic
├── api_key.py                 # Your Gemini API key (not pushed to repo)
├── system_prompt.py           # Custom medical diagnostic prompt
├── README.md
└── gemini-env/                # Python virtual environment (local)
