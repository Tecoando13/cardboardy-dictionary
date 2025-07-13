const fs = require('fs');
const path = require('path');

const dictionary = JSON.parse(fs.readFileSync('./data/latestdictionary.json', 'utf-8'));
const outputDir = path.join(__dirname, 'words');

if (!fs.existsSync(outputDir)) fs.mkdirSync(outputDir);

for (const [word, entry] of Object.entries(dictionary)) {
  const fileName = `${word}.html`;

  var content = "";

  for (i=0; i < entry.length; i++) {
    t = ""
    for (ti=0; ti < entry[i].tags.length; ti++) {
      t += `<span class="entrytag"><i>(${entry[i].tags[ti]})</i></span> `;
    }
    content += `<p>${i+1}. ${t} ${entry[i].definition}</p>`;
  }

  const html = `
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      <title>${word}</title>
      <link rel="stylesheet" href="../styles.css" />
    </head>
    <body>
      <a href="../index.html">← Back</a>
      <h1>${word}</h1>` +
      `${content}` +
    `</body>
    </html>
  `;

  fs.writeFileSync(path.join(outputDir, fileName), html);
  console.log(`Generated ${fileName}`);
}
