const apiUrl = "https://jsonplaceholder.typicode.com/users";
const listGroup = document.getElementById("list-group");
users = [];

async function loadUsers() {
    const response = await fetch(apiUrl);
    return response.json();
}

function renderUsers(){
    const tableBody = document.getElementById("tableBody");
    tableBody.innerHTML = "";

    users.forEach(element => {
        let row = document.createElement("tr");
            // row.setAttribute("class", "list-item");
            row.innerHTML = `
                <td>${element.id}</td>
                <td>${element.name}</td>
                <td>
                    <button class="btn btn-info" onclick="editUser(${element.id})">Bearbeiten</button>
                    <button class="btn btn-danger" onclick="deleteUser(${element.id})">Löschen</button>
                </td>
            `;
            tableBody.appendChild(row)
    });
}

async function init(){
    users = await loadUsers();
    renderUsers();
}

function deleteUser(id){
    if(confirm(`Willst du das Mitlgieder mit der ID ${id} wirklich löschen?`)){
        const deletedUser = users.find((user) => user.id === id);
        users = users.filter((user) => user.id !== deletedUser.id);
        tableBody.innerHTML = "";
        renderUsers();
    }
}

function addMember(event){
    event.preventDefault();
    const newNameInput = document.getElementById("new-name-input").value;
    const newMember = {
        id: users.length + 1,
        name: newNameInput,
    };
    users.push(newMember);
    tableBody.innerHTML = "";
    renderUsers();
}

init();