FROM node:18-slim
WORKDIR /usr/src/app
COPY package.json package-lock.json ./ 
## npm install will now use the lock file for a reproducible build
RUN npm install
COPY . .
EXPOSE 3000
#CMD ["node", "server.js"]
CMD ["npm", "start"]
