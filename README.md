# EmailerV2 – Django App for Automated E-mailing

EmailerV2 is a Django application that enables users to create email templates, manage contacts, configure SMTP email settings, and automatically send personalized emails to contacts during working hours using a background thread.

**Note:**  
When writing a message template, use the placeholder `COMPANY` where you want the contact’s company name to appear, and `SUBJECT` where you want the contact’s name or greeting to be inserted dynamically in the email.

---

## Features

- User registration and login  
- Configure SMTP connection (email, password, host, port)  
- Create message templates with placeholders `COMPANY` and `SUBJECT` to personalize emails  
- Manage contacts with assigned message templates  
- Automatic background email sending during working hours  
- Web interface to manage emails, messages, and contacts  
- Responsive and mobile-friendly web interface  

---

## Usage

- Log in and configure your SMTP settings.  
- Most of the time, SMTP providers require you to generate a **custom app password** or **authentication token** instead of using your regular account password for secure access.
- Add message templates using `COMPANY` and `SUBJECT` placeholders to customize the email content per contact.  
- Add contacts with name, company, email, and select which message template to send them.  
- The app automatically sends emails in the background during working hours, replacing placeholders with actual contact data.  

---


## Deployment

To deploy this project with Docker run:

```bash
  git clone https://github.com/jkfmCZ/emailerV2
```
```bash
  docker-compose up --build -d
```
The application will be available at:
```bash
  http://localhost:8069/
```



## Future Improvements

- Add support for using authentication tokens (e.g., OAuth tokens or app passwords) instead of plain passwords for SMTP authentication.  
- Do other than Docker deployment.
---
