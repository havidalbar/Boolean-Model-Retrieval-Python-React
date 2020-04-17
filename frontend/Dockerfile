FROM node:alpine
WORKDIR /app
ENV PATH /app/node_modules/.bin:$PATH
COPY . ./
RUN npm install -q
RUN npm install -gq react-scripts
CMD ["npm", "start"]