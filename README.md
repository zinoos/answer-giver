# 🧠 Researcher – AI Question Answering Terminal

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Transformers](https://img.shields.io/badge/Transformers-🤗-ff69b4.svg)](https://huggingface.co/docs/transformers)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

```
░█████╗░███╗░░██╗░██████╗░██╗░░░░░░░██╗███████╗██████╗░  
██╔══██╗████╗░██║██╔════╝░██║░░██╗░░██║██╔════╝██╔══██╗  
███████║██╔██╗██║╚█████╗░░╚██╗████╗██╔╝█████╗░░██████╔╝  
██╔══██║██║╚████║░╚═══██╗░░████╔═████║░██╔══╝░░██╔══██╗  
██║░░██║██║░╚███║██████╔╝░░╚██╔╝░╚██╔╝░███████╗██║░░██║  
╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░░░░╚═╝░░░╚═╝░░╚══════╝╚═╝░░╚═╝  
```

A sleek terminal-based **AI researcher** that answers any question you ask — instantly powered by 🤗 [Transformers](https://huggingface.co) and the **Fathom-Search-4B** model.  
Perfect for quick scientific or factual lookups right from your console.

---

## 🚀 Features
- 🧩 Interactive terminal interface  
- 💬 Uses Hugging Face’s `pipeline` for text generation  
- ✨ Clean “one-sentence” answers with optional token control  
- ❌ Type `exit` or `quit` to close the app  

---

## 🖥️ Usage
1. **Clone the repo**
    ```bash
    git clone https://github.com/<your-username>/researcher
    cd researcher
    ```

2. **Install dependencies**
    ```bash
    pip install transformers torch
    ```

   *(Optional: install `keyboard` if you want to expand input features later.)*

3. **Run it**
    ```bash
    python main.py
    ```

You’ll see this banner:
```
What do you want to know?
> 
```
Then simply ask:
```
> What is the speed of light?
```

---

## ⚙️ Example Output
```
Answer: The speed of light in a vacuum is exactly 299,792,458 meters per second.
```

---

## 🧩 Configuration
Inside `main.py`, you can adjust:
```python
max_new_tokens = 50  # Controls answer length
```
or change prompt style:
```python
prompt = f"Answer the following question in one sentence:\n\n{question}\n\nAnswer:"
```

---

## 📂 Project Structure
```
researcher/
│
├── main.py          # Core app logic
├── README.md        # This file
└── requirements.txt # Dependencies (optional)
```

---

## 🧠 Model
This project uses the [`FractalAIResearch/Fathom-Search-4B`](https://huggingface.co/FractalAIResearch/Fathom-Search-4B) model from Hugging Face, optimized for reasoning and factual text generation.

---

## 🪪 License
This project is licensed under the **MIT License**.  

---
