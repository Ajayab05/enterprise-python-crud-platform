const API_URL = "/api/employees";

window.onload = function () {
    loadEmployees();
};

function loadEmployees() {
    fetch(API_URL)
        .then(response => response.json())
        .then(data => {
            let html = "";

            data.forEach(emp => {
                html += `
                <tr>
                    <td>${emp.id}</td>
                    <td>${emp.name}</td>
                    <td>${emp.email}</td>
                    <td>${emp.department}</td>
                    <td>${emp.salary}</td>
                    <td>
                        <button class="btn btn-danger btn-sm"
                                onclick="deleteEmployee(${emp.id})">
                            Delete
                        </button>
                    </td>
                </tr>`;
            });

            document.getElementById("employees").innerHTML = html;
        })
        .catch(err => console.error(err));
}

function saveEmployee() {
    const employee = {
        name: document.getElementById("name").value,
        email: document.getElementById("email").value,
        department: document.getElementById("department").value,
        salary: document.getElementById("salary").value
    };

    fetch(API_URL, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(employee)
    })
    .then(() => {
        loadEmployees();
    });
}

function deleteEmployee(id) {
    fetch(`${API_URL}/${id}`, {
        method: "DELETE"
    })
    .then(() => loadEmployees());
}