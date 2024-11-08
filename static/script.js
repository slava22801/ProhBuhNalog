let navbar = document.querySelector("Nav .nav");
let menu = document.querySelector(".bars");

menu.onClick = () => {
	navbar.classList.toggle("active");
}





document.getElementById('dataForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent default form submission

    const formData = new form(this);
    const data = Object.fromEntries(formData.entries());

    fetch('/submit', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});
