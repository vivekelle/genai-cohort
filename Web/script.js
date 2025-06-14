function addTodo() {
  const todoInput = document.getElementById('todo-input');
  const todoList = document.getElementById('todo-list');
  const todoText = todoInput.value.trim();
  if (todoText === '') return;
  const li = document.createElement('li');
  li.innerHTML = todoText + ' <button class=\'delete-btn\'>Delete</button>';
  li.querySelector('.delete-btn').onclick = function() { li.remove(); };
  todoList.appendChild(li);
  todoInput.value = '';
}

document.getElementById('todo-input').addEventListener('keypress', function(e) {
  if (e.key === 'Enter') {
    addTodo();
  }
});
// Test append
