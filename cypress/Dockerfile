FROM cypress/included:15.18.1

WORKDIR /e2e

COPY package.json ./
RUN npm install

COPY cypress.config.js ./
COPY cypress ./cypress

CMD ["npx", "cypress", "run", "--headless", "--browser", "electron"]
