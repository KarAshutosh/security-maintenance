const ping = require('ping');
const axios = require('axios');
const nodemailer = require('nodemailer');
require('dotenv').config();

const EMAIL_USER = process.env.EMAIL_USER;
const EMAIL_PASS = process.env.EMAIL_PASS;
const EMAIL_RECEIVER = process.env.EMAIL_RECEIVER;
// Define the hosts you want to monitor
const hostsToMonitor = ['alpha.lifesignals.com', 'us-trials.lifesignals.com'];

const monitorInMS = 1000;

// Email configuration https://support.google.com/accounts/answer/185833
const transporter = nodemailer.createTransport({
    service: 'Gmail', 
    auth: {
        user: EMAIL_USER,
        pass: EMAIL_PASS,

    },
});

function sendEmail(host, message) {
    const mailOptions = {
        from: EMAIL_USER,
        to: EMAIL_RECEIVER,
        subject: `Host ${host} is down`,
        text: `The host ${host} is not responding. ${message}`,
    };

    transporter.sendMail(mailOptions, (error, info) => {
        if (error) {
            logWithTimestamp('Error sending email:', error);
        } else {
            logWithTimestamp('Email sent:', info.response);
        }
    });
}

function checkHostWithPing(host) {
    ping.sys.probe(host, (isAlive) => {
        if (!isAlive) {
            logWithTimestamp(`PING FAILED: Host ${host} is down. Trying HTTP request.`);
            checkHostWithHTTP(host);
        } else {
            logWithTimestamp(`PING SUCCESS: Host ${host} is up.`);
        }
    });
}
  
async function checkHostWithHTTP(host) {
    try {
        const response = await axios.get(`https://${host}`);
        if (response.status === 200) {
            logWithTimestamp(`HTTPS SUCCESS: Host ${host} is up.`);
        } else {
            console.log(`HTTPS FAILED: Host ${host} returned a non-200 status code. Sending an email.`);
            var message = 'Returned a non-200 status code';
            sendEmail(host, message);
        }
    } catch (error) {
        logWithTimestamp(`HTTPS FAILED: Host ${host} is down. Sending an email.`);
        var message = 'Error: ' + error;
        sendEmail(host, message);
    }
}

function logWithTimestamp(message) {
    const timestamp = new Date().toISOString();
    console.log(`[${timestamp}] ${message}`);
}

setInterval(() => {
    hostsToMonitor.forEach((host) => {
        checkHostWithPing(host);
    });
}, monitorInMS);
