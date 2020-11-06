FROM node:15.0.1-alpine

# make the 'app' folder the current working directory
WORKDIR /usr/src/frontend

# copy both 'package.json' and 'package-lock.json' (if available)
COPY package*.json ./

# install project dependencies
RUN npm install

COPY . .

EXPOSE 8080

CMD ["npm", "run", "serve"]
