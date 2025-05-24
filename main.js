let currentUser = "";
let tasks = []; // store tasks in memory for now

function signup() {
  // Your existing signup code here...
}

function login() {
  // Your existing login code here...
  // For demo, we’ll skip server and just simulate login
  const username = document.getElementById("username").value;
  currentUser = username;
  document.getElementById("auth").style.display = "none";
  document.getElementById("todoSection").style.display = "block";
  document.getElementById("userDisplay").textContent = username;
  loadTasks();
}

function logout() {
  currentUser = "";
  tasks = [];
  document.getElementById("auth").style.display = "block";
  document.getElementById("todoSection").style.display = "none";
  document.getElementById("username").value = "";
  document.getElementById("password").value = "";
  document.getElementById("taskList").innerHTML = "";
}

function addTask() {
  const title = document.getElementById("title").value.trim();
  const description = document.getElementById("description").value.trim();
  const due_date = document.getElementById("due_date").value;

  if (!title) {
    alert("Please enter a task title.");
    return;
  }

  const newTask = {
    id: Date.now(), // unique id
    title,
    description,
    due_date,
    completed: false,
  };

  tasks.push(newTask);
  renderTasks();

  // Clear input fields after adding
  document.getElementById("title").value = "";
  document.getElementById("description").value = "";
  document.getElementById("due_date").value = "";
}

function renderTasks() {
  const taskList = document.getElementById("taskList");
  taskList.innerHTML = ""; // Clear current list

  if (tasks.length === 0) {
    taskList.innerHTML = "<p>No tasks added yet.</p>";
    return;
  }

  tasks.forEach(task => {
    const taskDiv = document.createElement("div");
    taskDiv.className = "task";

    taskDiv.innerHTML = `
      <b>${task.title}</b>
      <div>${task.description || ""}</div>
      <div>Due: ${task.due_date || "No date"}</div>
      <button onclick="editTask(${task.id})">Edit</button>
      <button onclick="deleteTask(${task.id})">Delete</button>
    `;

    taskList.appendChild(taskDiv);
  });
}

function editTask(id) {
  const task = tasks.find(t => t.id === id);
  if (!task) return;

  const newTitle = prompt("Edit task title:", task.title);
  if (newTitle === null) return; // Cancelled

  const newDescription = prompt("Edit task description:", task.description);
  if (newDescription === null) return;

  const newDueDate = prompt("Edit due date (YYYY-MM-DD):", task.due_date);
  if (newDueDate === null) return;

  task.title = newTitle.trim() || task.title;
  task.description = newDescription.trim() || task.description;
  task.due_date = newDueDate || task.due_date;

  renderTasks();
}

function deleteTask(id) {
  tasks = tasks.filter(t => t.id !== id);
  renderTasks();
}

function loadTasks() {
  // Load from backend or local storage if available
  // For now, just render current tasks array
  renderTasks();
}
