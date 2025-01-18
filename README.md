# 🖥️ Selenium Automation Template  

_A robust Selenium template for browser automation using **Python & Chrome WebDriver**._  

---

## 🚀 Features  
- ✅ **Automated Browser Control**: Interact with Chrome using Selenium WebDriver.  
- ✅ **Persistent Sessions**: Load and save cookies for session retention.  
- ✅ **User-Agent & Profile Management**: Simulate real user activity with custom user-agent and profile settings.  
- ✅ **Element Interaction Helpers**: Includes functions for finding elements and handling iframes.  
- ✅ **Randomized Delays**: Simulates human-like browsing behavior.  

---

## 📦 Installation  

### 🔹 Prerequisites  
Ensure you have **Python 3.x** installed.  

### 🔹 Setup Virtual Environment & Install Dependencies  
```sh
# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate   # On Windows

# Install dependencies
pip install -r requirements.txt
```  

---

## ⚙️ Configuration  

### 1️⃣ **Set User Data Directory**  
Find your **Chrome user data directory** by opening `chrome://version/` in Chrome and set it in the script:  
```python
USER_DATA_DIRECTORY = "YOUR_USER_DATA_DIRECTORY"
```  

### 2️⃣ **Set Your User-Agent**  
Find your **User-Agent** using [this tool](https://www.whatismybrowser.com/detect/what-is-my-user-agent) and update:  
```python
YOUR_USER_AGENT = "YOUR_USER_AGENT"
```  

---

## 🚀 Running the Script  

```sh
python script.py
```  

---

## 🛠️ Functions Overview  

### 🔹 **Initialize Browser**  
```python
driver = browser_init()
```  
- Launches Chrome with the specified user data directory and user-agent.  
- Loads saved cookies for session persistence.  

### 🔹 **Save & Load Cookies**  
```python
save_cookies(driver)  # Save cookies
load_cookies(driver)  # Load cookies  
```  

### 🔹 **Wait for Element (with Timeout)**  
```python
element = wait_for_element(driver, xpath="//*[@id='example']", timeout=30)
```  
- Waits until an element is found or timeout is reached.  

### 🔹 **Basic Element Interactions**  
```python
driver.find_element(By.XPATH, xpath)       # Find by XPath  
driver.find_element(By.CLASS_NAME, class)  # Find by Class  
driver.find_element(By.ID, id)             # Find by ID  
```  

### 🔹 **Handle iFrames**  
```python
driver.switch_to.frame(iframe)             # Switch to iFrame  
driver.switch_to.default_content()         # Exit iFrame  
```  

---

## 📜 License  
This project is open-source and licensed under the **MIT License**.  

---


## 📢 Connect with Austin Reed  
🔗 **GitHub:** [gruntgrunt32](https://github.com/gruntgrunt32)  
🔗 **Website:** [austin-reed.com](https://austin-reed.com)  

---

### 🎉 **Happy Automating!** 🚀  
