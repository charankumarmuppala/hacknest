# 🚀 HackNest – Centralized Hackathon Management Platform

<p align="center">
  **Discover. Build. Compete.**
</p>

<p align="center">
  A centralized platform that brings students, hackathon organizers, and judges together to manage the complete hackathon journey in one place.
</p>

---

## 📌 About the Project

**HackNest** is a web-based Centralized Hackathon Management Platform designed to simplify and organize the entire hackathon process for colleges, universities, and student communities.

Currently, hackathon information is often shared through different platforms such as WhatsApp groups, Instagram, posters, emails, Google Forms, and spreadsheets. This makes it difficult for students to discover events, register on time, find teammates, and stay updated.

HackNest solves this problem by bringing everything into one platform. Students can explore hackathons, register, build teams, collaborate, and submit projects. Organizers can create and manage events, track participants, assign judges, and publish results. Judges can evaluate projects and provide feedback.

**Our goal is to make hackathon management simple, transparent, accessible, and organized.**

## 🎯 Problem Statement

Managing college hackathons through multiple disconnected tools creates several challenges:

- Hackathon information is scattered across different platforms.
- Students may miss registration deadlines and important announcements.
- Finding teammates with suitable skills can be difficult.
- Organizers face challenges managing registrations, teams, and submissions.
- Project evaluation and result management can become time-consuming.
- Communication between students, organizers, and judges is not centralized.

## 💡 Our Solution

HackNest provides a single platform where all hackathon-related activities can be managed efficiently.

It connects four major user roles:

### 👨‍🎓 1. Student
- Create and manage a personal profile.
- Discover upcoming and ongoing hackathons.
- View event details, rules, deadlines, and prizes.
- Register for hackathons.
- Create teams or join existing teams.
- Find teammates based on skills and interests.
- Communicate with team members.
- Submit projects.
- View results, feedback, and certificates.

### 🧑‍💼 2. Organizer
- Create and manage hackathon events.
- Set registration dates, deadlines, rules, and team limits.
- View and manage registered participants.
- Monitor team formation.
- Publish announcements and updates.
- Manage project submissions.
- Assign judges to hackathons.
- Publish results and distribute certificates.

### ⚖️ 3. Judge
- View assigned hackathons.
- Access submitted projects.
- Evaluate projects using defined criteria.
- Provide scores and feedback.
- View evaluation history.

### 🛡️ 4. Admin
- Manage students, organizers, and judges.
- Manage organizations and hackathons.
- Approve and manage judge accounts.
- Monitor platform activities.
- View reports and analytics.
- Manage platform settings and permissions.

## ✨ Key Features

| Feature | Description |
|---|---|
| User Authentication | Secure login, registration, and role-based access |
| Hackathon Discovery | Explore upcoming and ongoing hackathons |
| Event Management | Create, update, and manage hackathon events |
| Team Formation | Create teams and join existing teams |
| Participant Management | Organizers can monitor registrations |
| Announcements | Share important event updates |
| Project Submission | Submit project details and links |
| Judge Evaluation | Evaluate projects and provide feedback |
| Results Management | Publish rankings and winners |
| Certificate Management | Issue and access participation and winner certificates |

## 🛠️ Technology Stack

HackNest is developed using modern web technologies.

### Frontend
- React.js
- JavaScript
- HTML5
- CSS3
- Bootstrap

### Backend
- Python
- Django
- Django REST Framework

### Database
- PostgreSQL

### Development Tools
- Visual Studio Code
- Git
- GitHub
- Postman

## 🏗️ System Architecture

HackNest follows a frontend-backend architecture.

```text
          STUDENT
          ORGANIZER
          JUDGE
          ADMIN
              |
              v
      REACT.JS FRONTEND
              |
              v
      DJANGO REST APIs
              |
              v
       DJANGO BACKEND
              |
              v
         POSTGRESQL
          DATABASE
```

**How it works:**

1. Users interact with the React frontend.
2. React sends requests to the Django REST APIs.
3. Django handles authentication, permissions, and business logic.
4. PostgreSQL stores user, event, team, submission, and evaluation data.
5. The backend sends responses to the frontend for display.

## 🔄 Hackathon Workflow

The platform supports the complete hackathon lifecycle:

1. Organizer creates a hackathon.
2. Students discover and register for the event.
3. Students create or join teams.
4. Teams collaborate and prepare projects.
5. Organizers share announcements and updates.
6. Teams submit their projects before the deadline.
7. Organizers assign judges.
8. Judges evaluate projects and provide feedback.
9. Organizers publish results and rankings.
10. Certificates are issued to eligible participants and winners.

## 📂 Project Modules

The project is divided into the following modules:

- **Authentication Module:** User registration, login, and role-based permissions.
- **Student Module:** Student profiles, hackathon discovery, registration, and teams.
- **Organizer Module:** Hackathon creation, participant management, and announcements.
- **Team Module:** Team creation, joining, and collaboration.
- **Submission Module:** Project details, links, and file submissions.
- **Judge Module:** Judge assignments, evaluations, scores, and feedback.
- **Results Module:** Rankings, winners, and certificates.
- **Admin Module:** Platform-wide user and event management.

## ⚙️ Installation and Setup

Follow these steps to run the project locally.

### Prerequisites

Make sure you have installed:

- Python 3.x
- Node.js and npm
- PostgreSQL
- Git
- Visual Studio Code

### 1. Clone the Repository

```bash
git clone https://github.com/vijay0567/HackNest.git
```

```bash
cd HackNest
```

### 2. Backend Setup (Django)

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install backend dependencies:

```bash
pip install -r requirements.txt
```

Apply database migrations:

```bash
python manage.py migrate
```

Create an administrator account:

```bash
python manage.py createsuperuser
```

Start the Django development server:

```bash
python manage.py runserver
```

Backend runs at:

`http://127.0.0.1:8000/`

### 3. Frontend Setup (React)

Open another terminal and navigate to your React frontend directory:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start the React development server:

```bash
npm run dev
```

If your project uses Create React App instead of Vite, use:

```bash
npm start
```

Frontend runs at the local address displayed in your terminal.

### 4. Database Configuration

Create a PostgreSQL database and configure its connection details in your Django environment variables.

Example configuration:

```env
DB_NAME=hacknest
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=5432
```

**Note:** Configure your Django settings to read these environment variables. Never upload passwords, secret keys, or other sensitive information to GitHub.

## 🔮 Future Enhancements

The following features are planned to improve the platform further:

- 🤖 AI-based teammate recommendations using skills and interests.
- 💬 Real-time team chat and collaboration.
- 📧 Email and push notifications.
- 📱 QR-code-based event attendance.
- 🏆 Live hackathon leaderboards.
- 🔗 GitHub integration for project submissions.
- 📊 Advanced analytics and performance reports.
- 🌐 Cross-university hackathon discovery.
- 📲 Mobile application support.

## 🎓 Project Objectives

- Centralize hackathon information and activities.
- Improve communication between students and organizers.
- Simplify event registration and team formation.
- Make project evaluation more organized and transparent.
- Reduce manual work for hackathon organizers.
- Create a better hackathon experience for everyone.

## 🌟 Why HackNest?

HackNest is more than an event registration platform. It brings the different stages of a hackathon into one connected system.

From discovering an event to forming a team, submitting a project, receiving evaluation, and celebrating achievements, HackNest makes the entire journey easier to manage.

**One Platform. Every Hackathon. Endless Possibilities.**

## 👨‍💻 Developer

**Project Name:** HackNest – Centralized Hackathon Management Platform

**Developed By:** Muppala Charan Kumar

**Project Type:** Web Application

**Technology:** React.js, Django, Django REST Framework, PostgreSQL

## 📄 License

This project is developed for academic and educational purposes. Licensing and reuse permissions can be defined as the project evolves.

---

<p align="center">
  **Made with ❤️ to bring hackathon communities together.**
</p>

<p align="center">
  🚀 HackNest – Discover. Build. Compete.
</p>
