const fs = require('fs');
const path = require('path');

main('vue.json', '.html');
main('api.json', '.js');
function main(name, type) {
  let data = fs.readFileSync(path.join(__dirname, name)).toString();
  data = JSON.parse(data);

  for (const key in data) {
    if (data.hasOwnProperty(key)) {
      const element = data[key];
      if (!element.body) {
        const _path = path.join(__dirname, 'includes', key + type);
        if (fs.existsSync(_path)) {
          const _data = fs.readFileSync(_path).toString();
          data[key].prefix = key;
          data[key].body = _data;
        }
      }
    }
  }

  fs.writeFileSync('./snippets/' + name, JSON.stringify(data));
}
