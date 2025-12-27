Advanced AI Voice Assistant
Overview

This project is a modular, AI-driven voice assistant application designed to support real-time voice and text interaction, intelligent decision-making, and reliable information retrieval. The system combines speech processing, generative AI, and classical AI algorithms to produce accurate, context-aware responses.
The assistant prioritizes correctness, robustness, and architectural clarity over superficial features. Each capability is isolated into well-defined modules, enabling controlled behavior, predictable execution, and easy extensibility.

Key Capabilities:
1. Interaction & Input Handling:
Voice-based input using speech recognition
Text-based fallback for reliability
Unified input routing logic
Stateless UI with controlled session memory

2. Conversational Intelligence:
Generative AI integration (Google Gemini)
Context-aware response generation
Graceful fallback for unsupported queries

3. Knowledge Retrieval:
Wikipedia search and summarization
Intelligent disambiguation handling
A*-based traversal of related articles for relevance
Explicit failure reporting instead of silent errors

4. Decision-Making Logic:
Alpha-Beta pruning based decision engine
Deterministic selection when multiple options exist
Designed to avoid random or heuristic-only choices

5. Translation:
Multilingual translation support
Backtracking strategy to retry failed translations
Explicit error handling for API inconsistencies

6. Utility Skills:
Real-time weather information
Time queries
Lightweight joke responses
Easily extensible skill routing system

-> Design Principles:
- Modular skill isolation
- Algorithm-backed intelligence (not prompt-only)
- Explicit error handling
- Minimal hidden state
- Predictable execution paths

-> Tech Stack:
-UI Framework: Streamlit
-Language: Python
-Speech Processing: SpeechRecognition, pyttsx3
-AI Model: Google Gemini API
-Knowledge APIs: Wikipedia, OpenWeather
-Algorithms:
  Alpha-Beta Pruning
  A* Search
  Backtracking

->Architecture Highlights:
- Clear separation of concerns :
   UI layer
   Core orchestration
   Skills
   Algorithms
- Environment-based configuration
- Skill-scoped logic
- Deterministic routing and response flow

Intended Use:
- AI/ML academic projects
- Algorithm-enhanced AI demonstrations
- Voice-driven assistant prototypes
- Portfolio-grade system design showcase
