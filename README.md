# FILE-INTEGRITY-CHECKER
--------------------------------------------
# File Integrity Monitor
This Python tool detects file changes using SHA-256 hashing.

* Company: CODTECH IT SOLUTIONS
* Name: Jay Navghane
* Intern ID: COD08111
* Domain: Cyber security & Ethical Hacking
* Duration: 6 weeks
* Mentor: Neela Santosh
-----------------------------------------------

---

# 📌 **Task Description: File Integrity Monitoring Tool**

This task involves creating a Python-based **File Integrity Monitoring (FIM)** tool that detects changes in files by generating and comparing cryptographic hash values. Hash values are unique digital fingerprints of files, and even the smallest modification results in a completely different hash. By leveraging this property, the tool ensures that any unauthorized or accidental changes in files can be identified quickly and accurately.

The goal is to build a script that scans a selected folder, calculates the **SHA-256** hash of every file using Python’s built-in `hashlib` library, and stores these hash values in a JSON file for reference. When the tool is run again, it compares the newly calculated hashes with the previously stored ones. Based on this comparison, the tool categorizes each file as:

* **NEW FILE** – Appears for the first time
* **MODIFIED** – Hash value does not match the previous run
* **UNCHANGED** – File remains exactly the same

This system helps track changes over time and ensures the integrity of important files in a directory.

The task also includes improving the script to handle real-world scenarios, such as folder paths with spaces, user input validation, and readable output formatting. Once completed, the project is organized into a **GitHub-ready structure**, containing separate folders for source code, documentation, and example files, along with essential files like `README.md`, `LICENSE`, and `requirements.txt`.

Overall, this task demonstrates practical skills in Python programming, hashing techniques, file handling, data persistence using JSON, and creating structured, professional project repositories suitable for version control and public sharing.

---

Thank you !!!




**output**


<img width="1920" height="1020" alt="Image" src="https://github.com/user-attachments/assets/279599ef-8839-4035-a080-27fb004de2a4" />
