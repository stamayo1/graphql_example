FROM node:14

WORKDIR /app

COPY package*.json ./
RUN npm config set strict-ssl false
RUN npm install

COPY . .

CMD ["node", "index.js"]