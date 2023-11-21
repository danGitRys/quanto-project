FROM node:18.18.0

WORKDIR /app

COPY package.json ./
# install vite globally
RUN npm install -g vite
COPY . .
# install dependencies
RUN npm install

EXPOSE 3000

CMD npm run dev
