document.getElementById('add-weather-form').onsubmit = (e) => {
    console.log('ok')
    e.preventDefault()
    var humidity = document.getElementById('humidity_input').value
    var temp = document.getElementById('temprature_input').value
    console.log(humidity, temp)

    fetch(api_url, {
        method: 'POST',
        headers: { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({'humidity':humidity, 'temperature':temp}),
        redirect: 'follow'
    }).then((resp) => {
        if (!resp.ok) {
            throw Error(resp.statusText);
        }else {location.reload();}
    }).catch((err) => {
        alert("Please enter Humidity 35 : 65,\rAnd Temperature 19 : 28");
    });
}


