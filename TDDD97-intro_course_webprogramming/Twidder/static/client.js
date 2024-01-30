
function makeRequest (method, url, done, data={}) {
    console.log("REQUEST: " + url)
    var req = new XMLHttpRequest();
    req.open(method, url, true);
    req.setRequestHeader('content-type', 'application/json;charset=UTF-8');
    token = sessionStorage.getItem("token");
    if(token){
        req.setRequestHeader("Authorization", "Bearer " + token);
    }

    req.onload = function () {
        console.log(req)
        console.log("REQUEST: LOADED (STATUS " + req.status + ")")
        done(null, req);
    };
    
    req.onerror = function () {
        console.log(req)
        console.log("ERROR")
        done(req.statusText);
    };

    req.send(JSON.stringify(data));
}


displayView = function () {
    makeRequest("GET", "/get_user_data_by_token", function(err, res){
        if(res.status == 200){
            var response = JSON.parse(res.response);

            if (response.data) {
                document.getElementById("view").innerHTML =
                    document.getElementById("profile-view").innerHTML
                displayData();
            }
        }else{
            document.getElementById("view").innerHTML =
                document.getElementById("welcome-view").innerHTML;
        }
    })
}

window.onload = function () {
    displayView();
};

function sendWebsocket (data){

    // console.log(location.host)
    console.log(document.domain)

    const socket = new WebSocket('ws://' + location.host + '/api');
    socket.onopen = function () {
        console.log("Packet opened")
        console.log("Packetdata: " + data)

        socket.send(data)
    };
    socket.onmessage = function (msg){
        console.log('Server: ' + msg.data);
        if(msg.data == 'logout'){
            signOut();
            socket.close();
        }
    }
    socket.onerror = function (error) {
        console.log('WebSocket Error ' + error);
       };
}


function signIn() {
    password = document.getElementById("psw-login").value;
    email = document.getElementById("email-login").value;


    if (password.length < 6) {
        document.getElementById("login-error").innerHTML =
            "Password must be longer than 5 characters!";
        return;
    }

    data = {
        email: email,
        password: password
    }
    makeRequest("POST", "/sign_in", function(err, res){
        console.log('Response! ', res)
        console.log(res)
        if (res.status == 200){
            var response = JSON.parse(res.response);
            if (response.token){
                sessionStorage.setItem("token", response.token);
                sendWebsocket(response.token);
                displayView();
            }
        } else{
            document.getElementById("login-error").innerHTML = "Wrong username or password."
        }
    }, data)
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

    makeRequest("POST", "/sign_up", function(err, res){
        if(res.status == 201){
            let response = JSON.parse(res.response);

            data = {
                email: email,
                password: password
            }
            makeRequest("POST", "/sign_in", function(err, res){

                if (res.status == 200){
                    let response = JSON.parse(res.response);
                    if (response.token){
                        sessionStorage.setItem("token", response.token);
                        displayView();
                    }
                    else{
                        document.getElementById("sign-up-error").innerHTML = "Could not sign in"
                    }
                }
            }, data)

        }else{
            document.getElementById("sign-up-error").innerHTML = "Could not sign up."
        }
    }, data)
}

function signOut() {
    makeRequest("POST", "/sign_out", function(err, res){
        if (res.status == 200){
                sessionStorage.removeItem("token")
                displayView()
            }
    })
}

function displayData() {
    makeRequest("GET", "/get_user_data_by_token", function(err, res){
        if (res.status == 200) {
        let response = JSON.parse(res.response);
            data = response.data
            document.getElementById("user-name").innerHTML = data.firstname
            document.getElementById("user-fam-name").innerHTML = data.familyname
            document.getElementById("user-gender").innerHTML = data.gender
            document.getElementById("user-city").innerHTML = data.city
            document.getElementById("user-country").innerHTML = data.country
            document.getElementById("user-email").innerHTML = data.email
            refreshMessages()
        } 
    })
}

function changePassword() {
    document.getElementById("change-password-success").innerHTML = ""
    oldPassword = document.getElementById("old-password").value
    newPassword = document.getElementById("new-password").value
    repeatNewPassword = document.getElementById("repeat-new-password").value
    if (newPassword != repeatNewPassword) {

        document.getElementById("change-password-error").innerHTML = "Password is not equal"
        return;
    }
    if (newPassword.length < 6) {
        document.getElementById("change-password-error").innerHTML = "Password must be longer than 5 characters!"
        return;
    }

    data = {
        password: oldPassword,
        newpassword: newPassword,
    }

    makeRequest("POST","/change_password", function(err, res){
        if(res.status == 200){
            document.getElementById("change-password-error").innerHTML = "Password changed." //res.statusText;
        }else{
            document.getElementById("change-password-error").innerHTML = "Wrong password." 
        }
    }, data)
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
    message = document.getElementById("user-post").value

    data = {
        recipient: "self",
        message: message
    }

    makeRequest("POST",  "/post_message", function(err, res){
        if(res.status == 200){
            document.getElementById("post-message-error").innerHTML = "Post Successfull.";
        }
    }, data)
    refreshMessages()

}


function parseMessage(message) {
    return "<div class='wall-message'><div class='writer'>" +
        message.email_sender +
        "</div> <div class='content'>" +
        message.message + "</div><br></div>";
}

function refreshMessages() {
    document.getElementById("posts").innerHTML = ""
    makeRequest("GET", "/get_user_messages_by_token", function(err, res){
        if(res.status == 200){
            response = JSON.parse(res.response)
                response.data.forEach(message => 
                    document.getElementById("posts").innerHTML += parseMessage(message));
        }
    })
}

function browse() {

    email = document.getElementById("browse-email").value;

    data = {
        email : email
    }

    makeRequest("POST", "/get_user_data_by_email", function(err, res){


        if(res.status == 200){
            response = JSON.parse(res.response)

            //console.log(response)
            document.getElementById("browse-error").innerHTML = "";
            document.getElementById("browse-success").innerHTML = "User found.";

            //document.getElementById("browse-information").className = "show"

            document.getElementById("browse-header").innerHTML = response.data.email
            document.getElementById("browse-user-name").innerHTML = response.data.firstname
            document.getElementById("browse-user-fam-name").innerHTML = response.data.familyname
            document.getElementById("browse-user-gender").innerHTML = response.data.gender
            document.getElementById("browse-user-city").innerHTML = response.data.city
            document.getElementById("browse-user-country").innerHTML = response.data.country
            document.getElementById("browse-user-email").innerHTML = response.data.email

            document.getElementById("browse-wall-title").innerHTML = response.data.firstname + "'s Wall"

            refreshBrowseMessages();
        }else{
            document.getElementById("browse-error").innerHTML = "User not found.";
            document.getElementById("browse-success").innerHTML = "";
        }


    }, data)
}

function refreshBrowseMessages() {
    email = document.getElementById("browse-header").innerText;

    data = {
        email : email
    }

    makeRequest("POST", "/get_user_messages_by_email", function(err, res){
        if(res.status == 200){
            response = JSON.parse(res.response)
            document.getElementById("browse-posts").innerHTML = "";
            response.data.forEach(message => document.getElementById("browse-posts").innerHTML += parseMessage(message));
        }

    }, data)
}

function browsePost() {
    recipient = document.getElementById("browse-header").innerText;
    message = document.getElementById("browse-user-post").value

    data = {
        recipient : recipient,
        message: message
    }

    makeRequest("POST", "/post_message", function(err, res){
        if(res.status == 200){
            response = JSON.parse(res.response)
                document.getElementById("browse-post-message-success").innerHTML = "Post Successfull."
                document.getElementById("browse-user-post").value = ""
                refreshBrowseMessages();
            }
        else{
            document.getElementById("browse-post-message-error").innerHTML = "Post failed."
        }
    }, data)
}