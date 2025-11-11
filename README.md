# Instagram Unfollowers 

A simple **Instagram unfollowers tracking tool** built with **HTML** and **PyScript**.  
This app allows users to **securely upload their official Instagram data export** and instantly see who has unfollowed them — without needing to log into Instagram through a third-party service.

---

## 🚀 Features
- **100% client-side** – No backend, no databases. All processing happens in your browser.  
- **Safe and private** – Users never share their Instagram credentials.  
- **Simple upload process** – Just drag and drop your downloaded Instagram data file.  
- **Clean and lightweight UI** – Fast and responsive experience.  
- **Deployed on Vercel** – Quick and reliable hosting.

---

## 🛠️ Tech Stack
- **Frontend:** HTML, CSS  
- **Logic & Data Processing:** Python (via [PyScript](https://pyscript.net/))  
- **Deployment:** Vercel

---

## 📥 How It Works
1. **Request your Instagram data export**:
   - Open Instagram and go to **Settings → Privacy and Security → Download Data**.
   - Choose **JSON format** for best compatibility.
   - Instagram will email you a download link — save the `.zip` file.

2. **Upload the file to the app**:
   - Go to [https://yourappname.vercel.app](https://instagram-unfollowers-gray.vercel.app/)
   - Upload the Instagram data ZIP file using the app interface.

3. **See who unfollowed you**:
   - The app will process your data directly in your browser.
   - Instantly display the names of accounts that don't follow you back

---

## Testing

1. CD into the directory with the cloned repository
2. Run the command `python -m http.server 8000` to create a python HTTP server
3. Access the page from `http://localhost:8000/index.html`
