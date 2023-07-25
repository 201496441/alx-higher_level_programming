#!/usr/bin/env node

const request = require('request');

// Function to compute the number of completed tasks by user ID
function countCompletedTasks(apiUrl) {
  request(apiUrl, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
      return;
    }

    if (response.statusCode !== 200) {
      console.error('API request failed with status:', response.statusCode);
      return;
    }

    const todos = JSON.parse(body);
    const completedTasks = {};

    todos.forEach((todo) => {
      if (todo.completed) {
        if (completedTasks[todo.userId]) {
          completedTasks[todo.userId]++;
        } else {
          completedTasks[todo.userId] = 1;
        }
      }
    });

    console.log(completedTasks);
  });
}

// Get the API URL from the command-line arguments
const apiUrl = process.argv[2];

// Check if the API URL is provided
if (!apiUrl) {
  console.error('Usage: ./6-completed_tasks.js <API_URL>');
  process.exit(1);
}
// Call the function to compute the number of completed tasks
countCompletedTasks(apiUrl);
