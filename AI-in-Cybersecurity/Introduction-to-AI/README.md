# Introduction to AI in Cybersecurity

## Overview
This section covers my research and practical notes from the "AI in Cybersecurity" module on TryHackMe. It explores the evolution of AI, its underlying technologies, and its dual role as both a threat and a powerful defensive tool.

## Core Concepts
*   **Artificial Intelligence (AI):** Systems capable of human-like reasoning and problem-solving.
*   **Machine Learning (ML):** A subfield where models learn patterns from data. Includes supervised, unsupervised, and reinforcement learning[cite: 1].
*   **Deep Learning (DL):** Scalable ML that uses **Neural Networks** to process vast amounts of data without human intervention[cite: 1, 2].
*   **Large Language Models (LLMs):** Advanced DL models (like GPT) based on **Transformer** architectures that predict the next token in a sequence[cite: 2].



## AI Security Threats
Adversaries leverage AI to enhance existing attacks and exploit new vulnerabilities:
1.  **AI Model Vulnerabilities:** 
    *   **Prompt Injection:** Overriding original instructions to leak data[cite: 3].
    *   **Data Poisoning:** Manipulating training data to bias model output[cite: 3].
    *   **Privacy Leakage:** Inadvertent disclosure of sensitive training data[cite: 3].
2.  **Enhanced Attacks:** 
    *   **DeepFakes:** Generating highly realistic voice/video for social engineering[cite: 3].
    *   **Advanced Phishing:** Creating fluent, context-aware emails to bypass human instinct[cite: 3].

## AI as a Defensive Shield
Embracing AI can significantly reduce the cost and impact of data breaches (saving approx. $2.2M per breach according to IBM)[cite: 4].
*   **Anomalies Detection:** Rapid analysis of network traffic (e.g., using Splunk or MS Defender)[cite: 4].
*   **Automated Response:** Identifying and blocking phishing attempts in real-time[cite: 4].
*   **Investigation:** Using LLMs to summarize incident logs and suggest threat-hunting scenarios.

## Practical Lab: AI Assistant in SOC
During the lab, I used an AI assistant for:
*   **Log Analysis:** Explaining failed SSH login attempts[cite: 5].
*   **Regex Generation:** Creating patterns for Linux authentication logs[cite: 5].
*   **Fact-Checking:** Quickly retrieving technical values like DNS over HTTPS (DoH) ports and ephemeral port ranges[cite: 5].

## Conclusion
AI is not to be feared but harnessed. The key is **Secure AI**: implementing strict RBAC, MFA, and continuous model monitoring to ensure that the tools we use to defend ourselves don't become our greatest vulnerability[cite: 4, 5].
