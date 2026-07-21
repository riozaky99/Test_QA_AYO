// cypress/support/e2e.js

Cypress.Commands.add('apiRequest', (method, endpoint, body) => {
  return cy.request({
    method,
    url: endpoint,
    headers: { 'Content-Type': 'application/json' },
    body,
    failOnStatusCode: false,
  })
})
