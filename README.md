#  Autoformatting App

A lightweight web application that *automatically formats* your code snippets to improve readability, consistency, and style compliance.

---

##  Features

- **Real-time formatting**: Paste or type code, and see it auto-formatted instantly.
- **Multi-language support**: Works with common languages like JavaScript, TypeScript, JSON, HTML, CSS, and more.
- **Configurable**: Customize formatting rules (e.g., indent size, quotes style).
- **Copy & Download**: Easily copy formatted code or download it as a `.txt` file.
- **Clean UI**: Minimalist interface for quick formatting without distractions.

---

##  Technologies Used

- **Frontend**: React (Create React App)
- **Formatting Engine**:
  - [Prettier](https://prettier.io/) for code formatting and formatting rule support
- **State Management**: React Hooks (`useState`, `useEffect`)
- **Styling**: Pure CSS (or specify any library if used)
- **Testing**: Jest and React Testing Library (if tests are included)

---

##  Getting Started

### Prerequisites

- Node.js v14+
- npm or Yarn package manager

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/sobiamaqbool/Autoformatting-App.git
   cd Autoformatting-App
Install dependencies:
npm install

Start the development server:
npm start

The app will open in your browser at http://localhost:3000/.
 Usage
Paste or type your code into the source panel.
The formatted version appears automatically in the output panel.
Use Copy to copy formatted code.
Use Download to save it as a .txt file.
🔧 Configuration
Customize formatting rules in:
src/config/prettierConfig.js
Edit options like:
module.exports = {
  tabWidth: 2,
  semi: true,
  singleQuote: true,
};
Save and refresh — your custom rules will be applied automatically.
 Testing
Basic tests are available. To run them:
npm test

 Build for Production
To generate a production-ready build:
npm run build

This creates a /build folder with optimized files ready for deployment.
 Contributing
Contributions are welcome! 
Steps:
Fork the repo
Create a branch (git checkout -b feature-name)
Make changes and commit (git commit -m "Add feature")
Push (git push origin feature-name)
Open a Pull Request
 License
This project is licensed under the MIT License.

 Author
Sobia Maqbool
MPhil in Artificial Intelligence
GitHub: sobiamaqbool
Profile: Autoformatting-App
