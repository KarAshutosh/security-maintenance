const dns = require('dns');
const axios = require('axios');
const nodemailer = require('nodemailer');
const fs = require('fs');
require('dotenv').config();

function writeMessageToLogFile(message) {
  fs.appendFile('log.txt', message + '\n', (err) => { //WindowsScripts/subdomain-monitoring/
    if (err) {
      console.error('Error writing to WindowsScripts/subdomain-monitoring/log.txt file:', err);
    } 
  });
}

function logWithTimestamp(message) {
    const timestamp = new Date().toISOString();
    return `[${timestamp}] ${message}`;
}

const EMAIL_USER = process.env.EMAIL_USER;
const EMAIL_PASS = process.env.EMAIL_PASS;
const EMAIL_RECEIVER = process.env.EMAIL_RECEIVER;

// Replace with your domain and subdomain list
const domain = 'example.com';
const subdomains = ['subdomain1', 'subdomain2'];

let pollingInterval = 5000;

// Email configuration https://support.google.com/accounts/answer/185833
const transporter = nodemailer.createTransport({
    service: 'Gmail', 
    auth: {
        user: EMAIL_USER,
        pass: EMAIL_PASS,

    },
});

function sendEmail(message) {
    const mailOptions = {
        from: EMAIL_USER,
        to: EMAIL_RECEIVER,
        subject: `Subdomain takeover possibility`,
        text: `${message}`,
    };

    transporter.sendMail(mailOptions, (error, info) => {
        if (error) {
            writeMessageToLogFile(logWithTimestamp('Error sending email:', error));
        } else {
            writeMessageToLogFile(logWithTimestamp('Email sent:', info.response));
        }
    });
    return 600000;
}

async function checkSubdomainTakeover(domain, subdomains) {
    for (const subdomain of subdomains) {
        try {
            const subdomainExists = await checkDNSRecord(domain, subdomain);
            if (!subdomainExists) {
                const isVulnerable = await checkVulnerability(domain, subdomain);
                if (isVulnerable) {
                    let alertMessage = `Subdomain takeover vulnerability detected for ${subdomain}.${domain}`;
                    writeMessageToLogFile(logWithTimestamp(alertMessage));
                    sendEmail(alertMessage);
                    pollingInterval = 600000; 
                }
            }
        } catch (err) {
            console.error(`Error checking subdomain ${subdomain}.${domain}: ${err.message}`);
        }
    }
}
  
async function checkDNSRecord(domain, subdomain) {
    return new Promise((resolve, reject) => {
        dns.resolve(`${subdomain}.${domain}`, (err) => {
            if (err && err.code === 'ENOTFOUND') {
            resolve(false); 
            } else if (err) {
            reject(err);
            } else {
            resolve(true); 
            }
        });
    });
}
  
async function checkVulnerability(domain, subdomain) {
    try {
        const response = await axios.head(`http://${subdomain}.${domain}`);
        return response.status === 404; 
    } catch (err) {
        return false; 
    }
}
  
function runSubdomainCheck() {
    checkSubdomainTakeover(domain, subdomains);
    setTimeout(runSubdomainCheck, pollingInterval); 
}
  
runSubdomainCheck();