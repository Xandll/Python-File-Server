//dot menu
const dotsMenus = document.querySelectorAll('.dots-menu');

//hide everything before login
document.style.display = 'none';

dotsMenus.forEach(dotsMenu => {
  dotsMenu.addEventListener('click', (e) => {
    e.stopPropagation();
    const options = dotsMenu.parentNode.querySelector('.file-options');
    options.style.display = 'flex';
  });
});

document.addEventListener('click', () => {
  dotsMenus.forEach(dotsMenu => {
    const options = dotsMenu.parentNode.querySelector('.file-options');
    options.style.display = 'none';
  });
});

//rename file
function showRenameForm(filename) {
  document.getElementById('rename-form').style.display = 'block';
  document.getElementById('old_filename').value = filename;
}

//log in
function loginPopup() {
  var username = prompt("Please enter your username:");
  var password = prompt("Please enter your password:");

  if (username === "User1" && password === "Passw0rdForUser1") {
    alert("Logged in successfully!");
    localStorage.setItem("loggedIn", "true");
    document.style.display = 'block';
  } else if (username === "User2" && password === "Passw0rdForUser2") {
    alert("Logged in successfully!");
    localStorage.setItem("loggedIn", "true");
    document.style.display = 'block';
  } else {
    alert("Invalid username or password! Please try again.");
    loginPopup();
  }
}

//stay logged in
window.onload = function() {
  if (localStorage.getItem("loggedIn") === "true") {
    // Do nothing, user is logged in
  } else {
    loginPopup();
  }
};

//log out
function resetLogin() {
  localStorage.setItem("loggedIn", "false");
}