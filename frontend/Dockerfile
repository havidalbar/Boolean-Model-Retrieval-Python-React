FROM node:13-alpine
WORKDIR /app
ENV PATH /app/node_modules/.bin:$PATH
COPY . ./
RUN npm install -q
CMD ["npm", "start"]