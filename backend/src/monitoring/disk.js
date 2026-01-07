// Gather disk usage statistics
const { exec } = require('child_process');

function getDiskUsage() {
  return new Promise((resolve, reject) => {
    exec('df -h /', (err, stdout) => {
      if (err) return reject(err);

      const lines = stdout.split('\n');
      const parts = lines[1].split(/\s+/);

      resolve({
        filesystem: parts[0],
        size: parts[1],
        used: parts[2],
        available: parts[3],
        usagePercent: parts[4],
        mount: parts[5],
      });
    });
  });
}

module.exports = getDiskUsage;
