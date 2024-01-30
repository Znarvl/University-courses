const map = L.map('map').setView([58.40384776751319, 15.578484535217285], 15);
const form = document.querySelector('#path-form')
const markerIsStart = document.querySelector("#marker-point-start")
const markerIsEnd = document.querySelector("#marker-point-end")

var user_options = {}
  user_options.lastcarpath = document.getElementById("last-car-path")
  user_options.lastbikepath = document.getElementById("last-bike-path")
  user_options.logout = document.getElementById("logout")
  user_options.info = document.getElementsByClassName("user-options")
  setInfoDisplay(user_options.info, "none")

var clear_map = document.getElementById("clear-map")
var toggle_mode = document.getElementById("toggle-mode")

function submitForm(button){
  if(button.value == "Find car path"){
    form.addEventListener('submit', postShortestCarPath, {once: true})
  } else if(button.value == "Find bike path"){
    form.addEventListener('submit', postShortestBikePath, {once: true})
  } else{
    return false
  }
}

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

var car_path = L.layerGroup()
var bike_path = L.layerGroup()
var lastbike_path = L.layerGroup()
var lastcar_path = L.layerGroup()
var markers = L.layerGroup()

async function postShortestCarPath(event){
    event.preventDefault()
    var lat1 = parseFloat(document.querySelector('#lat1').value)
    var lng1 = parseFloat(document.querySelector('#lng1').value)
    var lat2 = parseFloat(document.querySelector('#lat2').value)
    var lng2 = parseFloat(document.querySelector('#lng2').value)

    // Check that they're not Nan (stops function if one is Nan)
    if(!lat1 || !lng1  || !lat2 || !lng2)
        return alert('Formatting Error: Coordinates are not float values.')

    req = {lat1, lng1, lat2, lng2} // Dictionary auto-keys

    res = await fetch('/shortest-car-path', {
        method:'POST',
        credentials: 'same-origin',
        body: JSON.stringify(req)
    })

    res = await res.json()
    console.log(res.path)
    car_path.clearLayers()
    var car_start_marker = L.marker([lat1, lng1]).addTo(car_path)
    var car_end_marker = L.marker([lat2, lng2]).addTo(car_path)
    var poly_car = L.polyline(res.path)
    car_path.addLayer(poly_car)
    markers.clearLayers()
    car_path.addTo(map)
}

async function postShortestBikePath(event){
    event.preventDefault()
    var lat1 = parseFloat(document.querySelector('#lat1').value)
    var lng1 = parseFloat(document.querySelector('#lng1').value)
    var lat2 = parseFloat(document.querySelector('#lat2').value)
    var lng2 = parseFloat(document.querySelector('#lng2').value)

    // Check that they're not Nan (stops function if one is Nan)
    if(!lat1 || !lng1  || !lat2 || !lng2)
        return alert('Formatting Error: Coordinates are not float values.')

    req = {lat1, lng1, lat2, lng2} // Dictionary auto-keys

    res = await fetch('/shortest-bike-path', {
        method:'POST',
        credentials: 'same-origin',
        body: JSON.stringify(req)
    })

    res = await res.json()
    console.log(res.path)
    bike_path.clearLayers()
    var bike_start_marker = L.marker([lat1, lng1]).addTo(bike_path)
    var bike_end_marker = L.marker([lat2, lng2]).addTo(bike_path)
    var poly_bike = L.polyline(res.path, {color: 'red'})
    bike_path.addLayer(poly_bike)
    markers.clearLayers()
    bike_path.addTo(map)
}

user_options.lastcarpath.onclick = async ()=> {
//response is a dictionary where the start and end keys are the markers saved
  var req = {}

  var res = await fetch('/last-car-path', {
      method:'POST',
      credentials: 'same-origin',
      body: JSON.stringify(req)
  })

  res = await res.json()
  console.log(res.path)
  if(res=="no last car path"){
    return alert("No car path saved!")
  } else{
    lastcar_path.clearLayers()
    var lastcar_start_marker = L.marker(res.start).addTo(lastcar_path)
    var lastcar_end_marker = L.marker(res.end).addTo(lastcar_path)
    var poly_lastcar = L.polyline(res.path, {color: 'purple'})
    lastcar_path.addLayer(poly_lastcar)
    lastcar_path.addTo(map)
  }
}

user_options.lastbikepath.onclick = async ()=> {
  var req = {}

  var res = await fetch('/last-bike-path', {
      method:'POST',
      credentials: 'same-origin',
      body: JSON.stringify(req)
  })

  res = await res.json()
  console.log(res.path)
  if(res=="no last bike path"){
    return alert("No bike path saved!")
  } else{
    lastbike_path.clearLayers()
    var lastbike_start_marker = L.marker(res.start).addTo(lastbike_path)
    var lastbike_end_marker = L.marker(res.end).addTo(lastbike_path)
    var poly_lastbike = L.polyline(res.path, {color: 'orange'})
    lastbike_path.addLayer(poly_lastbike)
    lastbike_path.addTo(map)
  }
}

clear_map.onclick = async ()=> {
  //Clears all map layers and sets the selection marker to Start
  lastbike_path.clearLayers()
  lastcar_path.clearLayers()
  bike_path.clearLayers()
  car_path.clearLayers()
  markers.clearLayers()
  if(markerIsEnd.checked){
    markerIsStart.checked = true
  }
}

function time_check() {
  /*between 20:00 and 05:00 night mode will be activated when accesing the site
  and if user stays until morning it will automatically change to day mode with
  interval time check defined further down*/
  var hour = new Date().getHours(); //gets users current time in hours
  if (hour <= 4 || hour >= 20){
    body.className = "night-mode";
  }
  if (!hour <= 4 && !hour >= 20){
    body.className = "day-mode";
  }
}

time_check() //initial time check when accessing site
var time_check_interval = setInterval(time_check, 60*1000)//runs the time check function every minute


toggle_mode.onclick = async ()=> {
  //Toggles night mode on and off
  var currentClass = body.className;
  clearInterval(time_check_interval)//turns off the time check interval
  body.className = currentClass == "day-mode" ? "night-mode" : "day-mode";
}

function handleMapClick ({latlng}){
    var {lat, lng} = latlng
    var marker = L.marker([lat, lng])
    if(markers.getLayers().length==2){
      markers.clearLayers()
    }
    markers.addLayer(marker)
    markers.addTo(map)
    var posNumber = markerIsStart.checked ? '1' : '2'
    document.querySelector('#lat' + posNumber).value = lat
    document.querySelector('#lng' + posNumber).value = lng
    if(markerIsStart.checked){
        markerIsEnd.checked = true
    }else if(markerIsEnd.checked){
      markerIsStart.checked = true
    }
}


map.on('click', handleMapClick)


var login = {}
login.button = document.getElementById("login")
login.info = document.getElementById("login-info")
login.info.style.display = "none"
login.username = document.getElementById("login-username")
login.password = document.getElementById("login-password")
login.submit = document.getElementById("login-submit")
login.show = false

var register = {}
register.button = document.getElementById("register")
register.info = document.getElementById("register-info")
register.info.style.display = "none"
register.username = document.getElementById("register-username")
register.password1 = document.getElementById("register-password1")
register.password2 = document.getElementById("register-password2")
register.submit = document.getElementById("register-submit")
register.show = false

var user_access = {}
  user_access.info = document.getElementById("user-access")
  user_access.info.style.display = "block"

login.button.onclick = ()=> {
    if(!login.show){
  login.button.textContent = "Hide Login"
  login.show = true
  login.info.style.display = "block"
    } else {
  login.button.textContent = "Show Login"
  login.show = false
  login.info.style.display = "none"
    }
}

function setInfoDisplay(collection, val){
  //hides or shows user options
  for(var i= 0; i<collection.length; i++){
    collection.item(i).style.display = val
  }
}

user_options.logout.onclick = async ()=> {
  var req = {}
  var res = await fetch('/logout',{
method: 'POST',
credentials: 'same-origin',
body: JSON.stringify(req)
  })
  res = await res.json()
  console.log(res)
  user_access.info.style.display = "block"
  setInfoDisplay(user_options.info, "none")
    if(register.show){
      register.button.textContent = "Show Register"
      register.show = false
      register.info.style.display = "none"
  }
    if(login.show){
      login.button.textContent = "Show Login"
      login.show = false
      login.info.style.display = "none"
  }
  return alert("You are now logged out")
  }

login.submit.onclick = async ()=> {
    var username = login.username.value,
  password = login.password.value;

    var req = {
  username,
  password
    }
    var res = await fetch('/login',{
  method: 'POST',
  credentials: 'same-origin',
  body: JSON.stringify(req)
    })
    res = await res.json()
    console.log(res)
    if(res=="success"){
      user_access.info.style.display = "none"
      setInfoDisplay(user_options.info, "block")
      user_options.logout.textContent = "Logout: " + String(username)
      return alert("Success: User logged in")
    }else if(res=="user not found"){
      return alert("Error: Wrong username or password")
    }


}

register.button.onclick = () => {
    if(!register.show){
  register.button.textContent = "Hide Register"
  register.show = true
  register.info.style.display = "block"
    } else {
  register.button.textContent = "Show Register"
  register.show = false
  register.info.style.display = "none"
    }
}

register.submit.onclick = async ()=> {
    var username = register.username.value,
  password1 = register.password1.value,
  password2 = register.password2.value;
    if (password1 != password2)
  return alert("The passwords don't match")
    var req = {
  username,
  password: password1
    }
    var res = await fetch('/register',{
  method: 'POST',
  credentials: 'same-origin',
  body: JSON.stringify(req)
    })
    res = await res.json()
    console.log(res)
    if(res=="success"){
      user_access.info.style.display = "none"
      setInfoDisplay(user_options.info, "block")
      user_options.logout.textContent = "Logout: " + String(username)
      return alert("Success: User registered and logged in")
    }else if(res=="user exists"){
      return alert("Error: This username is already taken")
    }

}
