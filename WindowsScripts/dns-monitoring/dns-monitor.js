const dns = require('dns');
const cron = require('node-cron');
const nodemailer = require('nodemailer');
const fs = require('fs');
require('dotenv').config();

function writeMessageToLogFile(message) {
  fs.appendFile('WindowsScripts/dns-monitoring/log.txt', message + '\n', (err) => {
    if (err) {
      console.error('Error writing to WindowsScripts/dns-monitoring/log.txt file:', err);
    } 
  });
}

function logWithTimestamp(message) {
    const timestamp = new Date().toISOString();
    return `[${timestamp}] ${message}`;
}

function arraysEqual(arr1, arr2) {

    if (arr1 === undefined || arr2 === undefined) return false;
    if (arr1.length !== arr2.length) return false;
    for (let i = 0; i < arr1.length; i++) {
        if (arr1[i] !== arr2[i]) return false;
    }
    return true;
}

const EMAIL_USER = process.env.EMAIL_USER;
const EMAIL_PASS = process.env.EMAIL_PASS;
const EMAIL_RECEIVER = process.env.EMAIL_RECEIVER;

// Define an array of DNS names you want to check
const dnsNames = ['lifesignals.com'];

const previousIPs = {};
let checkingInterval = 5000;
let firstCheck = true;

// Email configuration https://support.google.com/accounts/answer/185833
const transporter = nodemailer.createTransport({
    service: 'Gmail', 
    auth: {
        user: EMAIL_USER,
        pass: EMAIL_PASS,

    },
});

function sendEmail(dnsName, IP) {
    const mailOptions = {
        from: EMAIL_USER,
        to: EMAIL_RECEIVER,
        subject: `DNS name of ${dnsName} affected`,
        text: `The DNS name of ${dnsName} is returning the IP ${IP}`,
    };

    transporter.sendMail(mailOptions, (error, info) => {
        if (error) {
            writeMessageToLogFile(logWithTimestamp('Error sending email:', error));
        } else {
            writeMessageToLogFile(logWithTimestamp('Email sent:', info.response));
        }
    });
}

function checkDNS() {
    dnsNames.forEach((dnsName) => {
        dns.resolve(dnsName, (err, addresses) => {
            if (err) {
                writeMessageToLogFile(logWithTimestamp(`Error resolving DNS name ${dnsName}: ${err.message}`));
                return;
            }
    
            const previousAddress = previousIPs[dnsName];
            if (!arraysEqual(previousAddress, addresses)) {
                writeMessageToLogFile(logWithTimestamp(`DNS name ${dnsName} has changed. New IP addresses: ${addresses.join(', ')}`));
            if (!firstCheck) {
                checkingInterval = 600000; // 10 minutes if IP has changed (not on the first check)
                sendEmail(dnsName, addresses.join(', '))
            }
            } else {
                writeMessageToLogFile(logWithTimestamp(`DNS name ${dnsName} remains the same. IP addresses: ${addresses.join(', ')}`));
                checkingInterval = 5000; // 5 seconds if IP hasn't changed
            }
    
            previousIPs[dnsName] = addresses;
            firstCheck = false;
        });
    });
  
    setTimeout(() => {
        checkDNS();
    }, checkingInterval);
}



checkDNS();

