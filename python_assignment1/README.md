# Python Assignment - User Input & Chatbots

Complete assignment for Python course covering input handling and chatbot frameworks.

---

## 📁 Project Files

```
python_assignment1/
├── user_input_collector.py   # Main Python assignment
├── tawk_demo.html             # Tawk.to demo page
├── FLOWISE_GUIDE.md           # Flowise setup guide
├── HOW_TO_RUN.md              # Class demonstration guide
├── README.md                  # This file
└── data/                      # Saved user data (auto-created)
    └── user_data.json
```

---

## 🎯 Assignment Parts

### Part 1: Python Input Script ✅

**File:** `user_input_collector.py`

A Python script that collects and validates user input for different data types:
- **String** - name, email, city
- **Integer** - age (with validation)
- **Float** - height, salary (with validation)

**Features:**
- ✅ Input validation with error checking
- ✅ Colored terminal output  
- ✅ Data type demonstrations
- ✅ JSON file export
- ✅ User-friendly error messages

**Run:**
```bash
python user_input_collector.py
```

---

### Part 2: Chatbot Frameworks

#### A. Flowise (AI Chatbot) 🤖

**What it is:** Visual tool to build AI chatbots with drag-and-drop

**Quick Start:**
```bash
npm install -g flowise
npx flowise start
```
Then open: http://localhost:3000

**Features:**
- Drag-and-drop chatbot builder
- Multiple AI models (OpenAI, HuggingFace, etc.)
- Conversation memory
- Document Q&A
- Free and open-source

**Full Guide:** See `FLOWISE_GUIDE.md`

---

#### B. Tawk.to (Live Chat) 💬

**What it is:** Free live chat widget for websites

**Quick Start:**
1. Sign up at https://www.tawk.to/
2. Create a property
3. Copy widget code
4. Paste into `tawk_demo.html`
5. Open `tawk_demo.html` in browser

**Features:**
- Live chat with visitors
- Automated responses
- Mobile apps
- 100% FREE forever

**Demo File:** `tawk_demo.html`

---

## 🚀 How to Use

### Python Script
```bash
# Run the main assignment
python user_input_collector.py

# Follow the prompts:
# 1. Enter name (string)
# 2. Enter email (string)
# 3. Enter age (integer)
# 4. Enter height (float)
# 5. Enter city (string)
# 6. Enter salary (float)

# See results and data types
# Save to JSON file (optional)
```

### Flowise
```bash
# Install (one time)
npm install -g flowise

# Run
npx flowise start

# Create chatbot:
# 1. Open http://localhost:3000
# 2. Click "Add New"
# 3. Drag components:
#    - Chat Model (e.g., ChatOpenAI)
#    - Memory (e.g., Buffer Memory)
#    - Chain (e.g., Conversation Chain)
# 4. Connect them
# 5. Click "Save" and test
```

### Tawk.to
```bash
# Setup:
# 1. Register at tawk.to
# 2. Get widget code
# 3. Add to tawk_demo.html
# 4. Open in browser
```

---

## 📊 What You'll Learn

### Python Skills:
- ✅ Collecting user input
- ✅ Data types (str, int, float)
- ✅ Input validation
- ✅ Error handling (try-except)
- ✅ Type conversion
- ✅ File operations (JSON)
- ✅ String formatting

### Chatbot Skills:
- ✅ AI chatbot concepts
- ✅ Visual flow building
- ✅ Widget integration
- ✅ Automation setup

---

## 📝 Assignment Requirements

### ✅ Python Input (Complete)
- [x] String input with validation
- [x] Integer input with range checking
- [x] Float input with validation
- [x] Display all data types
- [x] Error handling
- [x] Clean code structure

### ✅ Flowise (Complete)
- [x] Installation guide
- [x] Setup instructions
- [x] Component documentation
- [x] Examples provided

### ✅ Tawk.to (Complete)
- [x] Demo HTML file
- [x] Integration guide
- [x] Configuration steps
- [x] Features explained

---

## 💡 Common Issues

### Python Script
**Issue:** Colors not showing in terminal  
**Fix:** Use Windows Terminal or Command Prompt (not PowerShell ISE)

**Issue:** Module not found  
**Fix:** No external packages needed - uses Python standard library only

### Flowise
**Issue:** Installation fails  
**Fix:** Make sure Node.js 18+ is installed: `node --version`

**Issue:** Port 3000 already in use  
**Fix:** Use different port: `npx flowise start --PORT=3001`

### Tawk.to
**Issue:** Widget not showing  
**Fix:** Check if you copied the complete script including `<script>` tags

---

## 🎓 For Class Presentation

See `HOW_TO_RUN.md` for step-by-step demonstration guide.

---

## 📚 Resources

- Python Documentation: https://docs.python.org/3/
- Flowise: https://flowiseai.com/
- Tawk.to: https://www.tawk.to/
- Python Input/Output: https://docs.python.org/3/tutorial/inputoutput.html

---

## 🔄 Updates

**Version 1.0** - Initial release
- Python input collector
- Flowise guide
- Tawk.to demo

---

## ✨ Features Summary

| Feature | Status | Description |
|---------|--------|-------------|
| String Input | ✅ | Collects name, email, city |
| Integer Input | ✅ | Collects age with validation |
| Float Input | ✅ | Collects height, salary |
| Validation | ✅ | Range and type checking |
| Error Handling | ✅ | User-friendly messages |
| Colors | ✅ | Colored terminal output |
| JSON Export | ✅ | Save data to file |
| Flowise Guide | ✅ | Complete setup instructions |
| Tawk.to Demo | ✅ | HTML integration example |

---

**Assignment Status:** ✅ COMPLETE

All requirements fulfilled and ready for submission! 🎉
