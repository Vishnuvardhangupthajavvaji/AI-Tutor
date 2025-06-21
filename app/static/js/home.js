// script.js
document.getElementById('ask-btn').addEventListener('click', () => {
    const question = document.getElementById('question').value;
    if (!question.trim()) {
      alert('Please enter a question!');
      return;
    }
    alert(`Your question: "${question}" has been submitted.`);
  });