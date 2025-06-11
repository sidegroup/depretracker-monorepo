const http = require('http');
const fs = require('fs');
const path = require('path');

const PORT = 8080;
const DIST_FOLDER = path.join(__dirname, 'dist', 'wedext', 'browser');

console.log(`Diretório atual: ${__dirname}`);
console.log(`Pasta de distribuição: ${DIST_FOLDER}`);

const MIME_TYPES = {
  '.html': 'text/html',
  '.js': 'text/javascript',
  '.css': 'text/css',
  '.json': 'application/json',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.gif': 'image/gif',
  '.svg': 'image/svg+xml',
  '.ico': 'image/x-icon',
  '.woff': 'application/font-woff',
  '.woff2': 'application/font-woff2',
  '.ttf': 'font/ttf',
  '.eot': 'application/vnd.ms-fontobject',
  '.otf': 'font/otf'
};

const server = http.createServer((req, res) => {
  console.log(`Requisição: ${req.url}`);

  // Normaliza o caminho da URL para evitar caminhos relativos
  let filePath = path.join(DIST_FOLDER, req.url === '/' ? 'index.html' : req.url);
  
  // Se o caminho não tiver extensão, tenta servir o index.html (para rotas SPA)
  if (!path.extname(filePath)) {
    filePath = path.join(DIST_FOLDER, 'index.html');
  }

  const extname = path.extname(filePath);
  let contentType = MIME_TYPES[extname] || 'application/octet-stream';

  fs.readFile(filePath, (err, content) => {
    if (err) {
      if (err.code === 'ENOENT') {
        // Arquivo não encontrado, tenta servir o index.html para rotas SPA
        fs.readFile(path.join(DIST_FOLDER, 'index.html'), (err, content) => {
          if (err) {
            res.writeHead(500);
            res.end(`Erro: ${err.code}`);
          } else {
            res.writeHead(200, { 'Content-Type': 'text/html' });
            res.end(content, 'utf-8');
          }
        });
      } else {
        // Outro tipo de erro
        res.writeHead(500);
        res.end(`Erro: ${err.code}`);
      }
    } else {
      // Sucesso - arquivo encontrado
      res.writeHead(200, { 'Content-Type': contentType });
      res.end(content, 'utf-8');
    }
  });
});

server.listen(PORT, () => {
  console.log(`Servidor rodando em http://localhost:${PORT}`);
  console.log(`Servindo arquivos de ${DIST_FOLDER}`);
});
