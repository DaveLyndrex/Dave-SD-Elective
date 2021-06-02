var client = mqtt.connect('wss://mqtt.eclipseprojects.io:443/mqtt') //connect to the broker.

var topic = document.getElementById('topic') //declaring variable named "topic". Then get the id "topic" from the web and store.
var subtopic = document.getElementById('subtopic') //decraring variable named "subtopic". Then get the id "subtopic" from the web and store.

client.on('connect', function() { //onconnect function
    console.log('connected') //if connected, log "connected" in console.
})

var topicValue = document.getElementById('topic').value; //declaring variable named "topicValue" and store the value of the id "topic".
var payloadValue = document.getElementById('payload').value; //declaring variable named "paloadValue" and store the value of the id "payload".

client.on('message', function(topicValue, payloadValue) { //onmessage function with the parameter topicValue and payloadValue.
    $(".table tbody").append("<tr><td>" + topicValue + "</td><td>" + payloadValue + "</td></tr>") //insert the of the topic and payload being being publish into table body.

})

$(document).ready(function() { //signals if the DOm of the page is now ready.
        $('#publish').click(function() { //when clicking the id publish,
            client.publish(topic.value, payload.value) //it will publish the topic value and the payload value.
        })
        $('#subscribe').click(function() { //when clicking the id subscribe,
            if (subtopic.value == "") { //checking if the subtopic button is click but it has an empty value,
                alert("Please Fill up before Subscribing.") //it will alert this message.
            } else { //or else,
                client.subscribe(subtopic.value) //subscribe to the subtopic value.
            } //closing of the function
        })
    }) //closing of the onready function.