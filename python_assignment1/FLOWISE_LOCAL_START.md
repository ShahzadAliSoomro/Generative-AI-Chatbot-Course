# 🚀 Flowise Local Setup - Quick Start

## ✅ Direct Run (No Installation Needed!)

### Option 1: NPX (Recommended - Easiest)
```bash
# Run directly without installing
npx flowise@latest start

# Wait for: "Server started on port 3000"
# Then open: http://localhost:3000
```

**Pehli baar thoda time lagega (packages download hote hain)**

---

## 🎯 After Starting

1. **Wait for message:**
   ```
   Server started on port 3000
   ```

2. **Open browser:**
   ```
   http://localhost:3000
   ```

3. **You'll see Flowise Dashboard! 🎉**

---

## 🤖 Create Your First Chatbot

### Step 1: Click "Add New Chatflow"
- Name it: "My First Bot"

### Step 2: Add Components (Drag from left sidebar)

**For Simple Bot (No API Key Needed):**
1. Search "HuggingFace Inference"
2. Drag "Conversation Chain"
3. Connect them

**For Advanced Bot (Need OpenAI Key):**
1. Drag "ChatOpenAI" from Chat Models
2. Drag "Buffer Memory" from Memory  
3. Drag "Conversation Chain" from Chains
4. Connect: Memory → Chain ← ChatOpenAI

### Step 3: Test
- Click "Save"
- Click "Chat" icon
- Start chatting!

---

## 🛑 Stop Flowise

**In Terminal:**
- Press `Ctrl + C`

---

## 💡 Common Issues

### Issue: Port 3000 already in use
**Fix:**
```bash
npx flowise@latest start --PORT=3001
# Then open: http://localhost:3001
```

### Issue: Taking too long
**Wait:** Pehli baar 2-3 minutes lag sakte hain (downloading packages)

### Issue: Error showing
**Try:** Close terminal and run again:
```bash
npx flowise@latest start
```

---

## 🎓 For Assignment

### What to Show:
1. **Open Flowise** in browser
2. **Show Dashboard** 
3. **Explain**: "This is a visual chatbot builder"
4. **Show components** sidebar
5. **Explain** how to connect components

### No Need to:
- ❌ Create complex chatbots
- ❌ Get API keys
- ❌ Deep technical setup

**Just showing the interface is enough! ✅**

---

## 📝 Screenshot Locations (Good for Presentation)

Take screenshots of:
1. Flowise Dashboard (main page)
2. Components sidebar (left side)
3. A simple chatflow (if time permits)

---

## ⚡ Quick Demo Script

> "Flowise is running locally on port 3000. Here's the dashboard where you can visually build chatbots. On the left, you have components like Chat Models, Memory, and Chains. You drag and drop them to create intelligent conversations. It supports multiple AI models and is completely free and open-source."

---

## 🎯 Alternative (If Flowise Doesn't Start)

**No Problem!**
- Show `FLOWISE_GUIDE.md` documentation
- Explain concepts verbally
- Show architecture diagram
- Reference official website: https://flowiseai.com

**Your main assignment is Python script anyway! ✅**

---

**Status:** Flowise is starting in background...  
**Check:** http://localhost:3000 (wait 2-3 minutes)  
**Ready:** When you see the dashboard! 🚀

