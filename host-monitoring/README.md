# Host Monitoring Script

A Node.js script for monitoring the availability of hosts using ICMP ping and HTTP requests. If a host is found to be unreachable, it sends an email notification.

## Prerequisites

Before running the script, you'll need the following:

- Node.js installed on your system.
- Environment variables set for your Gmail email address (`EMAIL_USER`) and the generated app password (`EMAIL_PASS`) for sending email notifications.

## Installation

1. Clone this repository to your local machine:
```
git clone https://github.com/yourusername/host-monitor.git
cd host-monitor
npm install
```

## Configuration
Create a .env file in the project directory and set your environment variables:

```
EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_generated_app_password
```
Replace your_email@gmail.com with your Gmail email address and your_generated_app_password with the app password generated for your Gmail account. 

Follow instructions at https://support.google.com/accounts/answer/185833 to get app password.

## Usage
To start monitoring the specified hosts, run the script using Node.js:

```
node host-monitor.js
```

## Customization
* Edit the hostsToMonitor array in host-monitor.js to specify the hosts you want to monitor.
* Customize the email content and recipient address in the sendEmail function within host-monitor.js.

Note: If a host goes down, scans are performed every 10 minutes to prevent spam from email.
