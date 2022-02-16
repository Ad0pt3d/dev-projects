const bytes = require('bytes');
const fs = require('fs');
const buffer = fs.readFileSync('filesize.txt');
const sizeString = buffer.toString();
const sizeBytes = bytes(sizeString);

console.log(`${sizeString}, ${sizeBytes}`)