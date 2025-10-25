# Flowise Chatbot Setup Guide

## Overview
Flowise is an open-source UI visual tool to build customized LLM orchestration flows & AI agents with a drag-and-drop interface.

---

## Installation Methods

### Method 1: NPM (Recommended for Development)

```bash
# Install Flowise globally
npm install -g flowise

# Start Flowise
npx flowise start

# Access at: http://localhost:3000
```

### Method 2: Docker (Recommended for Production)

```bash
# Pull and run Flowise container
docker run -d --name flowise -p 3000:3000 flowiseai/flowise

# Access at: http://localhost:3000
```

### Method 3: Git Clone (For Developers)

```bash
# Clone the repository
git clone https://github.com/FlowiseAI/Flowise.git
cd Flowise

# Install dependencies
npm install

# Build the code
npm run build

# Start Flowise
npm start
```

---

## Creating Your First Chatbot

### Step 1: Access Flowise Dashboard
1. Open browser and navigate to `http://localhost:3000`
2. You'll see the Flowise dashboard with example chatflows

### Step 2: Create New Chatflow
1. Click the **"Add New"** button (+ icon)
2. Give your chatflow a name (e.g., "My First Chatbot")
3. You'll see a blank canvas with a toolbox on the left

### Step 3: Add Components

#### A. Add a Chat Model
1. From the left sidebar, expand **"Chat Models"**
2. Drag and drop one of these:
   - **ChatOpenAI** (if you have OpenAI API key)
   - **ChatOllama** (for local models - free)
   - **ChatGoogleGenerativeAI** (if you have Google API key)
3. Configure the model:
   - For OpenAI: Enter your API key, select model (gpt-3.5-turbo, gpt-4)
   - For Ollama: Make sure Ollama is running locally, select model (llama2, mistral)

#### B. Add Memory (Optional but Recommended)
1. Expand **"Memory"** section
2. Drag **"Buffer Memory"** to the canvas
3. This allows the chatbot to remember conversation history
4. Connect it to your chat model

#### C. Add a Chain
1. Expand **"Chains"** section
2. Drag **"Conversation Chain"** to the canvas
3. This orchestrates the conversation flow

#### D. Connect Components
1. Click on the output port (small circle) of one component
2. Drag to the input port of another component
3. Typical flow:
   ```
   Memory → Conversation Chain ← Chat Model
   ```

### Step 4: Configure Your Chatbot

#### System Prompt (Optional)
Add a prompt to define your chatbot's personality:

```
You are a helpful and friendly assistant. You provide clear, 
concise answers and always maintain a positive tone. 
If you don't know something, you admit it honestly.
```

#### Temperature Setting
- Lower (0.0-0.3): More focused and deterministic
- Medium (0.4-0.7): Balanced
- Higher (0.8-1.0): More creative and random

### Step 5: Test Your Chatbot
1. Click the **"Save"** button (top right)
2. Click the **"Chat"** icon to open the test interface
3. Start chatting with your bot!

---

## Example Chatflows

### 1. Simple Q&A Bot

**Components:**
- ChatOpenAI (or ChatOllama)
- Conversation Chain

**Setup:**
1. Add ChatOpenAI
2. Add Conversation Chain
3. Connect: ChatOpenAI → Conversation Chain
4. Set system prompt: "You are a helpful Q&A assistant"

### 2. Customer Support Bot

**Components:**
- ChatOpenAI
- Buffer Memory
- Conversation Chain

**Setup:**
1. Add all three components
2. Connect: Memory → Conversation Chain ← ChatOpenAI
3. System prompt: "You are a customer support agent for [Company]. Be helpful, professional, and empathetic."

### 3. Document Q&A Bot

**Components:**
- Document Loaders (PDF, Text, etc.)
- Text Splitter
- Embeddings (OpenAI Embeddings)
- Vector Store (Pinecone, Qdrant, etc.)
- ChatOpenAI
- Conversational Retrieval QA Chain

**Setup:**
1. Upload documents using Document Loader
2. Split text into chunks
3. Create embeddings
4. Store in vector database
5. Connect to Retrieval QA Chain

---

## Using Ollama (Free Local Models)

### Install Ollama
```bash
# On Mac
brew install ollama

# On Linux
curl https://ollama.ai/install.sh | sh

# On Windows
# Download from https://ollama.ai/download
```

### Download Models
```bash
# Download Llama 2 (7B)
ollama pull llama2

# Download Mistral (7B)
ollama pull mistral

# Download CodeLlama (for coding tasks)
ollama pull codellama
```

### Use in Flowise
1. Make sure Ollama is running: `ollama serve`
2. In Flowise, add **ChatOllama** component
3. Select your downloaded model
4. Start chatting!

---

## API Integration

### Embed Your Chatbot

Once created, you can embed your chatbot in a website:

```html
<!DOCTYPE html>
<html>
<head>
    <title>My Chatbot</title>
</head>
<body>
    <h1>Chat with Our AI Assistant</h1>
    
    <script type="module">
        import Chatbot from "https://cdn.jsdelivr.net/npm/flowise-embed/dist/web.js"
        Chatbot.init({
            chatflowid: "YOUR_CHATFLOW_ID",
            apiHost: "http://localhost:3000",
            theme: {
                button: {
                    backgroundColor: "#3B81F6",
                    right: 20,
                    bottom: 20,
                },
                chatWindow: {
                    welcomeMessage: "Hello! How can I help you today?",
                    backgroundColor: "#ffffff",
                    height: 600,
                    width: 400,
                }
            }
        })
    </script>
</body>
</html>
```

### REST API Usage

```bash
# Make API calls to your chatflow
curl -X POST http://localhost:3000/api/v1/prediction/YOUR_CHATFLOW_ID \
  -H "Content-Type: application/json" \
  -d '{"question": "Hello, who are you?"}'
```

---

## Advanced Features

### 1. Tools & Agents
Add tools for your chatbot to use:
- Calculator
- Web Search (SerpAPI, Google Search)
- Wikipedia
- Weather API
- Custom API calls

### 2. Document Chat
Upload and chat with:
- PDF files
- Text documents
- CSV files
- Web pages
- YouTube transcripts

### 3. Multiple Language Models
Compare responses from different models simultaneously

### 4. Prompt Engineering
Use advanced prompt templates:
- Few-shot learning
- Chain-of-thought prompting
- Role-based prompting

---

## Best Practices

### 1. Start Simple
Begin with a basic chatflow and gradually add complexity

### 2. Test Thoroughly
Test edge cases and unexpected inputs

### 3. Monitor Costs
If using paid APIs (OpenAI), monitor your usage:
- Set usage limits
- Use cheaper models for testing (gpt-3.5-turbo)
- Consider caching responses

### 4. Security
- Never expose API keys in frontend code
- Use environment variables for sensitive data
- Implement rate limiting

### 5. User Experience
- Set clear expectations about what the bot can do
- Provide fallback options
- Handle errors gracefully

---

## Troubleshooting

### Issue: Flowise won't start
**Solution:**
- Check if port 3000 is already in use
- Try running on different port: `npx flowise start --PORT=3001`

### Issue: ChatOllama not connecting
**Solution:**
- Ensure Ollama is running: `ollama serve`
- Check Ollama is accessible: `curl http://localhost:11434/api/tags`

### Issue: OpenAI API errors
**Solution:**
- Verify API key is correct
- Check you have credits/quota available
- Ensure you're using a valid model name

### Issue: Memory not working
**Solution:**
- Ensure Buffer Memory is properly connected
- Check the session ID is consistent across requests

---

## Resources

- **Official Website:** https://flowiseai.com/
- **Documentation:** https://docs.flowiseai.com/
- **GitHub Repository:** https://github.com/FlowiseAI/Flowise
- **Discord Community:** https://discord.gg/jbaHfsRVBW
- **YouTube Tutorials:** Search "Flowise AI tutorial"

---

## Assignment Checklist

- [ ] Install Flowise using one of the methods
- [ ] Create a simple chatbot with at least 3 components
- [ ] Test the chatbot with various questions
- [ ] Take screenshots of:
  - [ ] The chatflow design
  - [ ] Component configurations
  - [ ] Conversation example
- [ ] Document your chatbot's purpose and capabilities
- [ ] (Bonus) Embed the chatbot in an HTML page
- [ ] (Bonus) Create a Document Q&A bot

---

## Next Steps

1. Experiment with different models and compare results
2. Try adding tools and agents
3. Create a specialized chatbot for a specific domain
4. Learn about prompt engineering techniques
5. Explore vector databases and embeddings
6. Build a full-stack application using Flowise API

---

**Good luck with your Flowise chatbot! 🚀**

