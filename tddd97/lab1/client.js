displayView = function () {
    token = sessionStorage.getItem("token");
    data = serverstub.getUserDataByToken(token);

    if (data.data) {
        document.getElementById("view").innerHTML =
            document.getElementById("profile-view").innerHTML
        displayData();
        return;
    }
    document.getElementById("view").innerHTML =
        document.getElementById("welcome-view").innerHTML;
}

window.onload = function () {
    displayView();
};

function signIn() {
    password = document.getElementById("psw-login").value;
    email = document.getElementById("email-login").value;

    if (password.length < 6) {
        document.getElementById("login-error").innerHTML =
            "Password must be longer than 5 characters!";
        return;
    }
    res = serverstub.signIn(email, password)
    if (!res.success) {
        document.getElementById("login-error").innerHTML = res.message
        return;
    }
    sessionStorage.setItem("token", res.data);
    displayView();

    return res.success
}

function signUp() {
    email = document.getElementById("email-create").value;
    password = document.getElementById("psw-create").value;
    assuredPassword = document.getElementById("psw-again").value;
    if (password.length < 6) {
        document.getElementById("sign-up-error").innerHTML =
            "Password must be longer than 5 characters!";
        return;
    }
    if (password != assuredPassword) {
        document.getElementById("sign-up-error").innerHTML =
            "Not identical passwords";
        return;
    }
    data = {
        email: email,
        password: password,
        firstname: document.getElementById("fname").value,
        familyname: document.getElementById("fam-name").value,
        gender: document.getElementById("gender-value").value,
        city: document.getElementById("city").value,
        country: document.getElementById("country").value,
    }
    res = serverstub.signUp(data)
    if (!res.success) {
        document.getElementById("sign-up-error").innerHTML = res.message
        return;
    }
    res = serverstub.signIn(email, password);
    if (!res.success) {
        document.getElementById("sign-up-error").innerHTML = res.message
        return;
    }
    sessionStorage.setItem("token", res.data);
    document.getElementById("sign-up-error").innerHTML = res.message

    displayView();
    return;
}

function signOut() {
    token = sessionStorage.getItem("token")
    res = serverstub.signOut(token)
    if (res.success) {
        displayView();
    }

}

function displayData() {
    token = sessionStorage.getItem("token")
    data = serverstub.getUserDataByToken(token)
    document.getElementById("user-name").innerHTML = data.data.firstname
    document.getElementById("user-fam-name").innerHTML = data.data.familyname
    document.getElementById("user-gender").innerHTML = data.data.gender
    document.getElementById("user-city").innerHTML = data.data.city
    document.getElementById("user-country").innerHTML = data.data.country
    document.getElementById("user-email").innerHTML = data.data.email
    refreshMessages()
}

function changePassword() {
    document.getElementById("change-password-success").innerHTML = ""
    oldPassword = document.getElementById("old-password").value
    newPassword = document.getElementById("new-password").value
    repeatNewPassword = document.getElementById("repeat-new-password").value
    token = sessionStorage.getItem("token");
    if (newPassword != repeatNewPassword) {

        document.getElementById("change-password-error").innerHTML = "Password is not equal"
        return;
    }
    if (newPassword.length < 6) {
        document.getElementById("change-password-error").innerHTML = "Password must be longer than 5 characters!"
        return;
    }
    res = serverstub.changePassword(token, oldPassword, newPassword);

    if (!res.success) {
        document.getElementById("change-password-error").innerHTML = res.message
        return;
    }
    document.getElementById("change-password-error").innerHTML = ""
    document.getElementById("change-password-success").innerHTML = res.message
    return;
}

function switchTab(event, tab) {
    tablinks = document.getElementsByClassName("tab-button");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" current", "");
    }
    event.currentTarget.className += " current";

    tablinks = document.getElementsByClassName("tab-container");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" show", "");
    }
    document.getElementById(tab).className += " show";

}

function post() {
    token = sessionStorage.getItem("token");
    recipient = serverstub.getUserDataByToken(token);
    email = recipient.data.email;
    textMessage = document.getElementById("user-post").value

    res = serverstub.postMessage(token, textMessage, email)
    if (!res) {
        document.getElementById("post-message-error").innerHTML = res.message
        return;
    }
    document.getElementById("post-message-success").innerHTML = res.message
    document.getElementById("user-post").value = ""
    refreshMessages();
}

function parseMessage(message) {
    return "<div class='wall-message'><div class='writer'>" +
        message.writer +
        "</div> <div class='content'>" +
        message.content + "</div><br></div>";
}

function refreshMessages() {
    token = sessionStorage.getItem("token");
    res = serverstub.getUserMessagesByToken(token);
    document.getElementById("posts").innerHTML = "";
    res.data.forEach(message => document.getElementById("posts").innerHTML += parseMessage(message));
    return;

}

function browse() {

    token = sessionStorage.getItem("token");
    email = document.getElementById("browse-email").value;
    res = serverstub.getUserDataByEmail(token, email)
    if (!res.success) {
        document.getElementById("browse-error").innerHTML = res.message;
        document.getElementById("browse-success").innerHTML = "";

        return
    }
    document.getElementById("browse-error").innerHTML = "";
    document.getElementById("browse-success").innerHTML = res.message;

    //document.getElementById("browse-information").className = "show"

    document.getElementById("browse-header").innerHTML = res.data.email
    document.getElementById("browse-user-name").innerHTML = res.data.firstname
    document.getElementById("browse-user-fam-name").innerHTML = res.data.familyname
    document.getElementById("browse-user-gender").innerHTML = res.data.gender
    document.getElementById("browse-user-city").innerHTML = res.data.city
    document.getElementById("browse-user-country").innerHTML = res.data.country
    document.getElementById("browse-user-email").innerHTML = res.data.email

    document.getElementById("browse-wall-title").innerHTML = res.data.firstname + "'s Wall"

    refreshBrowseMessages();
}

function refreshBrowseMessages() {
    token = sessionStorage.getItem("token");
    email = document.getElementById("browse-header").innerText;
    res = serverstub.getUserMessagesByEmail(token, email);
    document.getElementById("browse-posts").innerHTML = "";
    res.data.forEach(message => document.getElementById("browse-posts").innerHTML += parseMessage(message));

}

function browsePost() {
    token = sessionStorage.getItem("token");
    email = document.getElementById("browse-header").innerText;
    recipient = serverstub.getUserDataByEmail(token, email);
    email = recipient.data.email;
    textMessage = document.getElementById("browse-user-post").value

    res = serverstub.postMessage(token, textMessage, email)
    if (!res) {
        document.getElementById("browse-post-message-error").innerHTML = res.message
        return;
    }
    document.getElementById("browse-post-message-success").innerHTML = res.message
    document.getElementById("browse-user-post").value = ""
    refreshBrowseMessages();

}