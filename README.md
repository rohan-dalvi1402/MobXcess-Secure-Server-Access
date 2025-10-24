# MobXcess: Secure Server Access from Mobile Device  
### A Secure REST-Based Alternative to SSH for Remote Server Management  
---
Secure REST-based framework for remote server access via mobile devices. Implements RSA-4096 encryption, QR-based key exchange and predefined command execution for safe and efficient server management.

## 🔐 Overview  

**MobXcess** is a secure and efficient protocol designed to enable remote server access from **mobile devices**, serving as an alternative to traditional SSH.  
It introduces a **REST-based communication model** fortified with **RSA-4096 encryption** and **QR-based key exchange**, ensuring data privacy, integrity and authentication.  

This repository presents both the **server-side implementation** and the **client-side mobile interface** described in our technical paper submitted to **IC-ICN 2023 (Springer Nature)**.  

---

## 📄 Technical Paper  

**Title:** *MobXcess: Secure Server Access from Mobile Device*  
**Author:** Rohan Dalvi  
**Conference:** IC-ICN 2023 – International Conference on Intelligent Computing and Networking (Springer Nature)  
**Date:** 22<sup>nd</sup> February 2023  

📘 *The paper is available in the [`docs/`](docs/) folder.*

---

## ⚙️ Key Features  

- 🔒 **RSA-4096 Encryption** – Ensures end-to-end confidentiality of communications  
- 📱 **Mobile Integration** – Execute predefined server commands through a secure mobile interface  
- 🧠 **Command Control** – All executable commands are predefined and managed by the administrator  
- 🧾 **REST API Endpoints** – `/getCommands`, `/runCommand` and other secure endpoints  
- 🧍 **Trusted Device Verification** – Client authentication via unique device UIDs  
- 🔑 **QR-Based Key Exchange** – Simplifies secure key transfer between client and server  
- ⚡ **Auto Reload Configuration** – Updates JSON files without requiring server restarts  

---

## 🧩 System Architecture  

### **Server**
- Parses predefined command JSON files  
- Exposes REST endpoints secured with RSA encryption  
- Authenticates clients using UID hashes and public keys  

### **Client (Mobile Application)**
- Fetches and executes commands securely via REST calls  
- Stores cryptographic keys in encrypted local storage  
- Enforces authentication through password or biometrics  

---

## 🧰 Tech Stack  

| Component | Technology Used |
|------------|----------------|
| Server     | Python / Node.js / Java |
| Mobile App | Flutter / React Native / Android Studio |
| Encryption | RSA 4096-bit (PKCS8) |
| API Type   | REST |
| Storage    | Encrypted local database (client-side) |

---

## ⚙️ Setup Instructions  

### **Server**
```bash
cd server
pip install -r requirements.txt
python app.py

